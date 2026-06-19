# Análisis de Arquitectura de Información
## Banco de Bogotá — www.bancodebogota.com

> Documento generado a partir del árbol de URLs crawleado (`nowps/data/hierarchy.json`).
> Se excluyen URLs con `/wps`, `/documents` y `/s` para enfocarse en el contenido público navegable.

---

## 1. Resumen ejecutivo

El sitio tiene **887 nodos** en su árbol de contenido, distribuidos en **5 niveles de profundidad** y organizados bajo **31 secciones en el primer nivel**. La arquitectura presenta problemas estructurales graves: duplicidad de secciones para el mismo público, raíz sobrecargada, criterios de agrupación inconsistentes, contenido técnico/legal mezclado con contenido de producto, y páginas temporales o de prueba visibles en producción.

El **92% de las páginas tienen problemas SEO detectados**, lo que sugiere que los problemas de estructura se extienden también a la capa de metadatos.

---

## 2. Métricas generales del árbol

| Métrica | Valor |
|---|---|
| Dominio raíz | `www.bancodebogota.com` |
| Total de nodos en el árbol | 887 |
| Profundidad máxima | 5 niveles |
| Secciones en el nivel raíz (L1) | 31 |
| Secciones L1 con subsecciones | 15 |
| Páginas sueltas en raíz (sin hijos) | 16 |
| Páginas con problemas SEO detectados | ~92% |

### Distribución de nodos por nivel

| Nivel | Nodos | Descripción |
|---|---|---|
| 0 | 1 | Raíz del dominio |
| 1 | 31 | Secciones principales |
| 2 | 230 | Subsecciones |
| 3 | 428 | Sub-subsecciones |
| 4 | 169 | Cuarto nivel |
| 5 | 28 | Quinto nivel |

La masa de contenido está concentrada en los niveles 2 y 3 (658 nodos), lo que indica que la jerarquía visible para el usuario es más profunda de lo recomendable para un banco de consumo masivo.

---

## 3. Inventario de secciones de primer nivel (L1)

Las 31 secciones en la raíz se pueden clasificar por su naturaleza:

### 3.1 Secciones de negocio (productos y servicios)

| Sección | Páginas | Subsecciones | Avg. palabras |
|---|---|---|---|
| `/empresas` | 211 | 22 | 552 |
| `/personas` | 201 | 20 | 981 |
| `/atencion-al-cliente` | 138 | 11 | 556 |
| `/tyc` | 168 | 104 | 1.906 |
| `/banca-empresas` | 21 | 9 | 613 |
| `/banca-personas` | 15 | 8 | 566 |
| `/alianzas` | 9 | 2 | 679 |
| `/tasas-y-tarifas` | 18 | 17 | 95 |
| `/educacion-financiera` | 31 | 8 | 807 |
| `/bre-b` | 2 | 1 | — |

### 3.2 Secciones institucionales

| Sección | Páginas | Subsecciones |
|---|---|---|
| `/sostenibilidad` | 17 | 8 |
| `/nuestra-organizacion` | 7 | 1 |
| `/informe-de-gestion` | 1 | 0 |
| `/informe-gestion-2025` | 1 | 0 |
| `/informe-gestion-2024-3` | 1 | 0 |
| `/diversidad-e-inclusion` | 5 | 4 |
| `/transparencia` | 1 | 0 |

### 3.3 Secciones en inglés (sin estructura multilingüe)

| Sección | Páginas | Equivalente en español |
|---|---|---|
| `/sustainability` | 6 | `/sostenibilidad` |
| `/management-report-2024` | 1 | `/informe-de-gestion` |
| `/fifa-2026-en` | 1 | `/fifa-2026` |

### 3.4 Campañas temporales como secciones permanentes

| Sección | Páginas | Tipo |
|---|---|---|
| `/fifa-2026` | 11 | Campaña deportiva |
| `/dia-de-la-mujer-y-del-hombre` | 1 | Campaña de fecha especial |
| `/proyecto-unicef` | 1 | Campaña de responsabilidad social |
| `/depositos-2026` | 1 | Campaña de producto con año |
| `/aliados-pyme` | 1 | Landing de campaña |

