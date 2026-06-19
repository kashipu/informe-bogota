# Tarjetas de crédito — Propuesta de arquitectura
## Banco de Bogotá — www.bancodebogota.com

> Propuesta de reorganización basada en el modelo de ecosistema de producto definido en
> [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md) y la arquitectura integral
> de [arquitectura-integral-sitemap.md](arquitectura-integral-sitemap.md).
> Cada tarjeta tiene su propio ecosistema de contenido; el contenido satelital (TyC, FAQ,
> instructivos, tasas) vive dentro del árbol del producto, no en secciones globales.

---

## 1. Principios del modelo propuesto

### 1.1 Una URL canónica por tarjeta

Cada tarjeta tiene una única URL de referencia. Las alianzas no viven en `/alianzas/` sino
dentro del árbol de tarjetas, bajo su propia subcarpeta. `/alianzas/` desaparece como sección.

### 1.2 El ecosistema vive dentro del producto

```
/personas/tarjetas-de-credito/[tarjeta]/
├── (landing)
├── /beneficios              ← lo que incluye (asistencias, seguros, millas)
├── /tasas-y-tarifas         ← tasa de interés, cuota de manejo, comisiones
├── /como-solicitarla        ← requisitos + proceso + CTA
├── /gestiona-tu-tarjeta/    ← instructivos post-venta
├── /preguntas-frecuentes    ← FAQ específicas
└── /terminos-y-condiciones  ← reglamento legal
```

Las campañas temporales son efímeras y viven ancladas al producto:
```
/personas/tarjetas-de-credito/[tarjeta]/campanas/[nombre]
```

### 1.3 Las alianzas se anidan bajo el producto base o bajo su propio hub

- Si la alianza tiene múltiples niveles (Movistar Clásica/Gold/Platinum): tiene su propio hub con subniveles.
- Si la alianza es una variante única (Claro, Tigo, Decathlon): vive como página dentro de `/alianzas/` de la categoría.

### 1.4 Separación de tipos de página

Las páginas funcionales que hoy conviven con los productos se reubican:

| Página actual | Nuevo destino | Razón |
|---|---|---|
| `/avances` | `/personas/tarjetas-de-credito/gestionar/avances/` | Es operativa, no producto |
| `/alivios` | `/personas/tarjetas-de-credito/gestionar/alivios/` | Es operativa |
| `/compra-cartera` | `/personas/tarjetas-de-credito/gestionar/compra-cartera/` | Es operativa |
| `/cerorollo` | `/personas/tarjetas-de-credito/gestionar/cerorollo/` | Es beneficio general |
| `/instacupo` | `/personas/tarjetas-de-credito/gestionar/instacupo/` | Es operativa |
| `/pago-impuestos` | `/personas/tarjetas-de-credito/gestionar/pago-impuestos/` | Es operativa |
| `/pago-minimo-alterno` | `/personas/tarjetas-de-credito/gestionar/pago-minimo-alterno/` | Es operativa |
| `/cuota-de-manejo` | Contenido dentro de `/tasas-y-tarifas` de cada tarjeta | Dato, no página |
| `/sin-cuota-de-manejo` | Filtro en el comparador del hub | UI, no página |
| `/black-week` | `/personas/tarjetas-de-credito/campanas/black-week/` | Campaña temporal |

---

## 2. Estructura propuesta — `/personas/tarjetas-de-credito/`

```
/personas/tarjetas-de-credito/                    ← Hub comparador
│  Contenido: comparador de tarjetas con filtros (sin cuota, con millas, alianzas),
│  accesos directos a las más solicitadas, banner de campañas activas.
│
├── /tarjetas-propias/                            ← Agrupación editorial (no jerarquía técnica)
│   ├── /clasica/
│   ├── /economia/
│   ├── /masivo/
│   ├── /gold/
│   ├── /platinum/
│   ├── /premium/
│   ├── /infinite/
│   ├── /signature/
│   ├── /black/
│   └── /on/
│
├── /alianzas/                                    ← Hub de alianzas cobranded
│   ├── /movistar/
│   ├── /biomax/
│   ├── /latam-pass/
│   ├── /claro/
│   ├── /tigo/
│   ├── /decathlon/
│   └── /mercado-libre/
│
├── /convenios/                                   ← Hub de convenios institucionales
│   └── /anderson/
│
├── /gestionar/                                   ← Operativa general (válida para todas)
│   ├── /avances
│   ├── /compra-cartera
│   ├── /alivios
│   ├── /cerorollo
│   ├── /instacupo
│   ├── /pago-impuestos
│   └── /pago-minimo-alterno
│
└── /campanas/                                    ← Campañas temporales del portafolio
    └── /black-week
```

