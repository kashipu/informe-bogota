#!/usr/bin/env python3
"""
generate_filtered_reports.py — Reportes visuales filtrados + analítica

Lee data/pages.jsonl (y opcionalmente data/wps_redirects.json) y produce:

  nowps/data/hierarchy.json   — árbol para D3 con métricas enriquecidas por nodo
  nowps/data/stats.json       — resumen básico
  nowps/data/insights.json    — análisis SEO, performance, status, contenido
  nowps/data/seo_issues.csv   — páginas con problemas SEO (faltantes/duplicados)
  nowps/data/broken_pages.csv — errores y 4xx/5xx
  nowps/data/slow_pages.csv   — top N más lentas
  nowps/data/duplicates.csv   — páginas con mismo content_hash

Mejoras frente a la versión anterior:
- Auditoría SEO: títulos/descripciones/h1 faltantes o duplicados, noindex
- Análisis de performance: páginas lentas, pesadas, agregado por sección
- Distribución de status codes, idiomas, tipos Schema.org
- Detección de contenido duplicado por content_hash
- Nodos de la jerarquía enriquecidos con: pages, avg_words, avg_ms,
  ok/redirect/broken counts, seo_issues
- Cross-reference opcional con wps_redirects.json para % migración
"""
from __future__ import annotations

import csv
import json
import os
import shutil
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse

# ====================== CONFIG ====================== #
INPUT_PAGES = "data/pages.jsonl"
INPUT_WPS = "data/wps_redirects.json"      # opcional
OUTPUT_DIR = "nowps"
OUTPUT_DATA_DIR = os.path.join(OUTPUT_DIR, "data")
OUTPUT_HIERARCHY = os.path.join(OUTPUT_DATA_DIR, "hierarchy.json")
OUTPUT_STATS = os.path.join(OUTPUT_DATA_DIR, "stats.json")
OUTPUT_INSIGHTS = os.path.join(OUTPUT_DATA_DIR, "insights.json")
OUTPUT_SEO_CSV = os.path.join(OUTPUT_DATA_DIR, "seo_issues.csv")
OUTPUT_BROKEN_CSV = os.path.join(OUTPUT_DATA_DIR, "broken_pages.csv")
OUTPUT_SLOW_CSV = os.path.join(OUTPUT_DATA_DIR, "slow_pages.csv")
OUTPUT_DUPES_CSV = os.path.join(OUTPUT_DATA_DIR, "duplicates.csv")

EXCLUDED_PATHS = ["/wps", "/documents", "/s/minisitios", "/s"]

SKIP_ERROR_PAGES = True
SKIP_BLOCKED = True
ONLY_OK_STATUS = False
# Excluir páginas no válidas (404/4xx/5xx/errores) SOLO del árbol de jerarquía,
# manteniéndolas en la analítica y en broken_pages.csv.
TREE_ONLY_OK_STATUS = True
USE_FINAL_URL = True
HTML_FILES = ["grahp.html", "icicle.html", "pack.html"]
BASE_NAME = "www.bancodebogota.com"

# Umbrales SEO (best practices)
TITLE_MIN = 30
TITLE_MAX = 65
DESC_MIN = 70
DESC_MAX = 160
SLOW_THRESHOLD_MS = 2000
TOP_N = 50          # filas exportadas en CSVs de "top"


# ====================== FILTROS ====================== #

def should_exclude(url: str) -> bool:
    path = urlparse(url).path
    for excluded in EXCLUDED_PATHS:
        if excluded == "/s":
            if path == "/s" or path.startswith("/s/"):
                return True
        elif excluded in path:
            return True
    return False


def should_skip_record(rec: Dict) -> bool:
    if SKIP_ERROR_PAGES and rec.get("title") == "ERROR_RED":
        return True
    if SKIP_BLOCKED and rec.get("title") == "BLOQUEADA_POR_ROBOTS":
        return True
    if ONLY_OK_STATUS:
        sc = rec.get("status_code")
        if sc is None or not (200 <= sc < 400):
            return True
    return False


# ====================== HIERARCHY ====================== #

def insert_path(hroot: Dict, segs: List[str], metrics: Dict) -> None:
    """Inserta una URL en el árbol acumulando métricas en cada nivel."""
    node = hroot
    for seg in segs:
        if not seg:
            continue
        children = node.setdefault("children", {})
        node = children.setdefault(seg, _new_node())
        _accumulate(node, metrics)


def _new_node() -> Dict:
    return {
        "__count": 0, "__words": 0, "__ms_sum": 0, "__ms_n": 0,
        "__ok": 0, "__redirect": 0, "__broken": 0, "__seo_issues": 0,
    }


