#!/usr/bin/env python3
"""
Site Crawler asíncrono — Banco de Bogotá (configurable)

Mejoras frente a la versión anterior:
- Concurrencia real con asyncio + httpx (HTTP/2, keep-alive, connection pooling)
- Reintentos con backoff exponencial ante 5xx / errores de red
- Parser lxml (más rápido y tolerante que html.parser)
- Sitemap robusto: descubre desde robots.txt, soporta <sitemapindex>, .xml.gz
- Metadatos extendidos: OG, Twitter Cards, JSON-LD, h1, lang, robots,
  word_count, content_hash, response_time_ms, content_length, final_url,
  redirected, n_internal_links, n_external_links, n_images
- Filtrado por extensión (skip de PDFs/imagenes/etc), strip de tracking params
- Resumibilidad opcional desde data/pages.jsonl previo
- Progreso visible con tqdm

Outputs (streaming JSONL + árbol final):
  data/pages.jsonl, data/edges.jsonl, data/errors.jsonl, data/hierarchy.json
"""
from __future__ import annotations

import asyncio
import gzip
import hashlib
import json
import logging
import os
import re
import time
from collections import deque
from dataclasses import asdict, dataclass, field
from logging.handlers import RotatingFileHandler
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse, parse_qsl, urlencode
import urllib.robotparser as robotparser
import xml.etree.ElementTree as ET

import httpx
from bs4 import BeautifulSoup
from tqdm import tqdm

# =========================== CONFIGURACIÓN =========================== #

BASE_URL = "https://www.bancodebogota.com/"
MAX_PAGES = float("inf")       # float('inf') = ilimitado
MAX_DEPTH = 8
CONCURRENCY = 16               # peticiones simultáneas (ajustar según servidor)
PER_HOST_DELAY = 0.0           # delay artificial por petición (0 = sin throttle extra)
TIMEOUT = 20.0
VERIFY_TLS = True
HTTP2 = True
OBEY_ROBOTS = False

# Reintentos
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 0.8       # segundos; espera = base * 2^intento

# Sitemap
USE_SITEMAP = True
SITEMAP_URLS: List[str] = [
    "https://www.bancodebogota.com/sitemap.xml",
    "https://www.bancodebogota.com/personas/sitemap.xml",
    "https://www.bancodebogota.com/atencion-al-cliente/sitemap.xml",
    "https://www.bancodebogota.com/empresas/sitemap.xml",
    "https://bancodebogota.com/sitemap.xml",
]
DISCOVER_SITEMAP_FROM_ROBOTS = True

# Semillas adicionales — URLs que se garantizan en la cola aunque no
# estén enlazadas desde BASE_URL ni en sitemap.
EXTRA_SEEDS: List[str] = [
    "https://www.bancodebogota.com/personas",
    "https://www.bancodebogota.com/empresas",
    "https://www.bancodebogota.com/pymes",
    "https://www.bancodebogota.com/atencion-al-cliente",
    "https://www.bancodebogota.com/atencion-al-cliente/instructivos",
    # Apex domain (sin www) — se cubre por same_origin pero lo encolamos
    # explícito por si la home apex tiene enlaces no presentes en www.
    "https://bancodebogota.com/",
]
RECORD_BLOCKED_URLS = True

# Resumibilidad — si True, lee data/pages.jsonl previo y omite esas URLs
RESUME = False

# Filtrado por extensión (no se siguen ni se descargan)
SKIP_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".bmp",
    ".mp3", ".mp4", ".wav", ".avi", ".mov", ".webm",
    ".css", ".js", ".woff", ".woff2", ".ttf", ".eot",
}

# Tracking params que se eliminan al normalizar URLs (mejora dedup)
TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "msclkid", "mc_cid", "mc_eid", "_ga",
}

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
DEFAULT_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
}

DEBUG = False
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "crawler.log")

# =========================== DATACLASSES =========================== #

