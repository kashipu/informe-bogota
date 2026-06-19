# Arquitectura integral y sitemap propuesto
## Banco de Bogotá — www.bancodebogota.com

> Documento 360 que integra los cuatro análisis previos en un modelo unificado.
> Cubre productos, no-productos, canales, servicios, contenido internacional,
> patrones de contenido especiales y todos los casos no considerados en análisis parciales.
> Orientado a generar un sitemap mejor estructurado y una mejora incremental en SEO.
>
> Fuentes:
> - [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md)
> - [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md)
> - [paginas-no-producto-estructura.md](paginas-no-producto-estructura.md)
> - [contenido-no-considerado.md](contenido-no-considerado.md)

---

## 1. El modelo: seis pilares y cómo se relacionan

El sitio completo se organiza en **seis secciones raíz** con roles distintos y complementarios.
Cada sección tiene una responsabilidad específica; el contenido que hoy está disperso
se puede asignar inequívocamente a una de ellas.

```
www.bancodebogota.com/
│
├── /personas/              OFERTA COMERCIAL — personas naturales
├── /empresas/              OFERTA COMERCIAL — personas jurídicas
├── /ayuda/                 SOPORTE — canales, operativa, seguridad, derechos
├── /sobre-el-banco/        INSTITUCIONAL — quiénes somos, ESG, informes
├── /educacion-financiera/  EDITORIAL — contenido de valor sin propósito transaccional
└── /tasas-y-tarifas/       REFERENCIA — precios consolidados y archivos históricos
```

### 1.1 Cómo se relacionan las seis secciones

```
                    ┌─────────────────────────────────────┐
                    │       TRÁFICO ORGÁNICO (SEO)         │
                    └──────────────┬──────────────────────┘
                                   │
          ┌────────────────────────▼──────────────────────────┐
          │              /educacion-financiera/                 │
          │    Captura tráfico informacional (¿qué es...?      │
          │    ¿cómo funciona...? ¿cuánto cuesta...?)          │
          │    → enlaza hacia el producto relevante             │
          └─────────────────────────┬─────────────────────────┘
                                    │ CTA → conoce más
          ┌─────────────────────────▼─────────────────────────┐
          │         /personas/  ·  /empresas/                  │
          │    Centro del ecosistema de producto.               │
          │    Cada producto tiene su propio árbol:             │
          │    landing → variantes → beneficios                │
          │    → tasas → TyC → FAQ → instructivos              │
          └──────┬──────────────────┬────────────────┬─────────┘
                 │                  │                │
    ┌────────────▼────┐   ┌─────────▼────────┐  ┌──▼────────────┐
    │  /tasas-y-      │   │     /ayuda/       │  │ /sobre-el-    │
    │  tarifas/       │   │  Post-venta:      │  │  banco/       │
    │  Referencia     │   │  canales, cómo    │  │  Confianza:   │
    │  de precios     │   │  operar, soporte  │  │  ESG, informes│
    │  consolidada    │   │  y seguridad      │  │  institución  │
    └─────────────────┘   └──────────────────┘  └───────────────┘
```

**Flujo del usuario a través del modelo:**

| Intención | Entrada | Destino | Función |
|---|---|---|---|
| Informacional ("¿cómo funciona un CDT?") | Búsqueda orgánica | `/educacion-financiera/` | Captura tráfico de descubrimiento |
| Consideración ("CDT banco bogotá tasas") | Búsqueda orgánica | `/personas/cdt/` | Convierte con información del producto |
| Transaccional ("abrir CDT online") | Búsqueda de marca | `/personas/cdt/como-abrirlo/` | CTA directa |
| Post-venta ("cómo consultar mi CDT") | Búsqueda de soporte | `/ayuda/como-operar/consultas/` | Retención y satisfacción |
| Institucional ("informe sostenibilidad banco bogotá") | Búsqueda corporativa | `/sobre-el-banco/sostenibilidad/` | Credibilidad y marca |

---

## 2. El ecosistema de producto: modelo universal

Cada producto (tarjeta, crédito, seguro, cuenta, CDT, leasing) es el centro de su propio ecosistema de contenido.
Las páginas satélite orbitan alrededor del producto y le dan profundidad temática.

```
                        ┌─────────────────┐
                        │  LANDING DEL    │   ← Página canónica del producto
                        │   PRODUCTO      │      Propuesta de valor, CTA solicitar
                        └────────┬────────┘
                                 │
        ┌──────────┬─────────────┼───────────────┬──────────────┐
        │          │             │               │              │
   ┌────▼───┐ ┌────▼────┐ ┌─────▼─────┐ ┌──────▼─────┐ ┌──────▼──────┐
   │VARIANTES│ │BENEFICIOS│ │  TASAS Y  │ │   CÓMO    │ │  ALIANZAS   │
   │         │ │          │ │  TARIFAS  │ │ SOLICITARLO│ │ COBRANDED   │
   │/gold    │ │/salas-vip│ │/tasas     │ │/solicitar │ │/latam-pass  │
   │/platinum│ │/asistenc.│ │           │ │           │ │/movistar    │
   └─────────┘ └──────────┘ └───────────┘ └────────────┘ └─────────────┘
        │
   ┌────▼──────────────┬─────────────────┬──────────────┐
   │                   │                 │              │
┌──▼──────────┐ ┌──────▼──────┐ ┌───────▼────┐ ┌──────▼─────┐
│  GESTIÓN    │ │    FAQ      │ │ SIMULADOR  │ │    TyC     │
│ POST-VENTA  │ │             │ │            │ │            │
│/activa      │ │/preguntas-  │ │/simulador  │ │/terminos-y-│
│/bloquea     │ │ frecuentes  │ │            │ │condiciones │
│/cambia-fecha│ └─────────────┘ └────────────┘ └────────────┘
└─────────────┘
        │
   ┌────▼──────────────┐
   │    CAMPAÑAS       │
   │   (efímeras)      │
   │/campanas/black-wk │
   │/campanas/fifa-2026│
   └───────────────────┘
```

### 2.1 Qué tipos de página aplican a qué productos

| Tipo de página | TC | Crédito | Ahorro | CDT | Seguro | Leasing | Empresas |
|---|---|---|---|---|---|---|---|
| Landing producto | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variante | ✓ (muchas) | ✓ | ✓ | ✓ | ✓ (familias) | ✓ | ✓ |
| Beneficios | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Tasas y tarifas | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| Cómo solicitarlo | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Gestión post-venta | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Alianza cobranded | ✓ | ✓ | — | — | — | — | — |
| FAQ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Simulador | — | ✓ | — | ✓ | — | ✓ | — |
| TyC | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Campaña temporal | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |

**Estado actual:** Ningún producto tiene más de 3 de estos 11 tipos integrados en su árbol.

---

## 3. Sitemap propuesto completo

### 3.1 `/personas/` — Hub de audiencia personal

