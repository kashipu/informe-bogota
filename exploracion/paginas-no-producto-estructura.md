# Estructura de páginas no-producto
## Banco de Bogotá — www.bancodebogota.com

> Complemento de [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md).
> Este documento cubre las páginas que no pertenecen a ningún ecosistema de producto:
> soporte, institucional, educación, precios, campañas y páginas funcionales.

---

## 1. Mapa de páginas no-producto

Las páginas que no son productos se agrupan en **7 familias funcionales**. Actualmente están dispersas
en múltiples secciones sin una lógica clara.

| Familia | Páginas actuales | Secciones donde viven hoy | Problema |
|---|---|---|---|
| **Soporte y ayuda** | 138 | `/atencion-al-cliente` | Mezcla canales, operativa, FAQ, seguridad y regulatorio |
| **Sobre el banco** | ~25 | `/nuestra-organizacion`, `/sostenibilidad`, `/diversidad-e-inclusion`, `/informe-*` | Fragmentada en 6+ secciones raíz |
| **Educación financiera** | 31 | `/educacion-financiera` | Mezcla artículos editoriales con páginas corporativas |
| **Tasas y tarifas** | 18 | `/tasas-y-tarifas` | Vigentes y archivo histórico al mismo nivel |
| **Segmentación de audiencia** | 36 | `/banca-personas`, `/banca-empresas` | Duplica la entrada de `/personas` y `/empresas` |
| **Alianzas globales** | 9 | `/alianzas` | Debería ser directorio + ancla en cada producto |
| **Campañas y eventos** | 14+ | Secciones raíz sueltas | Sin lifecycle, sin anclaje al producto |

---

## 2. Soporte y ayuda al cliente

### Estado actual

`/atencion-al-cliente` tiene **138 páginas en 11 subsecciones** que mezclan cuatro tipos de contenido completamente distintos:

```
/atencion-al-cliente/
  /canales/                        ← dónde operar (físico, digital, electrónico)
    /canales-de-atencion-presencial/
      /corresponsales-bancarios/
      /oficinas/ (12 variantes de oficina)
    /canales-digitales/            ← banca móvil, banca virtual, token
    /canales-electronicos/         ← cajeros, multifuncional
    /disponibilidad-de-canales
    /transacciones/ (12 tipos)     ← cómo hacer cada operación

  /preguntas-frecuentes/           ← dudas por producto (30 páginas planas)
    /medios-de-pago/ (12 subpágs)  ← dasboard de medios, dentro de FAQ

  /seguridad-bancaria/             ← educación sobre fraudes (20 páginas)
    /seguridad-en-cajeros/
    /seguridad-en-internet/
    /seguridad-en-oficinas/
    /seguridad-en-tu-celular/
    /seguridad-cheques-consignaciones/

  /instructivos/ (11 páginas)      ← guías paso a paso de tarjetas/cuentas
  /proteccion-al-consumidor/       ← marco regulatorio (10 páginas)
  /impuestos/                      ← pago de impuestos con el banco (4 páginas)
  /defensor-del-consumidor         ← contacto regulatorio
  /pqrs                            ← canal de quejas
  /reglamentos                     ← repositorio de reglamentos
  /servilineas                     ← directorio de teléfonos

  /canales-de-atencion-presencial/ ← DUPLICADO del nodo dentro de /canales
    /oficinas/
      /centro-atencion-libranza
```

### Problema central

Soporte mezcla en un mismo nivel jerárquico:
- **Dónde operar** (canales físicos y digitales)
- **Cómo operar** (transacciones, instructivos)
- **Cómo estar seguro** (seguridad bancaria)
- **Cuáles son mis derechos** (protección al consumidor, defensor)
- **Cómo contactar** (PQRS, servilineas)
- **Cómo pagar impuestos** (impuestos, mal ubicado aquí)

Además, los "medios de pago" (12 páginas: datáfono, QR, link de pagos, webcheckout...) viven dentro de `/preguntas-frecuentes/medios-de-pago`, siendo en realidad un catálogo de productos de cobro para negocios.