---

## 3. Ecosistema por tarjeta — Tarjetas propias

### 3.1 Tarjeta Clásica

```
/personas/tarjetas-de-credito/clasica/
├── (landing)                      Propuesta de valor, para quién es, CTA solicitar
├── /beneficios                    Qué incluye (asistencias básicas si aplica)
├── /tasas-y-tarifas               Tasa de interés, cuota de manejo, comisiones
├── /como-solicitarla              Requisitos, documentos, proceso, CTA
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta         → (de: /atencion-al-cliente/instructivos/activa-tus-tarjetas)
│   ├── /bloquear-por-perdida      → (de: /atencion-al-cliente/instructivos/bloquear-tarjetas...)
│   ├── /cambiar-fecha-de-pago     → (de: /atencion-al-cliente/instructivos/cambio-fecha-pago...)
│   └── /congelar-tarjeta          → (de: /atencion-al-cliente/instructivos/congelar-tarjeta...)
├── /preguntas-frecuentes          FAQ específica de la Clásica
└── /terminos-y-condiciones        Reglamento legal

Redirects:
  /personas/tarjetas-de-credito/clasica/vtu  → 301 → /personas/tarjetas-de-credito/clasica/
```

### 3.2 Tarjeta Economía

```
/personas/tarjetas-de-credito/economia/
├── (landing)
├── /beneficios
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   └── /cambiar-fecha-de-pago
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.3 Tarjeta Masivo

```
/personas/tarjetas-de-credito/masivo/
├── (landing)
├── /beneficios
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   └── /cambiar-fecha-de-pago
├── /campanas/
│   └── /vive-tu-mundial-fifa     → (de: /tyc/2026/vive-tu-mundial-fifa-masivo)
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.4 Tarjeta Gold

```
/personas/tarjetas-de-credito/gold/
├── (landing)                      Propuesta de valor, acceso a beneficios diferenciados
├── /beneficios/
│   ├── (hub de beneficios)
│   ├── /salas-vip-mastercard      → (de: /asistencias/salas-vip-tc-black-mastercard — generalizar)
│   └── /asistencias-en-viaje
├── /tasas-y-tarifas               Tasa, cuota de manejo Gold
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   ├── /diferido-automatico       → (de: /atencion-al-cliente/instructivos/diferido-automatico...)
│   └── /refinanciar-deuda         → (de: /atencion-al-cliente/instructivos/refinanciar-deuda-tc)
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.5 Tarjeta Platinum

```
/personas/tarjetas-de-credito/platinum/
├── (landing)
├── /beneficios/
│   └── /salas-vip-mastercard
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   ├── /diferido-automatico
│   └── /refinanciar-deuda
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.6 Tarjeta Premium (Mastercard / Visa)

La tarjeta Premium es el único caso con bifurcación por red de pago. La propuesta es conservar
la distinción pero hacerla explícita y simétrica.

```
/personas/tarjetas-de-credito/premium/
├── (landing)                      Comparar Premium Mastercard vs Premium Visa
│
├── /mastercard/                   → (de: /personas/tarjetas-de-credito/premium/master)
│   ├── (landing Mastercard)
│   ├── /beneficios/
│   │   └── /salas-vip-mastercard
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   ├── /bloquear-por-perdida
│   │   ├── /cambiar-fecha-de-pago
│   │   └── /diferido-automatico
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
└── /visa/                         → (de: /personas/tarjetas-de-credito/premium/visa)
    ├── (landing Visa)
    ├── /beneficios/
    │   └── /visa-airport-companion → (de: /asistencias/visa-airport-companion)
    ├── /tasas-y-tarifas
    ├── /como-solicitarla
    ├── /gestiona-tu-tarjeta/
    │   ├── /activa-tu-tarjeta
    │   ├── /bloquear-por-perdida
    │   ├── /cambiar-fecha-de-pago
    │   └── /diferido-automatico
    ├── /preguntas-frecuentes
    └── /terminos-y-condiciones

Redirects:
  /personas/tarjetas-de-credito/premium/master → 301 → /personas/tarjetas-de-credito/premium/mastercard/
  /personas/tarjetas-de-credito/premium/visa   → permanece con redirección al nuevo ecosistema
```

### 3.7 Tarjeta Infinite (Visa)

```
/personas/tarjetas-de-credito/infinite/
├── (landing)                      Tarjeta Visa tope de gama
├── /beneficios/
│   ├── /visa-airport-companion    → (de: /asistencias/visa-airport-companion)
│   ├── /concierge
│   └── /asistencias-globales
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   ├── /diferido-automatico
│   └── /refinanciar-deuda
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.8 Tarjeta Signature (Visa)

```
/personas/tarjetas-de-credito/signature/
├── (landing)
├── /beneficios/
│   ├── /visa-airport-companion
│   └── /concierge
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   └── /diferido-automatico
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