```
/personas/
│
├── [segmentos: joven | preferente | premium | pensionados | básico]
│
├── /tarjetas-de-credito/               ← Comparador de tarjetas
│   ├── /clasica/                        · Tarjetas propias
│   │   └── /terminos-y-condiciones
│   ├── /gold/
│   │   ├── /beneficios/
│   │   │   ├── /salas-vip-mastercard
│   │   │   └── /visa-airport-companion
│   │   ├── /tasas-y-tarifas
│   │   ├── /como-solicitarla
│   │   ├── /gestiona-tu-tarjeta/
│   │   │   ├── /activa-tu-tarjeta
│   │   │   ├── /bloquear-por-perdida
│   │   │   └── /cambiar-fecha-de-pago
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   ├── /platinum/        (mismo ecosistema)
│   ├── /infinite/
│   ├── /signature/
│   ├── /black/
│   ├── /economia/
│   ├── /on/
│   ├── /masivo/
│   ├── /biomax-clasica/  · Tarjetas alianza
│   ├── /biomax-gold/
│   ├── /movistar/
│   │   ├── /movistar-clasica
│   │   ├── /movistar-gold
│   │   └── /movistar-platinum
│   ├── /claro/
│   ├── /tigo/
│   ├── /latam-pass/
│   │   ├── /clasica-latam
│   │   ├── /gold-latam
│   │   ├── /platinum-latam
│   │   └── /signature-latam
│   ├── /amparada/
│   ├── /convenios/
│   │   └── /anderson          · Tarjetas convenio institucional
│   ├── /tasas-y-tarifas       ← Tabla comparativa de todas las TC
│   └── /como-funciona         ← Educación dentro del producto
│
├── /creditos/                          ← Comparador de créditos
│   ├── /vivienda/
│   │   ├── /vivienda-nueva
│   │   ├── /vivienda-sostenible
│   │   ├── /remodelacion
│   │   ├── /colombianos-en-el-exterior
│   │   ├── /compra-de-cartera
│   │   ├── /reduce-tu-cuota
│   │   ├── /beneficios-gobierno/
│   │   │   ├── /frech-no-vis
│   │   │   └── /vivienda-interes-prioritario
│   │   ├── /simulador
│   │   ├── /tasas-de-interes
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   ├── /libre-inversion/
│   │   ├── /simulador
│   │   ├── /tasas-de-interes
│   │   ├── /convenios/
│   │   │   ├── /anderson
│   │   │   └── /hamilton
│   │   ├── /preguntas-frecuentes
│   │   └── /terminos-y-condiciones
│   ├── /vehiculo/
│   │   ├── /moto
│   │   ├── /motos-alto-cilindraje
│   │   ├── /simulador
│   │   └── /terminos-y-condiciones
│   ├── /libranza/
│   ├── /consumo/
│   ├── /crediestudiantil/       (colfuturo incluido)
│   ├── /crediservice/
│   ├── /ceropay/
│   ├── /cupoagil/
│   ├── /adelanto-de-nomina/
│   ├── /bajo-monto/
│   ├── /compra-de-cartera/
│   ├── /aportes-voluntarios/
│   ├── /tipos-de-credito        ← educación/comparador
│   ├── /tasas-de-interes        ← tabla general
│   └── /gestiona-tu-credito/
│       ├── /opciones-ponerte-al-dia
│       └── /refinanciar-deuda
│
├── /cuenta-de-ahorros/
│   ├── /nomina/
│   ├── /econocuenta/
│   ├── /cuenta-facil/
│   ├── /flexiahorro/
│   ├── /rentahorro/
│   ├── /cuenta-mi-trabajo/
│   ├── /joven/
│   ├── /premium/
│   ├── /prestige/
│   ├── /pensionados/
│   ├── /programado/
│   ├── /afc/
│   ├── /agremiada/
│   ├── /alcancias/
│   ├── /aventura/
│   ├── /libreahorro/
│   ├── /dale/
│   ├── /mi-grupo-es-aval/
│   ├── /remesas-internacionales/
│   ├── /convenios/
│   │   └── /hamilton
│   ├── /tarjetas-debito/        ← tarjetas asociadas a la cuenta
│   │   ├── /clasica
│   │   ├── /preferente
│   │   ├── /premium
│   │   ├── /amazonia
│   │   ├── /amparada
│   │   └── /unicef
│   ├── /requisitos
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /cuenta-corriente/
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /cdt/
│   ├── /tradicional/
│   ├── /especial/
│   ├── /simulador
│   ├── /tasas-de-interes
│   ├── /preguntas-frecuentes
│   └── /terminos-y-condiciones
│
├── /seguros/
│   ├── /vida-y-salud/           ← Familia: protección personal
│   │   ├── /vida-ahorrador
│   │   ├── /vida-alto-valor
│   │   ├── /proteccion-vida
│   │   ├── /enfermedad-grave
│   │   ├── /cancer
│   │   ├── /cancer-femenino
│   │   ├── /proteccion-integral-cancer
│   │   ├── /proteccion-integral-familia
│   │   ├── /retiro-mas-seguro
│   │   └── /seguro-proteccion-salud
│   ├── /proteccion-creditos/    ← Familia: seguros de deuda
│   │   ├── /cuota-protegida/
│   │   │   ├── /asalariados
│   │   │   ├── /independientes
│   │   │   ├── /vivienda
│   │   │   └── /libranza
│   │   ├── /cuenta-protegida/
│   │   │   └── /integral
│   │   └── /polizas-asociadas-a-creditos
│   ├── /patrimonio-y-hogar/     ← Familia: bienes
│   │   ├── /hogar-seguro
│   │   ├── /auto-protegido-plus
│   │   ├── /movilidad-segura
│   │   └── /proteccion-personal
│   ├── /asistencias/            ← Familia: servicios adicionales
│   │   ├── /multiasistencias
│   │   ├── /bolso-protegido
│   │   ├── /proteccion-mascotas
│   │   └── /tarjeta-protegida
│   └── /siniestros
│
├── /leasing/
│   ├── /habitacional/
│   ├── /habitacional-no-familiar/
│   ├── /inmobiliario/
│   ├── /vehiculos/
│   ├── /maquinaria-equipo-software/
│   ├── /recarga-leasing/
│   ├── /simulador
│   └── /terminos-y-condiciones
│
├── /medios-de-pago/
│   ├── /bre-b/
│   │   └── /llaves
│   ├── /transfiya/
│   ├── /tag-aval/
│   ├── /avances/
│   └── /remesas/
│
├── /programa-de-beneficios/
│   ├── /tuplus/
│   ├── /mejores-puntos/
│   ├── /buscador-de-puntos       ← (hoy: /BuscadordePuntosAval)
│   └── /experiencias-aval/
│
└── /ofertas/                     ← Campañas y promociones activas
    ├── /preaprobado-tarjeta
    ├── /instacupo
    └── /campanas/
        ├── /fifa-2026/           ← (hoy: sección raíz)
        └── /dia-de-la-mujer/
```

---

### 3.2 `/empresas/` — Hub de audiencia empresarial