### Estructura propuesta

```
/ayuda/                             ← nuevo nombre: más claro que "atención al cliente"
│
├── /contacto                       ← punto de entrada: teléfonos, PQRS, chat
│   ├── /servilineas
│   ├── /pqrs
│   └── /defensor-del-consumidor
│
├── /canales/                       ← dónde operar
│   ├── /oficinas/                  ← directorio unificado con filtros, no 12 páginas
│   │   └── /corresponsales-bancarios
│   ├── /cajeros-y-multifuncionales
│   ├── /banca-movil
│   ├── /banca-virtual
│   ├── /avalpay-center             ← (personas y empresas)
│   └── /disponibilidad-de-canales
│
├── /como-operar/                   ← cómo hacer transacciones
│   ├── /transferencias
│   ├── /pagos
│   ├── /consultas-y-extractos
│   ├── /bloqueos
│   └── /apple-pay-google-pay
│
├── /instructivos/                  ← tutoriales genéricos (específicos van en el producto)
│   ├── /activa-tus-tarjetas
│   ├── /crea-tu-clave-segura
│   └── /uso-de-bre-b
│
├── /seguridad/                     ← educación sobre fraude
│   ├── /phishing-y-estafas-digitales
│   ├── /seguridad-en-cajeros
│   ├── /seguridad-en-oficinas
│   └── /seguridad-en-tu-celular
│
├── /preguntas-frecuentes/          ← buscador de FAQ; las FAQ por producto viven en el producto
│   └── [buscador/índice]
│
├── /impuestos/                     ← servicio de pago de impuestos con el banco
│   ├── /calendario
│   ├── /canales-de-pago
│   └── /beneficios
│
└── /tus-derechos/                  ← marco de protección al consumidor
    ├── /proteccion-datos-personales
    ├── /habeas-data
    ├── /uso-de-cookies
    └── /superintendencia-financiera
```

### Medios de pago para negocios

Las 12 páginas de `/preguntas-frecuentes/medios-de-pago` (datáfono, QR, link de pagos, webcheckout) no son FAQ: son un catálogo de soluciones de cobro para comercios. Su lugar es dentro del portafolio empresarial:

```
Destino propuesto: /empresas/soluciones-de-cobro/
  /datafono-digital
  /datafono-fisico
  /codigo-qr
  /link-de-pagos
  /webcheckout
  /micrositio-abierto
  /micrositio-cerrado
  /pasarela-gou
```

---

## 3. Sobre el banco (Institucional)

### Estado actual: 6 fragmentos sin hub

El contenido institucional existe en **6 secciones distintas en la raíz**, sin ningún nodo padre que las agrupe:

| Sección actual | Páginas | Contenido |
|---|---|---|
| `/nuestra-organizacion` | 4 | Historia del banco, defensor del consumidor, derechos del consumidor, habeas data |
| `/sostenibilidad` | 17 | Estrategia ASG, ambiental, social, gobierno, Fundación Banco de Bogotá |
| `/sustainability` | 6 | Versión EN de sostenibilidad (asimétrica: más contenido que la versión ES) |
| `/diversidad-e-inclusion` | 5 | Programas por tipo de discapacidad |
| `/informe-de-gestion` | 1 | Informe de gestión (genérico) |
| `/informe-gestion-2025` | 1 | Informe 2025 |
| `/informe-gestion-2024-3` | 1 | Informe 2024 (versión 3 — número de versión interno en URL) |
| `/management-report-2024` | 1 | Versión EN del informe 2024 |
| `/transparencia` | 1 | Página de transparencia (8.075 palabras — la más densa del sitio) |

Problemas adicionales en `/sostenibilidad`:
- Existe `/sostenibilidad/Biblioteca` y `/sostenibilidad/biblioteca` — misma página con capitalización diferente en la URL (duplicado técnico)
- Existe `/sostenibilidad/library-anterior` — sufijo de versión interna expuesto

### Estructura propuesta: hub `/sobre-el-banco`

