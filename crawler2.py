#!/usr/bin/env python3
"""
crawler2.py — WPS Redirect Mapper (async)

Lee data/pages.jsonl y mapea todas las URLs que contienen "/wps" a sus
destinos finales, capturando además la cadena completa de saltos.

Mejoras frente a la versión anterior:
- Concurrencia con asyncio + httpx (HTTP/2 + connection pooling)
- HEAD-first con fallback a GET (ahorra ancho de banda)
- Reintentos con backoff exponencial
- Captura de toda la cadena de redirecciones (status + URL en cada salto)
- Clasificación del tipo de redirección (3xx, meta-refresh, JS, ninguna)
- Progreso visible con tqdm
- Dedup de URLs origen idénticas

Output: data/wps_redirects.json
"""
from __future__ import annotations

import asyncio
import csv
import json
import logging
import os
import re
import time
from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional
from urllib.parse import urlparse

import httpx
from tqdm import tqdm

# ====================== CONFIG ====================== #
INPUT_PAGES = os.path.join("data", "pages.jsonl")
OUT_JSON = os.path.join("data", "wps_redirects.json")
OUT_MIGRATION_CSV = os.path.join("data", "wps_migration_map.csv")

TIMEOUT = 20.0
VERIFY_TLS = True
HTTP2 = True
CONCURRENCY = 16
MAX_URLS: Optional[int] = None     # None = todas; entero para pruebas
MAX_RETRIES = 2
RETRY_BACKOFF_BASE = 0.6
HEAD_FIRST = True                  # intentar HEAD antes que GET
MAX_REDIRECT_HOPS = 20

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
}

LOG_LEVEL = logging.INFO

# ====================== MODELOS ====================== #

@dataclass
class RedirectHop:
    url: str
    status_code: int


@dataclass
class RedirectMapping:
    source_url: str
    final_url: Optional[str]
    has_redirect: bool
    redirects_out_of_wps: bool       # True si el final ya NO contiene /wps (migrada)
    still_in_wps: bool               # True si el final SIGUE conteniendo /wps
    redirect_type: str               # "http_3xx" | "meta_refresh" | "js" | "none" | "error"
    n_hops: int
    chain: List[Dict] = field(default_factory=list)
    final_status: Optional[int] = None
    elapsed_ms: Optional[int] = None
    error: Optional[str] = None


# ====================== LOGGING ====================== #
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("wps")

# ====================== HELPERS ====================== #

META_REFRESH_RE = re.compile(
    r"""<meta[^>]+http-equiv\s*=\s*["']?refresh["']?[^>]+content\s*=\s*["']?\s*\d+\s*;\s*url\s*=\s*([^"'>\s]+)""",
    re.IGNORECASE,
)
JS_LOCATION_RE = re.compile(
    r"""(?:window\.)?location(?:\.href)?\s*=\s*["']([^"']+)["']""",
    re.IGNORECASE,
)


def has_wps(url: str) -> bool:
    try:
        return "/wps" in urlparse(url).path
    except Exception:
        return "/wps" in (url or "")


def detect_body_redirect(body: str) -> Optional[str]:
    """Detecta meta-refresh o location JS en el body. Devuelve la URL destino si la hay."""
    m = META_REFRESH_RE.search(body)
    if m:
        return m.group(1).strip()
    m = JS_LOCATION_RE.search(body)
    if m:
        return m.group(1).strip()
    return None


async def fetch_one(client: httpx.AsyncClient, method: str, url: str) -> Optional[httpx.Response]:
    for attempt in range(MAX_RETRIES + 1):
        try:
            r = await client.request(method, url, timeout=TIMEOUT, follow_redirects=False)
            return r
        except (httpx.TimeoutException, httpx.TransportError):
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BACKOFF_BASE * (2 ** attempt))
                continue
        except Exception:
            return None
    return None