### 3.5 Páginas sueltas sin categoría (huérfanas)

Estas 16 páginas viven directamente en la raíz sin pertenecer a ninguna sección jerárquica:

```
/BuscadordePuntosAval      /aliados-pyme          /buscador
/depositos-2026            /dia-de-la-mujer-y-del-hombre
/exte-cuenta-ahorros       /fifa-2026-en          /informe-de-gestion
/informe-gestion-2024-3    /informe-gestion-2025  /management-report-2024
/pagina-404                /personas-test         /proyecto-unicef
/tag-aval                  /transparencia
```

---

## 4. Problemas de arquitectura identificados

### 4.1 Raíz sobrecargada — 31 secciones en el primer nivel

**Impacto: Alto**

Una navegación principal efectiva en banca de consumo debería tener entre 5 y 8 opciones. Con 31 secciones en la raíz, el modelo mental que el sitio propone al usuario es inmanejable. Ni la navegación global ni ningún mega-menú puede representar coherentemente 31 destinos de primer nivel.

De esas 31 secciones, **16 son páginas sueltas sin hijos** (el 51%), lo que indica que no son secciones en sentido jerárquico sino páginas que nunca encontraron su lugar en la estructura y aterrizaron en la raíz por defecto.

**Ejemplo del problema:**
El usuario que quiere conocer las tasas de sus productos necesita encontrar `/tasas-y-tarifas`. Pero esa sección convive en el mismo nivel con `/fifa-2026`, `/proyecto-unicef` y `/BuscadordePuntosAval`, sin ninguna lógica que permita al usuario predecir dónde está cada cosa.

---

### 4.2 Duplicidad estructural: dos secciones para el mismo público

**Impacto: Alto**

El sitio tiene dos secciones paralelas para los mismos segmentos de usuario sin que quede claro cuál es la canónica:

#### Personas

| Sección | Páginas | Criterio de organización |
|---|---|---|
| `/personas` | 201 | Por tipo de **producto** (créditos, seguros, tarjetas, ahorros) |
| `/banca-personas` | 15 | Por tipo de **cliente** (premium, joven, pensionados, portafolio básico) |

Son dos modelos mentales distintos coexistiendo sin coordinación. Un usuario joven con cuenta de ahorros no sabe si debe ir a `/personas/cuenta-de-ahorros` o a `/banca-personas/joven`.

#### Empresas

| Sección | Páginas | Criterio de organización |
|---|---|---|
| `/empresas` | 211 | Por tipo de **producto/servicio** |
| `/banca-empresas` | 21 | Por **segmento empresarial** (pyme, corporativa, microempresas, institucional) |

`/banca-empresas` contiene los 9 segmentos del modelo comercial del banco (corporativa, empresarial, institucional, oficial, social, microfinanzas, etc.), mientras que `/empresas` organiza los productos sin referencia al segmento. Un cliente no sabe por cuál de los dos caminos debe empezar.

---

### 4.3 `/tyc` como sección de primer nivel — 168 páginas, 104 subsecciones directas

**Impacto: Alto**

`/tyc` (Términos y Condiciones) es la **tercera sección más grande del sitio** y la que tiene más subsecciones directas (104). Esto crea tres problemas:

1. **Descontextualización:** Los términos y condiciones de un producto cobran sentido cuando están junto al producto. Un usuario que explora `/personas/tarjetas-de-credito/gold` debería encontrar ahí los TyC de la tarjeta, no necesitar navegar a `/tyc/2025-tarjeta-gold`.

2. **Explosión de subsecciones:** La subsección `/tyc/2026` tiene por sí sola 63 páginas hijas, una por cada campaña o alianza activa en el año. Esto no es arquitectura; es un repositorio plano con fecha como prefijo.