@dataclass
class PageRecord:
    url: str
    final_url: Optional[str]
    redirected: bool
    status_code: Optional[int]
    response_time_ms: Optional[int]
    content_length: Optional[int]
    title: str
    h1: Optional[str]
    lang: Optional[str]
    meta_description: str
    meta_robots: Optional[str]
    canonical: Optional[str]
    og: Dict[str, str] = field(default_factory=dict)
    twitter: Dict[str, str] = field(default_factory=dict)
    jsonld_types: List[str] = field(default_factory=list)
    word_count: int = 0
    content_hash: Optional[str] = None
    n_internal_links: int = 0
    n_external_links: int = 0
    n_images: int = 0
    parent_url: Optional[str] = None
    depth: int = 0

# =========================== LOGGING =========================== #

def setup_logger() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)
    logger = logging.getLogger("crawler")
    logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fmt)
        fh = RotatingFileHandler(LOG_FILE, maxBytes=2_000_000, backupCount=3, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fmt)
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger

# =========================== URL HELPERS =========================== #

def normalize_url(base: str, href: str) -> Optional[str]:
    try:
        absu = urljoin(base, href)
        absu, _ = urldefrag(absu)
        p = urlparse(absu)
        if p.scheme not in ("http", "https"):
            return None
        # Strip tracking params
        if p.query:
            kept = [(k, v) for k, v in parse_qsl(p.query, keep_blank_values=True)
                    if k.lower() not in TRACKING_PARAMS]
            new_q = urlencode(kept)
            p = p._replace(query=new_q)
        # Lowercase host
        p = p._replace(netloc=p.netloc.lower())
        return urlunparse(p)
    except Exception:
        return None


def _canonical_host(netloc: str) -> str:
    """Normaliza host para comparaciones de origen (apex == www)."""
    h = netloc.lower()
    if h.startswith("www."):
        h = h[4:]
    return h


def same_origin(a: str, b: str) -> bool:
    pa, pb = urlparse(a), urlparse(b)
    return (pa.scheme, _canonical_host(pa.netloc)) == (pb.scheme, _canonical_host(pb.netloc))


def has_skip_extension(url: str) -> bool:
    path = urlparse(url).path.lower()
    return any(path.endswith(ext) for ext in SKIP_EXTENSIONS)

# =========================== METADATA EXTRACTION =========================== #

WORD_RE = re.compile(r"\w+", re.UNICODE)


def _attr_str(tag, key: str) -> str:
    """Obtiene un atributo como str plano (bs4 a veces devuelve listas)."""
    if not tag:
        return ""
    v = tag.get(key)
    if v is None:
        return ""
    if isinstance(v, list):
        return " ".join(str(x) for x in v).strip()
    return str(v).strip()