```
/sobre-el-banco/
│
├── /quienes-somos
│   ├── /historia
│   ├── /nuestra-mision-y-vision
│   └── /grupo-aval               ← referencia a la holding
│
├── /sostenibilidad/
│   ├── /estrategia-asg
│   ├── /ambiental
│   ├── /social
│   ├── /gobierno-corporativo
│   └── /biblioteca               ← un solo nodo, sin duplicados
│
├── /fundacion-banco-de-bogota/
│   ├── /quienes-somos
│   ├── /educacion-y-bienestar-social/
│   │   └── /historias/           ← perfiles de beneficiarios
│   ├── /emprendimiento-social-y-climatico
│   └── /proteccion-ambiental
│
├── /diversidad-e-inclusion/
│   ├── /discapacidad-auditiva
│   ├── /discapacidad-cognitiva
│   ├── /discapacidad-fisica
│   └── /discapacidad-visual
│
├── /informes/
│   ├── /informe-gestion-2025     ← vigente
│   ├── /informe-gestion-2024
│   ├── /transparencia
│   └── /archivo/                 ← versiones anteriores, no en nivel principal
│       └── /informe-gestion-2023 ...
│
└── /en/                          ← versión en inglés, estructura espejo
    ├── /sustainability/
    │   ├── /esg-strategy
    │   ├── /environmental
    │   ├── /social
    │   ├── /governance
    │   └── /library
    └── /management-report-2025
```

**Nota sobre `transparencia`:** Con 8.075 palabras es el documento más denso del sitio. Debería ser una sección con subpáginas temáticas, no una sola página.

---

## 4. Educación financiera

### Estado actual

`/educacion-financiera` tiene 31 páginas organizadas en 8 subsecciones, con dos problemas estructurales:

**Problema 1: "nuestra-organizacion" dentro de educación**

Una subsección llamada `nuestra-organizacion` (7 páginas) vive dentro de educación financiera con contenido mixto: artículos editoriales (`como-funciona-la-economia`, `historia-del-dinero`) mezclados con páginas corporativas (`defensor-del-consumidor`, `ley-de-habeas-data`, `nuestra-historia`).

```
/educacion-financiera/nuestra-organizacion/
  /como-funciona-la-economia        ← artículo editorial ✓ (pertenece aquí)
  /historia-del-dinero              ← artículo editorial ✓
  /deberes-y-derechos               ← artículo editorial ✓
  /nuestra-historia                 ← página corporativa ✗ (pertenece a /sobre-el-banco)
  /defensor-del-consumidor          ← página regulatoria ✗ (pertenece a /ayuda/tus-derechos)
  /ley-de-habeas-data               ← página legal ✗ (pertenece a /ayuda/tus-derechos)
```

**Problema 2: Simuladores mal ubicados**

Los dos únicos simuladores del sitio están en educación, no en los productos:
- `/educacion-financiera/simulador-credito-libre-inversion` → debería estar en `/personas/creditos/libre-inversion/simulador`
- `/educacion-financiera/simulador-credito-vivienda` → debería estar en `/personas/creditos/vivienda/simulador`

Los simuladores pueden referenciar desde educación hacia el producto, pero su URL canónica debe ser la del producto.

**Problema 3: Duplicidad de tema con el producto**

`/educacion-financiera/como-funciona-una-tarjeta-de-credito` (1.029 palabras) es un artículo independiente sobre tarjetas. Pero también existe `/educacion-financiera/tarjeta-de-credito/como-funcionan-las-tarjetas-de-credito` (757 palabras). Dos páginas sobre el mismo tema con URL similar.

### Estructura propuesta