### 3.9 Tarjeta Black (Mastercard)

```
/personas/tarjetas-de-credito/black/             ← URL simplificada (hoy: /black-master)
├── (landing)
├── /beneficios/
│   ├── /salas-vip-mastercard      → (de: /asistencias/salas-vip-tc-black-mastercard)
│   └── /concierge
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   └── /diferido-automatico
├── /preguntas-frecuentes
└── /terminos-y-condiciones

Redirect:
  /personas/tarjetas-de-credito/black-master → 301 → /personas/tarjetas-de-credito/black/
```

### 3.10 Tarjeta ON

```
/personas/tarjetas-de-credito/on/
├── (landing)                      Tarjeta 100% digital, sin sucursal
├── /beneficios                    Cashback, sin cuota de manejo (si aplica)
├── /tasas-y-tarifas
├── /como-solicitarla              Énfasis en proceso digital
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   ├── /bloquear-por-perdida
│   ├── /cambiar-fecha-de-pago
│   └── /diferido-automatico
├── /campanas/
│   └── /on-al-natural             → (de: /tyc/2026/tarjeta-credito-on-al-natural)
├── /preguntas-frecuentes
└── /terminos-y-condiciones        → (de: /tyc/2025-reglamento-y-beneficios-tc-on)
```

### 3.11 Tarjeta Amparada

```
/personas/tarjetas-de-credito/amparada/
├── (landing)                      Tarjeta con seguro de desempleo incorporado
├── /beneficios                    Cobertura del seguro, condiciones
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   └── /bloquear-por-perdida
├── /preguntas-frecuentes
└── /terminos-y-condiciones
```

---

## 4. Ecosistema por tarjeta — Alianzas cobranded

### 4.1 Alianza Movistar

Hub único para toda la familia Movistar. Las 5 URLs actuales se consolidan en una jerarquía limpia.

```
/personas/tarjetas-de-credito/alianzas/movistar/     ← Hub alianza Movistar
├── (landing hub)                  Comparar los tres niveles de la tarjeta Movistar
│
├── /clasica/                      → (de: /personas/tarjetas-de-credito/movistar-clasica)
│   ├── (landing Movistar Clásica)
│   ├── /beneficios                Acumulación de megas, descuentos Movistar
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   ├── /bloquear-por-perdida
│   │   └── /cambiar-fecha-de-pago
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /gold/                         → (de: /personas/tarjetas-de-credito/movistar-gold)
│   ├── (landing Movistar Gold)
│   ├── /beneficios
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   ├── /bloquear-por-perdida
│   │   └── /cambiar-fecha-de-pago
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
└── /platinum/                     → (de: /personas/tarjetas-de-credito/movistar-platinum)
    ├── (landing Movistar Platinum)
    ├── /beneficios
    ├── /tasas-y-tarifas
    ├── /como-solicitarla
    ├── /gestiona-tu-tarjeta/
    │   ├── /activa-tu-tarjeta
    │   ├── /bloquear-por-perdida
    │   └── /cambiar-fecha-de-pago
    ├── /preguntas-frecuentes
    └── /terminos-y-condiciones

Redirects:
  /personas/tarjetas-de-credito/movistar            → 301 → /personas/tarjetas-de-credito/alianzas/movistar/
  /personas/tarjetas-de-credito/movistar-clasica    → 301 → /personas/tarjetas-de-credito/alianzas/movistar/clasica/
  /personas/tarjetas-de-credito/movistar-gold       → 301 → /personas/tarjetas-de-credito/alianzas/movistar/gold/
  /personas/tarjetas-de-credito/movistar-platinum   → 301 → /personas/tarjetas-de-credito/alianzas/movistar/platinum/
  /alianzas/tarjeta-de-credito/movistar-alianza     → 301 → /personas/tarjetas-de-credito/alianzas/movistar/
```

### 4.2 Alianza Biomax

```
/personas/tarjetas-de-credito/alianzas/biomax/       ← Hub alianza Biomax
├── (landing hub)                  Comparar Biomax Clásica y Biomax Gold
│
├── /clasica/                      → (de: /personas/tarjetas-de-credito/biomax-clasica)
│   ├── (landing Biomax Clásica)
│   ├── /beneficios                Descuentos en gasolina, acumulación de puntos Biomax
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   └── /bloquear-por-perdida
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
└── /gold/                         → (de: /personas/tarjetas-de-credito/biomax-gold)
    ├── (landing Biomax Gold)
    ├── /beneficios
    ├── /tasas-y-tarifas
    ├── /como-solicitarla
    ├── /gestiona-tu-tarjeta/
    │   ├── /activa-tu-tarjeta
    │   └── /bloquear-por-perdida
    ├── /preguntas-frecuentes
    └── /terminos-y-condiciones

Redirects:
  /personas/tarjetas-de-credito/biomax-clasica → 301 → /personas/tarjetas-de-credito/alianzas/biomax/clasica/
  /personas/tarjetas-de-credito/biomax-gold    → 301 → /personas/tarjetas-de-credito/alianzas/biomax/gold/
```