```
/empresas/
│
├── [segmentos: pyme | microempresas | corporativa | institucional | social | banca-internacional]
│
├── /creditos/
│   ├── /capital-de-trabajo/
│   │   ├── /cartera-ordinaria
│   │   ├── /tesoreria-y-liquidez
│   │   └── /cupo-rotativo-pagos
│   ├── /credito-rotativo/
│   │   ├── /crediservice-comercial
│   │   ├── /credito-activo
│   │   └── /pago-cesantias
│   ├── /contingencias/
│   │   ├── /aval-bancario
│   │   ├── /garantia-bancaria
│   │   └── /aceptaciones-bancarias
│   ├── /credito-constructor/
│   │   └── /sostenible
│   ├── /lineas-de-facturas/
│   │   ├── /factoring-con-recurso
│   │   ├── /factoring-sin-recurso
│   │   ├── /confirming            ← URL canónica única
│   │   ├── /pago-proveedores
│   │   └── /financiacion-distribuidores
│   ├── /fomento/
│   │   ├── /bancoldex
│   │   ├── /finagro
│   │   └── /findeter
│   └── /creditos-sostenibles/
│       └── /desarrollo-sostenible
│
├── /recaudos-y-pagos/
│   ├── /recaudo-electronicos/
│   ├── /recaudo-oficinas/
│   ├── /pagos/
│   └── /suite-integral-tesoreria/
│
├── /inversion-y-liquidez/
│   ├── /cdt/
│   │   ├── /tradicional
│   │   └── /especial
│   ├── /cuenta-corriente/
│   │   ├── /grandes-empresas
│   │   └── /pequenas-empresas
│   ├── /cuenta-superdia/
│   ├── /fiducias/               ← URL canónica única (fusiona /soluciones-fiduciarias)
│   │   ├── /administracion/
│   │   ├── /inmobiliaria/
│   │   └── /inversion/
│   └── /remesas-negociadas/
│
├── /comercio-internacional/     ← URL canónica única
│   ├── /cartas-de-credito/
│   │   ├── /importacion
│   │   └── /exportacion
│   ├── /cobranzas/
│   │   ├── /importacion
│   │   └── /exportacion
│   ├── /giros/
│   │   ├── /directos
│   │   └── /financiados
│   ├── /prefinanciacion-exportaciones/
│   ├── /reintegros/
│   ├── /confirming/             ← referencia cruzada a /creditos/lineas-de-facturas/confirming
│   ├── /avales-y-garantias/
│   ├── /divisas/                ← URL canónica única (fusiona negocio/negocios de divisas)
│   │   └── /compra-de-dolares
│   ├── /operaciones-de-cobertura/
│   │   ├── /forward
│   │   ├── /swap-tasas
│   │   ├── /swap-tipo-cambio
│   │   └── /opciones
│   ├── /servicios-digitales/
│   └── /presencia-internacional/ ← (hoy dispersas en 2 secciones)
│       ├── /miami
│       ├── /new-york
│       ├── /panama              ← URL canónica única (fusiona /panama y /sucursal-panama)
│       └── /nassau
│
├── /tarjetas/
│   ├── /credito/
│   │   ├── /negocios
│   │   ├── /negocios-elite
│   │   ├── /corporativa
│   │   ├── /compras-institucionales
│   │   ├── /destinos
│   │   ├── /latam-business
│   │   ├── /crecer              ← aclarar relación con /debito/crecer
│   │   └── /logros
│   └── /debito/
│       ├── /negocios
│       ├── /afinidad
│       ├── /cedula-cafetera
│       ├── /crecer
│       └── /logros
│
├── /leasing/
│   ├── /vehiculos
│   ├── /maquinaria-equipo
│   ├── /inmobiliario
│   ├── /importacion
│   ├── /leaseback
│   └── /recarga-leasing
│
├── /soluciones-de-cobro/        ← (hoy: /preguntas-frecuentes/medios-de-pago)
│   ├── /datafono-digital
│   ├── /datafono-fisico
│   ├── /codigo-qr
│   ├── /link-de-pagos
│   ├── /webcheckout
│   ├── /micrositio-abierto
│   ├── /micrositio-cerrado
│   └── /pasarela-gou
│
├── /soluciones-de-logistica/
│   ├── /almacenamiento
│   ├── /transporte-nacional
│   ├── /comercio-exterior
│   └── /transporte-internacional
│
├── /soluciones-de-informacion/
│   ├── /centro-servicios-corporativos
│   └── /portal-empresarial
│
├── /portal-negocios/            ← (hoy: /empresas/portales — 36 instructivos)
│   ├── (landing del portal)
│   ├── /como-acceder
│   └── /instructivos/
│       ├── /primer-ingreso
│       ├── /configuracion-usuarios
│       ├── /transferencias
│       └── ... (34 instructivos restantes)
│
├── /seguros/                    ← (hoy: /empresas/seguros-pyme suelto)
│   └── /seguros-pyme
│
├── /bre-b/                      ← (hoy: /empresas/bre-b suelto)
│
├── /pyme/                       ← Portafolio específico pyme
│   ├── /cuenta-integral
│   ├── /planes-integrales
│   ├── /cuenta-en-dolares       ← (hoy: /empresas/cuenta-en-dolares-pyme)
│   ├── /seguros                 ← (hoy: /empresas/seguros-pyme)
│   ├── /enko/                   ← (hoy: /empresas/enko)
│   └── /aliados/                ← (hoy: /banca-empresas/pyme/alianzas)
│
└── /educacion-financiera/       ← Educación para empresas (no hay en personas)
    └── /territorios             ← (hoy: /empresas/educacion-financiera-territorios)
```

---

### 3.3 `/ayuda/` — Soporte unificado

```
/ayuda/
├── /contacto/
│   ├── /servilineas
│   ├── /pqrs
│   └── /defensor-del-consumidor
├── /canales/
│   ├── /oficinas/               ← directorio con filtros, no 12 páginas
│   │   └── /corresponsales-bancarios
│   ├── /cajeros-y-multifuncionales
│   ├── /banca-movil
│   ├── /banca-virtual
│   ├── /avalpay-center/
│   │   └── /empresas
│   └── /disponibilidad
├── /como-operar/
│   ├── /transferencias
│   ├── /pagos
│   ├── /consultas-y-extractos
│   ├── /bloqueos
│   └── /wallets/                ← (hoy: apple-pay, google-pay, click-to-pay)
│       ├── /apple-pay
│       ├── /google-pay
│       └── /click-to-pay
├── /instructivos/               ← genéricos (los específicos viven en el producto)
├── /seguridad/
│   ├── /phishing-y-estafas
│   ├── /cajeros
│   ├── /celular
│   ├── /oficinas
│   ├── /cheques
│   └── /portales-empresariales
├── /impuestos/
│   ├── /calendario
│   └── /canales-de-pago
└── /tus-derechos/
    ├── /proteccion-datos-personales
    ├── /habeas-data
    ├── /uso-de-cookies
    ├── /relacion-con-el-cliente
    └── /superintendencia-financiera
```

---

### 3.4 `/sobre-el-banco/` — Hub institucional

```
/sobre-el-banco/
├── /quienes-somos
│   ├── /nuestra-historia
│   └── /grupo-aval
├── /sostenibilidad/
│   ├── /estrategia-asg
│   ├── /ambiental
│   ├── /social
│   ├── /gobierno-corporativo
│   └── /biblioteca              ← (fusiona /Biblioteca y /biblioteca)
├── /fundacion/
│   ├── /quienes-somos
│   ├── /educacion-y-bienestar/
│   │   └── /historias/
│   │       ├── /alejandro-torres
│   │       ├── /astrid-sarria
│   │       ├── /cristian-ropero
│   │       └── /paola-monroy
│   ├── /emprendimiento-social-y-climatico
│   └── /proteccion-ambiental
├── /diversidad-e-inclusion/
│   ├── /discapacidad-auditiva
│   ├── /discapacidad-cognitiva
│   ├── /discapacidad-fisica
│   └── /discapacidad-visual
├── /informes/
│   ├── /informe-gestion-2025    ← vigente
│   ├── /transparencia           ← desagregada en sub-temas
│   └── /archivo/                ← versiones anteriores
│       └── /informe-gestion-2024
├── /presencia-internacional/    ← (hoy disperso en empresas)
│   ├── /miami
│   ├── /new-york
│   ├── /panama
│   └── /nassau
└── /en/                         ← versión inglés, estructura espejo
    ├── /sustainability/
    │   ├── /esg-strategy
    │   ├── /environmental
    │   ├── /social
    │   ├── /governance
    │   └── /library
    └── /informes/
        └── /management-report-2025
```

---

### 3.5 `/educacion-financiera/` — Hub editorial

```
/educacion-financiera/
├── /finanzas-personales/
│   ├── /como-hacer-un-presupuesto
│   ├── /capacidad-de-endeudamiento
│   ├── /como-aumentar-el-patrimonio
│   └── /cuanto-vale-estudiar
├── /credito/
│   ├── /tipos-de-credito
│   ├── /antes-de-pedir-un-credito
│   ├── /tipos-de-tasas-de-interes
│   └── /vida-crediticia
├── /tarjetas/
│   ├── /como-funcionan
│   ├── /compras-internacionales
│   └── /seguridad-en-tarjetas
├── /inversion/
│   ├── /tipos-de-inversion
│   ├── /titulos-valores
│   └── /riesgos-financieros
├── /seguros/
│   └── /que-es-un-seguro
└── /economia/
    ├── /como-funciona-la-economia
    ├── /historia-del-dinero
    └── /deberes-y-derechos-consumidor
```

---

### 3.6 `/tasas-y-tarifas/` — Referencia consolidada