def _accumulate(node: Dict, m: Dict) -> None:
    node["__count"] += 1
    node["__words"] += m["word_count"]
    if m["response_time_ms"] is not None:
        node["__ms_sum"] += m["response_time_ms"]
        node["__ms_n"] += 1
    sc = m["status_code"]
    if sc is None:
        node["__broken"] += 1
    elif 200 <= sc < 300:
        node["__ok"] += 1
    elif 300 <= sc < 400:
        node["__redirect"] += 1
    else:
        node["__broken"] += 1
    if m["has_seo_issue"]:
        node["__seo_issues"] += 1


def hierarchy_to_d3(node: Dict, name: str = "/") -> Dict:
    out: Dict = {"name": name}
    children_map = node.get("children", {})
    count = node.get("__count", 0)
    ms_n = node.get("__ms_n", 0)
    out["pages"] = count
    out["avg_words"] = int(node.get("__words", 0) / count) if count else 0
    out["avg_ms"] = int(node.get("__ms_sum", 0) / ms_n) if ms_n else 0
    out["ok"] = node.get("__ok", 0)
    out["redirects"] = node.get("__redirect", 0)
    out["broken"] = node.get("__broken", 0)
    out["seo_issues"] = node.get("__seo_issues", 0)
    if children_map:
        out["children"] = [hierarchy_to_d3(children_map[k], k) for k in sorted(children_map.keys())]
    else:
        out["value"] = max(count, 1)
    return out


# ====================== SEO AUDIT ====================== #

def audit_seo(rec: Dict) -> List[str]:
    """Devuelve la lista de problemas SEO del registro."""
    issues: List[str] = []
    title = (rec.get("title") or "").strip()
    desc = (rec.get("meta_description") or "").strip()
    h1 = (rec.get("h1") or "").strip()
    canonical = rec.get("canonical")
    robots = (rec.get("meta_robots") or "").lower()

    if not title or title in ("SIN_TITULO", "ERROR_RED"):
        issues.append("missing_title")
    elif len(title) < TITLE_MIN:
        issues.append("title_too_short")
    elif len(title) > TITLE_MAX:
        issues.append("title_too_long")

    if not desc or desc in ("SIN_DESCRIPCION", "ERROR_RED"):
        issues.append("missing_description")
    elif len(desc) < DESC_MIN:
        issues.append("description_too_short")
    elif len(desc) > DESC_MAX:
        issues.append("description_too_long")

    if not h1:
        issues.append("missing_h1")
    if not canonical:
        issues.append("missing_canonical")
    if "noindex" in robots:
        issues.append("noindex")
    if rec.get("word_count", 0) < 100:
        issues.append("thin_content")

    return issues


# ====================== MAIN ====================== #