```
/educacion-financiera/
│
├── /finanzas-personales/           ← economía cotidiana
│   ├── /como-hacer-un-presupuesto
│   ├── /capacidad-de-endeudamiento
│   ├── /como-aumentar-el-patrimonio
│   └── /cuanto-vale-estudiar
│
├── /credito/                       ← entender el crédito
│   ├── /tipos-de-credito
│   ├── /antes-de-pedir-un-credito
│   ├── /tipos-de-tasas-de-interes
│   └── /buena-vida-crediticia
│
├── /tarjetas/                      ← entender las tarjetas
│   ├── /como-funcionan
│   ├── /compras-internacionales
│   └── /seguridad-en-tarjetas
│
├── /inversion/                     ← entender la inversión
│   ├── /tipos-de-inversion
│   ├── /titulos-valores
│   └── /riesgos-financieros
│
├── /seguros/                       ← entender los seguros
│   └── /que-es-un-seguro
│
└── /historia-y-economia/           ← contexto macroeconómico
    ├── /como-funciona-la-economia
    ├── /historia-del-dinero
    └── /deberes-y-derechos-consumidor
```

Los simuladores se referencian desde la sección temática, pero su URL canónica es el producto.

---

## 5. Tasas y tarifas

### Estado actual

`/tasas-y-tarifas` tiene 18 páginas: **4 vigentes** y **13 de archivo histórico**, todas al mismo nivel.

```
/tasas-y-tarifas/
  /tarifas-personas          [103w]   ← vigente
  /tarifas-empresas          [102w]   ← vigente
  /tarifas-pyme              [147w]   ← vigente
  /tarifas-internacional     [130w]   ← vigente
  /tasas-2014                [79w]    ← archivo
  /tasas-2015                [79w]    ← archivo
  ...
  /tasas-2026                [65w]    ← ¿vigente o archivo?
```

Problema adicional: las 4 páginas vigentes son tablas generales por segmento (personas, empresas, pyme, internacional) con apenas 95–147 palabras promedio. Funcionan como documentos descargables, no como páginas de contenido.

### Estructura propuesta

Las tarifas vigentes deben existir en **dos lugares**:

1. **Referencia desde el producto** (canónica): `/personas/tarjetas-de-credito/gold/tasas-y-tarifas` — tasas específicas de esa tarjeta
2. **Tabla consolidada** (transversal): Una sola tabla/comparador accesible desde la navegación principal

```
/tasas-y-tarifas/                   ← página comparador (tabla dinámica filtrable)
  (contenido: tabla filtrable por producto, segmento, tipo)

/tasas-y-tarifas/archivo/           ← histórico, no indexable o de baja prioridad
  /2014
  /2015
  ...
  /2025
```

Los PDFs de tasas históricas deberían referenciarse desde `/sobre-el-banco/informes/` o desde un enlace dentro de la tabla, sin ser páginas independientes indexadas.

---

## 6. Segmentación de audiencia

### Estado actual

`/banca-personas` (15 páginas) y `/banca-empresas` (21 páginas) son portafolios por segmento de cliente: premium, joven, pensionados, pyme, corporativa, institucional, etc.

```
/banca-personas/
  /infantil              /joven              /pensionados
  /portafolio-integral-basico               /portafolio-personas
  /portafolio-personas-alto                 /preferente       /premium

/banca-empresas/
  /corporativa     /empresarial    /institucional    /microempresas
  /microfinanzas   /oficial        /pyme             /social
  /empresas/banca-internacional
```

Estas secciones responden a la pregunta "¿quién eres tú como cliente?" mientras que `/personas` y `/empresas` responden "¿qué producto necesitas?". Son dos modelos mentales que deberían complementarse, no coexistir como secciones paralelas.

### Estructura propuesta

El modelo de segmentación debería ser la **puerta de entrada** al hub de audiencia, no una sección separada. Hay dos formas de resolver esto:

**Opción A — Segmentación como filtro en `/personas`:**
```
/personas/
  (hub con selector: ¿eres Joven / Preferente / Premium / Pensionado?)
  → filtra los productos relevantes para ese segmento

/personas/segmentos/               ← explicativo, no navegacional
  /joven
  /preferente
  /premium
  /pensionados
```

**Opción B — Segmentación como landing de entrada:**
```
/personas/                         ← selecciona tu segmento
  /basico   /joven   /preferente   /premium   /pensionados

/personas/joven/                   ← hub de productos para jóvenes
  /cuenta-de-ahorros
  /tarjetas-de-credito
  /creditos
  ...
```