```
/tasas-y-tarifas/
├── (tabla comparativa filtrable: por audiencia, por producto)
├── /personas/                   ← tabla vigente por producto
├── /empresas/
├── /pyme/
├── /internacional/
└── /archivo/                    ← histórico, sin indexación prioritaria
    ├── /2025
    ├── /2024
    └── ... /2014
```

---

## 4. Relaciones entre secciones: matriz de vínculos

| Origen | Vínculo | Destino | Tipo de relación |
|---|---|---|---|
| `/educacion-financiera/credito/` | CTA "Solicita tu crédito" | `/personas/creditos/libre-inversion/` | Descubrimiento → producto |
| `/personas/tarjetas-de-credito/gold/` | "Ver tasas y tarifas" | `/personas/tarjetas-de-credito/gold/tasas-y-tarifas` | Producto → precios |
| `/personas/tarjetas-de-credito/gold/` | "Términos y condiciones" | `/personas/tarjetas-de-credito/gold/terminos-y-condiciones` | Producto → legal |
| `/personas/creditos/vivienda/` | "Simula tu cuota" | `/personas/creditos/vivienda/simulador` | Producto → herramienta |
| `/personas/seguros/vida-y-salud/` | "¿Cómo presentar un siniestro?" | `/ayuda/instructivos/` o `/personas/seguros/siniestros/` | Producto → soporte |
| `/tasas-y-tarifas/` | "Ver tasas tarjeta Gold" | `/personas/tarjetas-de-credito/gold/tasas-y-tarifas` | Referencia global → producto |
| `/ayuda/seguridad/phishing/` | "Activa tus alertas" | `/personas/cuenta-de-ahorros/gestiona/alertas/` | Soporte → producto |
| `/sobre-el-banco/sostenibilidad/` | "Crédito constructor sostenible" | `/empresas/creditos/credito-constructor/sostenible/` | Institucional → producto |
| `/personas/tarjetas-de-credito/movistar/` | hreflang | — | Producto monolingüe |
| `/sobre-el-banco/en/sustainability/` | hreflang | `/sobre-el-banco/sostenibilidad/` | EN ↔ ES |

---

## 5. Estrategia de mejora incremental en SEO

La mejora no puede ser un proyecto de todo-o-nada. Se propone en cuatro fases ordenadas por impacto inmediato vs. esfuerzo.

### Fase 1 — Correcciones sin cambio de URL (semanas 1–4)
*Sin redirects, sin riesgo de pérdida de ranking.*

| Acción | Impacto SEO | Esfuerzo |
|---|---|---|
| Corregir meta titles y meta descriptions en el 92% de páginas con `seo_issues` | Alto | Medio |
| Eliminar `/pagina-404` y `/personas-test` del sitemap.xml | Medio | Bajo |
| Añadir `hreflang` entre `/sostenibilidad/` ↔ `/sustainability/` y pares EN/ES | Medio | Bajo |
| Añadir canonical tags en páginas duplicadas (antes de hacer redirects) | Medio | Bajo |
| Mejorar el contenido thin: VTU (159w→400w+), tasas históricas (79w→descripción real) | Medio | Medio |
| Añadir `noindex` a páginas de archivo (`/tasas-y-tarifas/tasas-20xx`) | Bajo | Bajo |
| Desindexar `/empresas/login` (24 palabras, es funcional, no editorial) | Bajo | Bajo |
| Renombrar slugs con nomenclatura interna en `/personas/promociones/` | Bajo | Medio |

---

### Fase 2 — Consolidación de duplicados (meses 1–2)
*Redirects 301 de bajo riesgo: contenido duplicado o menor que no tiene ranking relevante.*

| Redirect | De | A |
|---|---|---|
| Duplicado nominal | `/empresas/recaudo-y-pagos` | `/empresas/recaudos-y-pagos/` |
| Duplicado singular/plural | `/empresas/comercio-int.../negocio-de-divisas` | `/empresas/comercio-int.../negocios-de-divisas/` |
| Duplicado parcial | `/empresas/soluciones-fiduciarias/*` | `/empresas/inversion-y-liquidez/fiducias/` |
| Sucursales dispersas | `/empresas/soluciones-de-comercio-.../nassau` | `/empresas/comercio-internacional/presencia-internacional/nassau/` |
| Panamá duplicada | `/empresas/.../sucursal-panama` | `/empresas/.../panama/` |
| Informes dispersos | `/informe-de-gestion`, `/informe-gestion-2024-3` | `/sobre-el-banco/informes/` |
| Fragmentos institucionales | `/nuestra-organizacion/*`, `/transparencia` | `/sobre-el-banco/` |
| Sostenibilidad EN | `/sustainability/*` | `/sobre-el-banco/en/sustainability/` |
| Herramientas mal ubicadas | `/BuscadordePuntosAval` | `/personas/programa-de-beneficios/buscador/` |
| Archivo histórico | `/tasas-y-tarifas/tasas-20xx` (13 URLs) | `/tasas-y-tarifas/archivo/` |
| Campaña temporal | `/fifa-2026/*` | `/personas/ofertas/campanas/fifa-2026/` |

---

### Fase 3 — Integración de TyC y FAQ en ecosistemas de producto (meses 2–4)
*El mayor impacto SEO del plan. Crea páginas nuevas con keywords específicos de producto.*

**Distribuir los 168 TyC actuales de `/tyc/` hacia sus productos:**

```
/tyc/2025-reglamento-y-beneficios-tc-on
  → 301 → /personas/tarjetas-de-credito/on/terminos-y-condiciones/

/tyc/2025-campana-tc-amor-y-amistad
  → 301 → /personas/tarjetas-de-credito/campanas/[nombre]/terminos-y-condiciones/

/tyc/2025-banca-movil-whatsapp-bre-b
  → 301 → /personas/bre-b/terminos-y-condiciones/
```

**Crear FAQ por producto** (páginas nuevas, no redirects):

Productos prioritarios por volumen de búsqueda estimado:
1. `/personas/tarjetas-de-credito/[variante]/preguntas-frecuentes` — 35 páginas nuevas
2. `/personas/seguros/[seguro]/preguntas-frecuentes` — 34 páginas nuevas
3. `/personas/cuenta-de-ahorros/[variante]/preguntas-frecuentes` — 27 páginas nuevas
4. `/personas/creditos/[producto]/preguntas-frecuentes` — 20 páginas nuevas

Las 30 páginas existentes de `/atencion-al-cliente/preguntas-frecuentes/[producto]` se migran
con 301 a `/personas/[categoria]/[producto]/preguntas-frecuentes/`.

**Crear simuladores por producto** (herramientas nuevas):
- `/personas/creditos/vivienda/simulador`
- `/personas/creditos/libre-inversion/simulador`
- `/personas/creditos/vehiculo/simulador`
- `/personas/cdt/simulador`
- `/personas/leasing/simulador`

Los dos existentes en `/educacion-financiera/simulador-*` se redirigen a los nuevos.

---

### Fase 4 — Reorganización estructural (meses 4–8)
*Los cambios de mayor impacto pero mayor esfuerzo. Requieren coordinación CMS y posible pérdida temporal de ranking.*

| Cambio | Páginas | Riesgo |
|---|---|---|
| Fusionar `/banca-personas/*` en `/personas/segmentos/` | 15 | Bajo (poco ranking) |
| Fusionar `/banca-empresas/*` en `/empresas/[segmento]/` | 21 | Bajo |
| Crear hub `/sobre-el-banco/` y mover institucional | ~25 | Bajo |
| Crear hub `/ayuda/` desde `/atencion-al-cliente/` | 138 | **Alto** — sección grande con ranking |
| Reorganizar `/personas/seguros/` en 4 familias | 43 | Medio |
| Mover instructivos de portal a `/empresas/portal-negocios/instructivos/` | 36 | Bajo |
| Mover medios de cobro de FAQ a `/empresas/soluciones-de-cobro/` | 12 | Bajo |

**Nota sobre `/atencion-al-cliente/`:** Es la sección con más páginas (138) después de productos. Tiene ranking acumulado en términos de soporte. El cambio a `/ayuda/` debe hacerse con redirects 301 correctos y monitoreo de posiciones en las semanas siguientes.

