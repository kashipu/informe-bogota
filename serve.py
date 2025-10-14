#!/usr/bin/env python3
"""
serve.py - Servidor HTTP simple para visualizaciones

Uso:
    python serve.py

Luego abre: http://localhost:8000
"""
import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor activo en http://localhost:{PORT}")
    print(f"Abre http://localhost:{PORT} en tu navegador")
    print("Presiona Ctrl+C para detener")
    httpd.serve_forever()