3. **Peso SEO mal distribuido:** Las páginas de TyC tienen el promedio de palabras más alto del sitio (1.906 palabras promedio), lo que significa que los rastreadores encuentran más "contenido denso" en páginas legales que en páginas de producto.

**Muestra de la estructura actual de `/tyc`:**
```
/tyc/
  2025-akt-moto-forte
  2025-alianza-0-interes-claro
  2025-alianza-alfa
  2025-alianza-ambiente-gourmet
  ... (101 más)
  2026/
    cdts-con-millas-lifemiles-26
    san-valentin-mastercard-2026
    ... (61 más)
```

---

### 4.4 Criterios de agrupación inconsistentes entre `/personas` y `/empresas`

**Impacto: Medio-Alto**

Las dos secciones más grandes del sitio usan lógicas de organización distintas:

**`/personas`** organiza por tipo de producto:
- `tarjetas-de-credito` (44 pág)
- `seguros` (43 pág)
- `cuenta-de-ahorros` (36 pág)
- `creditos` (33 pág)
- `leasing`, `cdt`, `portafolios`...

**`/empresas`** mezcla productos con canales digitales:
- `portales` (37 pág) — canal digital, no producto
- `recaudos-y-pagos` (36 pág) — servicio transaccional
- `comercio-internacional-y-tesoreria` (32 pág) — línea de negocio
- `productos-de-credito` (30 pág) — categoría de producto
- `tarjetas-de-credito` (10 pág) — tipo de producto

En empresas, la sección `portales` contiene **36 páginas de instructivos** para el portal transaccional (cómo configurar usuarios, cómo hacer transferencias, cómo activar cheques), que son documentación técnica de soporte, no contenido de producto. Están en el mismo nivel jerárquico que las líneas de negocio.

---

### 4.5 Profundidad excesiva en `/atencion-al-cliente`

**Impacto: Medio**

La sección de atención al cliente tiene **138 páginas** en 11 subsecciones, con rutas que llegan a 5 niveles de profundidad:

```
/atencion-al-cliente
  /canales
    /canales-de-atencion-presencial
      /corresponsales-bancarios
        /beneficios-corresponsal       ← Nivel 5
        /como-ser-corresponsal         ← Nivel 5
      /oficinas
        /autobanco
        /oficina-express
        /oficina-incluyente
        /oficina-insignia
        /oficina-joven
        /oficina-premium
        /oficina-solo-clientes
        /oficina-tradicional
        /oficinas-universales
        ... (12 tipos de oficina)
```

Un usuario buscando la oficina más cercana debe atravesar 4 niveles de navegación antes de llegar al directorio. Adicionalmente, el banco tiene **12 tipos de oficina** como páginas independientes en el cuarto nivel, lo que sugiere que cada variante de oficina tiene su propia página en lugar de existir un directorio unificado con filtros.

Problema adicional: existe **duplicidad de la ruta de canales presenciales**. La sección `/atencion-al-cliente/canales/canales-de-atencion-presencial` convive con una segunda instancia de `/atencion-al-cliente/canales-de-atencion-presencial` que apunta a una sub-ruta de oficinas diferente.

---

### 4.6 Fragmentación de reportes institucionales

**Impacto: Medio**

Los informes de gestión y sostenibilidad existen como **4 URLs independientes en la raíz** sin agruparse bajo `/nuestra-organizacion` (que ya existe con 7 páginas):

```
/informe-de-gestion          (sin año, 1 pág)
/informe-gestion-2024-3      (versión 3 de 2024, 1 pág)
/informe-gestion-2025        (2025, 1 pág)
/management-report-2024      (versión en inglés, 1 pág)
```

Nótese el slug `informe-gestion-2024-3`, que usa un sufijo `-3` que parece un número de versión interno expuesto públicamente en la URL.

La sección `/nuestra-organizacion` (que sería el lugar lógico para estos contenidos) actualmente contiene páginas de educación financiera general (`/como-funciona-la-economia`, `/historia-del-dinero`) y del defensor del consumidor, no información corporativa.

