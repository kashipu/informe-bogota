#!/usr/bin/env python3
"""
Site Crawler (Python) — Banco de Bogotá Personas (configurable)

Features
- BFS crawl starting from BASE_URL (configurable)
- Robots.txt compliance (can be disabled)
- Extracts: url, status_code, title, meta_description, canonical, parent_url, depth
- Collects internal links (same scheme+host) and builds parent→child edges
- Writes streaming outputs for scalability:
    - data/pages.jsonl    (one JSON object per page)
    - data/edges.jsonl    (one JSON object per discovered link)
    - data/errors.jsonl   (network/parse errors)
- Generates path-based hierarchy for later D3 visualization:
    - data/hierarchy.json (tree built from URL path segments)

"""
from __future__ import annotations
import json
import os
import time
import logging
from logging.handlers import RotatingFileHandler
from collections import deque
from dataclasses import dataclass
from typing import Optional, Set, Dict, Tuple, List

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urldefrag
import urllib.robotparser as robotparser

# =========================== CONFIGURACIÓN =========================== #

BASE_URL = "https://www.bancodebogota.com/personas"  # URL inicial
MAX_PAGES = float('inf')   # Poner un número alto o float('inf') para escanear todo el portal
MAX_DEPTH = 8              # profundidad máxima
DELAY = 0.5                # segundos entre solicitudes
OBEY_ROBOTS = False        # respetar robots.txt (pon en False SOLO para depurar)
TIMEOUT = 20.0             # timeout por solicitud
VERIFY_TLS = True          # si hay problemas de SSL, prueba False (no recomendado)

# Descubrimiento adicional por sitemap
USE_SITEMAP = True
SITEMAP_URLS = [
    "https://www.bancodebogota.com/sitemap.xml",
]

# Si una URL está bloqueada por robots, aún la registramos (sin hacer GET)
RECORD_BLOCKED_URLS = True

# Headers para parecer un navegador real
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
}

# Logging / diagnóstico
DEBUG = True               # True = más verboso
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "crawler.log")

# =========================== DATACLASSES =========================== #

@dataclass
class PageRecord:
    url: str
    status_code: Optional[int]
    title: str
    meta_description: str
    canonical: Optional[str]
    parent_url: Optional[str]
    depth: int

# =========================== HELPERS =========================== #