### 4.3 Alianza Latam Pass

La familia más grande. 5 URLs actuales → estructura jerárquica coherente.

```
/personas/tarjetas-de-credito/alianzas/latam-pass/   ← Hub Latam Pass (hoy: /tarjetas-latam)
├── (landing hub)                  Comparar los 4 niveles, explicación del programa de millas
│
├── /clasica/                      → (de: /personas/tarjetas-de-credito/clasica-latam-pass)
│   ├── (landing Latam Pass Clásica)
│   ├── /beneficios                Acumulación de millas, beneficios básicos
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   └── /bloquear-por-perdida
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /gold/                         → (de: /personas/tarjetas-de-credito/gold-latam-pass)
│   ├── (landing Latam Pass Gold)
│   ├── /beneficios                Acumulación acelerada de millas
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   ├── /bloquear-por-perdida
│   │   └── /cambiar-fecha-de-pago
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /platinum/                     → (de: /personas/tarjetas-de-credito/platinum-latam-pass)
│   ├── (landing Latam Pass Platinum)
│   ├── /beneficios                Salas VIP, millas de bienvenida, concierge
│   ├── /tasas-y-tarifas
│   ├── /como-solicitarla
│   ├── /gestiona-tu-tarjeta/
│   │   ├── /activa-tu-tarjeta
│   │   ├── /bloquear-por-perdida
│   │   └── /cambiar-fecha-de-pago
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
└── /signature/                    → (de: /personas/tarjetas-de-credito/signature-latam-pass)
    ├── (landing Latam Pass Signature)
    ├── /beneficios                Visa Airport Companion, millas ilimitadas
    ├── /tasas-y-tarifas
    ├── /como-solicitarla
    ├── /gestiona-tu-tarjeta/
    │   ├── /activa-tu-tarjeta
    │   ├── /bloquear-por-perdida
    │   ├── /cambiar-fecha-de-pago
    │   └── /diferido-automatico
    ├── /preguntas-frecuentes
    └── /terminos-y-condiciones

Redirects:
  /personas/tarjetas-de-credito/tarjetas-latam         → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/
  /personas/tarjetas-de-credito/clasica-latam-pass     → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/clasica/
  /personas/tarjetas-de-credito/gold-latam-pass        → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/gold/
  /personas/tarjetas-de-credito/platinum-latam-pass    → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/platinum/
  /personas/tarjetas-de-credito/signature-latam-pass   → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/signature/
```

### 4.4 Alianza Claro

```
/personas/tarjetas-de-credito/alianzas/claro/        → (de: /alianzas/tarjeta-de-credito/claro)
├── (landing Tarjeta Claro)
├── /beneficios                    Datos gratis, descuentos Claro
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   └── /bloquear-por-perdida
├── /preguntas-frecuentes
└── /terminos-y-condiciones        → (de: /tyc/2025-alianza-0-interes-claro)

Redirect:
  /alianzas/tarjeta-de-credito/claro → 301 → /personas/tarjetas-de-credito/alianzas/claro/
```

### 4.5 Alianza Tigo

```
/personas/tarjetas-de-credito/alianzas/tigo/         → (de: /alianzas/tarjeta-de-credito/tigo)
├── (landing Tarjeta Tigo)
├── /beneficios                    Datos, descuentos Tigo
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   └── /bloquear-por-perdida
├── /preguntas-frecuentes
└── /terminos-y-condiciones        → (de: /tyc/2025-tigo-0-porciento-interes)

Redirect:
  /alianzas/tarjeta-de-credito/tigo → 301 → /personas/tarjetas-de-credito/alianzas/tigo/
```

### 4.6 Alianza Decathlon

```
/personas/tarjetas-de-credito/alianzas/decathlon/    → (de: /alianzas/tarjeta-de-credito/decathlon)
├── (landing Tarjeta Decathlon)
├── /beneficios                    Descuentos en tiendas Decathlon, cuotas sin interés
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   └── /activa-tu-tarjeta
├── /preguntas-frecuentes
└── /terminos-y-condiciones

Redirect:
  /alianzas/tarjeta-de-credito/decathlon → 301 → /personas/tarjetas-de-credito/alianzas/decathlon/
```

