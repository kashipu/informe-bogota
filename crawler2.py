#!/usr/bin/env python3
"""
crawler2.py - WPS Redirect Mapper

Lee el output del crawler (data/pages.jsonl) y mapea todas las URLs que
contienen "/wps" a sus destinos finales de redirección.

Output:
- data/wps_redirects.json: Mapeo simple de URL origen → URL destino

Uso:
    python crawler2.py

Requisitos: requests
    pip install requests
"""
from __future__ import annotations
import json
import os
import time
import logging
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict
from urllib.parse import urlparse

import requests

# ====================== CONFIG ====================== #
INPUT_PAGES = os.path.join("data", "pages.jsonl")
OUT_JSON = os.path.join("data", "wps_redirects.json")

TIMEOUT = 20.0
VERIFY_TLS = True
DELAY = 0.25        # segundos entre requests (politeness)
MAX_URLS = None     # None = todas; o pon un entero para limitar en pruebas

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
}

LOG_LEVEL = logging.INFO

# ====================== MODELOS ====================== #
@dataclass
class RedirectMapping:
    """Mapeo simple de URL origen con /wps a URL destino final."""
    source_url: str
    final_url: Optional[str]
    has_redirect: bool
    error: Optional[str] = None

# ====================== LOGGING ====================== #
logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("wps")

# ====================== HELPERS ====================== #
def has_wps(url: str) -> bool:
    try:
        return "/wps" in urlparse(url).path
    except Exception:
        return "/wps" in (url or "")

# ====================== MAIN ====================== #
def main():
    """Mapea URLs con /wps a sus destinos finales de redirección."""
    if not os.path.exists(INPUT_PAGES):
        raise FileNotFoundError(f"No existe {INPUT_PAGES}. Corre primero el crawler para generar pages.jsonl")

    os.makedirs("data", exist_ok=True)

    redirects: List[Dict] = []
    total_processed = 0
    total_with_redirect = 0
    total_errors = 0

    logger.info("Iniciando mapeo de redirecciones /wps...")

    with open(INPUT_PAGES, "r", encoding="utf-8") as f_in:
        for line in f_in:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue

            url = rec.get("url")
            if not url or not has_wps(url):
                continue

            if MAX_URLS and total_processed >= MAX_URLS:
                break

            total_processed += 1
            error: Optional[str] = None
            final_url: Optional[str] = None
            has_redirect = False

            try:
                logger.debug(f"Verificando: {url}")
                resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True, verify=VERIFY_TLS)
                final_url = resp.url
                has_redirect = (final_url != url)

                if has_redirect:
                    total_with_redirect += 1
                    logger.info(f"Redirección: {url} → {final_url}")

            except requests.RequestException as e:
                error = str(e)
                total_errors += 1
                logger.error(f"Error en {url}: {error}")

            mapping = RedirectMapping(
                source_url=url,
                final_url=final_url,
                has_redirect=has_redirect,
                error=error
            )
            redirects.append(asdict(mapping))

            time.sleep(DELAY)

    # Guardar resultado
    output = {
        "summary": {
            "total_urls_checked": total_processed,
            "urls_with_redirect": total_with_redirect,
            "urls_without_redirect": total_processed - total_with_redirect - total_errors,
            "errors": total_errors
        },
        "redirects": redirects
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    logger.info(f"\n{'='*60}")
    logger.info(f"Resumen:")
    logger.info(f"  URLs con /wps verificadas: {total_processed}")
    logger.info(f"  URLs con redirección: {total_with_redirect}")
    logger.info(f"  URLs sin redirección: {total_processed - total_with_redirect - total_errors}")
    logger.info(f"  Errores: {total_errors}")
    logger.info(f"{'='*60}")
    logger.info(f"Resultados guardados en: {OUT_JSON}")


if __name__ == "__main__":
    main()
