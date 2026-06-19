# Tarjetas de crédito — Estado actual
## Banco de Bogotá — www.bancodebogota.com

> Documento basado en el crawl real del sitio (`nowps/data/hierarchy.json`).
> Registra la estructura tal como existe hoy: URLs reales, ubicación del contenido satelital
> (TyC, FAQ, instructivos, tasas) y los problemas estructurales identificados.

---

## 1. Resumen del inventario

| Sección | URLs | Observación |
|---|---|---|
| `/personas/tarjetas-de-credito/` | 44 | Sección principal — mezcla productos, funciones y campañas |
| `/alianzas/tarjeta-de-credito/` | 7 | Sección paralela — duplica alianzas que ya están en `/personas/` |
| `/empresas/tarjetas-de-credito/` | 10 | Tarjetas empresariales sin ecosistema |
| `/empresas/tarjetas-debito/` | 6 | Separada de crédito — sin cruzar con personas |
| TyC en `/tyc/` | ~48 | Dispersos globalmente, sin ancla al producto |
| FAQ en `/atencion-al-cliente/` | 3 | Genéricas, no por tarjeta |
| Instructivos en `/atencion-al-cliente/` | 7 | Genéricos, no por tarjeta |
| Tasas en `/tasas-y-tarifas/` | 1 tabla general | Sin desagregación por producto |
| **Total de URLs relacionadas** | **~125** | Distribuidas en 5 secciones distintas |

---

## 2. Árbol completo — `/personas/tarjetas-de-credito/`

### 2.1 Tarjetas propias del banco

```
/personas/tarjetas-de-credito/                   ← Hub comparador (36 hijos directos)
│
├── /clasica                                      · Tarjeta de entrada
│   └── /vtu                                      ⚠ Slug interno expuesto (164 palabras)
│
├── /economia                                     · Variante económica
├── /masivo                                       · Tarjeta para distribución masiva
│
├── /gold                                         · Nivel medio
├── /platinum                                     · Nivel alto
│
├── /premium                                      · Nivel premium — rama inusual
│   ├── /premium/master                           · Versión Mastercard
│   └── /premium/visa                             · Versión Visa
│                                                 ⚠ Único producto con bifurcación por red
│
├── /infinite                                     · Tarjeta Visa tope de gama
├── /signature                                    · Tarjeta Visa premium
├── /black-master                                 · Tarjeta Mastercard tope de gama
│
├── /on                                           · Tarjeta digital (sin sucursal)
├── /amparada                                     · Tarjeta con seguro incorporado
│
└── /aliada                                       · Tarjeta de convenio
    └── /vtu                                      ⚠ Slug interno expuesto (163 palabras)
```

**Convenio institucional:**
```
├── /tc-anderson                                  · Tarjeta convenio Anderson
```

### 2.2 Tarjetas alianza (cobranded) — presentes bajo `/personas/`

```
/personas/tarjetas-de-credito/
│
├── /biomax-clasica                               · Alianza Biomax — nivel clásico
├── /biomax-gold                                  · Alianza Biomax — nivel gold
│
├── /movistar                                     · Hub alianza Movistar (landing general)
├── /movistar-clasica                             · Movistar — nivel clásico
├── /movistar-gold                                · Movistar — nivel gold
├── /movistar-platinum                            · Movistar — nivel platinum
│
├── /clasica-latam-pass                           · Alianza Latam Pass — nivel clásico
├── /gold-latam-pass                              · Alianza Latam Pass — nivel gold
├── /platinum-latam-pass                          · Alianza Latam Pass — nivel platinum
├── /signature-latam-pass                         · Alianza Latam Pass — nivel signature
└── /tarjetas-latam                               · Hub general de tarjetas Latam Pass
```

### 2.3 Páginas funcionales mezcladas con productos