### 4.7 Alianza Mercado Libre

```
/personas/tarjetas-de-credito/alianzas/mercado-libre/ → (de: /alianzas/tarjeta-de-credito/mercado-libre)
├── (landing Tarjeta Mercado Libre)
├── /beneficios                    Cuotas sin interés en ML, cashback
├── /tasas-y-tarifas
├── /como-solicitarla
├── /gestiona-tu-tarjeta/
│   └── /activa-tu-tarjeta
├── /preguntas-frecuentes
└── /terminos-y-condiciones

Redirect:
  /alianzas/tarjeta-de-credito/mercado-libre → 301 → /personas/tarjetas-de-credito/alianzas/mercado-libre/
```

---

## 5. Ecosistema — Convenios institucionales

### 5.1 Convenio Anderson

```
/personas/tarjetas-de-credito/convenios/anderson/    → (de: /personas/tarjetas-de-credito/tc-anderson)
├── (landing Tarjeta Anderson)     Para empleados/miembros del convenio Anderson
├── /beneficios
├── /tasas-y-tarifas
├── /como-solicitarla              Requisitos específicos del convenio
├── /gestiona-tu-tarjeta/
│   ├── /activa-tu-tarjeta
│   └── /bloquear-por-perdida
├── /preguntas-frecuentes
└── /terminos-y-condiciones

Redirect:
  /personas/tarjetas-de-credito/tc-anderson → 301 → /personas/tarjetas-de-credito/convenios/anderson/
```

---

## 6. Estructura propuesta — `/empresas/tarjetas/`

Las tarjetas empresariales se reorganizan bajo una nueva ruta `/empresas/tarjetas/` que unifica
crédito y débito bajo un mismo hub, con separación clara entre modalidades.

```
/empresas/tarjetas/                                  ← Hub empresarial (hoy: dos rutas separadas)
├── /credito/                                        ← (de: /empresas/tarjetas-de-credito/)
│   ├── /negocios/
│   │   ├── (landing)              TC básica para pymes
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /gestiona-tu-tarjeta/
│   │   │   ├── /activa-tu-tarjeta
│   │   │   └── /bloquear-por-perdida
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /negocios-elite/
│   │   ├── (landing)              TC premium para pymes
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /gestiona-tu-tarjeta/
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /corporativa/
│   │   ├── (landing)              TC para grandes empresas
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /gestiona-tu-tarjeta/
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /compras-institucionales/
│   │   ├── (landing)              TC para entidades del Estado
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /destinos/
│   │   ├── (landing)              TC con beneficios de viaje para empresas
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /latam-business/
│   │   ├── (landing)              Alianza Latam para empresas
│   │   ├── /beneficios            Millas corporativas
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   │
│   ├── /visa-distribucion/        → (de: /tarjeta-visa-distribucion)
│   │   ├── (landing)              TC para redes de distribución
│   │   ├── /beneficios
│   │   ├── /tasas-y-tarifas
│   │   └── /terminos-y-condiciones
│   │
│   └── /microempresas/            ← Hub para portafolio microempresas
│       ├── /crecer/               → (de: /empresas/tarjetas-de-credito/crecer)
│       │   ├── (landing TC Crecer)  Distinguir claramente: esta es CRÉDITO
│       │   ├── /beneficios
│       │   ├── /tasas-y-tarifas
│       │   ├── /como-solicitarla
│       │   ├── /preguntas-frecuentes
│       │   └── /terminos-y-condiciones
│       └── /logros/               → (de: /empresas/tarjetas-de-credito/logros)
│           ├── (landing TC Logros)   Distinguir claramente: esta es CRÉDITO
│           ├── /beneficios
│           ├── /tasas-y-tarifas
│           ├── /como-solicitarla
│           ├── /preguntas-frecuentes
│           └── /terminos-y-condiciones
│
└── /debito/                                         ← (de: /empresas/tarjetas-debito/)
    ├── /negocios/
    ├── /afinidad/
    ├── /cedula-cafetera/
    ├── /microempresas/
    │   ├── /crecer/               → (de: /empresas/tarjetas-debito/crecer) — DÉBITO
    │   └── /logros/               → (de: /empresas/tarjetas-debito/logros) — DÉBITO
    └── (cada una con ecosistema mínimo)
```