async def trace_redirects(client: httpx.AsyncClient, url: str) -> RedirectMapping:
    """Sigue manualmente la cadena de redirecciones HTTP + body (meta/JS)."""
    t0 = time.perf_counter()
    chain: List[Dict] = []
    redirect_type = "none"
    current = url
    visited = {current}
    final_status: Optional[int] = None
    error: Optional[str] = None

    for hop in range(MAX_REDIRECT_HOPS):
        # HEAD primero (cuando aplica)
        r: Optional[httpx.Response] = None
        if HEAD_FIRST and hop == 0:
            r = await fetch_one(client, "HEAD", current)
            # Algunos servidores no soportan HEAD bien; si no es 2xx/3xx, caemos a GET
            if r is None or (r.status_code >= 400 and r.status_code != 405):
                r = await fetch_one(client, "GET", current)
        else:
            r = await fetch_one(client, "GET", current)

        if r is None:
            error = "request_failed"
            redirect_type = "error"
            break

        chain.append({"url": current, "status_code": r.status_code})
        final_status = r.status_code

        # Redirección HTTP 3xx
        if 300 <= r.status_code < 400 and "location" in r.headers:
            next_url = str(httpx.URL(current).join(r.headers["location"]))
            if next_url in visited:
                error = "redirect_loop"
                break
            visited.add(next_url)
            current = next_url
            redirect_type = "http_3xx"
            continue

        # 200 OK — revisar body por meta-refresh / JS
        if r.status_code == 200 and "text/html" in r.headers.get("content-type", "").lower():
            # Si veníamos de HEAD, hacer GET ahora para inspeccionar body
            if HEAD_FIRST and hop == 0 and not r.content:
                rg = await fetch_one(client, "GET", current)
                if rg is not None:
                    r = rg
                    chain[-1]["status_code"] = r.status_code
                    final_status = r.status_code
            body = r.text or ""
            target = detect_body_redirect(body)
            if target:
                next_url = str(httpx.URL(current).join(target))
                if next_url in visited:
                    break
                visited.add(next_url)
                current = next_url
                redirect_type = "meta_refresh" if META_REFRESH_RE.search(body) else "js"
                continue
        break

    elapsed_ms = int((time.perf_counter() - t0) * 1000)
    final_url = current
    has_redirect = final_url != url and redirect_type != "error"

    # Análisis clave: ¿la /wps original ya migró fuera de /wps?
    if redirect_type == "error":
        redirects_out_of_wps = False
        still_in_wps = False
    else:
        final_has_wps = has_wps(final_url)
        redirects_out_of_wps = has_redirect and not final_has_wps
        still_in_wps = final_has_wps

    return RedirectMapping(
        source_url=url,
        final_url=final_url if redirect_type != "error" else None,
        has_redirect=has_redirect,
        redirects_out_of_wps=redirects_out_of_wps,
        still_in_wps=still_in_wps,
        redirect_type=redirect_type,
        n_hops=max(0, len(chain) - 1),
        chain=chain,
        final_status=final_status,
        elapsed_ms=elapsed_ms,
        error=error,
    )


# ====================== MAIN ====================== #

