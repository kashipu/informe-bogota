# Canales Digitales — Propuesta de arquitectura
## Banco de Bogotá — www.bancodebogota.com

> Propuesta de reorganización que eleva los canales digitales a sección propia, separándolos
> de Atención al Cliente. El contenido de transacciones pasa a ser **Funcionalidades** dentro
> de cada canal. Los instructivos se asocian al canal o producto al que pertenecen.
> Ver contexto en [arquitectura-integral-sitemap.md](arquitectura-integral-sitemap.md).

---

## 1. Problema de la arquitectura actual

### 1.1 Los canales viven en el lugar equivocado

```
atencion-al-cliente/canales/canales-digitales/   ← banca-movil, banca-virtual, token
atencion-al-cliente/canales/canales-electronicos/ ← cajeros, multifuncional
```

Ubicarlos bajo Atención al Cliente implica que son un mecanismo de soporte, no plataformas
transaccionales. Un usuario que quiere descargar la app o registrarse en banca virtual no busca
en "atención al cliente".

### 1.2 Transacciones: sección ciega sin dueño de canal

```
atencion-al-cliente/canales/transacciones/
  apple-pay, google-pay, click-to-pay, compras, consultas,
  extractos-certificados, inscripciones, pagos, programacion-de-pagos,
  recarga-cuenta-ahorros-pse, transferencias-utilizaciones, bloqueos
```

Esta lista agrupa todas las funcionalidades de todos los canales juntas. No responde la
pregunta real del usuario: **"¿qué puedo hacer en banca móvil?"** o
**"¿puedo pagar impuestos desde cajeros?"**

### 1.3 Instructivos: cajón genérico desconectado del canal

Los 12 instructivos en `atencion-al-cliente/instructivos/` mezclan guías de canal
(cómo registrarse en banca virtual, cómo usar BRE-B) con guías de producto
(diferido automático, refinanciar deuda). El usuario que quiere aprender a usar
banca móvil no tiene razón para buscar en "atención al cliente > instructivos".

### 1.4 Servilínea: no existe como sección

No hay nodo en el árbol para Servilínea. Es un canal asistido sin presencia en la arquitectura.

### 1.5 Rutas duplicadas

```
atencion-al-cliente/canales-electronicos/canales/cajeros
atencion-al-cliente/canales/canales-electronicos/cajeros        ← mismo contenido, dos URLs
```

### 1.6 Token mal clasificado

Token aparece como "canal digital" pero es un habilitador de seguridad transversal,
no un canal de operación.

---

## 2. Principios del modelo propuesto

### 2.1 Los canales son productos: tienen sección propia a nivel raíz

Los canales digitales no dependen de Atención al Cliente. Viven al mismo nivel que
`/personas/` y `/empresas/`.

### 2.2 Transacciones = Instructivos del canal

El contenido de `/canales/transacciones/` se redistribuye como subsección
`/instructivos/` dentro de cada canal. `instructivos` es el nodo raíz de todo
el contenido operativo: cubre tanto qué se puede hacer como el paso a paso de cómo hacerlo.
La pregunta que responde es: "estoy en banca móvil, ¿qué puedo hacer y cómo?"

### 2.3 Instructivos: siguen al canal o al producto

- Si el instructivo enseña a operar **un canal** → vive dentro del canal.
- Si enseña a operar **un producto** → vive dentro del producto.
- Regla de prueba: si el instructivo desaparecería si el canal desaparece → es del canal.

### 2.4 Canales asistidos son canales, no contactos de soporte

WhatsApp (BRE-B) y Servilínea son canales transaccionales. Tienen funcionalidades
propias y viven en la misma sección que banca móvil y banca virtual.

### 2.5 Token y clave segura son habilitadores de seguridad, no canales

Se agrupan bajo un nodo de seguridad transversal, referenciado desde cada canal.

---

## 3. Arquitectura propuesta

> **Nota de modelo:** `instructivos` reemplaza a `funcionalidades` como nodo raíz de contenido
> operativo. Cada cosa que el usuario puede hacer en un canal tiene su instructivo; no hay
> separación entre "qué puedo hacer" y "cómo lo hago".