**Redirects de empresas:**
```
/empresas/tarjetas-de-credito/            → 301 → /empresas/tarjetas/credito/
/empresas/tarjetas-de-credito/negocios   → 301 → /empresas/tarjetas/credito/negocios/
/empresas/tarjetas-de-credito/crecer     → 301 → /empresas/tarjetas/credito/microempresas/crecer/
/empresas/tarjetas-de-credito/logros     → 301 → /empresas/tarjetas/credito/microempresas/logros/
/empresas/tarjetas-debito/               → 301 → /empresas/tarjetas/debito/
/empresas/tarjetas-debito/crecer         → 301 → /empresas/tarjetas/debito/microempresas/crecer/
/empresas/tarjetas-debito/logros         → 301 → /empresas/tarjetas/debito/microempresas/logros/
```

---

## 7. Gestión centralizada del TyC

### 7.1 Clasificación de los ~48 TyC actuales

Los TyC de tarjetas se redistribuyen en tres categorías:

**Categoría A — TyC de producto base** (1 por tarjeta, en `/terminos-y-condiciones`):
```
/tyc/2025-reglamento-y-beneficios-tc-on
  → 301 → /personas/tarjetas-de-credito/on/terminos-y-condiciones/
```

**Categoría B — TyC de campaña** (viven dentro de la campaña del producto):
```
/tyc/2026/tarjeta-credito-on-al-natural
  → 301 → /personas/tarjetas-de-credito/on/campanas/on-al-natural/terminos-y-condiciones/

/tyc/2026/vive-tu-mundial-fifa-masivo
  → 301 → /personas/tarjetas-de-credito/masivo/campanas/mundial-fifa/terminos-y-condiciones/

/tyc/2025-campana-tc-amor-y-amistad
  → 301 → /personas/tarjetas-de-credito/campanas/amor-y-amistad/terminos-y-condiciones/

/tyc/2025-halloween-tarjeta-de-credito
  → 301 → /personas/tarjetas-de-credito/campanas/halloween/terminos-y-condiciones/
```

**Categoría C — TyC de operativa general** (van a la sección de gestión):
```
/tyc/2025-tasas-especiales-avances
  → 301 → /personas/tarjetas-de-credito/gestionar/avances/terminos-y-condiciones/

/tyc/2025-tus-avances-premian-3.0
  → 301 → /personas/tarjetas-de-credito/gestionar/avances/campanas/avances-premian/

/tyc/2025-upgrade-tarjeta-de-credito
  → 301 → /personas/tarjetas-de-credito/gestionar/upgrade/terminos-y-condiciones/
```

**Categoría D — TyC de alianza** (dentro del ecosistema de la alianza):
```
/tyc/2025-alianza-0-interes-claro
  → 301 → /personas/tarjetas-de-credito/alianzas/claro/terminos-y-condiciones/

/tyc/2025-tigo-0-porciento-interes
  → 301 → /personas/tarjetas-de-credito/alianzas/tigo/terminos-y-condiciones/

/tyc/2025-usala-y-gana-latam-pass
  → 301 → /personas/tarjetas-de-credito/alianzas/latam-pass/campanas/usala-y-gana/terminos-y-condiciones/
```

---

## 8. FAQ por producto — Páginas nuevas a crear

No se trata de redirects sino de contenido nuevo. Prioridad estimada por volumen de búsqueda:

| Nueva URL | Basada en contenido de | Prioridad |
|---|---|---|
| `/personas/tarjetas-de-credito/gold/preguntas-frecuentes` | `/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito` (extraer) | Alta |
| `/personas/tarjetas-de-credito/on/preguntas-frecuentes` | Ídem + contenido propio ON | Alta |
| `/personas/tarjetas-de-credito/clasica/preguntas-frecuentes` | Ídem | Alta |
| `/personas/tarjetas-de-credito/alianzas/movistar/preguntas-frecuentes` | Ídem + preguntas de alianza | Media |
| `/personas/tarjetas-de-credito/alianzas/latam-pass/preguntas-frecuentes` | Ídem + preguntas de millas | Media |
| `/empresas/tarjetas/credito/negocios/preguntas-frecuentes` | `/atencion-al-cliente/preguntas-frecuentes/tarjeta-credito-empresas` (extraer) | Media |
| `/personas/tarjetas-de-credito/platinum/preguntas-frecuentes` | Ídem | Baja |

La FAQ global existente:
```
/atencion-al-cliente/preguntas-frecuentes/tarjetas-credito
  → Pasa a ser un buscador unificado de FAQ de tarjetas con links a cada producto
```

---

## 9. Tabla maestra de redirects

### 9.1 Personas — tarjetas propias