---

## 6. Inventario completo de redirects 301

### 6.1 Secciones completas

| Origen (patrón) | Destino | Fase |
|---|---|---|
| `/banca-personas/**` | `/personas/segmentos/[segmento]/` | 4 |
| `/banca-empresas/**` | `/empresas/[segmento]/` | 4 |
| `/tyc/**` | `/[audiencia]/[categoria]/[producto]/terminos-y-condiciones/` | 3 |
| `/alianzas/tarjeta-de-credito/**` | `/personas/tarjetas-de-credito/[alianza]/` | 3 |
| `/atencion-al-cliente/**` | `/ayuda/` | 4 |
| `/nuestra-organizacion/**` | `/sobre-el-banco/` | 2 |
| `/sostenibilidad/**` | `/sobre-el-banco/sostenibilidad/` | 2 |
| `/sustainability/**` | `/sobre-el-banco/en/sustainability/` | 2 |
| `/diversidad-e-inclusion/**` | `/sobre-el-banco/diversidad-e-inclusion/` | 2 |

### 6.2 URLs individuales

| Origen | Destino | Fase |
|---|---|---|
| `/informe-de-gestion` | `/sobre-el-banco/informes/` | 2 |
| `/informe-gestion-2024-3` | `/sobre-el-banco/informes/archivo/2024/` | 2 |
| `/informe-gestion-2025` | `/sobre-el-banco/informes/2025/` | 2 |
| `/management-report-2024` | `/sobre-el-banco/en/informes/archivo/2024/` | 2 |
| `/transparencia` | `/sobre-el-banco/transparencia/` | 2 |
| `/empresas/recaudo-y-pagos` | `/empresas/recaudos-y-pagos/` | 2 |
| `/empresas/negocio-de-divisas` | `/empresas/comercio-internacional/divisas/` | 2 |
| `/empresas/soluciones-fiduciarias/**` | `/empresas/inversion-y-liquidez/fiducias/` | 2 |
| `/empresas/sucursal-panama` | `/empresas/comercio-internacional/presencia-internacional/panama/` | 2 |
| `/tasas-y-tarifas/tasas-20[0-9][0-9]` (×13) | `/tasas-y-tarifas/archivo/` | 1 |
| `/BuscadordePuntosAval` | `/personas/programa-de-beneficios/buscador/` | 2 |
| `/tag-aval` | `/personas/medios-de-pago/tag-aval/` | 2 |
| `/bre-b/**` | `/personas/medios-de-pago/bre-b/` | 2 |
| `/fifa-2026/**` | `/personas/ofertas/campanas/fifa-2026/` | 2 |
| `/dia-de-la-mujer-y-del-hombre` | `/personas/ofertas/campanas/dia-de-la-mujer/` | 2 |
| `/proyecto-unicef` | `/personas/cuenta-de-ahorros/tarjetas-debito/unicef/` | 2 |
| `/depositos-2026` | `/personas/cdt/` | 2 |
| `/aliados-pyme` | `/empresas/pyme/aliados/` | 2 |
| `/educacion-financiera/simulador-credito-vivienda` | `/personas/creditos/vivienda/simulador/` | 3 |
| `/educacion-financiera/simulador-credito-libre-inversion` | `/personas/creditos/libre-inversion/simulador/` | 3 |
| `/educacion-financiera/nuestra-organizacion/nuestra-historia` | `/sobre-el-banco/quienes-somos/` | 4 |
| `/educacion-financiera/nuestra-organizacion/defensor-del-consumidor` | `/ayuda/tus-derechos/defensor/` | 4 |
| `/personas/bienvenida/**` | `/personas/[producto]/como-empezar/` | 4 |
| `/personas/portafolios/**` | `/personas/segmentos/` | 4 |
| `/personas/opciones-ponerte-al-dia` | `/personas/creditos/gestiona-tu-credito/opciones-ponerte-al-dia/` | 3 |
| `/personas/promociones/cuota-en-pausa` | `/personas/creditos/gestiona-tu-credito/cuota-en-pausa/` | 3 |
| `/personas/depositos` | `/personas/cdt/` | 2 |
| `/personas/bienes-e-inmuebles` | `/sobre-el-banco/` o `/personas/leasing/` | 4 |
| `/empresas/login` | Portal transaccional (redirect funcional) | 1 |
| `/pagina-404` | Eliminar del sitemap | 1 |
| `/personas-test` | Eliminar de producción | 1 |

---

## 7. Proyección del nuevo sitemap

| Sección | Páginas actuales | Páginas en el nuevo modelo | Cambio |
|---|---|---|---|
| `/personas/` | 201 | ~250 | +49 (FAQ y TyC integrados) |
| `/empresas/` | 211 | ~220 | +9 (consolidación duplicados) |
| `/ayuda/` | 138 (en `/atencion-al-cliente`) | ~100 | -38 (FAQ migran al producto) |
| `/sobre-el-banco/` | ~25 (fragmentado) | ~40 | +15 (consolidación) |
| `/educacion-financiera/` | 31 | ~25 | -6 (migración a productos e institucional) |
| `/tasas-y-tarifas/` | 18 | ~8 | -10 (archivo sin indexación) |
| `/tyc/` | 168 | 0 | -168 (redistribuidas en productos) |
| Páginas raíz sueltas | 16 | 0 | -16 (clasificadas o eliminadas) |
| **Total** | **~887 nodos** | **~643 nodos indexables** | **-244 páginas de baja calidad** |

La reducción de 244 páginas no significa eliminar contenido: significa consolidar duplicados,
archivar contenido histórico y distribuir TyC en sus productos correctos.
El número de páginas de alta calidad e indexables sube respecto al estado actual.

---

## 8. KPIs para medir la mejora incremental

| Métrica | Estado actual | Objetivo Fase 1–2 | Objetivo Fase 3–4 |
|---|---|---|---|
| Páginas con `seo_issues` | 92% | <50% | <20% |
| Secciones en la raíz | 31 | 20 (limpiar huérfanas) | 6 |
| Profundidad máxima | 5 niveles | 5 niveles | 4 niveles |
| Productos con TyC integrado | 0 de 13 | 0 | 13 de 13 |
| Productos con FAQ propia | 0 de 13 | 6 de 13 | 13 de 13 |
| Productos con simulador | 0 de 5 relevantes | 0 | 5 de 5 |
| Páginas duplicadas activas | 15+ pares | <5 pares | 0 |
| Pares hreflang implementados | 0 | 4 pares mínimos | Todos los pares EN/ES |
| URLs con nomenclatura interna expuesta | 30+ | <10 | 0 |

---

## 9. Contenido internacional: modelo y ubicación

El banco tiene presencia y contenido en inglés y en múltiples países. Actualmente ese contenido está disperso sin una arquitectura coherente.

### 9.1 Inventario de contenido internacional actual

| Tipo | URLs actuales | Estado |
|---|---|---|
| Sostenibilidad EN | `/sustainability/` (6 pág: environmental, social, governance, esg-strategy, library) | Sección raíz separada, sin hreflang |
| Informe de gestión EN | `/management-report-2024` | URL raíz, sin hreflang, sin par 2025 |
| FIFA en inglés | `/fifa-2026-en` | 1 página, sin relación con `/fifa-2026/` |
| Ciberseguridad EN | `/atencion-al-cliente/proteccion-al-consumidor/cybersecurity-and-security-management` | Página en inglés dentro de sección en español |
| Sucursales internacionales | Miami, New York, Panamá, Nassau (dentro de `/empresas/comercio-int`) | 4 países, en sección de producto, no institucional |
| Productos en exterior | `/empresas/comercio-int.../productos-y-servicios-en-el-exterior/` | Páginas de oferta internacional para empresas |
| Banca Internacional | `/banca-empresas/empresas/banca-internacional` (97w) | Thin content, sin ecosistema |