```
/personas/tarjetas-de-credito/
│
├── /avances                                      · Información sobre avances en efectivo
├── /alivios                                      · Alivios financieros (gestión de deuda)
├── /compra-cartera                               · Traslado de deuda desde otro banco
├── /cerorollo                                    · Diferidos sin interés (promociión)
├── /instacupo                                    · Aumento de cupo inmediato
├── /pago-impuestos                               · Pago de impuestos con TC
├── /pago-minimo-alterno                          · Información sobre pago mínimo
├── /cuota-de-manejo                              · Información sobre cuota de manejo
├── /sin-cuota-de-manejo                          · Tarjetas sin cuota (comparador)
└── /black-week                                   ⚠ Campaña temporal al mismo nivel que productos
```

⚠ **Problema:** 10 páginas funcionales y una campaña conviven al mismo nivel jerárquico que las tarjetas-producto, sin distinción visual ni estructural para el usuario.

### 2.4 Asistencias y beneficios

```
/personas/tarjetas-de-credito/
│
├── /asistencias                                  · Hub de asistencias (solo existen 2 hijas)
│   ├── /salas-vip-tc-black-mastercard            · Beneficio específico de Black
│   └── /visa-airport-companion                  · Beneficio específico de Visa
│
└── /tasas-de-interes                             · Tabla general (aplica a todas las TC)
```

⚠ **Problema:** `/asistencias` solo documenta beneficios de 2 tarjetas premium. Las demás tarjetas no tienen ninguna página de beneficios en su árbol.

---

## 3. Árbol completo — `/alianzas/tarjeta-de-credito/`

```
/alianzas/                                        ← Sección paralela (9 URLs total)
└── /tarjeta-de-credito/                          ← Hub de alianzas (duplica la lógica de /personas/)
    ├── /claro                                    · Tarjeta Claro — no presente en /personas/
    ├── /comprar-apple-sin-intereses              · Oferta puntual — no es una tarjeta
    ├── /decathlon                                · Tarjeta Decathlon — no presente en /personas/
    ├── /mercado-libre                            · Tarjeta Mercado Libre — no presente en /personas/
    ├── /movistar-alianza                         ⚠ DUPLICADO: /personas/tarjetas-de-credito/movistar (y 3 sub)
    └── /tigo                                     · Tarjeta Tigo — no presente en /personas/
```

### Mapa de inconsistencias entre `/personas/` y `/alianzas/`

| Alianza | En `/personas/tarjetas-de-credito/` | En `/alianzas/tarjeta-de-credito/` | Problema |
|---|---|---|---|
| Movistar | `/movistar` + `/movistar-clasica` + `/movistar-gold` + `/movistar-platinum` | `/movistar-alianza` | 5 URLs para la misma alianza |
| Biomax | `/biomax-clasica` + `/biomax-gold` | — | No tiene URL en /alianzas/ |
| Latam Pass | `/clasica-latam-pass` + `/gold-latam-pass` + `/platinum-latam-pass` + `/signature-latam-pass` + `/tarjetas-latam` | — | No tiene URL en /alianzas/ |
| Claro | — | `/claro` | Solo existe en /alianzas/ |
| Tigo | — | `/tigo` | Solo existe en /alianzas/ |
| Decathlon | — | `/decathlon` | Solo existe en /alianzas/ |
| Mercado Libre | — | `/mercado-libre` | Solo existe en /alianzas/ |
| Anderson | `/tc-anderson` | — | Convenio, no alianza comercial |

**Resultado:** No hay un modelo único para las alianzas. Cada una resolvió su URL de forma distinta.

---

## 4. Árbol completo — Empresas

### 4.1 `/empresas/tarjetas-de-credito/`

```
/empresas/tarjetas-de-credito/                   ← Hub (10 páginas, sin ecosistema)
├── /negocios                                     · TC básica para empresas
├── /negocios-elite                               · TC premium para empresas
├── /corporativa                                  · TC para grandes corporaciones
├── /compras-institucionales                      · TC para entidades públicas/instituciones
├── /destinos                                     · TC con beneficios de viaje
├── /latam-business                               · Alianza Latam para empresas
├── /crecer                                       · TC microempresas — nivel crecer
├── /logros                                       · TC microempresas — nivel logros
└── /tarjeta-visa-distribucion                   · TC para distribuidores
```

