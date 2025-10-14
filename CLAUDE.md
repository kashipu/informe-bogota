# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python-based web crawler designed for site mapping and analysis, specifically configured for crawling Banco de Bogotá's website. The crawler performs BFS (breadth-first search) traversal, respects robots.txt, and generates multiple output formats for visualization and analysis.

## Core Scripts

- **crawler.py**: Main crawler that performs BFS crawling with robots.txt compliance, extracts page metadata, and generates streaming JSONL outputs plus a hierarchy JSON for D3.js visualizations
- **crawler2.py**: Maps URLs containing "/wps" to their final redirect destinations
- **generate_filtered_reports.py**: Generates filtered visualizations excluding /wps, /documents, /s paths

## Running the Crawler

```bash
# Install dependencies
pip install -r requirements.txt

# Run main crawler
python crawler.py

# Check WPS redirects (requires crawler.py output first)
python crawler2.py

# Generate filtered reports (excludes /wps, /documents, /s)
python generate_filtered_reports.py

# View reports in browser (required for HTML visualizations)
python serve.py
# Then open: http://localhost:8000
```

**Important:** HTML visualizations must be served via HTTP server (not opened directly as files) due to CORS restrictions when loading JSON data.

## Deployment

This project is optimized for **Vercel** deployment:

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

Or connect your GitHub repository to Vercel for automatic deployments.

**Files included in deployment:**
- All HTML files (visualizations)
- `data/hierarchy.json` and `nowps/data/hierarchy.json` (required for visualizations)
- Configuration: `vercel.json`

**Files excluded from deployment:**
- Python scripts (only needed for data generation)
- Intermediate data files (.jsonl, logs)
- Virtual environment

## Output Files

The crawler generates data in the `data/` directory:

- **pages.jsonl**: Streaming output with one JSON object per crawled page (url, status_code, title, meta_description, canonical, parent_url, depth)
- **edges.jsonl**: Streaming output with parent→child link relationships (source, target)
- **errors.jsonl**: Network and parse errors encountered during crawling
- **hierarchy.json**: Path-based hierarchy tree for D3.js visualizations (generated from URL path segments)
- **wps_redirects.json**: (from crawler2.py) Simple mapping of URLs with "/wps" to their final redirect destinations, includes summary statistics

Logs are stored in `logs/crawler.log` with rotation (max 2MB, 3 backups).

## Configuration

Both scripts have extensive configuration constants at the top of each file:

### crawler.py Configuration
- `BASE_URL`: Starting URL for the crawl
- `MAX_PAGES`: Maximum pages to crawl (set to float('inf') for unlimited)
- `MAX_DEPTH`: Maximum crawl depth from starting URL
- `DELAY`: Seconds between requests (politeness)
- `OBEY_ROBOTS`: Whether to respect robots.txt (set to False only for debugging)
- `TIMEOUT`: HTTP request timeout in seconds
- `VERIFY_TLS`: SSL certificate verification toggle
- `USE_SITEMAP`: Whether to seed URLs from sitemap.xml
- `SITEMAP_URLS`: List of sitemap URLs to parse
- `RECORD_BLOCKED_URLS`: Whether to record robots.txt-blocked URLs in output
- `DEBUG`: Verbose logging toggle

### crawler2.py Configuration
- `INPUT_PAGES`: Path to pages.jsonl from crawler.py
- `TIMEOUT`: HTTP request timeout
- `DELAY`: Seconds between requests
- `MAX_URLS`: Limit for testing (None = process all)

## Architecture

### crawler.py Architecture

**Crawling Strategy**: BFS with deque-based queue, tracks visited URLs to avoid duplicates

**Data Models**:
- `PageRecord` dataclass: url, status_code, title, meta_description, canonical, parent_url, depth

**Key Components**:
1. **Robots.txt Handler**: Uses urllib.robotparser to check allowed URLs before fetching
2. **Session Management**: requests.Session with browser-like headers for realistic crawling
3. **URL Normalization**: Resolves relative URLs, removes fragments, filters by same-origin policy
4. **HTML Parser**: BeautifulSoup extracts metadata (title, meta description, canonical) and internal links
5. **Hierarchy Builder**: Constructs path-based tree from URL segments for D3.js visualization
6. **Streaming Output**: Writes JSONL line-by-line for scalability with large crawls

**Optional Sitemap Seeding**: If `USE_SITEMAP=True`, parses sitemap.xml files and adds matching URLs to crawl queue with depth=1

**Error Handling**: Network errors written to errors.jsonl, blocked URLs optionally recorded with status=None

### crawler2.py Architecture

**Purpose**: Maps URLs containing "/wps" to their final redirect destinations

**Data Models**:
- `RedirectMapping` dataclass: source_url, final_url, has_redirect, error

**Process Flow**:
1. Reads pages.jsonl from crawler.py
2. Filters for URLs containing "/wps" in path
3. Makes GET request with allow_redirects=True to follow redirect chain
4. Captures final destination URL
5. Outputs single JSON file with summary statistics and simple redirect mappings

**Output Structure**:
- `summary` object with counts (total_urls_checked, urls_with_redirect, urls_without_redirect, errors)
- `redirects` array with simple source → destination mappings (source_url, final_url, has_redirect, error)

## HTML Visualizations

### Main Dashboard
- **index.html**: Main dashboard with links to all reports (complete and filtered)

### Complete Reports
HTML files for visualizing all crawled data (using D3.js):
- `grahp.html`: Tree graph visualization
- `icicle.html`: Icicle (partition) chart visualization
- `pack.html`: Circle packing visualization

These read from `data/hierarchy.json` generated by crawler.py.

### Filtered Reports (nowps/)
The `nowps/` directory contains filtered visualizations excluding URLs with /wps, /documents, /s, /s/minisitios:
- `nowps/index.html`: Filtered reports dashboard
- `nowps/grahp.html`: Filtered tree graph
- `nowps/icicle.html`: Filtered icicle chart
- `nowps/pack.html`: Filtered circle packing

These read from `nowps/data/hierarchy.json` generated by generate_filtered_reports.py.

## Development Notes

- The crawler is URL-scoped by origin (scheme + netloc) and will only follow internal links
- All URLs are normalized (absolute, defragmented) before being added to visited set or queue
- Parent-child relationships are tracked for every discovered link and written to edges.jsonl
- The hierarchy tree is built from URL path segments, not parent-child crawl relationships
- Both scripts use rotating file handlers for logging to prevent unbounded log growth
- JSONL format allows processing large datasets line-by-line without loading entire file into memory