---

### 4.7 Ausencia de estructura multilingüe coherente

**Impacto: Medio**

El contenido en inglés está disperso en tres ubicaciones independientes sin ninguna convención:

| URL en inglés | URL en español | Coherencia |
|---|---|---|
| `/sustainability` (6 pág, 5 subsecciones) | `/sostenibilidad` (1 pág) | Asimétrico: la versión EN tiene más contenido que la ES |
| `/management-report-2024` (1 pág) | `/informe-de-gestion` (1 pág) | Mismo contenido, URL diferente por idioma |
| `/fifa-2026-en` (1 pág) | `/fifa-2026` (11 pág) | La versión EN está drásticamente reducida |
| `/atencion-al-cliente/proteccion-al-consumidor/cybersecurity-and-security-management` | `/atencion-al-cliente/proteccion-al-consumidor/gestion-de-ciberseguridad-y-seguridad` | Mismo contenido dentro de una sección en español |

No existe una sección `/en/` ni atributos `hreflang` que relacionen las versiones entre sí. Para los motores de búsqueda, estas son páginas completamente independientes.

---

### 4.8 Secciones con nombres técnicos o versiones internas expuestas públicamente

**Impacto: Medio**

Varios slugs revelan convenciones de nomenclatura interna que nunca deberían llegar a URLs públicas:

| URL | Problema |
|---|---|
| `/personas-test` | Página de prueba en producción |
| `/pagina-404` | La página de error está indexada como contenido normal |
| `/exte-cuenta-ahorros` | Prefijo interno `exte-` (extensión?) expuesto |
| `/personas/cuenta-de-ahorros/pensionados-3` | Sufijo de versión `-3` expuesto en URL |
| `/personas/promociones/exte-ca` | Abreviatura interna sin significado para el usuario |
| `/personas/promociones/exte-tc` | Abreviatura interna sin significado para el usuario |
| `/informe-gestion-2024-3` | Número de versión en URL pública |
| `/depositos-2026` | Nombre de campaña con año hardcodeado |

---

### 4.9 Dispersión del producto `Bre-B` en múltiples secciones

**Impacto: Medio**

`Bre-B` (producto de pagos del banco) aparece fragmentado en al menos **5 ubicaciones distintas** del árbol sin una sección canónica:

```
/bre-b/llaves                                            ← Sección raíz propia (2 pág)
/empresas/bre-b                                          ← Dentro de empresas (1 pág)
/atencion-al-cliente/canales/transacciones               ← Implícito en transacciones
/atencion-al-cliente/instructivos/uso-de-bre-b          ← Instructivo en soporte
/atencion-al-cliente/instructivos/bre-b-en-whatsapp     ← Segundo instructivo
/atencion-al-cliente/preguntas-frecuentes/instructivos-bre-b ← Preguntas frecuentes
/tyc/2025-banca-movil-whatsapp-bre-b                    ← TyC
/tyc/2026/recibe-transferencias-a-cuentas-bdb-con-bre-b ← TyC de campaña
```

Un usuario que quiere conocer Bre-B completo no tiene un punto de entrada único. El producto está disperso entre una sección raíz propia (que solo tiene 2 páginas), una página dentro de empresas, instructivos en atención al cliente, y términos y condiciones en `/tyc`.

---

### 4.10 `/tasas-y-tarifas` como archivo histórico

**Impacto: Bajo-Medio**

La sección `/tasas-y-tarifas` tiene 18 páginas, pero **13 de ellas son archivos históricos** por año (desde `tasas-2014` hasta `tasas-2026`). El promedio de contenido es de apenas **95 palabras por página**, el más bajo de todas las secciones principales. Esto sugiere que las páginas históricas son documentos PDF embebidos o tablas de datos mínimas.

El problema: todas las versiones históricas conviven al mismo nivel que las tarifas actuales (`tarifas-personas`, `tarifas-empresas`, `tarifas-pyme`, `tarifas-internacional`), sin distinción entre contenido vigente y contenido de archivo.

