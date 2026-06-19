# Taxonomía de tipos de página y ecosistemas de contenido
## Banco de Bogotá — www.bancodebogota.com

> Análisis derivado del crawl de `nowps/data/hierarchy.json` (887 nodos, 5 niveles de profundidad).
> El objetivo de este documento es identificar los tipos de página que existen en el sitio,
> proponer una jerarquía de contenido por producto/servicio, y diagnosticar los gaps actuales.

---

## 1. Tipos de página identificados en el sitio

El sitio tiene **16 tipos de página distintos** mezclados sin un modelo estructural explícito.
A continuación se definen por su función, su volumen actual y ejemplos reales.

| # | Tipo | Función | Nodos actuales | Ejemplo real |
|---|---|---|---|---|
| 1 | **Landing de sección** | Hub navegacional de una categoría | 20 | `/personas`, `/empresas`, `/atencion-al-cliente` |
| 2 | **Landing de producto** | Página principal que presenta un producto | ~180 | `/personas/creditos`, `/personas/tarjetas-de-credito` |
| 3 | **Micro-landing de variante** | Página de una versión específica del producto | ~157 | `/personas/tarjetas-de-credito/gold`, `/personas/tarjetas-de-credito/signature` |
| 4 | **Landing de alianza / cobranded** | Producto en co-marca con una empresa tercera | 23 | `/alianzas/tarjeta-de-credito/claro`, `/alianzas/tarjeta-de-credito/latam` |
| 5 | **Términos y condiciones (TyC)** | Página legal de un producto, campaña o alianza | 175 | `/tyc/2025-reglamento-y-beneficios-tc-on` |
| 6 | **Tarifas y tasas** | Tablas de precios, tasas de interés, cuotas | 21 | `/tasas-y-tarifas/tarifas-personas`, `/personas/tarjetas-de-credito/tasas-de-interes` |
| 7 | **Instructivo / tutorial** | Guías paso a paso para operar el producto | 45 | `/atencion-al-cliente/instructivos/uso-de-bre-b` |
| 8 | **FAQ / Preguntas frecuentes** | Respuestas a dudas comunes por producto | 2* | `/atencion-al-cliente/preguntas-frecuentes` |
| 9 | **Simulador** | Herramienta interactiva de cálculo | 2 | `/educacion-financiera/simulador-credito-libre-inversion` |
| 10 | **Seguridad bancaria** | Educación sobre fraudes y amenazas | 21 | `/atencion-al-cliente/seguridad-bancaria/phishing` |
| 11 | **Canal físico** | Descripción de tipos de punto de atención | 19 | `/atencion-al-cliente/canales/.../oficina-premium` |
| 12 | **Canal digital** | Descripción de apps, portales, medios digitales | 10 | `/atencion-al-cliente/canales/canales-digitales/banca-movil` |
| 13 | **Operativa transaccional** | Información sobre cómo ejecutar operaciones | 52 | `/atencion-al-cliente/canales/transacciones/transferencias` |
| 14 | **Educación financiera** | Artículos y guías de contenido financiero | 30 | `/educacion-financiera/creditos/antes-de-pedir-un-credito` |
| 15 | **Institucional / ESG** | Informes, sostenibilidad, diversidad | 13 | `/sostenibilidad`, `/diversidad-e-inclusion` |
| 16 | **Campaña temporal** | Landing de promoción o evento con fecha de vigencia | 6+ | `/fifa-2026`, `/dia-de-la-mujer-y-del-hombre` |

_* La cifra real es mayor: las FAQ existen pero dispersas como hojas sueltas bajo `/atencion-al-cliente/preguntas-frecuentes` (30 páginas), no como tipo estructurado por producto._

---

## 2. El problema central: ausencia de ecosistemas de producto

Actualmente el sitio organiza su contenido **por tipo de página** en lugar de **por producto**.

**Modelo actual (organización por tipo):**
```
/personas/tarjetas-de-credito/gold        ← landing variante
/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito  ← FAQ
/atencion-al-cliente/instructivos/activa-tus-tarjetas       ← instructivo
/tasas-y-tarifas/tarifas-personas         ← tarifa general (no por producto)
/tyc/2025-reglamento-y-beneficios-tc-on   ← TyC en sección global
```

Todo lo que rodea a la Tarjeta ON está en **4 secciones distintas del sitio** sin ningún vínculo estructural entre sí.