def setup_logger() -> logging.Logger:
    """Configura y devuelve un logger para registrar eventos del crawler.

    Crea un logger con handlers para la consola y para un archivo rotativo.
    El nivel de logging se ajusta según la constante DEBUG.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger("crawler")
    logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    ch = logging.StreamHandler(); ch.setLevel(logging.DEBUG if DEBUG else logging.INFO); ch.setFormatter(fmt)
    fh = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3, encoding="utf-8"); fh.setLevel(logging.DEBUG); fh.setFormatter(fmt)
    if not logger.handlers:
        logger.addHandler(ch); logger.addHandler(fh)
    return logger


def normalize_url(base: str, href: str) -> Optional[str]:
    """Normaliza una URL relativa o absoluta.

    Args:
        base: La URL base desde la cual se encontró el href.
        href: El valor del atributo href a normalizar.

    Returns:
        La URL absoluta y sin fragmentos, o None si ocurre un error.
    """
    try:
        abs_url = urljoin(base, href)
        abs_url, _ = urldefrag(abs_url)
        return abs_url
    except Exception:
        return None


def same_origin(a: str, b: str) -> bool:
    """Comprueba si dos URLs pertenecen al mismo origen (esquema + host).

    Args:
        a: La primera URL.
        b: La segunda URL.

    Returns:
        True si ambas URLs tienen el mismo origen, False en caso contrario.
    """
    pa, pb = urlparse(a), urlparse(b)
    return (pa.scheme, pa.netloc) == (pb.scheme, pb.netloc)


def extract_meta(soup: BeautifulSoup) -> Tuple[str, str]:
    """Extrae el título y la meta descripción de un objeto BeautifulSoup.

    Returns:
        Una tupla conteniendo (título, meta_descripción).
    """
    title = soup.title.string.strip() if soup.title and soup.title.string else "SIN_TITULO"
    desc_tag = (
        soup.find("meta", attrs={"name": "description"})
        or soup.find("meta", attrs={"property": "og:description"})
        or soup.find("meta", attrs={"name": "Description"})
    )
    meta_description = (
        desc_tag.get("content", "").strip() if desc_tag and desc_tag.get("content") else "SIN_DESCRIPCION"
    )
    return title, meta_description


def extract_canonical(soup: BeautifulSoup) -> Optional[str]:
    """Extrae la URL canónica de un objeto BeautifulSoup.

    Returns:
        La URL canónica si se encuentra, de lo contrario None.
    """
    link = soup.find("link", rel=lambda v: v and "canonical" in v)
    if link and link.get("href"):
        return link.get("href").strip()
    return None


def is_html_response(resp: requests.Response) -> bool:
    """Verifica si la respuesta HTTP es de tipo HTML.

    Returns:
        True si el Content-Type es HTML, False en caso contrario.
    """
    ctype = resp.headers.get("Content-Type", "").lower()
    return "text/html" in ctype or "application/xhtml" in ctype


def fetch_sitemap_urls(logger: logging.Logger, base_origin: str, base_prefix: str) -> List[str]:
    """Descarga y parsea sitemaps para extraer URLs.

    Args:
        logger: La instancia del logger.
        base_origin: El origen base (ej. 'https://www.example.com').
        base_prefix: El prefijo de URL para filtrar (ej. 'https://www.example.com/es/').

    Returns:
        Una lista de URLs únicas encontradas en los sitemaps que coinciden con el prefijo."""
    urls: List[str] = []
    for sm in SITEMAP_URLS:
        try:
            resp = requests.get(sm, headers=DEFAULT_HEADERS, timeout=TIMEOUT, verify=VERIFY_TLS)
            logger.info(f"Sitemap GET {sm} -> {resp.status_code}")
            if resp.status_code == 200 and resp.text:
                # parse naive (sin XML deps) buscando <loc>...</loc>
                for line in resp.text.splitlines():
                    line = line.strip()
                    if line.startswith("<loc>") and line.endswith("</loc>"):
                        loc = line.replace("<loc>", "").replace("</loc>", "").strip()
                        if loc.startswith(base_prefix):
                            urls.append(loc)
        except Exception as e:
            logger.warning(f"Sitemap error {sm}: {e}")
    # deduplicate
    urls = sorted(set(urls))
    logger.info(f"Sitemap URLs filtradas por prefijo: {len(urls)}")
    return urls

# =========================== HIERARCHY BUILDER =========================== #

def insert_path(hroot: Dict, path_segments: List[str]):
    """Inserta una ruta de URL en el árbol de jerarquía.

    Args:
        hroot: El nodo raíz del diccionario de jerarquía.
        path_segments: Una lista de segmentos de la ruta de la URL."""
    node = hroot
    for seg in path_segments:
        if not seg:
            continue
        children = node.setdefault("children", {})
        node = children.setdefault(seg, {"__count": 0})
        node["__count"] = node.get("__count", 0) + 1


def hierarchy_to_d3(node: Dict, name: str = "/") -> Dict:
    """Convierte el formato de jerarquía interno a un formato compatible con D3.js.

    Args:
        node: El nodo actual en el árbol de jerarquía.
        name: El nombre del nodo actual.

    Returns: Un diccionario con la estructura que espera D3.js (name, children, value)."""
    out = {"name": name}
    children_map = node.get("children", {})
    if children_map:
        out["children"] = [hierarchy_to_d3(children_map[k], k) for k in sorted(children_map.keys())]
    else:
        out["value"] = node.get("__count", 1)
    return out

# =========================== MAIN CRAWLER =========================== #

def crawl():
    """Función principal que ejecuta el proceso de crawling."""
    logger = setup_logger()
    logger.info("Iniciando crawler")
    base_url = BASE_URL
    parsed_base = urlparse(base_url)
    origin = f"{parsed_base.scheme}://{parsed_base.netloc}"

    rp = robotparser.RobotFileParser()
    robots_url = urljoin(origin, "/robots.txt")
    if OBEY_ROBOTS:
        try:
            rp.set_url(robots_url)
            rp.read()
            logger.info(f"robots.txt leído: {robots_url}")
        except Exception as e:
            logger.warning(f"No se pudo leer robots.txt: {e}")

    session = requests.Session(); session.headers.update(DEFAULT_HEADERS)

    visited: Set[str] = set()
    q = deque([(base_url, None, 0)])
    hroot: Dict = {"__count": 0}

    # Seed opcional por sitemap (URLs bajo el prefijo del path base)
    if USE_SITEMAP:
        base_prefix = origin + urlparse(base_url).path
        sm_urls = fetch_sitemap_urls(logger, origin, base_prefix)
        for u in sm_urls:
            if u not in visited:
                q.append((u, base_url, 1))
                logger.debug(f"Seed sitemap: {u}")

    pages_count = 0

    os.makedirs("data", exist_ok=True)
    try:
        with open("data/pages.jsonl", "w", encoding="utf-8") as pages_fp, \
             open("data/edges.jsonl", "w", encoding="utf-8") as edges_fp, \
             open("data/errors.jsonl", "w", encoding="utf-8") as errors_fp:

            while q and pages_count < MAX_PAGES:
                url, parent, depth = q.popleft()
                logger.debug(f"Dequeued url={url} depth={depth} parent={parent}")

                if depth > MAX_DEPTH:
                    logger.debug(f"Saltado por DEPTH>{MAX_DEPTH}: {url}")
                    continue
                if not same_origin(base_url, url):
                    logger.debug(f"Saltado por origen distinto: {url}")
                    continue
                if url in visited:
                    logger.debug(f"Saltado por duplicado: {url}")
                    continue

                if OBEY_ROBOTS:
                    try:
                        allowed = rp.can_fetch(session.headers.get("User-Agent", "*"), url)
                        if not allowed:
                            logger.info(f"Bloqueado por robots.txt: {url}")
                            visited.add(url)
                            if RECORD_BLOCKED_URLS:
                                rec = PageRecord(url, None, "BLOQUEADA_POR_ROBOTS", "BLOQUEADA_POR_ROBOTS", None, parent, depth)
                                pages_fp.write(json.dumps(rec.__dict__, ensure_ascii=False) + "\n")
                                pages_count += 1
                            continue
                    except Exception as e:
                        logger.warning(f"Error verificando robots para {url}: {e}")

                status_code = None
                title = "SIN_TITULO"
                meta_description = "SIN_DESCRIPCION"
                canonical = None
                links_to_enqueue: List[str] = []

                try:
                    resp = session.get(url, timeout=TIMEOUT, allow_redirects=True, verify=VERIFY_TLS)
                    status_code = resp.status_code
                    logger.debug(f"GET {url} -> {status_code} {resp.headers.get('Content-Type','')}")

                    if is_html_response(resp) and resp.text:
                        soup = BeautifulSoup(resp.text, "html.parser")
                        title, meta_description = extract_meta(soup)
                        canonical = extract_canonical(soup)
                        for a in soup.find_all("a", href=True):
                            cand = normalize_url(resp.url, a["href"])
                            if not cand or not same_origin(origin, cand):
                                continue
                            links_to_enqueue.append(cand)
                    else:
                        logger.debug(f"No-HTML o sin cuerpo en {url}")
                except requests.RequestException as e:
                    logger.error(f"RequestException en {url}: {e}")
                    errors_fp.write(json.dumps({"url": url, "error": str(e)}, ensure_ascii=False) + "\n")

                visited.add(url)
                rec = PageRecord(url, status_code, title, meta_description, canonical, parent, depth)
                pages_fp.write(json.dumps(rec.__dict__, ensure_ascii=False) + "\n")
                pages_count += 1

                up = urlparse(url)
                segs = [seg for seg in up.path.split("/") if seg]
                insert_path(hroot, segs)

                for child in links_to_enqueue:
                    if child not in visited:
                        q.append((child, url, depth + 1))
                        edges_fp.write(json.dumps({"source": url, "target": child}, ensure_ascii=False) + "\n")
                        logger.debug(f"Enqueued child {child} (from {url})")

                time.sleep(DELAY)

    except Exception as e:
        logger.critical(f"El crawler ha fallado con un error inesperado: {e}", exc_info=True)
    finally:
        logger.info("Proceso de crawling finalizado o interrumpido.")

    d3tree = hierarchy_to_d3(hroot, name=urlparse(base_url).netloc)
    with open("data/hierarchy.json", "w", encoding="utf-8") as f:
        json.dump(d3tree, f, ensure_ascii=False, indent=2)

    logger.info(f"Crawl finished: {pages_count} pages. Outputs in ./data/")

# =========================== ENTRY POINT =========================== #

if __name__ == "__main__":
    crawl()