### 9.2 Modelo propuesto: dos capas de contenido internacional

**Capa 1 — Versiones en inglés de contenido institucional** (audiencia: inversores, reguladores, medios internacionales)

```
/sobre-el-banco/en/
├── /sustainability/
│   ├── /esg-strategy
│   ├── /environmental
│   ├── /social
│   ├── /governance
│   └── /library
├── /informes/
│   ├── /management-report-2025   ← crear; hoy solo existe 2024
│   └── /management-report-2024
└── /about-us                     ← crear si se quiere proyección internacional
```

Cada página EN debe tener su par `hreflang`:
```html
<!-- En /sobre-el-banco/sostenibilidad/ambiental/ -->
<link rel="alternate" hreflang="es-CO" href="/sobre-el-banco/sostenibilidad/ambiental/" />
<link rel="alternate" hreflang="en"    href="/sobre-el-banco/en/sustainability/environmental/" />
```

**Capa 2 — Presencia internacional del banco** (audiencia: empresas con operaciones en el exterior, colombianos en el exterior)

```
/sobre-el-banco/presencia-internacional/
├── /miami/               ← sucursal Miami (hoy en /empresas/comercio-int.../miami)
├── /new-york/            ← sucursal Nueva York
├── /panama/              ← sucursal Panamá (fusiona /panama y /sucursal-panama)
└── /nassau/              ← sucursal Nassau (hoy en /soluciones-de-comercio-int...)
```

Estas páginas no son "productos para empresas" sino hechos institucionales del banco.
Su lugar es `/sobre-el-banco/`, con referencias desde `/empresas/comercio-internacional/`.

**Capa 3 — Productos para clientes internacionales** (audiencia: clientes con necesidades cross-border)

Permanecen en `/empresas/comercio-internacional/` por ser oferta de producto:
```
/empresas/comercio-internacional/
├── /productos-para-el-exterior/  ← oferta para empresas con operaciones fuera
│   ├── /miami
│   ├── /new-york
│   └── /panama
└── ...
```

Y para personas:
```
/personas/creditos/vivienda/colombianos-en-el-exterior/  ← ya existe, bien ubicado
/personas/cuenta-de-ahorros/remesas-internacionales/     ← ya existe, bien ubicado
```

### 9.3 Colombianos en el exterior: un segmento transversal no articulado

El banco tiene contenido disperso para colombianos fuera del país pero no lo articula como segmento:

| Contenido actual | Ubicación | Propuesta |
|---|---|---|
| Crédito vivienda colombianos exterior | `/personas/creditos/vivienda/colombianos-en-el-exterior/` | ✓ bien ubicado |
| Remesas internacionales (personas) | `/personas/cuenta-de-ahorros/remesas-internacionales/` | ✓ bien ubicado |
| Remesas negociadas (empresas) | `/empresas/inversion-y-liquidez/remesas-negociadas/` | ✓ bien ubicado |
| Servicios digitales moneda extranjera | `/empresas/comercio-int.../servicios-digitales-moneda-extranjera/` | ✓ bien ubicado |
| Giros directos y financiados | `/empresas/comercio-internacional/giros/` | ✓ bien ubicado |

Estos productos ya están bien ubicados en sus secciones. El gap es que no hay una **página hub** que los agrupe para el usuario que busca "productos banco bogotá para colombianos en el exterior". Propuesta:

```
/personas/colombianos-en-el-exterior/   ← hub nuevo, enlaza a productos existentes
  → /personas/creditos/vivienda/colombianos-en-el-exterior/
  → /personas/cuenta-de-ahorros/remesas-internacionales/
  → /personas/medios-de-pago/remesas/
```

---

## 10. Patrones de contenido especiales: resolución completa

Todos los patrones identificados en [contenido-no-considerado.md](contenido-no-considerado.md) y su ubicación definitiva en el nuevo modelo.

### 10.1 Patrón VTU — Canal de venta interno

**Qué son:** Landing pages de productos específicos diseñadas para un canal de venta (call center / fuerza de ventas). Actualmente indexadas públicamente con slugs sin significado para el usuario.

| URL actual | Palabras | Diagnóstico |
|---|---|---|
| `/personas/tarjetas-de-credito/clasica/vtu` | 164w | Thin, slug interno |
| `/personas/tarjetas-de-credito/aliada/vtu` | 163w | Thin, slug interno |
| `/personas/creditos/libre-inversion/vtu` | 847w | Contenido normal |
| `/personas/creditos/crediservice/vtua` | 856w | Contenido normal, variante `vtua` |
| `/personas/cdt/tradicional/vtu` | 159w | Thin, slug interno |

**Resolución:**
- Las páginas thin (≤164w): hacer `noindex` + enriquecer contenido o fusionar con la landing del producto y redirigir
- Las páginas con contenido normal (847w+): renombrar slug a algo descriptivo

```
/personas/creditos/libre-inversion/vtu  →  /personas/creditos/libre-inversion/oferta-especial/
/personas/creditos/crediservice/vtua    →  /personas/creditos/crediservice/oferta-especial/
/personas/tarjetas-de-credito/clasica/vtu → fusionar en /clasica/ + 301
/personas/tarjetas-de-credito/aliada/vtu  → fusionar en /aliada/ + 301
/personas/cdt/tradicional/vtu            → fusionar en /cdt/tradicional/ + 301
```

### 10.2 Patrón Anderson / Hamilton — Convenios institucionales

**Qué son:** Productos diseñados para empleados o miembros de instituciones específicas (probablemente universidades o empresas con convenio). El slug usa el apellido del convenio con prefijos de producto (`li-`, `ca-`, `tc-`).

| URL actual | Producto | Propuesta |
|---|---|---|
| `/personas/creditos/libre-inversion/li-anderson-g` | Crédito libre inversión | `/personas/creditos/libre-inversion/convenio-anderson/` |
| `/personas/creditos/libre-inversion/li-hamilton` | Crédito libre inversión | `/personas/creditos/libre-inversion/convenio-hamilton/` |
| `/personas/cuenta-de-ahorros/ca-hamilton` | Cuenta de ahorros | `/personas/cuenta-de-ahorros/convenio-hamilton/` |
| `/personas/tarjetas-de-credito/tc-anderson` | Tarjeta de crédito | `/personas/tarjetas-de-credito/convenio-anderson/` |

Todos los convenios de una misma institución deberían agruparse:
```
/personas/convenios/anderson/
  → /personas/tarjetas-de-credito/convenio-anderson/
  → /personas/creditos/convenio-anderson/

/personas/convenios/hamilton/
  → /personas/cuenta-de-ahorros/convenio-hamilton/
  → /personas/creditos/convenio-hamilton/
```

### 10.3 Programa de beneficios y lealtad — Tres fragmentos, un ecosistema

| Fragmento actual | Propuesta |
|---|---|
| `/BuscadordePuntosAval` (raíz, 122w) | `/personas/programa-de-beneficios/buscador/` |
| `/personas/experiencias-aval` (suelta, 419w) | `/personas/programa-de-beneficios/experiencias/` |
| `/personas/beneficios/plan-lealtad-mejores-puntos` | `/personas/programa-de-beneficios/mejores-puntos/` |
| `/personas/beneficios/programa-lealtad-tuplus` | `/personas/programa-de-beneficios/tuplus/` |

```
/personas/programa-de-beneficios/   ← hub nuevo
  /tuplus
  /mejores-puntos
  /experiencias
  /buscador
  /como-acumular-puntos             ← nuevo (gap de contenido)
  /como-redimir                     ← nuevo (gap de contenido)
```

### 10.4 Bienvenida / Onboarding — Integración en el ecosistema de producto

`/personas/bienvenida/` tiene 3 páginas de onboarding genéricas. El modelo correcto es que cada producto tenga su propia página de bienvenida como satélite:

```
Hoy:
  /personas/bienvenida/tarjetas-credito   ← genérico para todas las tarjetas
  /personas/bienvenida/cuentas-de-ahorro
  /personas/bienvenida/credito-libre-inversion

Propuesto:
  /personas/tarjetas-de-credito/[variante]/bienvenida   ← contextual al producto exacto
  /personas/cuenta-de-ahorros/[variante]/bienvenida
  /personas/creditos/libre-inversion/bienvenida
```

Fase de transición: `/personas/bienvenida/*` → 301 → `/personas/[producto]/bienvenida/`

### 10.5 Portafolios de segmento — Tercera instancia de duplicado

`/personas/portafolios/` (masivo, preferente, premium) es la tercera instancia de segmentación, además de `/banca-personas/` y los portafolios integrales dentro de `/banca-personas/[segmento]/`.

Resolución: Una sola URL por segmento:
```
/personas/segmentos/masivo/          ← fusiona /portafolios/masivo + /banca-personas info
/personas/segmentos/preferente/      ← fusiona /portafolios/preferente + /banca-personas/preferente
/personas/segmentos/premium/         ← fusiona las 3 instancias premium

Redirects:
  /personas/portafolios/masivo     → /personas/segmentos/masivo/
  /banca-personas/portafolio-personas → /personas/segmentos/
  /banca-personas/preferente/**    → /personas/segmentos/preferente/
  /banca-personas/premium/**       → /personas/segmentos/premium/
```

### 10.6 Promociones con slugs técnicos — Limpieza y reclasificación

| Slug actual | Tipo real | Destino propuesto |
|---|---|---|
| `/personas/promociones/exte-ca` | Extensión campaña cuenta ahorros | `/personas/cuenta-de-ahorros/campanas/exte/` |
| `/personas/promociones/exte-tc` | Extensión campaña tarjeta crédito | `/personas/tarjetas-de-credito/campanas/exte/` |
| `/personas/promociones/ext-cuenta-facil` | Extensión cuenta fácil | `/personas/cuenta-de-ahorros/cuenta-facil/oferta/` |
| `/personas/promociones/productos-digitales-chf` | Productos digitales | `/personas/ofertas/productos-digitales/` |
| `/personas/promociones/cuota-en-pausa` | Alivio financiero (no campaña) | `/personas/creditos/gestiona-tu-credito/cuota-en-pausa/` |
| `/personas/promociones/oferta-instacupo` | Duplica `/tarjetas-de-credito/instacupo` | Redirigir 301 |
| `/personas/promociones/mas-de-una-vez-cashback` | Campaña cashback | `/personas/tarjetas-de-credito/campanas/cashback/` |
| `/personas/promociones/mas-de-una-vez-millas` | Campaña millas | `/personas/tarjetas-de-credito/campanas/millas/` |
| `/personas/promociones/preaprobado-tarjeta-credito` | Lead de producto preaprobado | `/personas/tarjetas-de-credito/preaprobada/` |

### 10.7 Sostenibilidad dentro de `/empresas/leasing/` — Anomalía

`/empresas/leasing/sostenibilidad` (1.058w) es la única página de sostenibilidad dentro de un ecosistema de producto. Dos posibles diagnósticos:

- Si el contenido es sobre **leasing sostenible** (financiamiento de activos verdes): renombrar a `/empresas/leasing/leasing-sostenible/` (ya existe `/personas/leasing/` sin esta página — oportunidad de paridad)
- Si es contenido institucional replicado: reemplazar por enlace a `/sobre-el-banco/sostenibilidad/` + 301

### 10.8 Fundación: perfiles de beneficiarios como tipo de página

4 perfiles de personas reales están publicados a 4 niveles de profundidad sin un modelo de contenido explícito.

```
Hoy:
  /sostenibilidad/fundacion-banco-de-bogota/educacion-y-bienestar-social/alejandro-torres

Propuesto:
  /sobre-el-banco/fundacion/historias/alejandro-torres
```

Este tipo de contenido requiere:
1. Una plantilla de tipo "historia de impacto" con schema `Person` o `Article`
2. Un índice en `/sobre-el-banco/fundacion/historias/`
3. URLs más cortas (nivel 3, no nivel 4)
4. Plan de publicación: ¿se van a agregar más historias? ¿cuál es la cadencia?

### 10.9 Páginas técnicas en el árbol de contenido — Resolución definitiva

| URL | Tipo real | Acción |
|---|---|---|
| `/empresas/login` (24w) | Redirección a portal transaccional | Implementar como redirect HTTP 302 en infraestructura, no como página CMS |
| `/empresas/requerimientos-sistema` (1.251w) | Documentación técnica del portal | `/ayuda/portal-empresarial/requerimientos/` |
| `/empresas/flujo-solicitud-de-novedades` (683w) | Proceso interno expuesto | `/ayuda/portal-empresarial/solicitar-novedades/` (con nombre descriptivo) |
| `/personas/extractos` (597w) | Funcionalidad transaccional | `/ayuda/como-operar/consultas-y-extractos/` |
| `/personas/informacion-productos-servicios/formato-apertura-productos` (47w) | Formulario descargable | Embeber en la landing del producto correspondiente |
| `/buscador` (8w) | UI del sitio | Eliminar del árbol; el buscador es una función, no una sección |

### 10.10 Duplicados en `/empresas/comercio-internacional/` — Resolución definitiva

| Duplicado | Acción |
|---|---|
| `/negocio-de-divisas` vs `/negocios-de-divisas` | Conservar `/divisas/` como nueva URL canónica; 301 desde ambos |
| `/panama` vs `/sucursal-panama` | Conservar `/panama/`; 301 desde `/sucursal-panama` |
| `confirming` en comercio-internacional y en lineas-de-facturas | Página canónica en `/lineas-de-facturas/confirming/`; referencia cruzada en comercio-internacional |
| `crecer` y `logros` en TC y débito empresas | Verificar si son el mismo producto en dos modalidades; si sí: consolidar bajo `/empresas/tarjetas/programas/crecer/`; si no: diferenciar los nombres |
| `/inversion-y-liquidez/fiducias` (17 pág) vs `/soluciones-fiduciarias` (2 pág) | Conservar como canónica `/inversion-y-liquidez/fiducias/`; 301 desde `/soluciones-fiduciarias/**` |

### 10.11 Productos de personas subdesarrollados — Priorización

Productos con una sola página y sin ecosistema mínimo, ordenados por potencial de búsqueda:

| Producto | Páginas actuales | Prioridad | Qué falta |
|---|---|---|---|
| `/personas/cuenta-corriente` | 1 (1.025w) | Alta | Variantes, tasas, FAQ |
| `/personas/depositos` | 1 (1.615w) | Alta | Fusionar con `/cdt/` o crear ecosistema propio |
| `/personas/servicio-transfiya` | 1 (942w) | Media | Mover a `/medios-de-pago/transfiya/`; agregar instructivo y FAQ |
| `/personas/bienes-e-inmuebles` | 1 (111w) | Baja | Thin content; o enriquecer o fusionar con `/leasing/inmobiliario/` |

### 10.12 Páginas sueltas en la raíz — Destino final de todas

