# Web Crawler - Banco de Bogotá

Crawler de arquitectura web con visualizaciones D3.js para análisis de estructura de sitios.

## 🚀 Deploy en Vercel

### Preparación
1. Asegúrate de tener los archivos JSON generados:
```bash
python crawler.py
python generate_filtered_reports.py
```

2. Confirma que existen:
   - `data/hierarchy.json`
   - `nowps/data/hierarchy.json`

### Deploy

**Opción 1: Via CLI**
```bash
npm i -g vercel
vercel
```

**Opción 2: Via GitHub**
1. Push el repositorio a GitHub
2. Conecta el repo en [vercel.com](https://vercel.com)
3. Deploy automático

**Archivos incluidos en deploy:**
- ✅ Todos los HTML (index.html, visualizaciones)
- ✅ `data/hierarchy.json`
- ✅ `nowps/data/hierarchy.json`
- ❌ Logs, venv, archivos .jsonl intermedios

## 🛠️ Desarrollo Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar crawler
python crawler.py

# Mapear redirecciones /wps
python crawler2.py

# Generar reportes filtrados
python generate_filtered_reports.py

# Ver visualizaciones
python serve.py
# Abrir: http://localhost:8000
```

## 📊 Estructura

```
crawler/
├── index.html              # Dashboard principal
├── grahp.html             # Vista de árbol
├── icicle.html            # Vista de jerarquía
├── pack.html              # Vista de concentración
├── data/
│   └── hierarchy.json     # Datos completos
└── nowps/
    ├── index.html         # Dashboard filtrado
    ├── grahp.html
    ├── icicle.html
    ├── pack.html
    └── data/
        └── hierarchy.json # Datos filtrados
```

## 📝 Scripts

- **crawler.py**: Crawler principal BFS
- **crawler2.py**: Mapeo de redirecciones /wps
- **generate_filtered_reports.py**: Genera reportes sin /wps, /documents, /s
- **serve.py**: Servidor HTTP local para desarrollo