def extract_metadata(soup: BeautifulSoup) -> Dict:
    # Title
    title = soup.title.string.strip() if soup.title and soup.title.string else "SIN_TITULO"

    # Lang
    lang: Optional[str] = None
    if soup.html:
        lang_val = _attr_str(soup.html, "lang")
        lang = lang_val or None

    # H1 (primer h1)
    h1 = None
    h1_tag = soup.find("h1")
    if h1_tag and h1_tag.get_text(strip=True):
        h1 = h1_tag.get_text(strip=True)[:300]

    # Meta description
    desc_tag = (
        soup.find("meta", attrs={"name": "description"})
        or soup.find("meta", attrs={"name": "Description"})
        or soup.find("meta", attrs={"property": "og:description"})
    )
    meta_description = _attr_str(desc_tag, "content") or "SIN_DESCRIPCION"

    # Meta robots
    robots_tag = soup.find("meta", attrs={"name": re.compile(r"^robots$", re.I)})
    meta_robots = _attr_str(robots_tag, "content") or None

    # Canonical
    canonical: Optional[str] = None
    for link in soup.find_all("link"):
        rel_val = link.get("rel")
        rels: List[str] = []
        if isinstance(rel_val, list):
            rels = [str(x).lower() for x in rel_val]
        elif isinstance(rel_val, str):
            rels = [rel_val.lower()]
        if "canonical" in rels:
            canonical = _attr_str(link, "href") or None
            break

    # Open Graph
    og: Dict[str, str] = {}
    for tag in soup.find_all("meta", attrs={"property": re.compile(r"^og:", re.I)}):
        key = _attr_str(tag, "property")[3:]
        val = _attr_str(tag, "content")
        if key and val:
            og[key] = val

    # Twitter Cards
    twitter: Dict[str, str] = {}
    for tag in soup.find_all("meta", attrs={"name": re.compile(r"^twitter:", re.I)}):
        key = _attr_str(tag, "name")[8:]
        val = _attr_str(tag, "content")
        if key and val:
            twitter[key] = val

    # JSON-LD types
    jsonld_types: List[str] = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "{}")
            items = data if isinstance(data, list) else [data]
            for item in items:
                if isinstance(item, dict):
                    t = item.get("@type")
                    if isinstance(t, list):
                        jsonld_types.extend(str(x) for x in t)
                    elif t:
                        jsonld_types.append(str(t))
        except Exception:
            continue

    # Word count + content hash (sobre texto visible)
    text = soup.get_text(separator=" ", strip=True)
    word_count = len(WORD_RE.findall(text))
    content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()[:32]

    # Images
    n_images = len(soup.find_all("img"))

    return {
        "title": title,
        "lang": lang,
        "h1": h1,
        "meta_description": meta_description,
        "meta_robots": meta_robots,
        "canonical": canonical,
        "og": og,
        "twitter": twitter,
        "jsonld_types": jsonld_types,
        "word_count": word_count,
        "content_hash": content_hash,
        "n_images": n_images,
    }

# =========================== SITEMAP =========================== #

NS_RE = re.compile(r"^\{[^}]+\}")


def _strip_ns(tag: str) -> str:
    return NS_RE.sub("", tag)