La Opción A es más flexible y no duplica el catálogo de productos. La Opción B es más clara para segmentos muy diferenciados (premium, corporativa) donde el portafolio es sustancialmente distinto.

Para empresas, la segmentación es más crítica porque los productos varían más por tamaño de empresa:
```
/empresas/
  /pyme/              → portafolio pyme completo
  /microempresas/     → microcréditos y microfinanzas
  /corporativa/       → banca de inversión y tesorería
  /institucional/     → sector público y fondos
  /social/            → cooperativas y organizaciones
  /banca-internacional → empresas con operaciones en el exterior
```

---

## 7. Alianzas

### Estado actual

`/alianzas` tiene 9 páginas: tarjetas cobranded (Claro, Movistar, Tigo, Decathlon, Apple, Mercado Libre) y `crediconvenio`.

```
/alianzas/
  /crediconvenio
  /tarjeta-de-credito/
    /claro
    /comprar-apple-sin-intereses
    /decathlon
    /mercado-libre
    /movistar-alianza
    /tigo
```

El problema: estas páginas también existen dentro del portafolio de tarjetas en `/personas/tarjetas-de-credito/movistar`, `/personas/tarjetas-de-credito/movistar-clasica`, etc. Hay duplicidad entre la sección de alianzas y la sección del producto.

### Estructura propuesta

**El producto cobranded tiene una sola URL canónica dentro del producto:**
```
/personas/tarjetas-de-credito/movistar/     ← canónica
/personas/tarjetas-de-credito/movistar-clasica/
/personas/tarjetas-de-credito/movistar-gold/
```

**`/alianzas` se convierte en un directorio de socios, no de productos:**
```
/alianzas/                                  ← directorio de empresas aliadas
  /movistar      → redirige a /personas/tarjetas-de-credito/movistar
  /claro         → redirige a /personas/tarjetas-de-credito/claro
  /decathlon     → redirige a /personas/tarjetas-de-credito/decathlon
  /latam-pass    → redirige a /personas/tarjetas-de-credito/latam-pass
  /crediconvenio → redirige a /personas/creditos/crediconvenio
```

Este directorio es útil para usuarios que llegan buscando "tarjeta banco bogotá movistar" (también accesible desde la página de Movistar o Claro). Pero la URL de referencia para SEO y para el contenido es siempre la del producto.

---

## 8. Campañas y eventos temporales

### Estado actual

Las campañas activas viven como secciones raíz permanentes:

| Sección | Páginas | Producto asociado |
|---|---|---|
| `/fifa-2026` | 11 | Tarjetas, ahorro, experiencias |
| `/dia-de-la-mujer-y-del-hombre` | 1 | Cuenta nómina (beneficios) |
| `/proyecto-unicef` | 1 | Tarjeta débito UNICEF |
| `/depositos-2026` | 1 | CDT / depósitos |
| `/aliados-pyme` | 1 | Portafolio pyme |

El problema: sin un modelo de ciclo de vida, cuando la campaña termina la URL queda huérfana, o se deja el contenido publicado sin actualizar, o se borra sin redirección.

### Modelo propuesto: campañas ancladas al producto

```
Ubicación canónica:
  /personas/tarjetas-de-credito/campanas/fifa-2026/
  /personas/cuenta-de-ahorros/campanas/dia-de-la-mujer/
  /personas/cdt/campanas/depositos-2026/
  /empresas/pyme/campanas/aliados-pyme/

Redirección de vanity URL:
  /fifa-2026  →  /personas/tarjetas-de-credito/campanas/fifa-2026 (301)
```

La campaña FIFA tiene la estructura más desarrollada del sitio para este tipo de contenido (11 páginas: sedes, hospitality, skyboxes, golden ticket, tips de ahorro). Sus subpáginas son una mezcla de contenido informativo (sedes, récords, cuánto cuesta) y páginas de producto (golden ticket, hospitality). Se puede mantener como micrositio pero anclado al producto y con ciclo de vida explícito.