**Modelo propuesto (organización por ecosistema de producto):**
```
/personas/tarjetas-de-credito/on          ← landing del producto
  /tasas-y-tarifas                        ← tasas específicas
  /beneficios                             ← beneficios y coberturas
  /terminos-y-condiciones                 ← TyC propios
  /como-solicitarla                       ← instructivo de adquisición
  /preguntas-frecuentes                   ← FAQ del producto
```

Cada producto tiene su propio "ecosistema" donde el usuario puede resolver toda la jornada (descubrir → entender → comparar → decidir → gestionar) sin salir de la sección del producto.

---

## 3. Definición de tipos de página por rol en el ecosistema

### Nivel 0 — Raíz de audiencia
Punto de entrada por segmento. Define el modelo mental del usuario.

| Tipo | Propósito | Audiencia |
|---|---|---|
| **Hub de audiencia** | Selección de segmento | Cualquier visitante |

Ejemplos: `/personas`, `/empresas`
Contenido: navegación a categorías de producto, accesos directos a los productos más buscados, banners de campañas activas.

---

### Nivel 1 — Categoría de producto (Landing de categoría)
Agrupa todos los productos de una misma naturaleza para esa audiencia.

| Tipo | Propósito | Ejemplos actuales |
|---|---|---|
| **Landing de categoría** | Comparar productos de una familia | `/personas/tarjetas-de-credito`, `/personas/creditos`, `/personas/seguros` |

Contenido típico: comparador de productos, tarjetas de presentación de cada variante, filtros por necesidad del cliente.
Volumen actual: ~15–20 páginas funcionando como esto.

---

### Nivel 2 — Producto principal (Landing de producto)
Página canónica de un producto específico. Es el centro del ecosistema.

| Tipo | Propósito | Ejemplo actual |
|---|---|---|
| **Landing de producto** | Presentar, convencer y dirigir al proceso de adquisición | `/personas/tarjetas-de-credito/gold`, `/personas/creditos/libranza` |

Contenido típico: propuesta de valor, características principales, requisitos, CTA de solicitud, acceso a subpáginas del ecosistema.
Volumen actual: ~180 páginas identificadas como landings de producto.

---

### Nivel 3 — Páginas del ecosistema (satélites del producto)
Páginas especializadas que viven **dentro** del producto, no en secciones globales.

| Tipo de satélite | Propósito | Dónde está hoy | Dónde debería estar |
|---|---|---|---|
| **Variante** | Versión específica (clásica, gold, premium) | Junto al producto ✓ | Junto al producto ✓ |
| **Tasas y tarifas** | Precios, tasas, cuotas de manejo | `/tasas-y-tarifas/` (global) ✗ | `/[producto]/tasas-y-tarifas` |
| **Términos y condiciones** | Contrato del producto | `/tyc/` (global) ✗ | `/[producto]/terminos-y-condiciones` |
| **Beneficios y coberturas** | Detalles de lo que incluye | Disperso en la landing ✗ | `/[producto]/beneficios` |
| **Cómo solicitar / gestionar** | Pasos de adquisición y operación | `/atencion-al-cliente/instructivos/` ✗ | `/[producto]/como-solicitarlo` |
| **Preguntas frecuentes** | Dudas del producto | `/atencion-al-cliente/preguntas-frecuentes/` (global) ✗ | `/[producto]/preguntas-frecuentes` |
| **Simulador** | Cálculo de cuotas, proyecciones | `/educacion-financiera/` ✗ | `/[producto]/simulador` |
| **Alianza cobranded** | Versión del producto con una marca | `/alianzas/` (global) ✗ | `/[producto]/alianzas/[marca]` |

**Hallazgo crítico:** Ninguno de los productos actuales tiene TyC, FAQ ni simulador dentro de su propio árbol.

```
GAP por producto (estado actual):
  /personas/creditos          TyC=NO   FAQ=NO   Simulador=NO   Tasas=SÍ (solo 1 pág)
  /personas/seguros           TyC=NO   FAQ=NO   Simulador=NO   Tasas=NO
  /personas/cuenta-de-ahorros TyC=NO   FAQ=NO   Simulador=NO   Tasas=NO
  /personas/tarjetas-de-credito  TyC=NO   FAQ=NO   Simulador=NO   Tasas=SÍ (2 págs)
  /personas/leasing           TyC=NO   FAQ=NO   Simulador=NO   Tasas=NO
  /personas/cdt               TyC=NO   FAQ=NO   Simulador=NO   Tasas=NO
```