async def fetch_bytes(client: httpx.AsyncClient, url: str) -> Optional[bytes]:
    try:
        r = await client.get(url, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        data = r.content
        if url.lower().endswith(".gz") or r.headers.get("Content-Type", "").lower().startswith("application/x-gzip"):
            try:
                data = gzip.decompress(data)
            except Exception:
                pass
        return data
    except Exception:
        return None


async def parse_sitemap_recursive(
    client: httpx.AsyncClient,
    sitemap_url: str,
    base_prefix: str,
    found: Set[str],
    logger: logging.Logger,
    depth: int = 0,
) -> None:
    if depth > 3:
        return
    data = await fetch_bytes(client, sitemap_url)
    if not data:
        logger.warning(f"Sitemap inaccesible: {sitemap_url}")
        return
    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        logger.warning(f"Sitemap parse error {sitemap_url}: {e}")
        return

    tag = _strip_ns(root.tag).lower()
    if tag == "sitemapindex":
        sub_urls = []
        for sm in root:
            for child in sm:
                if _strip_ns(child.tag).lower() == "loc" and child.text:
                    sub_urls.append(child.text.strip())
        logger.info(f"Sitemap index {sitemap_url}: {len(sub_urls)} sub-sitemaps")
        await asyncio.gather(*[
            parse_sitemap_recursive(client, su, base_prefix, found, logger, depth + 1)
            for su in sub_urls
        ])
    elif tag == "urlset":
        added = 0
        for u in root:
            for child in u:
                if _strip_ns(child.tag).lower() == "loc" and child.text:
                    loc = child.text.strip()
                    # Aceptar cualquier URL del mismo dominio canónico
                    # (apex y www se consideran el mismo origen).
                    if same_origin(base_prefix, loc):
                        found.add(loc)
                        added += 1
        logger.info(f"Sitemap {sitemap_url}: +{added} URLs")


async def discover_sitemaps_from_robots(client: httpx.AsyncClient, origin: str, logger: logging.Logger) -> List[str]:
    out: List[str] = []
    try:
        r = await client.get(urljoin(origin, "/robots.txt"), timeout=TIMEOUT)
        if r.status_code == 200:
            for line in r.text.splitlines():
                if line.lower().startswith("sitemap:"):
                    out.append(line.split(":", 1)[1].strip())
    except Exception as e:
        logger.debug(f"robots.txt no leído para sitemap discovery: {e}")
    return out


async def collect_sitemap_urls(client: httpx.AsyncClient, origin: str, base_prefix: str, logger: logging.Logger) -> List[str]:
    candidates: List[str] = list(SITEMAP_URLS)
    if DISCOVER_SITEMAP_FROM_ROBOTS:
        candidates.extend(await discover_sitemaps_from_robots(client, origin, logger))
    candidates = [c for c in {x.strip() for x in candidates} if c]
    found: Set[str] = set()
    await asyncio.gather(*[
        parse_sitemap_recursive(client, sm, base_prefix, found, logger)
        for sm in candidates
    ])
    logger.info(f"Sitemap total URLs únicas: {len(found)}")
    return sorted(found)

# =========================== HIERARCHY =========================== #

def insert_path(hroot: Dict, segs: List[str]) -> None:
    node = hroot
    for seg in segs:
        if not seg:
            continue
        children = node.setdefault("children", {})
        node = children.setdefault(seg, {"__count": 0})
        node["__count"] = node.get("__count", 0) + 1


def hierarchy_to_d3(node: Dict, name: str = "/") -> Dict:
    out: Dict = {"name": name}
    cm = node.get("children", {})
    if cm:
        out["children"] = [hierarchy_to_d3(cm[k], k) for k in sorted(cm.keys())]
    else:
        out["value"] = node.get("__count", 1)
    return out

# =========================== FETCH (con reintentos) =========================== #

async def fetch_with_retry(client: httpx.AsyncClient, url: str) -> Tuple[Optional[httpx.Response], Optional[str], int]:
    """Devuelve (response | None, error | None, elapsed_ms)."""
    last_err = None
    t0 = time.perf_counter()
    for attempt in range(MAX_RETRIES + 1):
        try:
            r = await client.get(url, timeout=TIMEOUT, follow_redirects=True)
            elapsed = int((time.perf_counter() - t0) * 1000)
            # Reintentar 5xx
            if 500 <= r.status_code < 600 and attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BACKOFF_BASE * (2 ** attempt))
                continue
            return r, None, elapsed
        except (httpx.TimeoutException, httpx.TransportError) as e:
            last_err = f"{type(e).__name__}: {e}"
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BACKOFF_BASE * (2 ** attempt))
                continue
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            break
    elapsed = int((time.perf_counter() - t0) * 1000)
    return None, last_err, elapsed

# =========================== CRAWLER ASÍNCRONO =========================== #