⚠ **Nota:** Las tarjetas `crecer` y `logros` también existen en `/empresas/tarjetas-debito/crecer` y `/logros` — dos modalidades (crédito y débito) con el mismo nombre, sin diferenciación clara.

### 4.2 `/empresas/tarjetas-debito/` (referencia contextual)

```
/empresas/tarjetas-debito/                       ← Sección separada (6 páginas)
├── /negocios
├── /afinidad
├── /cedula-cafetera
├── /crecer                                       ⚠ Mismo nombre que TC crecer
└── /logros                                       ⚠ Mismo nombre que TC logros
```

---

## 5. Contenido satelital disperso

### 5.1 TyC en `/tyc/` — ~48 entradas relacionadas con tarjetas

Ningún TyC vive dentro del árbol de la tarjeta a la que aplica. Todos están en la sección global `/tyc/`.

**TyC de reglamento / producto base:**
```
/tyc/2025-reglamento-y-beneficios-tc-on
```

**TyC de campañas de facturación:**
```
/tyc/2025-campana-tc-amor-y-amistad
/tyc/2025-halloween-tarjeta-de-credito
/tyc/2025-vacaciones-tarjeta-credito
/tyc/2025-la-expedicion-del-camello
/tyc/2025-golden-ticket
/tyc/2025-experiencia-del-futbol-tc-octubre
/tyc/2025-despega-con-tus-compras
/tyc/2026/retos-facturacion-tarjeta-credito
/tyc/2026/tu-tarjeta-credito-te-pone-a-jugar
/tyc/2026/tarjeta-credito-on-al-natural
/tyc/2026/acepta-tu-tarjeta-credito-laminas-mundial
/tyc/2026/vive-tu-mundial-fifa-masivo
/tyc/2026/experiencia-del-futbol-mas-grande-masivo
/tyc/2026/el-futbol-comienza-con-la-app
```

**TyC de avances:**
```
/tyc/2025-tasas-especiales-avances
/tyc/2025-tasas-especiales-no-avanceros
/tyc/2025-tus-avances-premian-3.0
/tyc/2025-tus-avances-te-premian-noviembre
/tyc/2026/avance-sorprender-a-mama
```

**TyC de alianzas:**
```
/tyc/2025-alianza-0-interes-claro
/tyc/2025-tc-0-ishop-colombia
/tyc/2025-tigo-0-porciento-interes
/tyc/2025-usala-y-gana-latam-pass
/tyc/2025-usala-y-gana-latam-pass-mas-cuotas
/tyc/2025-alianza-despegar-tarjetazo
/tyc/2025-alianza-micelu-tarjeta-credito
/tyc/2025-cross-border-tc-td-visa
/tyc/2025-cdts-con-millas-lifemiles
/tyc/2026/cdts-con-millas-lifemiles-26
```

**TyC de gestión / retención:**
```
/tyc/2025-upgrade-tarjeta-de-credito
/tyc/2025-retencion-novacion
/tyc/2025-retencion-para-ampliacion-plazo
/tyc/2025-tarjeta-credito-cero-porciento-interes
/tyc/2025-tasa-especial-para-disminucion-cuota
/tyc/2026/cuota-comodin-post-desembolso
/tyc/2025-colocacion-tc-bonos-kift
/tyc/2025-pladani-masivo
```

**TyC de colocación / adquisición:**
```
/tyc/2025-enrolamiento-apple-pay-tc-mastercard
/tyc/2025-facturacion-apple-pay-tc-mastercard
/tyc/2026/recibe-pagos-con-qr-y-gana
```

**TyC de servicios asociados:**
```
/tyc/2025-crediservice-siempre-contigo
/tyc/2025-exoneracion-cuota-administracion-crediservice
/tyc/2025-fin-de-anio-con-crediservice
/tyc/2025-vamos-a-la-experiencia-del-futbol-masivo
```

### 5.2 FAQ en `/atencion-al-cliente/preguntas-frecuentes/`