---

### 4.11 Contenido de `/educacion-financiera` con `nuestra-organizacion` como subsección

**Impacto: Bajo-Medio**

Dentro de `/educacion-financiera` existe una subsección llamada `nuestra-organizacion` con 7 páginas. Esto genera un conflicto con la sección homónima `/nuestra-organizacion` que existe en la raíz:

```
/nuestra-organizacion (raíz)         → 4 páginas sobre el banco
/educacion-financiera/nuestra-organizacion → 7 páginas de educación financiera
```

El mismo nombre en dos lugares distintos del árbol con contenidos distintos crea ambigüedad tanto para usuarios como para motores de búsqueda.

---

### 4.12 Seguro de cancer — inconsistencia de nomenclatura

**Impacto: Bajo**

Dentro de `/personas/seguros` existen dos páginas con nombres distintos para el mismo producto:

```
/personas/seguros/cancer
/personas/seguros/cancer-femenino
/personas/seguros/proteccion-integral-cancer
```

Tres páginas con nombres solapados y sin jerarquía explícita entre ellas.

---

## 5. Mapa de duplicidades

| Contenido | URL A | Páginas | URL B | Páginas | Tipo de duplicidad |
|---|---|---|---|---|---|
| Banca personas | `/personas` | 201 | `/banca-personas` | 15 | Doble modelo mental |
| Banca empresas | `/empresas` | 211 | `/banca-empresas` | 21 | Doble modelo mental |
| Sostenibilidad ES | `/sostenibilidad` | 1 | — | — | Vaciada |
| Sostenibilidad EN | `/sustainability` | 6 | — | — | Sin par coherente |
| Informe gestión | `/informe-de-gestion` | 1 | `/informe-gestion-2025` | 1 | Misma sección, distintas URLs |
| Informe EN | `/management-report-2024` | 1 | `/informe-de-gestion` | 1 | Sin relación hreflang |
| FIFA ES | `/fifa-2026` | 11 | `/fifa-2026-en` | 1 | Sin estructura multilingüe |
| Canales presenciales | `/atencion-al-cliente/canales/canales-de-atencion-presencial` | 18 | `/atencion-al-cliente/canales-de-atencion-presencial` | 1 | Mismo nombre, dos URLs |
| Educación financiera org | `/educacion-financiera/nuestra-organizacion` | 7 | `/nuestra-organizacion` | 4 | Mismo nombre, distintos contenidos |
| Tarjeta de crédito | `/personas/tarjetas-de-credito` | 44 | `/alianzas/tarjeta-de-credito` | 7 | Mismo producto, distintas secciones |
| Leasing | `/personas/leasing` | 7 | `/empresas/leasing` | 8 | Mismo producto, dos audiencias |

---

## 6. Profundidad: ruta más larga

```
/atencion-al-cliente
  /canales
    /canales-de-atencion-presencial
      /corresponsales-bancarios
        /beneficios-corresponsal   ← NIVEL 5
```

5 niveles de profundidad para llegar a información sobre beneficios de ser corresponsal bancario. Ningún flujo de usuario real navega 5 clics desde la raíz.

---

## 7. Hallazgos SEO

| Problema | Alcance |
|---|---|
| Páginas con `seo_issues` detectados | ~92% del sitio |
| Páginas de TyC con alto peso de texto | 168 páginas, 1.906 palabras promedio |
| Contenido thin (<300 palabras) en secciones con 5+ páginas | 6 secciones |
| Páginas de tasas históricas (contenido de archivo) sin separación | 13 de 18 páginas en `/tasas-y-tarifas` |
| Página 404 indexada como contenido | 1 página en la raíz |
| Página de test en producción | `/personas-test` |
| URLs con versiones internas expuestas | 7+ casos identificados |

La sección más problemática por densidad de issues es `/atencion-al-cliente`, con **137 de 138 páginas** con `seo_issues`, seguida de `/personas` con una ratio similar.