| URL actual | URL propuesta | Tipo |
|---|---|---|
| `/personas/tarjetas-de-credito/black-master` | `/personas/tarjetas-de-credito/black/` | 301 — cambio de slug |
| `/personas/tarjetas-de-credito/clasica/vtu` | `/personas/tarjetas-de-credito/clasica/` | 301 — slug interno eliminado |
| `/personas/tarjetas-de-credito/aliada/vtu` | `/personas/tarjetas-de-credito/aliada/` | 301 — slug interno eliminado |
| `/personas/tarjetas-de-credito/premium/master` | `/personas/tarjetas-de-credito/premium/mastercard/` | 301 — renombrar |
| `/personas/tarjetas-de-credito/asistencias` | Contenido fusionado en `/beneficios` por tarjeta | 301 |
| `/personas/tarjetas-de-credito/asistencias/salas-vip-tc-black-mastercard` | `/personas/tarjetas-de-credito/black/beneficios/salas-vip/` | 301 |
| `/personas/tarjetas-de-credito/asistencias/visa-airport-companion` | `/personas/tarjetas-de-credito/infinite/beneficios/visa-airport-companion/` | 301 |
| `/personas/tarjetas-de-credito/black-week` | `/personas/tarjetas-de-credito/campanas/black-week/` | 301 |

### 9.2 Personas — alianzas

| URL actual | URL propuesta | Tipo |
|---|---|---|
| `/personas/tarjetas-de-credito/biomax-clasica` | `/personas/tarjetas-de-credito/alianzas/biomax/clasica/` | 301 |
| `/personas/tarjetas-de-credito/biomax-gold` | `/personas/tarjetas-de-credito/alianzas/biomax/gold/` | 301 |
| `/personas/tarjetas-de-credito/movistar` | `/personas/tarjetas-de-credito/alianzas/movistar/` | 301 |
| `/personas/tarjetas-de-credito/movistar-clasica` | `/personas/tarjetas-de-credito/alianzas/movistar/clasica/` | 301 |
| `/personas/tarjetas-de-credito/movistar-gold` | `/personas/tarjetas-de-credito/alianzas/movistar/gold/` | 301 |
| `/personas/tarjetas-de-credito/movistar-platinum` | `/personas/tarjetas-de-credito/alianzas/movistar/platinum/` | 301 |
| `/personas/tarjetas-de-credito/tarjetas-latam` | `/personas/tarjetas-de-credito/alianzas/latam-pass/` | 301 |
| `/personas/tarjetas-de-credito/clasica-latam-pass` | `/personas/tarjetas-de-credito/alianzas/latam-pass/clasica/` | 301 |
| `/personas/tarjetas-de-credito/gold-latam-pass` | `/personas/tarjetas-de-credito/alianzas/latam-pass/gold/` | 301 |
| `/personas/tarjetas-de-credito/platinum-latam-pass` | `/personas/tarjetas-de-credito/alianzas/latam-pass/platinum/` | 301 |
| `/personas/tarjetas-de-credito/signature-latam-pass` | `/personas/tarjetas-de-credito/alianzas/latam-pass/signature/` | 301 |
| `/personas/tarjetas-de-credito/tc-anderson` | `/personas/tarjetas-de-credito/convenios/anderson/` | 301 |

### 9.3 Sección `/alianzas/` → eliminada

| URL actual | URL propuesta | Tipo |
|---|---|---|
| `/alianzas/tarjeta-de-credito/claro` | `/personas/tarjetas-de-credito/alianzas/claro/` | 301 |
| `/alianzas/tarjeta-de-credito/tigo` | `/personas/tarjetas-de-credito/alianzas/tigo/` | 301 |
| `/alianzas/tarjeta-de-credito/decathlon` | `/personas/tarjetas-de-credito/alianzas/decathlon/` | 301 |
| `/alianzas/tarjeta-de-credito/mercado-libre` | `/personas/tarjetas-de-credito/alianzas/mercado-libre/` | 301 |
| `/alianzas/tarjeta-de-credito/movistar-alianza` | `/personas/tarjetas-de-credito/alianzas/movistar/` | 301 |
| `/alianzas/tarjeta-de-credito/comprar-apple-sin-intereses` | `/personas/tarjetas-de-credito/gestionar/compra-sin-intereses/` o eliminar | Evaluar |
| `/alianzas/crediconvenio` | `/personas/creditos/crediservice/` (evaluar si es el mismo producto) | Evaluar |

### 9.4 Páginas funcionales → reubicadas en gestión