### Lifecycle de una campaña

```
Estado: ACTIVA
  → URL canónica en el producto
  → Vanity URL redirige

Estado: FINALIZADA
  → Página archivada en /[producto]/campanas/archivo/[nombre]
  → Vanity URL redirige al archivo
  → TyC permanecen accesibles (requerimiento legal)

Estado: ELIMINADA
  → 301 permanente al producto padre
  → TyC se mueven a /[producto]/terminos-y-condiciones/archivo/
```

---

## 9. Páginas funcionales y técnicas

Estas páginas no son contenido editorial: son herramientas o estados del sistema.

| Página | Tipo real | Propuesta |
|---|---|---|
| `/buscador` | Función del sitio | No debe ser sección en el árbol. Es parte de la UI. |
| `/extractos` | Función transaccional | No es página de contenido. Redirige a banca virtual. |
| `/pagina-404` | Estado de error | Eliminar del árbol de contenido. La página 404 es un template, no una URL. |
| `/personas-test` | Página de prueba | Eliminar de producción inmediatamente. |
| `/tag-aval` | Producto de pagos (TAG) | Mover a `/personas/medios-de-pago/tag-aval` o `/personas/servicios/tag-aval` |
| `/BuscadordePuntosAval` | Herramienta de puntos | Mover a `/personas/beneficios/puntos-aval` |
| `/exte-cuenta-ahorros` | Extensión de campaña | Mover a `/personas/cuenta-de-ahorros/campanas/` |
| `/transparencia` | Informe regulatorio | Mover a `/sobre-el-banco/informes/transparencia` |

---

## 10. Contenido dentro de `/personas` que no es producto

Dentro de la sección `/personas` existen páginas que no son productos sino herramientas de navegación, programas de lealtad y contenido operativo:

| Sección | Tipo real | Propuesta |
|---|---|---|
| `/personas/bienvenida/` | Onboarding de cliente nuevo | `/personas/empieza-aqui/` o widget de bienvenida |
| `/personas/portafolios/` (masivo, preferente, premium) | Segmentación de audiencia | Fusionar con `/banca-personas/` |
| `/personas/beneficios/` (plan-lealtad, tuplus) | Programa de puntos | `/personas/programa-de-beneficios/` |
| `/personas/promociones/` | Ofertas activas | `/personas/ofertas/` con ciclo de vida |
| `/personas/informacion-productos-servicios/` | Hub legal genérico | Su `terminos-condiciones` va a `/personas/terminos-generales/` |
| `/personas/experiencias-aval/` | Programa experiencias | `/personas/beneficios/experiencias-aval/` |
| `/personas/juega-refiere-y-gana/` | Campaña de referidos | `/personas/campanas/refiere-y-gana/` |
| `/personas/opciones-ponerte-al-dia/` | Gestión de mora | `/personas/gestiona-tu-credito/ponerse-al-dia/` |
| `/personas/servicio-transfiya/` | Servicio de transferencias | `/personas/medios-de-pago/transfiya/` |
| `/personas/bienes-e-inmuebles/` | Activos del banco | `/sobre-el-banco/bienes-e-inmuebles/` |
| `/personas/depositos/` | Página de depósitos | Fusionar con `/personas/cdt/` o `/personas/cuenta-de-ahorros/` |

---

## 11. Árbol propuesto completo (páginas no-producto)