---

## 8. Propuesta de reorganización (dirección estratégica)

Las siguientes recomendaciones no son una implementación, sino la dirección de reorganización que resolvería los problemas estructurales identificados.

### 8.1 Estructura sugerida para la raíz (5–7 secciones)

```
/personas                    (fusiona /personas + /banca-personas)
/empresas                    (fusiona /empresas + /banca-empresas)
/atencion-al-cliente         (consolida soporte, canales, PQRS, seguridad)
/nuestra-organizacion        (institucional, sostenibilidad, informes, transparencia)
/educacion-financiera        (educación, simuladores)
/tasas-y-tarifas             (solo vigentes; histórico en subpágina de archivo)
```

Las campañas temporales (`/fifa-2026`, `/dia-de-la-mujer-y-del-hombre`) deben vivir como **subsecciones de `/personas/promociones`** o **micrositios vinculados**, no como secciones raíz.

### 8.2 Integrar `/tyc` dentro de cada producto

En lugar de una sección `/tyc` global, los términos y condiciones deben publicarse como páginas hijas del producto al que aplican:

```
/personas/tarjetas-de-credito/gold/terminos-y-condiciones
/alianzas/tarjeta-de-credito/claro/terminos-y-condiciones
```

### 8.3 Establecer una estrategia multilingüe

Definir una convención única para el contenido en inglés:
- Opción A: Subdirectorio `/en/` que espeja la estructura principal
- Opción B: Atributos `hreflang` que relacionen cada par ES/EN

### 8.4 Crear una sección de archivo para contenido histórico

Las tasas históricas, informes anteriores y TyC vencidos deben moverse a una estructura de archivo separada que no compita en indexación con el contenido vigente:

```
/tasas-y-tarifas/archivo/2014 ... /2025
/nuestra-organizacion/informes/2024
```

### 8.5 Producto Bre-B: un solo punto de entrada

Consolidar todo el contenido de Bre-B bajo una sección propia con las subsecciones adecuadas, y referenciar desde esa sección hacia los instructivos (que pueden seguir viviendo en `/atencion-al-cliente`):

```
/personas/bre-b              (descripción del producto)
  /personas/bre-b/llaves
  /personas/bre-b/como-funciona
→ Ver también: /atencion-al-cliente/instructivos/uso-de-bre-b
```

---

## 9. Priorización de problemas

| # | Problema | Impacto | Esfuerzo | Prioridad |
|---|---|---|---|---|
| 1 | Duplicidad `/personas` + `/banca-personas` y `/empresas` + `/banca-empresas` | Alto | Medio | **Inmediata** |
| 2 | `/tyc` como sección de primer nivel descontextualizada | Alto | Alto | **Corto plazo** |
| 3 | 16 páginas huérfanas en la raíz + limpieza de test/404 | Alto | Bajo | **Inmediata** |
| 4 | Reducir la raíz de 31 a 6–7 secciones | Alto | Alto | **Corto plazo** |
| 5 | Unificar informes institucionales bajo `/nuestra-organizacion` | Medio | Bajo | **Inmediata** |
| 6 | Estrategia multilingüe coherente | Medio | Medio | **Corto plazo** |
| 7 | Fragmentación de Bre-B en 5+ secciones | Medio | Medio | **Mediano plazo** |
| 8 | Profundidad excesiva en `/atencion-al-cliente/canales` | Medio | Medio | **Mediano plazo** |
| 9 | Separar tasas vigentes de tasas históricas | Bajo | Bajo | **Mediano plazo** |
| 10 | Slugs con nomenclatura interna expuesta | Bajo | Alto* | **Largo plazo** |

_* Alto esfuerzo porque cambiar slugs públicos implica redirecciones 301 y riesgo de pérdida de ranking._

---

*Análisis elaborado por Claude Code a partir del crawl de `www.bancodebogota.com`.*
*Fecha: junio 2026.*