| URL actual | URL propuesta | Tipo |
|---|---|---|
| `/personas/tarjetas-de-credito/avances` | `/personas/tarjetas-de-credito/gestionar/avances/` | 301 |
| `/personas/tarjetas-de-credito/alivios` | `/personas/tarjetas-de-credito/gestionar/alivios/` | 301 |
| `/personas/tarjetas-de-credito/compra-cartera` | `/personas/tarjetas-de-credito/gestionar/compra-cartera/` | 301 |
| `/personas/tarjetas-de-credito/cerorollo` | `/personas/tarjetas-de-credito/gestionar/cerorollo/` | 301 |
| `/personas/tarjetas-de-credito/instacupo` | `/personas/tarjetas-de-credito/gestionar/instacupo/` | 301 |
| `/personas/tarjetas-de-credito/pago-impuestos` | `/personas/tarjetas-de-credito/gestionar/pago-impuestos/` | 301 |
| `/personas/tarjetas-de-credito/pago-minimo-alterno` | `/personas/tarjetas-de-credito/gestionar/pago-minimo-alterno/` | 301 |
| `/personas/tarjetas-de-credito/cuota-de-manejo` | Contenido integrado en `/tasas-y-tarifas` de cada tarjeta | 301 |
| `/personas/tarjetas-de-credito/sin-cuota-de-manejo` | Filtro en el comparador del hub | 301 |

### 9.5 Instructivos → integrados en cada tarjeta

| URL actual | Nuevo destino | Tipo |
|---|---|---|
| `/atencion-al-cliente/instructivos/activa-tus-tarjetas` | Permanece global + enlace desde cada tarjeta | Mantener + referencia cruzada |
| `/atencion-al-cliente/instructivos/bloquear-tarjetas-por-perdida-robo` | Ídem | Ídem |
| `/atencion-al-cliente/instructivos/cambio-fecha-pago-tarjeta-credito` | Ídem | Ídem |
| `/atencion-al-cliente/instructivos/congelar-tarjeta-facil-seguro` | Ídem | Ídem |
| `/atencion-al-cliente/instructivos/diferido-automatico-tarjeta-credito` | Ídem | Ídem |
| `/atencion-al-cliente/instructivos/refinanciar-deuda-tc` | Ídem | Ídem |

*Los instructivos globales permanecen en `/atencion-al-cliente/` para búsquedas genéricas,
y además se referencian dentro de cada tarjeta bajo `/gestiona-tu-tarjeta/`.*

---

## 10. Proyección del nuevo inventario

| Categoría | URLs actuales | URLs en propuesta | Cambio |
|---|---|---|---|
| Tarjetas propias personas | 15 productos | 15 productos × ~6 satélites = ~90 URLs | +75 |
| Alianzas personas | 12 URLs dispersas | 7 familias × ~6 satélites = ~42 URLs | +30 |
| Convenios personas | 1 URL | 1 × ~5 satélites = 5 URLs | +4 |
| Sección /alianzas/ | 7 URLs | 0 (redistribuidas) | -7 |
| Páginas funcionales mezcladas | 10 URLs en raíz TC | 10 URLs bajo /gestionar/ | 0 neto |
| TyC globales TC | ~48 URLs en /tyc/ | 0 globales → distribuidas en productos | -48 globales |
| FAQ globales TC | 2 URLs | 0 globales → FAQ por producto (nuevas) | +15 nuevas |
| Instructivos TC globales | 7 URLs | Se mantienen + referencias cruzadas | 0 neto |
| Tarjetas empresas | 10 TC + 6 TD = 16 | 9 TC + 5 TD = 14 × ~5 satélites = ~70 | +54 |
| **Total URLs de TC** | **~125** | **~220 indexables de alta calidad** | **+95** |

El aumento de URLs no es burocrático: cada URL nueva es una página específica
(FAQ de la Gold, tasas de la Platinum, TyC de Claro) que compite en búsquedas
específicas que hoy el sitio pierde por no tener esa página.

---

## 11. KPIs de éxito para el rediseño de tarjetas

| Métrica | Estado actual | Objetivo |
|---|---|---|
| Tarjetas con TyC en su árbol | 0 de 15 | 15 de 15 |
| Tarjetas con FAQ propia | 0 de 15 | 15 de 15 |
| Tarjetas con instructivos contextualizados | 0 de 15 | 15 de 15 |
| Tarjetas con tasas desagregadas | 0 de 15 | 15 de 15 |
| URLs de alianzas duplicadas | 5 (Movistar) | 0 |
| Secciones con modelo de alianzas | 2 (`/personas/` y `/alianzas/`) | 1 (`/personas/tarjetas-de-credito/alianzas/`) |
| Slugs VTU indexados | 2 | 0 |
| Páginas funcionales mezcladas con productos | 10 | 0 |
| Pasos para completar jornada completa con una tarjeta | 4 secciones distintas | 1 sección |

---

*Documento elaborado para el rediseño de arquitectura de información de `www.bancodebogota.com`.*
*Ver también: [tarjetas-credito-estado-actual.md](tarjetas-credito-estado-actual.md) — estado previo a esta propuesta.*
*Fecha: junio 2026.*