def main() -> None:
    if not os.path.exists(INPUT_PAGES):
        raise FileNotFoundError(f"No existe {INPUT_PAGES}")

    os.makedirs(OUTPUT_DATA_DIR, exist_ok=True)

    hroot: Dict = _new_node()
    seen: Set[str] = set()

    total = 0
    excluded_by_path = 0
    skipped_records = 0
    included = 0
    duplicates = 0

    # Agregados globales
    status_dist: Counter = Counter()
    lang_dist: Counter = Counter()
    jsonld_dist: Counter = Counter()
    section_counter: Counter = Counter()
    issue_dist: Counter = Counter()

    # Por sección de primer nivel
    section_perf: Dict[str, List[int]] = defaultdict(list)
    section_words: Dict[str, List[int]] = defaultdict(list)
    section_issues: Counter = Counter()

    # Tracking para detección
    title_to_urls: Dict[str, List[str]] = defaultdict(list)
    desc_to_urls: Dict[str, List[str]] = defaultdict(list)
    hash_to_urls: Dict[str, List[str]] = defaultdict(list)

    # Listas para CSV
    rows_seo: List[Dict] = []
    rows_broken: List[Dict] = []
    rows_all_with_ms: List[Tuple[int, str, int, int]] = []  # (ms, url, status, depth)

    print("Procesando pages.jsonl...")
    with open(INPUT_PAGES, "r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue

            total += 1
            url: Optional[str] = rec.get("url")
            if not url:
                continue

            if USE_FINAL_URL and rec.get("redirected") and rec.get("final_url"):
                url = rec["final_url"]

            if should_skip_record(rec):
                skipped_records += 1
                continue
            if should_exclude(url):
                excluded_by_path += 1
                continue
            if url in seen:
                duplicates += 1
                continue
            seen.add(url)
            included += 1

            # Métricas
            sc = rec.get("status_code")
            rt = rec.get("response_time_ms")
            wc = int(rec.get("word_count") or 0)
            lang = (rec.get("lang") or "").strip().lower() or "unknown"
            depth = int(rec.get("depth") or 0)
            issues = audit_seo(rec)

            status_dist[sc if sc is not None else "error"] += 1
            lang_dist[lang] += 1
            for t in (rec.get("jsonld_types") or []):
                jsonld_dist[t] += 1
            for iss in issues:
                issue_dist[iss] += 1

            up = urlparse(url)
            segs = [seg for seg in up.path.split("/") if seg]
            top = segs[0] if segs else "(root)"
            section_counter[top] += 1
            if rt is not None:
                section_perf[top].append(rt)
            section_words[top].append(wc)
            if issues:
                section_issues[top] += 1

            # Solo páginas válidas (2xx/3xx) entran al árbol de jerarquía.
            if not (TREE_ONLY_OK_STATUS and (sc is None or not (200 <= sc < 400))):
                insert_path(hroot, segs, {
                    "word_count": wc,
                    "response_time_ms": rt,
                    "status_code": sc,
                    "has_seo_issue": bool(issues),
                })

            # Recopilar para detección de duplicados / SEO / broken
            title = (rec.get("title") or "").strip()
            desc = (rec.get("meta_description") or "").strip()
            chash = rec.get("content_hash")
            if title and title not in ("SIN_TITULO", "ERROR_RED"):
                title_to_urls[title].append(url)
            if desc and desc not in ("SIN_DESCRIPCION", "ERROR_RED"):
                desc_to_urls[desc].append(url)
            if chash:
                hash_to_urls[chash].append(url)

            if issues:
                rows_seo.append({
                    "url": url, "depth": depth, "status_code": sc,
                    "issues": ";".join(issues),
                    "title_len": len(title),
                    "desc_len": len(desc),
                    "h1": (rec.get("h1") or "")[:120],
                    "title": title[:120],
                })

            if sc is None or (isinstance(sc, int) and sc >= 400):
                rows_broken.append({
                    "url": url, "status_code": sc, "depth": depth,
                    "parent_url": rec.get("parent_url"),
                    "title": title[:120],
                })

            if rt is not None:
                rows_all_with_ms.append((int(rt), url, int(sc) if isinstance(sc, int) else 0, depth))

    # === Detección de duplicados ===
    dup_titles = {t: urls for t, urls in title_to_urls.items() if len(urls) > 1}
    dup_descs = {d: urls for d, urls in desc_to_urls.items() if len(urls) > 1}
    dup_content = {h: urls for h, urls in hash_to_urls.items() if len(urls) > 1}

    # === Cross-reference opcional con WPS ===
    wps_summary = None
    if os.path.exists(INPUT_WPS):
        try:
            with open(INPUT_WPS, "r", encoding="utf-8") as f:
                wps_data = json.load(f)
            wps_summary = wps_data.get("summary")
        except Exception:
            pass

    # === Per-section agg ===
    section_stats = []
    for sec, count in section_counter.most_common():
        perfs = section_perf.get(sec, [])
        words = section_words.get(sec, [])
        section_stats.append({
            "section": sec,
            "pages": count,
            "avg_ms": int(sum(perfs) / len(perfs)) if perfs else 0,
            "p95_ms": int(sorted(perfs)[int(len(perfs) * 0.95) - 1]) if len(perfs) >= 20 else None,
            "avg_words": int(sum(words) / len(words)) if words else 0,
            "seo_issues": section_issues.get(sec, 0),
        })

    # === Top N lentas ===
    rows_all_with_ms.sort(reverse=True)
    slow_top = rows_all_with_ms[:TOP_N]

    # === Escribir outputs ===
    # hierarchy.json (compatible + enriquecido)
    d3tree = hierarchy_to_d3(hroot, name=BASE_NAME)
    with open(OUTPUT_HIERARCHY, "w", encoding="utf-8") as f:
        json.dump(d3tree, f, ensure_ascii=False, indent=2)

    # stats.json (resumen ligero)
    stats = {
        "total_records": total,
        "included": included,
        "excluded_by_path": excluded_by_path,
        "skipped_records": skipped_records,
        "duplicates": duplicates,
        "sections_top_level": section_counter.most_common(),
    }
    with open(OUTPUT_STATS, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    # insights.json (analítica completa)
    insights = {
        "totals": {
            "records_read": total,
            "included": included,
            "excluded_by_path": excluded_by_path,
            "skipped_records": skipped_records,
            "duplicates_in_input": duplicates,
        },
        "status_distribution": dict(status_dist),
        "language_distribution": dict(lang_dist),
        "schema_org_types": dict(jsonld_dist.most_common(30)),
        "seo_issues_distribution": dict(issue_dist),
        "sections": section_stats,
        "duplicates": {
            "by_title": {
                "groups": len(dup_titles),
                "pages_affected": sum(len(v) for v in dup_titles.values()),
                "examples": [{"title": k, "urls": v[:5], "n": len(v)}
                             for k, v in sorted(dup_titles.items(), key=lambda x: -len(x[1]))[:20]],
            },
            "by_description": {
                "groups": len(dup_descs),
                "pages_affected": sum(len(v) for v in dup_descs.values()),
            },
            "by_content_hash": {
                "groups": len(dup_content),
                "pages_affected": sum(len(v) for v in dup_content.values()),
                "examples": [{"hash": k, "urls": v[:5], "n": len(v)}
                             for k, v in sorted(dup_content.items(), key=lambda x: -len(x[1]))[:20]],
            },
        },
        "performance": {
            "slow_threshold_ms": SLOW_THRESHOLD_MS,
            "n_slow_pages": sum(1 for ms, _, _, _ in rows_all_with_ms if ms >= SLOW_THRESHOLD_MS),
            "n_measured": len(rows_all_with_ms),
            "avg_ms": int(sum(ms for ms, *_ in rows_all_with_ms) / len(rows_all_with_ms)) if rows_all_with_ms else 0,
        },
        "broken_or_errors": len(rows_broken),
        "wps_migration": wps_summary,  # None si no existe el archivo
    }
    with open(OUTPUT_INSIGHTS, "w", encoding="utf-8") as f:
        json.dump(insights, f, ensure_ascii=False, indent=2)

    # CSVs accionables
    _write_csv(OUTPUT_SEO_CSV, ["url", "depth", "status_code", "issues", "title_len", "desc_len", "h1", "title"], rows_seo)
    _write_csv(OUTPUT_BROKEN_CSV, ["url", "status_code", "depth", "parent_url", "title"], rows_broken)
    with open(OUTPUT_SLOW_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["response_time_ms", "url", "status_code", "depth"])
        for ms, url, sc, d in slow_top:
            w.writerow([ms, url, sc, d])
    # duplicates.csv: una fila por URL agrupada por hash
    with open(OUTPUT_DUPES_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["content_hash", "group_size", "url"])
        for h, urls in sorted(dup_content.items(), key=lambda x: -len(x[1])):
            for u in urls:
                w.writerow([h, len(urls), u])

    # ===== Resumen en consola =====
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)
    print(f"  Registros leídos:           {total}")
    print(f"  Incluidos en jerarquía:     {included}")
    print(f"  Excluidos por path:         {excluded_by_path}")
    print(f"  Descartados (err/bloq/sc):  {skipped_records}")
    print(f"  Duplicados en input:        {duplicates}")
    print()
    print("  Status codes:")
    for sc, n in sorted(status_dist.items(), key=lambda x: -x[1])[:8]:
        print(f"    {sc}: {n}")
    print()
    print("  Top secciones (con avg_ms / seo_issues):")
    for s in section_stats[:10]:
        print(f"    /{s['section']:<22} pages={s['pages']:<5} avg_ms={s['avg_ms']:<5} seo_issues={s['seo_issues']}")
    print()
    print(f"  Problemas SEO totales:      {sum(issue_dist.values())}  en {len(rows_seo)} páginas")
    for iss, n in issue_dist.most_common():
        print(f"    {iss}: {n}")
    print()
    print(f"  Duplicados de título:       {len(dup_titles)} grupos / {sum(len(v) for v in dup_titles.values())} páginas")
    print(f"  Duplicados de contenido:    {len(dup_content)} grupos / {sum(len(v) for v in dup_content.values())} páginas")
    print(f"  Páginas lentas (>{SLOW_THRESHOLD_MS}ms): {insights['performance']['n_slow_pages']}")
    print(f"  Páginas rotas / errores:    {len(rows_broken)}")
    if wps_summary:
        print(f"  Migración /wps:             {wps_summary.get('migration_percent', 0)}%")
    print("=" * 60)
    print("Archivos generados:")
    print(f"  {OUTPUT_HIERARCHY}")
    print(f"  {OUTPUT_STATS}")
    print(f"  {OUTPUT_INSIGHTS}")
    print(f"  {OUTPUT_SEO_CSV}")
    print(f"  {OUTPUT_BROKEN_CSV}")
    print(f"  {OUTPUT_SLOW_CSV}")
    print(f"  {OUTPUT_DUPES_CSV}")

    # Copiar HTMLs
    for html in HTML_FILES:
        if os.path.exists(html):
            dest = os.path.join(OUTPUT_DIR, html)
            shutil.copy2(html, dest)
            print(f"  Copiado: {html} -> {dest}")


def _write_csv(path: str, fields: List[str], rows: List[Dict]) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


if __name__ == "__main__":
    main()
