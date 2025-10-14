#!/usr/bin/env python3
"""
generate_filtered_reports.py - Genera reportes visuales filtrados

Excluye URLs que contengan: /wps, /documents, /s, /s/minisitios
Genera: nowps/data/hierarchy.json y copia las visualizaciones HTML
"""
import json
import os
import shutil
from urllib.parse import urlparse

# Configuración
INPUT_PAGES = "data/pages.jsonl"
OUTPUT_DIR = "nowps"
OUTPUT_DATA_DIR = os.path.join(OUTPUT_DIR, "data")
OUTPUT_HIERARCHY = os.path.join(OUTPUT_DATA_DIR, "hierarchy.json")

# Paths a excluir (cualquier URL que contenga estos paths)
EXCLUDED_PATHS = ["/wps", "/documents", "/s/minisitios", "/s"]

def should_exclude(url):
    """Retorna True si la URL debe ser excluida."""
    path = urlparse(url).path
    # Excluir /s pero NO /services, /support, etc.
    for excluded in EXCLUDED_PATHS:
        if excluded == "/s":
            # Solo excluir si es exactamente /s o /s/algo (no /services)
            if path == "/s" or path.startswith("/s/"):
                return True
        elif excluded in path:
            return True
    return False

def insert_path(hroot, path_segments):
    """Inserta ruta en el árbol (reutilizado de crawler.py)."""
    node = hroot
    for seg in path_segments:
        if not seg:
            continue
        children = node.setdefault("children", {})
        node = children.setdefault(seg, {"__count": 0})
        node["__count"] = node.get("__count", 0) + 1

def hierarchy_to_d3(node, name="/"):
    """Convierte a formato D3 (reutilizado de crawler.py)."""
    out = {"name": name}
    children_map = node.get("children", {})
    if children_map:
        out["children"] = [hierarchy_to_d3(children_map[k], k) for k in sorted(children_map.keys())]
    else:
        out["value"] = node.get("__count", 1)
    return out

def main():
    if not os.path.exists(INPUT_PAGES):
        raise FileNotFoundError(f"No existe {INPUT_PAGES}")

    os.makedirs(OUTPUT_DATA_DIR, exist_ok=True)

    hroot = {"__count": 0}
    total = 0
    excluded = 0
    included = 0

    print("Filtrando URLs...")

    with open(INPUT_PAGES, "r", encoding="utf-8") as f:
        for line in f:
            try:
                rec = json.loads(line)
            except:
                continue

            url = rec.get("url")
            if not url:
                continue

            total += 1

            if should_exclude(url):
                excluded += 1
                continue

            included += 1
            up = urlparse(url)
            segs = [seg for seg in up.path.split("/") if seg]
            insert_path(hroot, segs)

    # Generar hierarchy.json
    base_url = "www.bancodebogota.com"
    d3tree = hierarchy_to_d3(hroot, name=base_url)

    with open(OUTPUT_HIERARCHY, "w", encoding="utf-8") as f:
        json.dump(d3tree, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Resumen:")
    print(f"  Total URLs procesadas: {total}")
    print(f"  URLs incluidas: {included}")
    print(f"  URLs excluidas: {excluded}")
    print(f"{'='*60}")
    print(f"\nHierarchy filtrado guardado en: {OUTPUT_HIERARCHY}")

    # Copiar HTMLs
    html_files = ["grahp.html", "icicle.html", "pack.html"]
    for html in html_files:
        if os.path.exists(html):
            dest = os.path.join(OUTPUT_DIR, html)
            shutil.copy2(html, dest)
            print(f"Copiado: {html} -> {dest}")

if __name__ == "__main__":
    main()