| Página raíz | Destino |
|---|---|
| `/BuscadordePuntosAval` | `/personas/programa-de-beneficios/buscador/` |
| `/aliados-pyme` | `/empresas/pyme/aliados/` |
| `/buscador` | Eliminar (es UI) |
| `/depositos-2026` | `/personas/cdt/` + 301 |
| `/dia-de-la-mujer-y-del-hombre` | `/personas/ofertas/campanas/dia-de-la-mujer/` + 301 |
| `/exte-cuenta-ahorros` | `/personas/cuenta-de-ahorros/campanas/` + 301 |
| `/fifa-2026-en` | `/sobre-el-banco/en/` o redirigir a `/fifa-2026/` con hreflang |
| `/informe-de-gestion` | `/sobre-el-banco/informes/` + 301 |
| `/informe-gestion-2024-3` | `/sobre-el-banco/informes/archivo/2024/` + 301 |
| `/informe-gestion-2025` | `/sobre-el-banco/informes/2025/` + 301 |
| `/management-report-2024` | `/sobre-el-banco/en/informes/archivo/2024/` + 301 |
| `/pagina-404` | Eliminar del sitemap.xml |
| `/personas-test` | Eliminar de producción **inmediatamente** |
| `/proyecto-unicef` | `/personas/cuenta-de-ahorros/tarjetas-debito/unicef/` + 301 |
| `/sostenibilidad` | `/sobre-el-banco/sostenibilidad/` + 301 |
| `/sustainability` | `/sobre-el-banco/en/sustainability/` + 301 |
| `/tag-aval` | `/personas/medios-de-pago/tag-aval/` + 301 |
| `/tasas-y-tarifas` | Permanece (se reestructura internamente) |
| `/transparencia` | `/sobre-el-banco/transparencia/` + 301 |
| `/bre-b` | `/personas/medios-de-pago/bre-b/` + 301 |

---

## 11. Tabla maestra: inventario completo con destino en nueva IA

Mapa de **todas** las secciones actuales hacia su ubicación en el modelo propuesto.

| URL actual | Páginas | Destino en nuevo modelo | Fase |
|---|---|---|---|
| `/personas/tarjetas-de-credito/**` | 44 | `/personas/tarjetas-de-credito/**` | Permanece |
| `/personas/seguros/**` | 43 | `/personas/seguros/[familia]/[seguro]/` | 4 |
| `/personas/cuenta-de-ahorros/**` | 36 | `/personas/cuenta-de-ahorros/**` | Permanece |
| `/personas/creditos/**` | 33 | `/personas/creditos/**` | Permanece |
| `/personas/promociones/**` | 10 | `/personas/ofertas/**` + `/personas/[producto]/campanas/` | 3 |
| `/personas/leasing/**` | 7 | `/personas/leasing/**` | Permanece |
| `/personas/bienvenida/**` | 4 | `/personas/[producto]/bienvenida/` | 4 |
| `/personas/cdt/**` | 4 | `/personas/cdt/**` | Permanece |
| `/personas/portafolios/**` | 4 | `/personas/segmentos/**` | 4 |
| `/personas/beneficios/**` | 3 | `/personas/programa-de-beneficios/**` | 3 |
| `/personas/informacion-productos-servicios/**` | 3 | distribuir en productos | 3 |
| `/personas/cuenta-corriente` | 1 | `/personas/cuenta-corriente/**` (expandir) | 3 |
| `/personas/depositos` | 1 | `/personas/cdt/` + 301 | 2 |
| `/personas/bienes-e-inmuebles` | 1 | `/personas/leasing/inmobiliario/` o eliminar | 4 |
| `/personas/experiencias-aval` | 1 | `/personas/programa-de-beneficios/experiencias/` | 3 |
| `/personas/extractos` | 1 | `/ayuda/como-operar/consultas-y-extractos/` | 3 |
| `/personas/feria-digital` | 1 | `/personas/ofertas/campanas/feria-digital/` | 3 |
| `/personas/juega-refiere-y-gana` | 1 | `/personas/ofertas/campanas/refiere-y-gana/` | 3 |
| `/personas/opciones-ponerte-al-dia` | 1 | `/personas/creditos/gestiona-tu-credito/opciones-ponerte-al-dia/` | 3 |
| `/personas/servicio-transfiya` | 1 | `/personas/medios-de-pago/transfiya/` | 2 |
| `/empresas/**` (productos) | 211 | `/empresas/**` (reorganizado) | 2–4 |
| `/banca-personas/**` | 15 | `/personas/segmentos/**` | 4 |
| `/banca-empresas/**` | 21 | `/empresas/[segmento]/**` | 4 |
| `/atencion-al-cliente/**` | 138 | `/ayuda/**` | 4 |
| `/tyc/**` | 168 | `/[audiencia]/[cat]/[producto]/terminos-y-condiciones/` | 3 |
| `/alianzas/**` | 9 | `/personas/tarjetas-de-credito/[alianza]/` (canónica) + directorio | 3 |
| `/educacion-financiera/**` | 31 | `/educacion-financiera/**` (depurada) | 4 |
| `/tasas-y-tarifas/**` | 18 | `/tasas-y-tarifas/**` (vigentes) + `/archivo/` | 2 |
| `/sostenibilidad/**` | 17 | `/sobre-el-banco/sostenibilidad/**` | 2 |
| `/sustainability/**` | 6 | `/sobre-el-banco/en/sustainability/**` | 2 |
| `/nuestra-organizacion/**` | 4 | `/sobre-el-banco/**` | 2 |
| `/diversidad-e-inclusion/**` | 5 | `/sobre-el-banco/diversidad-e-inclusion/**` | 2 |
| `/fifa-2026/**` | 11 | `/personas/ofertas/campanas/fifa-2026/**` | 2 |
| `/bre-b/**` | 2 | `/personas/medios-de-pago/bre-b/**` | 2 |
| `/aliados-pyme` | 1 | `/empresas/pyme/aliados/` | 2 |
| `/BuscadordePuntosAval` | 1 | `/personas/programa-de-beneficios/buscador/` | 2 |
| `/depositos-2026` | 1 | `/personas/cdt/` | 2 |
| `/dia-de-la-mujer-y-del-hombre` | 1 | `/personas/ofertas/campanas/dia-de-la-mujer/` | 2 |
| `/exte-cuenta-ahorros` | 1 | `/personas/cuenta-de-ahorros/campanas/` | 2 |
| `/fifa-2026-en` | 1 | `/sobre-el-banco/en/` o hreflang en `/fifa-2026/` | 2 |
| `/informe-de-gestion` | 1 | `/sobre-el-banco/informes/` | 2 |
| `/informe-gestion-2024-3` | 1 | `/sobre-el-banco/informes/archivo/2024/` | 2 |
| `/informe-gestion-2025` | 1 | `/sobre-el-banco/informes/2025/` | 2 |
| `/management-report-2024` | 1 | `/sobre-el-banco/en/informes/archivo/2024/` | 2 |
| `/pagina-404` | 1 | Eliminar del sitemap | 1 |
| `/personas-test` | 1 | Eliminar de producción | 1 |
| `/proyecto-unicef` | 1 | `/personas/cuenta-de-ahorros/tarjetas-debito/unicef/` | 2 |
| `/tag-aval` | 1 | `/personas/medios-de-pago/tag-aval/` | 2 |
| `/transparencia` | 1 | `/sobre-el-banco/transparencia/` | 2 |
| `/buscador` | 1 | Eliminar (es UI, no contenido) | 1 |

---

## 12. KPIs para medir la mejora incremental

| Métrica | Estado actual | Objetivo Fase 1–2 | Objetivo Fase 3–4 |
|---|---|---|---|
| Páginas con `seo_issues` | 92% | <50% | <20% |
| Secciones en la raíz | 31 | 20 (limpiar huérfanas) | 6 |
| Profundidad máxima | 5 niveles | 5 niveles | 4 niveles |
| Productos con TyC integrado | 0 de 13 | 0 | 13 de 13 |
| Productos con FAQ propia | 0 de 13 | 6 de 13 | 13 de 13 |
| Productos con simulador | 0 de 5 | 0 | 5 de 5 |
| Páginas duplicadas activas | 15+ pares | <5 pares | 0 |
| Pares hreflang implementados | 0 | 4 mínimos | Todos los pares EN/ES |
| URLs con nomenclatura interna | 30+ | <10 | 0 |
| Slugs VTU indexados públicamente | 5 | 0 | 0 |
| Páginas raíz sueltas | 16 | 0 | 0 |
| Ecosistema de lealtad fragmentado | 3 fragmentos | 3→1 hub | Hub completo |
| Contenido EN sin hreflang | 100% | <20% | 0% |
| Sucursales internacionales sin hub | 4 dispersas | Hub creado | Completo |

---

*Fecha: junio 2026.*