---

### PERSONAS

#### 3.1 Canales Digitales — Personas

```
/canales/personas/canales-digitales/banca-movil/
├── (landing)                          ← qué es, cómo descargar, CTA descarga
├── /instructivos/                     ← todo lo que hoy está en /transacciones/ + guías
│   ├── pagos
│   ├── transferencias-y-utilizaciones
│   ├── compras
│   ├── consultas-y-extractos
│   ├── inscripcion-cuentas-servicios
│   ├── programacion-de-pagos
│   ├── recarga-pse
│   ├── bloqueos
│   ├── apple-pay
│   ├── google-pay
│   └── click-to-pay
├── /como-activar/                     ← primer acceso, clave, token
├── /seguridad/                        ← token, clave segura, alertas
└── /preguntas-frecuentes/             ← migra desde atencion-al-cliente/preguntas-frecuentes/banca-movil

/canales/personas/canales-digitales/banca-virtual/
├── (landing)                          ← qué es, cómo acceder, CTA ingreso
├── /instructivos/
│   ├── pagos
│   ├── transferencias-y-utilizaciones
│   ├── compras
│   ├── consultas-y-extractos
│   ├── inscripcion-cuentas-servicios
│   ├── programacion-de-pagos
│   ├── recarga-pse
│   ├── bloqueos
│   └── click-to-pay
├── /como-registrarse/                 ← registro-banca-virtual-clave-segura (migra desde instructivos globales)
├── /seguridad/
└── /preguntas-frecuentes/
```

#### 3.2 Canales Físicos — Personas

```
/canales/personas/canales-fisicos/oficinas/
├── (landing)                          ← localizador de oficinas
├── /tipos-de-oficina/
│   ├── oficina-tradicional
│   ├── oficina-express
│   ├── oficina-premium
│   ├── oficina-incluyente
│   ├── oficina-joven
│   ├── oficina-insignia
│   ├── oficinas-universales
│   ├── oficina-solo-clientes
│   └── autobanco
└── /servicios-disponibles/

/canales/personas/canales-fisicos/cajeros/
├── (landing)                          ← localizador de cajeros
├── /instructivos/
│   ├── pagos
│   ├── transferencias
│   └── consultas
└── /cajero-multifuncional/

/canales/personas/canales-fisicos/corresponsales/
├── (landing)
├── /instructivos/
│   └── servicios-disponibles
├── /beneficios/
└── /como-ser-corresponsal/
```

#### 3.3 Canales Asistidos — Personas

```
/canales/personas/canales-asistidos/whatsapp-bre-b/
├── (landing)                          ← qué es BRE-B, cómo activarlo
├── /instructivos/
│   ├── bre-b-en-whatsapp              ← migra desde atencion-al-cliente/instructivos/
│   ├── uso-de-bre-b                   ← migra desde atencion-al-cliente/instructivos/
│   ├── consultas
│   ├── pagos
│   └── transferencias
└── /preguntas-frecuentes/             ← migra desde atencion-al-cliente/preguntas-frecuentes/instructivos-bre-b

/canales/personas/canales-asistidos/servilinea/
├── (landing)                          ← sección nueva, hoy no existe
├── /instructivos/
│   ├── bloqueos-y-cancelaciones
│   ├── consultas-y-saldos
│   ├── pagos
│   └── solicitudes
└── /horarios-y-contacto/

/canales/personas/canales-asistidos/asistente/
├── (landing)                          ← sección nueva
├── /instructivos/
│   ├── que-puede-hacer
│   └── como-activarlo
└── /preguntas-frecuentes/
```

---

### EMPRESAS

> Misma estructura que Personas. Los canales físicos y asistidos aplican igual.
> Los instructivos de `/empresas/portales/` (37 páginas) migran a
> Banca Virtual Empresas como instructivos organizados por tipo de operación.

#### 3.4 Canales Digitales — Empresas