async def run() -> None:
    if not os.path.exists(INPUT_PAGES):
        raise FileNotFoundError(
            f"No existe {INPUT_PAGES}. Corre primero el crawler para generar pages.jsonl"
        )
    os.makedirs("data", exist_ok=True)

    # Cargar URLs con /wps (dedup)
    urls: List[str] = []
    seen = set()
    with open(INPUT_PAGES, "r", encoding="utf-8") as f_in:
        for line in f_in:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            url = rec.get("url")
            if not url or not has_wps(url) or url in seen:
                continue
            seen.add(url)
            urls.append(url)
            if MAX_URLS and len(urls) >= MAX_URLS:
                break

    logger.info(f"Total URLs con /wps a verificar: {len(urls)}")

    limits = httpx.Limits(max_connections=CONCURRENCY * 2, max_keepalive_connections=CONCURRENCY)
    sem = asyncio.Semaphore(CONCURRENCY)
    results: List[RedirectMapping] = []

    async with httpx.AsyncClient(
        headers=HEADERS, http2=HTTP2, verify=VERIFY_TLS, limits=limits, timeout=TIMEOUT,
    ) as client:

        async def worker(u: str) -> RedirectMapping:
            async with sem:
                return await trace_redirects(client, u)

        pbar = tqdm(total=len(urls), desc="WPS redirects", unit="url")
        tasks = [asyncio.create_task(worker(u)) for u in urls]
        for fut in asyncio.as_completed(tasks):
            res = await fut
            results.append(res)
            pbar.update(1)
        pbar.close()

    # Clasificación según la intención real del análisis:
    #  - migradas: /wps original que ahora redirige a URL SIN /wps  (objetivo cumplido)
    #  - still_in_wps_redirect: redirige pero el destino TODAVÍA tiene /wps (no migrada del todo)
    #  - no_redirect: sigue sirviendo /wps directamente sin redirección
    #  - errors: no se pudo verificar
    migrated = [r for r in results if r.redirects_out_of_wps]
    still_wps_with_redirect = [r for r in results if r.has_redirect and r.still_in_wps]
    no_redirect = [r for r in results if not r.has_redirect and r.redirect_type != "error"]
    errors = [r for r in results if r.redirect_type == "error"]

    by_type: Dict[str, int] = {}
    for r in results:
        by_type[r.redirect_type] = by_type.get(r.redirect_type, 0) + 1

    total = len(results)

    # Mapa limpio de migraciones: de qué /wps → a qué URL limpia
    # Ordenado por URL origen para que el diff entre corridas sea legible.
    migration_map = sorted(
        [
            {
                "from": r.source_url,
                "to": r.final_url,
                "n_hops": r.n_hops,
                "redirect_type": r.redirect_type,
                "final_status": r.final_status,
            }
            for r in migrated
        ],
        key=lambda x: x["from"],
    )

    # Pendientes: /wps que todavía no migraron (con detalle mínimo)
    pending_map = sorted(
        [
            {
                "url": r.source_url,
                "final_url": r.final_url,
                "has_redirect": r.has_redirect,
                "final_status": r.final_status,
            }
            for r in (still_wps_with_redirect + no_redirect)
        ],
        key=lambda x: x["url"],
    )

    output = {
        "summary": {
            "total_urls_checked": total,
            "migrated_out_of_wps": len(migrated),
            "still_in_wps_with_redirect": len(still_wps_with_redirect),
            "no_redirect_still_wps": len(no_redirect),
            "errors": len(errors),
            "migration_percent": round(100 * len(migrated) / total, 2) if total else 0.0,
            "by_redirect_type": by_type,
        },
        # Mapa simple from → to de las páginas YA migradas (lo que pediste)
        "migration_map": migration_map,
        # Pendientes de migrar
        "pending_migration": pending_map,
        # Versiones detalladas (cadena completa, tiempos, etc.) por si se necesitan
        "migrated": [asdict(r) for r in migrated],
        "still_in_wps": [asdict(r) for r in (still_wps_with_redirect + no_redirect)],
        "errors": [asdict(r) for r in errors],
        # Compatibilidad: lista completa
        "redirects": [asdict(r) for r in results],
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # CSV con el mapa de migración (from,to) — ideal para Excel/reporting
    with open(OUT_MIGRATION_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["from_wps_url", "to_clean_url", "n_hops", "redirect_type", "final_status"])
        for m in migration_map:
            w.writerow([m["from"], m["to"], m["n_hops"], m["redirect_type"], m["final_status"]])

    logger.info("=" * 60)
    logger.info(f"  URLs con /wps verificadas:     {total}")
    logger.info(f"  Migradas (final SIN /wps):     {len(migrated)}  ({output['summary']['migration_percent']}%)")
    logger.info(f"  Redirige pero sigue en /wps:   {len(still_wps_with_redirect)}")
    logger.info(f"  Sin redirección (sirve /wps):  {len(no_redirect)}")
    logger.info(f"  Errores:                       {len(errors)}")
    logger.info(f"  Por tipo:                      {by_type}")
    logger.info("=" * 60)
    logger.info(f"Resultados guardados en: {OUT_JSON}")
    logger.info(f"Mapa de migración (CSV):  {OUT_MIGRATION_CSV}")


if __name__ == "__main__":
    asyncio.run(run())