---

## 4. Modelo de ecosistema de contenido por producto

Este es el modelo que debería aplicarse a cada producto del banco.

```
/[audiencia]/[categoria]/[producto]/
│
├── (raíz del producto)          ← Landing de producto
│     Propuesta de valor, características, requisitos, CTA
│
├── /variantes/                  ← Solo si el producto tiene versiones
│   ├── /clasica
│   ├── /gold
│   └── /premium
│
├── /beneficios                  ← Coberturas, ventajas, comparativo
│
├── /tasas-y-tarifas             ← Tabla de tasas y costos del producto
│
├── /como-solicitarlo            ← Proceso de adquisición
│
├── /gestiona-tu-producto        ← Operativa post-venta (instructivos)
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-tarjeta
│   └── /cambiar-fecha-pago
│
├── /alianzas/                   ← Solo si tiene cobranded
│   ├── /claro
│   └── /latam-pass
│
├── /preguntas-frecuentes        ← FAQ específicas del producto
│
├── /simulador                   ← Solo para productos con cálculo (créditos, CDT)
│
└── /terminos-y-condiciones      ← TyC legales del producto
```

### 4.1 Ejemplo aplicado: Tarjeta de crédito Gold

**Estado actual (disperso en el sitio):**
```
/personas/tarjetas-de-credito/gold               ← landing
/atencion-al-cliente/instructivos/activa-tus-tarjetas   ← instructivo (genérico)
/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito ← FAQ (genérica)
/tyc/2025-reglamento-y-beneficios-tc-on          ← TyC en sección global
/tasas-y-tarifas/tarifas-personas                ← tarifas generales
/alianzas/tarjeta-de-credito/latam-pass          ← alianza en sección separada
```

**Estado propuesto (ecosistema unificado):**
```
/personas/tarjetas-de-credito/gold
├── (landing Gold)               ← características, CTA solicitar
├── /beneficios
│   ├── /salas-vip-mastercard
│   └── /visa-airport-companion
├── /tasas-y-tarifas             ← tasa de interés, cuota de manejo
├── /como-solicitarla
├── /gestiona-tu-tarjeta
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   └── /cambiar-fecha-de-pago
├── /latam-pass                  ← versión alianza dentro del producto
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 4.2 Ejemplo aplicado: Crédito de vivienda

**Estado actual:**
```
/personas/creditos/portafolio-vivienda           ← landing de categoría vivienda
/personas/creditos/portafolio-vivienda/vivienda  ← producto principal (3.075w)
/personas/creditos/portafolio-vivienda/colombianos-en-el-exterior
/personas/creditos/portafolio-vivienda/compra-cartera
/personas/creditos/portafolio-vivienda/credito-remodelacion
/personas/creditos/portafolio-vivienda/reduce-tu-cuota
/personas/creditos/portafolio-vivienda/vivienda-sostenible
/personas/creditos/tasas-de-interes             ← tasas GENERALES de todos los créditos
/educacion-financiera/simulador-credito-vivienda ← simulador en otra sección
/tyc/[múltiples entradas de vivienda]            ← TyC en sección global
```

Este es el producto con la estructura más cercana al modelo ideal, pero le faltan: TyC integrado, FAQ y el simulador dentro del ecosistema.

**Estado propuesto:**
```
/personas/creditos/vivienda
├── (landing)
├── /variantes
│   ├── /vivienda-sostenible
│   ├── /colombianos-en-el-exterior
│   └── /credito-remodelacion
├── /beneficios-gobierno
│   ├── /frech-no-vis-sostenible
│   └── /vivienda-interes-prioritario
├── /tasas-y-tarifas
├── /simulador                   ← movido de /educacion-financiera
├── /como-solicitarlo
├── /gestiona-tu-credito
│   └── /reduce-tu-cuota
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 4.3 Ejemplo aplicado: Seguros de vida

El caso de seguros es el más fragmentado. Actualmente hay **41 páginas de seguros** todas al mismo nivel jerárquico bajo `/personas/seguros/`, sin ninguna agrupación por familia de seguro:

```
/personas/seguros/
  /vida-ahorrador       /vida-alto-valor        /proteccion-vida
  /seguro-proteccion-vida /retiro-mas-seguro     /enfermedad-grave
  /cancer               /cancer-femenino         /proteccion-integral-cancer
  /cuenta-protegida     /cuenta-protegida-integral
  /cuota-protegida      /cuota-protegida-asalariados  ... (8 variantes más)
  /hogar-seguro         /auto-protegido-plus    /movilidad-segura
  /bolso-protegido      /proteccion-mascotas    /multiasistencias
  ... (21 seguros más al mismo nivel)
```

41 productos planos, sin categorizar, sin TyC integrado, sin FAQ. El usuario no puede distinguir qué tipo de seguro necesita.

**Propuesta de reorganización con familias:**
```
/personas/seguros/
├── /vida-y-salud                ← Familia: protección personal
│   ├── /vida-ahorrador
│   ├── /vida-alto-valor
│   ├── /enfermedad-grave
│   ├── /cancer
│   └── (cada uno con: /beneficios, /tyc, /faq)
├── /proteccion-creditos         ← Familia: seguros asociados a deuda
│   ├── /cuota-protegida
│   ├── /cuota-protegida-vivienda
│   └── (variantes por tipo de crédito)
├── /patrimonio-y-hogar          ← Familia: bienes
│   ├── /hogar-seguro
│   ├── /auto-protegido-plus
│   └── /movilidad-segura
└── /asistencias                 ← Familia: servicios adicionales
    ├── /multiasistencias
    ├── /bolso-protegido
    └── /proteccion-mascotas
```

---

## 5. Tipos de página para el ecosistema de Empresas

El segmento empresas tiene sus propias particularidades. Además de los tipos estándar, requiere:

| Tipo adicional | Propósito | Ejemplo actual |
|---|---|---|
| **Instructivo de portal** | Guías de uso del portal transaccional (B2B) | `/empresas/portales/instructivo-*` (36 páginas) |
| **Segmento empresarial** | Portafolio para un tipo de empresa | `/banca-empresas/pyme`, `/banca-empresas/corporativa` |
| **Solución integrada** | Servicio que agrupa varios productos | `/empresas/comercio-internacional-y-tesoreria` |

Los 36 instructivos del portal empresarial deberían estar en su propio hub de documentación técnica, separados del catálogo de productos:

```
/empresas/portal-negocios/
├── (landing del portal)
├── /como-acceder
├── /instructivos/
│   ├── /primer-ingreso
│   ├── /configuracion-usuarios
│   ├── /transferencias
│   └── ... (resto de instructivos)
└── /soporte
```

---

## 6. Tipos de página de soporte (transversales a todos los productos)

Estos tipos de página son transversales y deben existir tanto en versión global como anclada a cada producto.

### 6.1 FAQ: el tipo más infrautilizado

El sitio tiene una sola sección de FAQ (`/atencion-al-cliente/preguntas-frecuentes`) con 30 subpáginas genéricas. **No hay FAQ por producto.** Esto fuerza al usuario a navegar a una sección de soporte para resolver dudas que deberían resolverse en la página del producto.

Estado actual de `/atencion-al-cliente/preguntas-frecuentes`:
```
/adelanto-de-nomina      /banca-movil           /banco-de-bogota
/cdt                     /ceropay               /crediestudiantil
/crediservice            /credito-de-vehiculo   /cuatro-por-mil
/cuenta-corriente        /cuenta-de-ahorros     /cupoagil-banco-de-bogota
/habeas-data             /instacupo             /instructivos-bre-b
/libranza                /libre-inversion       /medios-de-pago (13 sub)
/mi-trabajo              /portafolio-de-vivienda ...
```

Estas FAQ deberían migrarse a `/[producto]/preguntas-frecuentes` y la sección global convertirse en un buscador de FAQ unificado.

### 6.2 Simuladores: 2 páginas para toda la oferta de crédito

Solo existen 2 simuladores en el sitio, ambos en `/educacion-financiera/`:
- `simulador-credito-libre-inversion`
- `simulador-credito-vivienda`

No hay simulador de CDT, tarjeta de crédito, leasing ni ningún otro producto. Y los dos existentes están en la sección de educación, no dentro del producto.

### 6.3 Instructivos: genéricos vs. específicos de producto

Los 45 instructivos actuales están todos bajo `/atencion-al-cliente/instructivos/` y son en su mayoría genéricos (activa tu tarjeta, bloquea tu tarjeta). Los instructivos del portal empresarial (36 páginas) están bajo `/empresas/portales/`.