```
/canales/empresas/canales-digitales/banca-movil-empresas/
├── (landing)
├── /instructivos/
│   ├── como-descargar-y-activar
│   ├── pagos
│   ├── transferencias
│   └── consultas
└── /preguntas-frecuentes/

/canales/empresas/canales-digitales/banca-virtual-empresas/
├── (landing)                          ← hoy en /empresas/portales/ sin estructura
├── /instructivos/                     ← 37 instructivos de /empresas/portales/ migran aquí
│   ├── /configuracion/                ← onboarding y administración de usuarios
│   │   ├── primer-ingreso-portal
│   │   ├── ajuste-contrasena
│   │   ├── configuracion-de-usuarios
│   │   ├── limites-de-usuario
│   │   └── configuracion-horarios-acceso
│   ├── /transferencias/
│   │   ├── transferencias-a-terceros
│   │   ├── transferencias-internas
│   │   └── transferencias-inversion-externa
│   ├── /pagos/
│   │   ├── pago-de-servicios
│   │   ├── pago-impuestos-dian
│   │   ├── pago-impuestos-distritales-locales
│   │   ├── estructura-pagos-masivos
│   │   ├── pago-a-cuentas-afc
│   │   └── consultas-y-pagos-pse
│   ├── /consultas/
│   │   ├── consulta-de-extractos
│   │   ├── solicitar-extractos-pdf
│   │   ├── consulta-de-facturacion
│   │   ├── consulta-documentos-libranza-factoring
│   │   └── consulta-listado-bancos
│   └── /otras-operaciones/
│       ├── activacion-de-cheques
│       ├── carga-archivos-dispersion-fondos
│       ├── debitos-servicios-domiciliacion
│       ├── establecer-alertas
│       ├── exportar-prenotificaciones-recaudos
│       ├── inscripcion-eliminacion-beneficiarios
│       ├── validacion-archivos-cifrados-pgp
│       └── credito-rotativo
└── /preguntas-frecuentes/             ← portales-transaccionales migra aquí
```

#### 3.5 Canales Físicos — Empresas

```
/canales/empresas/canales-fisicos/oficinas/
├── (landing)
├── /tipos-de-oficina/
└── /servicios-disponibles/

/canales/empresas/canales-fisicos/cajeros/
├── (landing)
├── /instructivos/
└── /cajero-multifuncional/

/canales/empresas/canales-fisicos/corresponsales/
├── (landing)
└── /instructivos/
```

#### 3.6 Canales Asistidos — Empresas

```
/canales/empresas/canales-asistidos/whatsapp-bre-b/
├── (landing)
├── /instructivos/
└── /preguntas-frecuentes/

/canales/empresas/canales-asistidos/servilinea/
├── (landing)
├── /instructivos/
└── /horarios-y-contacto/

/canales/empresas/canales-asistidos/asistente/
├── (landing)
└── /instructivos/
```

#### 3.7 Corporate

```
/canales/empresas/corporate/
├── (landing)
├── /avalpay-center-empresa/
│   ├── (landing)
│   ├── /instructivos/
│   └── /preguntas-frecuentes/
└── /acceso-y-soporte/
```

---

## 4. Migración de contenido existente

### 4.1 Instructivos de personas — origen → destino

| URL actual | Destino propuesto | Tipo |
|---|---|---|
| `atencion-al-cliente/instructivos/bre-b-en-whatsapp` | `/canales/personas/canales-asistidos/whatsapp-bre-b/instructivos/` | Canal |
| `atencion-al-cliente/instructivos/uso-de-bre-b` | `/canales/personas/canales-asistidos/whatsapp-bre-b/instructivos/` | Canal |
| `atencion-al-cliente/instructivos/registro-banca-virtual-clave-segura` | `/canales/personas/canales-digitales/banca-virtual/como-registrarse/` | Canal |
| `atencion-al-cliente/instructivos/crea-tu-clave-segura` | `/canales/personas/canales-digitales/[banca-movil o banca-virtual]/seguridad/` | Canal |
| `atencion-al-cliente/instructivos/activa-tus-tarjetas` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/bloquear-tarjetas-por-perdida-robo` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/congelar-tarjeta-facil-seguro` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/cambio-fecha-pago-tarjeta-credito` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/diferido-automatico-tarjeta-credito` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/refinanciar-deuda-tc` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/desbloqueo-tarjeta-debito-clave-errada` | `/personas/tarjetas/instructivos/` | Producto |
| `atencion-al-cliente/instructivos/informacion-y-servicios-de-cuenta-de-ahorros` | `/personas/cuentas/instructivos/` | Producto |