```
/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito          ← FAQ personas (genérica)
/atencion-al-cliente/preguntas-frecuentes/tarjeta-credito-empresas  ← FAQ empresas (genérica)
/atencion-al-cliente/preguntas-frecuentes/medios-de-pago/pagos-con-tarjeta
```

⚠ **Problema:** No existe FAQ por variante de tarjeta. Una FAQ única cubre todas las tarjetas (clásica, gold, platinum, infinite, etc.) sin distinción.

### 5.3 Instructivos en `/atencion-al-cliente/instructivos/`

```
/atencion-al-cliente/instructivos/activa-tus-tarjetas                  · Genérico para todas
/atencion-al-cliente/instructivos/bloquear-tarjetas-por-perdida-robo   · Genérico para todas
/atencion-al-cliente/instructivos/cambio-fecha-pago-tarjeta-credito    · Solo TC
/atencion-al-cliente/instructivos/congelar-tarjeta-facil-seguro        · Genérico
/atencion-al-cliente/instructivos/desbloqueo-tarjeta-debito-clave-errada · Solo TD (mal clasificado con TC?)
/atencion-al-cliente/instructivos/diferido-automatico-tarjeta-credito  · Solo TC
/atencion-al-cliente/instructivos/refinanciar-deuda-tc                 · Solo TC
```

⚠ **Problema:** 7 instructivos genéricos para todas las tarjetas. Ninguno está contextualizado dentro del árbol de una tarjeta específica.

### 5.4 Tasas en `/tasas-y-tarifas/`

```
/tasas-y-tarifas/tarifas-personas    ← Tabla general: incluye TC, cuentas, créditos
/tasas-y-tarifas/tarifas-empresas    ← Tabla general: incluye TC empresas y otros productos
```

Solo existe una página por audiencia para todos los productos. No hay tasas por variante de tarjeta.

La única excepción es la página interna al árbol:
```
/personas/tarjetas-de-credito/tasas-de-interes   ← Tasas para todas las TC (no por variante)
```

---

## 6. Diagnóstico de problemas

### 6.1 Duplicidad de secciones para alianzas

El mismo producto (ej. Movistar) existe en dos rutas sin relación canónica declarada:

```
/personas/tarjetas-de-credito/movistar           ← hub movistar en personas
/personas/tarjetas-de-credito/movistar-clasica   ← variante en personas
/personas/tarjetas-de-credito/movistar-gold      ← variante en personas
/personas/tarjetas-de-credito/movistar-platinum  ← variante en personas
/alianzas/tarjeta-de-credito/movistar-alianza    ← DUPLICADO en /alianzas/
```

Total: 5 URLs para una sola alianza.

### 6.2 Ausencia total de ecosistema por tarjeta

Ninguna tarjeta tiene TyC, FAQ ni instructivos dentro de su propio árbol:

| Tarjeta | TyC | FAQ | Instructivos | Tasas propias | Beneficios |
|---|---|---|---|---|---|
| `/clasica` | NO (en /tyc/) | NO | NO | NO | NO |
| `/gold` | NO | NO | NO | NO | NO |
| `/platinum` | NO | NO | NO | NO | NO |
| `/infinite` | NO | NO | NO | NO | NO |
| `/signature` | NO | NO | NO | NO | NO |
| `/black-master` | NO | NO | NO | NO | NO |
| `/on` | NO* | NO | NO | NO | NO |
| `/premium` | NO | NO | NO | NO | NO |
| `/biomax-clasica` | NO | NO | NO | NO | NO |
| `/biomax-gold` | NO | NO | NO | NO | NO |
| `/movistar-clasica` | NO | NO | NO | NO | NO |
| `/claro` (alianzas) | NO | NO | NO | NO | NO |

*Existe `/tyc/2025-reglamento-y-beneficios-tc-on` pero vive en /tyc/, no en /on/.

### 6.3 Mezcla de tipos de página al mismo nivel

Dentro de `/personas/tarjetas-de-credito/` conviven sin distinción jerárquica:

| Tipo de página | Ejemplos |
|---|---|
| Productos (tarjetas) | `/gold`, `/platinum`, `/on`, `/clasica` |
| Funciones financieras | `/avances`, `/compra-cartera`, `/alivios` |
| Información sobre costos | `/cuota-de-manejo`, `/sin-cuota-de-manejo` |
| Ofertas de gestión | `/cerorollo`, `/instacupo`, `/pago-minimo-alterno` |
| Campaña temporal | `/black-week` |
| Beneficios (parciales) | `/asistencias` |
| Tasas generales | `/tasas-de-interes` |
| Canales de pago | `/pago-impuestos` |

8 tipos distintos de página en la misma jerarquía plana.

### 6.4 Slugs internos expuestos públicamente

| URL | Problema |
|---|---|
| `/personas/tarjetas-de-credito/clasica/vtu` | Nomenclatura de canal interno (164 palabras, thin content) |
| `/personas/tarjetas-de-credito/aliada/vtu` | Nomenclatura de canal interno (163 palabras, thin content) |

### 6.5 Modelo inconsistente para Latam Pass

```
/personas/tarjetas-de-credito/tarjetas-latam        ← Hub general
/personas/tarjetas-de-credito/clasica-latam-pass    ← Variante (slug compuesto)
/personas/tarjetas-de-credito/gold-latam-pass       ← Variante (slug compuesto)
/personas/tarjetas-de-credito/platinum-latam-pass   ← Variante (slug compuesto)
/personas/tarjetas-de-credito/signature-latam-pass  ← Variante (slug compuesto)
```

5 URLs para Latam Pass, con nombres compuestos en lugar de anidarse bajo un hub `/latam-pass/`.

### 6.6 Empresas sin ecosistema

Las 10 tarjetas empresariales no tienen:
- TyC propios en su árbol
- FAQ específica por tarjeta
- Instructivos de gestión
- Tasas desagregadas por producto

La única FAQ disponible es la genérica `/atencion-al-cliente/preguntas-frecuentes/tarjeta-credito-empresas`.

### 6.7 `crecer` y `logros` en dos modalidades sin diferenciación

```
/empresas/tarjetas-de-credito/crecer   ← TC para microempresas
/empresas/tarjetas-de-credito/logros   ← TC para microempresas
/empresas/tarjetas-debito/crecer       ← TD para microempresas (mismo nombre)
/empresas/tarjetas-debito/logros       ← TD para microempresas (mismo nombre)
```

Sin aclaración en URL ni en estructura de cuál es crédito y cuál es débito.

---

## 7. Mapa de dispersión del contenido satelital

Para un usuario que quiere resolver el ciclo completo con una tarjeta (ej. tarjeta Gold), debe visitar:

| Necesidad | URL actual | Sección |
|---|---|---|
| Conocer el producto | `/personas/tarjetas-de-credito/gold` | `/personas/` |
| Ver tasas de interés | `/personas/tarjetas-de-credito/tasas-de-interes` | `/personas/` |
| Ver cuota de manejo | `/personas/tarjetas-de-credito/cuota-de-manejo` | `/personas/` |
| Ver tarifas completas | `/tasas-y-tarifas/tarifas-personas` | `/tasas-y-tarifas/` |
| Activar la tarjeta | `/atencion-al-cliente/instructivos/activa-tus-tarjetas` | `/atencion-al-cliente/` |
| Bloquear por robo | `/atencion-al-cliente/instructivos/bloquear-tarjetas-por-perdida-robo` | `/atencion-al-cliente/` |
| Cambiar fecha pago | `/atencion-al-cliente/instructivos/cambio-fecha-pago-tarjeta-credito` | `/atencion-al-cliente/` |
| Resolver dudas | `/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito` | `/atencion-al-cliente/` |
| Leer el reglamento | `/tyc/2025-reglamento-y-beneficios-tc-on` (si es ON) | `/tyc/` |

El usuario recorre **4 secciones distintas del sitio** para completar una jornada básica con su tarjeta. No existe un punto único de gestión.

---

*Documento elaborado a partir del crawl de `www.bancodebogota.com`.*
*Ver también: [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md) — [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md)*
*Fecha: junio 2026.*