Propuesta: dos niveles de instructivos:
- **Instructivos globales** (válidos para cualquier producto): `/atencion-al-cliente/instructivos/` (permanece)
- **Instructivos de producto**: `/[producto]/gestiona-tu-[producto]/` (nuevo, específico)

---

## 7. Tipos de página para campañas temporales

Las campañas actualmente son secciones de primer nivel. Deben pasar a un modelo de micrositio anclado al producto que promueven.

| Campaña actual | Producto que promueve | Ubicación propuesta |
|---|---|---|
| `/fifa-2026` | Tarjeta de crédito, ahorros | `/personas/tarjetas-de-credito/campanas/fifa-2026` |
| `/dia-de-la-mujer-y-del-hombre` | Beneficios de cuenta nómina | `/personas/cuenta-de-ahorros/campanas/dia-de-la-mujer` |
| `/depositos-2026` | CDT / depósitos | `/personas/cdt/campanas/depositos-2026` |
| `/aliados-pyme` | Portafolio pyme | `/empresas/pyme/campanas/aliados-pyme` |

Los TyC de las campañas seguirían el mismo principio: viven dentro de la campaña.

---

## 8. Resumen: inventario de tipos de página por ecosistema

Cada producto debería poder instanciar estos tipos de página según aplique:

```
TIPO A — Hub de audiencia               (1 por audiencia: personas, empresas)
TIPO B — Landing de categoría           (1 por familia de producto)
TIPO C — Landing de producto            (1 por producto)
TIPO D — Micro-landing de variante      (1 por versión del producto)
TIPO E — Beneficios y coberturas        (1 por producto)
TIPO F — Tasas y tarifas                (1 por producto; tablas actualizables)
TIPO G — Cómo solicitarlo / adquirir    (1 por producto)
TIPO H — Gestión post-venta             (1 hub + n instructivos por producto)
TIPO I — Alianza cobranded              (1 por alianza dentro del producto)
TIPO J — FAQ del producto               (1 por producto)
TIPO K — Simulador                      (1 por producto con cálculo)
TIPO L — Términos y condiciones         (1 por producto + 1 por campaña activa)
TIPO M — Campaña temporal               (efímera, anclada al producto)
TIPO N — Educación financiera           (contenido editorial transversal)
TIPO O — Seguridad bancaria             (transversal, en soporte)
TIPO P — Regulatorio / consumidor       (transversal, en institucional)
```

### Aplicabilidad por producto:

| Producto | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Tarjeta crédito | ✓ | ✓ | ✓ (muchas) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Créditos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| Cuenta de ahorros | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ |
| Seguros | ✓ | ✓ | ✓ (familias) | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ |
| CDT | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| Leasing | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| Portal empresarial | ✓ | ✓ | — | — | ✓ | ✓ | ✓ (36 docs) | — | ✓ | — | ✓ |

**Estado actual:** Ningún producto tiene más de 3 de estos 11 tipos integrados en su propio árbol.
**Estado propuesto:** Cada producto puede instanciar entre 6 y 10 tipos según su naturaleza.

---

## 9. Implicaciones para la arquitectura de URLs

El modelo de ecosistema implica una estructura de URL predecible y consistente:

```
/[audiencia]/[categoria]/[producto]/[tipo-de-pagina]

Ejemplos:
  /personas/creditos/vivienda/simulador
  /personas/creditos/vivienda/terminos-y-condiciones
  /personas/tarjetas-de-credito/gold/como-solicitarla
  /personas/tarjetas-de-credito/gold/alianzas/latam-pass
  /personas/seguros/vida-ahorrador/preguntas-frecuentes
  /empresas/portal-negocios/instructivos/primer-ingreso
  /empresas/productos-de-credito/leasing/tasas-y-tarifas
```

Esta estructura permite:
- **Predecibilidad:** el usuario sabe dónde buscar cualquier tipo de información
- **Consistencia SEO:** las páginas de tasas, TyC y FAQ de cada producto compiten en búsquedas específicas ("tasas tarjeta gold banco bogotá")
- **Mantenimiento:** los equipos de contenido saben exactamente dónde publicar cada tipo de actualización
- **Redirects ordenados:** cuando se retira un producto, toda su carpeta puede redirigirse coherentemente

---

*Análisis elaborado por Claude Code a partir del crawl de `www.bancodebogota.com`.*
*Ver también: [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md)*
*Fecha: junio 2026.*