async def crawl_async() -> None:
    logger = setup_logger()
    logger.info("Iniciando crawler asíncrono")

    parsed_base = urlparse(BASE_URL)
    origin = f"{parsed_base.scheme}://{parsed_base.netloc}"
    base_prefix = origin + parsed_base.path

    # robots.txt
    rp = robotparser.RobotFileParser()
    if OBEY_ROBOTS:
        try:
            rp.set_url(urljoin(origin, "/robots.txt"))
            rp.read()
            logger.info("robots.txt cargado")
        except Exception as e:
            logger.warning(f"No se pudo leer robots.txt: {e}")

    # Cliente httpx con HTTP/2 + pool
    limits = httpx.Limits(max_connections=CONCURRENCY * 2, max_keepalive_connections=CONCURRENCY)
    async with httpx.AsyncClient(
        headers=DEFAULT_HEADERS,
        http2=HTTP2,
        verify=VERIFY_TLS,
        limits=limits,
        timeout=TIMEOUT,
    ) as client:

        # Resumibilidad
        visited: Set[str] = set()
        if RESUME and os.path.exists("data/pages.jsonl"):
            with open("data/pages.jsonl", "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        rec = json.loads(line)
                        visited.add(rec["url"])
                    except Exception:
                        pass
            logger.info(f"RESUME: {len(visited)} URLs previas omitidas")

        # Cola inicial
        q: deque = deque([(BASE_URL, None, 0)])

        # Semillas extra (URLs garantizadas)
        for s in EXTRA_SEEDS:
            sn = normalize_url(BASE_URL, s)
            if sn and sn not in visited:
                q.append((sn, BASE_URL, 1))
                logger.debug(f"Extra seed: {sn}")

        # Sitemap seeding
        if USE_SITEMAP:
            sm_urls = await collect_sitemap_urls(client, origin, base_prefix, logger)
            for u in sm_urls:
                un = normalize_url(BASE_URL, u)
                if un and un not in visited:
                    q.append((un, BASE_URL, 1))

        hroot: Dict = {"__count": 0}
        sem = asyncio.Semaphore(CONCURRENCY)
        pages_count = 0
        write_lock = asyncio.Lock()

        os.makedirs("data", exist_ok=True)
        mode = "a" if RESUME else "w"
        pages_fp = open("data/pages.jsonl", mode, encoding="utf-8")
        edges_fp = open("data/edges.jsonl", mode, encoding="utf-8")
        errors_fp = open("data/errors.jsonl", mode, encoding="utf-8")

        pbar = tqdm(desc="Crawling", unit="pg")

        async def process(url: str, parent: Optional[str], depth: int) -> List[Tuple[str, str, int]]:
            """Procesa una URL y devuelve los hijos a encolar."""
            nonlocal pages_count
            children: List[Tuple[str, str, int]] = []

            if depth > MAX_DEPTH or not same_origin(BASE_URL, url) or has_skip_extension(url):
                return children
            if OBEY_ROBOTS:
                try:
                    if not rp.can_fetch(USER_AGENT, url):
                        if RECORD_BLOCKED_URLS:
                            blocked = PageRecord(
                                url=url, final_url=None, redirected=False,
                                status_code=None, response_time_ms=None, content_length=None,
                                title="BLOQUEADA_POR_ROBOTS", h1=None, lang=None,
                                meta_description="BLOQUEADA_POR_ROBOTS", meta_robots=None,
                                canonical=None, parent_url=parent, depth=depth,
                            )
                            async with write_lock:
                                pages_fp.write(json.dumps(asdict(blocked), ensure_ascii=False) + "\n")
                                pages_count += 1
                        return children
                except Exception:
                    pass

            async with sem:
                if PER_HOST_DELAY > 0:
                    await asyncio.sleep(PER_HOST_DELAY)
                resp, err, elapsed_ms = await fetch_with_retry(client, url)

            if err:
                async with write_lock:
                    errors_fp.write(json.dumps({"url": url, "error": err}, ensure_ascii=False) + "\n")
                # Aún así dejamos rastro en pages
                rec = PageRecord(
                    url=url, final_url=None, redirected=False,
                    status_code=None, response_time_ms=elapsed_ms, content_length=None,
                    title="ERROR_RED", h1=None, lang=None,
                    meta_description=err, meta_robots=None,
                    canonical=None, parent_url=parent, depth=depth,
                )
                async with write_lock:
                    pages_fp.write(json.dumps(asdict(rec), ensure_ascii=False) + "\n")
                    pages_count += 1
                    pbar.update(1)
                return children

            assert resp is not None
            final_url = str(resp.url)
            redirected = final_url != url
            ctype = resp.headers.get("Content-Type", "").lower()
            content_length = len(resp.content) if resp.content else 0

            meta = {
                "title": "SIN_TITULO", "h1": None, "lang": None,
                "meta_description": "SIN_DESCRIPCION", "meta_robots": None,
                "canonical": None, "og": {}, "twitter": {}, "jsonld_types": [],
                "word_count": 0, "content_hash": None, "n_images": 0,
            }
            n_internal = 0
            n_external = 0

            if ("text/html" in ctype or "application/xhtml" in ctype) and resp.text:
                try:
                    soup = BeautifulSoup(resp.text, "lxml")
                except Exception:
                    soup = BeautifulSoup(resp.text, "html.parser")
                meta = extract_metadata(soup)
                for a in soup.find_all("a", href=True):
                    href = _attr_str(a, "href")
                    if not href:
                        continue
                    cand = normalize_url(final_url, href)
                    if not cand:
                        continue
                    if same_origin(origin, cand):
                        n_internal += 1
                        if cand not in visited and not has_skip_extension(cand):
                            children.append((cand, url, depth + 1))
                    else:
                        n_external += 1

            rec = PageRecord(
                url=url,
                final_url=final_url,
                redirected=redirected,
                status_code=resp.status_code,
                response_time_ms=elapsed_ms,
                content_length=content_length,
                title=meta["title"],
                h1=meta["h1"],
                lang=meta["lang"],
                meta_description=meta["meta_description"],
                meta_robots=meta["meta_robots"],
                canonical=meta["canonical"],
                og=meta["og"],
                twitter=meta["twitter"],
                jsonld_types=meta["jsonld_types"],
                word_count=meta["word_count"],
                content_hash=meta["content_hash"],
                n_internal_links=n_internal,
                n_external_links=n_external,
                n_images=meta["n_images"],
                parent_url=parent,
                depth=depth,
            )

            async with write_lock:
                pages_fp.write(json.dumps(asdict(rec), ensure_ascii=False) + "\n")
                pages_count += 1
                pbar.update(1)
                # Solo se incluyen en el árbol las páginas válidas (2xx/3xx).
                # Las 404 / 4xx / 5xx no deben aparecer en la jerarquía.
                if resp.status_code is not None and 200 <= resp.status_code < 400:
                    segs = [s for s in urlparse(url).path.split("/") if s]
                    insert_path(hroot, segs)
                for c_url, _, _ in children:
                    edges_fp.write(json.dumps({"source": url, "target": c_url}, ensure_ascii=False) + "\n")

            return children

        # Loop BFS por "olas" — cada ola lanza tareas concurrentes
        try:
            while q and pages_count < MAX_PAGES:
                batch: List[Tuple[str, Optional[str], int]] = []
                while q and len(batch) < CONCURRENCY * 4:
                    url, parent, depth = q.popleft()
                    if url in visited:
                        continue
                    visited.add(url)
                    batch.append((url, parent, depth))

                if not batch:
                    continue

                tasks = [process(u, p, d) for (u, p, d) in batch]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                for res in results:
                    if isinstance(res, BaseException):
                        logger.error(f"Task exception: {res}")
                        continue
                    assert isinstance(res, list)
                    for child in res:
                        c_url, c_parent, c_depth = child
                        if c_url not in visited:
                            q.append((c_url, c_parent, c_depth))

        except KeyboardInterrupt:
            logger.warning("Interrumpido por usuario")
        finally:
            pbar.close()
            pages_fp.close(); edges_fp.close(); errors_fp.close()

            # Árbol final para D3
            d3tree = hierarchy_to_d3(hroot, name=parsed_base.netloc)
            with open("data/hierarchy.json", "w", encoding="utf-8") as f:
                json.dump(d3tree, f, ensure_ascii=False, indent=2)
            logger.info(f"Crawl finalizado: {pages_count} páginas. Outputs en ./data/")


# =========================== ENTRY POINT =========================== #

if __name__ == "__main__":
    asyncio.run(crawl_async())