```
www.bancodebogota.com/
│
├── /personas/               ← Hub de audiencia (ver ecosistemas de producto)
├── /empresas/               ← Hub de audiencia (ver ecosistemas de producto)
│
├── /ayuda/                  ← SOPORTE (renombrado de /atencion-al-cliente)
│   ├── /contacto/
│   │   ├── /servilineas
│   │   ├── /pqrs
│   │   └── /defensor-del-consumidor
│   ├── /canales/
│   │   ├── /oficinas
│   │   ├── /cajeros
│   │   ├── /banca-movil
│   │   ├── /banca-virtual
│   │   └── /corresponsales-bancarios
│   ├── /como-operar/
│   │   ├── /transferencias
│   │   ├── /pagos
│   │   └── /consultas-y-extractos
│   ├── /instructivos/
│   ├── /seguridad/
│   │   ├── /phishing
│   │   ├── /cajeros
│   │   ├── /celular
│   │   └── /oficinas
│   ├── /impuestos/
│   │   ├── /calendario
│   │   └── /canales-de-pago
│   └── /tus-derechos/
│       ├── /proteccion-datos-personales
│       └── /uso-de-cookies
│
├── /sobre-el-banco/         ← INSTITUCIONAL (nuevo hub)
│   ├── /quienes-somos
│   ├── /sostenibilidad/
│   │   ├── /estrategia-asg
│   │   ├── /ambiental
│   │   ├── /social
│   │   ├── /gobierno
│   │   └── /biblioteca
│   ├── /fundacion/
│   │   ├── /educacion-y-bienestar
│   │   ├── /emprendimiento
│   │   └── /proteccion-ambiental
│   ├── /diversidad-e-inclusion/
│   ├── /informes/
│   │   ├── /informe-gestion-2025
│   │   └── /archivo/
│   ├── /transparencia
│   └── /en/                 ← versión EN, estructura espejo
│       └── /sustainability/
│
├── /educacion-financiera/   ← EDITORIAL
│   ├── /finanzas-personales/
│   ├── /credito/
│   ├── /tarjetas/
│   ├── /inversion/
│   └── /seguros/
│
├── /tasas-y-tarifas/        ← PRECIOS (tabla comparadora)
│   └── /archivo/
│
└── /alianzas/               ← DIRECTORIO de socios (redirige a productos)
```

---

## 12. Resumen de reorganizaciones necesarias

| Página o sección | Acción | Destino |
|---|---|---|
| `/atencion-al-cliente` | Renombrar + reestructurar | `/ayuda/` |
| `/nuestra-organizacion` (raíz) | Fusionar | `/sobre-el-banco/` |
| `/sostenibilidad` | Mover | `/sobre-el-banco/sostenibilidad/` |
| `/sustainability` | Mover | `/sobre-el-banco/en/sustainability/` |
| `/diversidad-e-inclusion` | Mover | `/sobre-el-banco/diversidad-e-inclusion/` |
| `/informe-de-gestion`, `/informe-gestion-*` | Consolidar | `/sobre-el-banco/informes/` |
| `/management-report-2024` | Mover | `/sobre-el-banco/en/management-report/` |
| `/transparencia` | Mover | `/sobre-el-banco/transparencia` |
| `/educacion-financiera/nuestra-organizacion/nuestra-historia` | Mover | `/sobre-el-banco/quienes-somos/` |
| `/educacion-financiera/nuestra-organizacion/defensor-del-consumidor` | Mover | `/ayuda/tus-derechos/` |
| `/educacion-financiera/simuladores` | URL canónica en producto | `/personas/creditos/[producto]/simulador` |
| `/tasas-y-tarifas/tasas-20xx` | Archivar | `/tasas-y-tarifas/archivo/` |
| `/banca-personas`, `/banca-empresas` | Integrar en hubs de audiencia | `/personas/segmentos/`, `/empresas/` |
| `/alianzas/tarjeta-de-credito/*` | Redirigir al producto | `/personas/tarjetas-de-credito/[alianza]` |
| `/fifa-2026`, `/dia-de-la-mujer*` | Anclar al producto | `/personas/[producto]/campanas/[nombre]` |
| `/preguntas-frecuentes/medios-de-pago` | Mover | `/empresas/soluciones-de-cobro/` |
| `/atencion-al-cliente/impuestos` | Mover | `/ayuda/impuestos/` |
| `/pagina-404` | Eliminar del árbol | — |
| `/personas-test` | Eliminar de producción | — |
| `/buscador` | Eliminar del árbol | Es UI, no contenido |

---

*Ver también: [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md) y [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md)*
*Fecha: junio 2026.*