### 4.2 Transacciones — distribución por canal

| Funcionalidad actual | Banca Móvil | Banca Virtual | Cajeros | Corresponsales | WhatsApp | Servilínea |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| pagos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| transferencias-utilizaciones | ✓ | ✓ | ✓ | — | — | ✓ |
| compras | ✓ | ✓ | — | — | — | — |
| consultas | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| extractos-certificados | ✓ | ✓ | — | — | — | ✓ |
| inscripciones-cuentas-servicios | ✓ | ✓ | — | — | — | — |
| programacion-de-pagos | ✓ | ✓ | — | — | — | — |
| recarga-cuenta-ahorros-pse | ✓ | ✓ | — | — | — | — |
| bloqueos | ✓ | ✓ | — | — | — | ✓ |
| apple-pay | ✓ | — | — | — | — | — |
| google-pay | ✓ | — | — | — | — | — |
| click-to-pay | ✓ | ✓ | — | — | — | — |

### 4.3 Secciones de atención al cliente que quedan (limpiadas)

```
/atencion-al-cliente/
├── /canales-de-atencion-presencial/   ← oficinas, corresponsales (solo info de atención)
├── /disponibilidad-de-canales/        ← horarios y estatus operativo
├── /pqrs/
├── /defensor-del-consumidor/
├── /impuestos/
└── /preguntas-frecuentes/             ← solo FAQ no relacionadas a canales digitales
```

---

## 5. Cómo los productos declaran sus canales

Cada producto (tarjeta de crédito, cuenta de ahorros, etc.) incluye una sección
**"¿Dónde puedo operarlo?"** con enlaces a los canales relevantes:

```
/personas/tarjetas-de-credito/[tarjeta]/
└── /donde-operarla/              ← no subpáginas propias, solo enlaces
    → /canales/personas/canales-digitales/banca-movil/
    → /canales/personas/canales-digitales/banca-virtual/
    → /canales/personas/canales-fisicos/cajeros/
    → /canales/personas/canales-asistidos/servilinea/
```

Esto evita la duplicación de tener `/banca-movil/tarjeta-credito/`
Y `/tarjeta-credito/banca-movil/` — la trampa clásica de arquitecturas
con dos dimensiones.

---

## 6. Resumen del cambio

| Aspecto | Estado actual | Propuesta |
|---|---|---|
| Ubicación canales digitales | Dentro de `atencion-al-cliente` | Sección propia a nivel raíz |
| Nodo de contenido operativo | `/transacciones/` separado de `/instructivos/` | `/instructivos/` unifica qué se hace y cómo |
| Instructivos globales | Cajón genérico en atención al cliente | Viven dentro del canal o producto al que pertenecen |
| Servilínea | No existe en el árbol | Canal asistido con sección propia (personas y empresas) |
| BRE-B/WhatsApp | Solo instructivos sueltos | Canal asistido con instructivos estructurados |
| Asistente | No existe en el árbol | Canal asistido nuevo (personas y empresas) |
| Token | Clasificado como canal digital | Habilitador de seguridad dentro de cada canal |
| Empresas/portales (37 instructivos) | Instructivos planos sin estructura ni jerarquía | Organizados en `/banca-virtual-empresas/instructivos/` por tipo de operación |
| Corporate/AvalPay | Entrada sin profundidad en canales digitales | Sección corporate con instructivos propios |
| Canales físicos empresas | No mapeados | Espejo de la estructura de personas |
| Canales asistidos empresas | No mapeados | WhatsApp, Servilínea, Asistente (espejo personas) |
