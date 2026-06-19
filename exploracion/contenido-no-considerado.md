# Contenido y páginas no consideradas anteriormente
## Banco de Bogotá — www.bancodebogota.com

> Complemento de los tres documentos previos. Cubre páginas y patrones que quedaron
> fuera del análisis de productos, no-productos y tipos de página.
> Ver: [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md),
> [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md),
> [paginas-no-producto-estructura.md](paginas-no-producto-estructura.md).

---

## 1. Duplicados internos en `/empresas` — no mencionados antes

Los documentos anteriores identificaron duplicados entre secciones raíz (`/personas` vs `/banca-personas`).
Dentro de `/empresas` existen duplicados adicionales que el análisis previo no cubrió.

### 1.1 Comercio internacional: tres instancias del mismo contenido

| URL | Páginas | Estado |
|---|---|---|
| `/empresas/comercio-internacional-y-tesoreria` | 32 | Sección principal (15 sub en comercio int., 7 en coberturas) |
| `/empresas/soluciones-de-comercio-internacional-y-tesoreria` | 3 | Duplicado parcial con nombres distintos |
| `/empresas/comercio-internacional-y-tesoreria/negocio-de-divisas` | 1 (167w) | Versión con singular |
| `/empresas/comercio-internacional-y-tesoreria/negocios-de-divisas` | 1 (312w) | Versión con plural + subpágina hija |

La diferencia entre `negocio-de-divisas` y `negocios-de-divisas` es un error de nomenclatura: dos páginas sobre el mismo servicio, la segunda con una subpágina hija (`/compra-de-dolares-y-otras-divisas`). Uno de los dos es un duplicado no intencional.

### 1.2 Fiducias: dos secciones paralelas

| URL | Páginas | Contenido |
|---|---|---|
| `/empresas/inversion-y-liquidez/fiducias` | 17 | Fiducias de administración (7), inmobiliaria (5), inversión (4) |
| `/empresas/soluciones-fiduciarias` | 2 | Solo fiducia de administración (1 sub) |

La sección `/soluciones-fiduciarias` es un subconjunto de lo que ya existe en `/inversion-y-liquidez/fiducias`. Probablemente surgió como landing de campaña o se construyó antes de que la sección principal tuviera contenido completo.

### 1.3 Recaudos y pagos: singular vs plural

| URL | Páginas | Estado |
|---|---|---|
| `/empresas/recaudos-y-pagos` | 36 | Sección principal completa (5 subsecciones) |
| `/empresas/recaudo-y-pagos` | 1 (264w) | Página suelta, mismo tema en singular |

Nombre idéntico en singular/plural. La versión con 1 página es probablemente un remanente o un error de publicación.

### 1.4 `confirming` en dos secciones distintas

| URL | Palabras |
|---|---|
| `/empresas/comercio-internacional-y-tesoreria/comercio-internacional/confirming` | 320w |
| `/empresas/productos-de-credito/lineas-de-facturas/confirming` | 486w |

Confirming es a la vez un instrumento de comercio exterior y una línea de crédito. Hay dos páginas independientes con el mismo nombre de producto en secciones distintas, sin referencia cruzada entre ellas.

### 1.5 Sucursales internacionales: cuatro ubicaciones, tres secciones distintas

Las oficinas internacionales del banco no tienen una sección unificada:

| URL | Palabras |
|---|---|
| `/empresas/comercio-internacional-y-tesoreria/productos-y-servicios-en-el-exterior/miami` | 1.230w |
| `/empresas/comercio-internacional-y-tesoreria/productos-y-servicios-en-el-exterior/new-york` | 1.159w |
| `/empresas/comercio-internacional-y-tesoreria/productos-y-servicios-en-el-exterior/panama` | 935w |
| `/empresas/comercio-internacional-y-tesoreria/productos-y-servicios-en-el-exterior/sucursal-panama` | 1.017w |
| `/empresas/soluciones-de-comercio-internacional-y-tesoreria/productos-y-servicios-en-el-exterior/nassau` | 1.033w |

Panama aparece dos veces (`/panama` y `/sucursal-panama`). Nassau está en una sección distinta al resto. La sucursal de Miami, NY, Panamá y Nassau deberían tener una sección propia dentro de `/sobre-el-banco/` o dentro de `/empresas/banca-internacional/`, no anidadas dentro de una categoría de producto.

**Propuesta:**
```
/sobre-el-banco/presencia-internacional/
  /miami
  /new-york
  /panama
  /nassau

o bien:

/empresas/banca-internacional/
  /miami
  /new-york
  /panama
  /nassau
```

### 1.6 `crecer` y `logros` en tarjetas de crédito y débito de empresas

| URL | Palabras |
|---|---|
| `/empresas/tarjetas-de-credito/crecer` | 1.115w |
| `/empresas/tarjetas-de-credito/logros` | 988w |
| `/empresas/tarjetas-debito/crecer` | 856w |
| `/empresas/tarjetas-debito/logros` | 826w |

Dos tarjetas con el mismo nombre (`crecer`, `logros`) en débito y crédito empresarial. No está claro si son el mismo producto en dos modalidades (en cuyo caso deben vincularse) o productos distintos con nombre similar (en cuyo caso se presta a confusión).

---

## 2. Páginas técnicas y de sistema dentro del árbol de contenido

Estas páginas son estados del sistema o herramientas de soporte técnico que no deberían aparecer como contenido navegable indexado.

| URL | Palabras | Problema |
|---|---|---|
| `/empresas/login` | 24w | Redirección al portal transaccional. No es contenido, es una función. |
| `/empresas/requerimientos-sistema` | 1.251w | Requisitos técnicos del portal (navegadores, Java). Debería estar en soporte técnico del portal, no en el catálogo de productos. |
| `/empresas/flujo-solicitud-de-novedades` | 683w | Formulario/proceso de solicitud de cambios en el portal. Nombre interno expuesto como URL pública. |
| `/personas/extractos` | 597w | Funcionalidad de descarga de extractos. Es operativa, no descripción de producto. |
| `/personas/informacion-productos-servicios/formato-apertura-productos` | 47w | 47 palabras. Probablemente un PDF embebido sin contenido indexable. |

**`/empresas/login`** es el caso más crítico: una página de 24 palabras que es solo un botón de acceso al portal. Que esta URL exista como nodo en el árbol de contenido significa que fue creada como página CMS en lugar de ser una redirección de infraestructura.

---

## 3. Páginas de producto en `/empresas` sin categoría

Estas páginas existen en `/empresas` pero flotan sin sección que las agrupe:

### 3.1 `/empresas/enko` (621w)
Programa para emprendedores y empresas. No está clasificado dentro de ninguna categoría del portafolio empresarial. Por su contenido debería estar en:
```
/empresas/pyme/enko/          ← si está orientado a pymes
o
/empresas/educacion-y-recursos/enko/   ← si es un programa educativo
```

### 3.2 `/empresas/educacion-financiera-territorios` (766w)
Educación financiera orientada a territorios específicos. Es la única página de educación financiera en el portafolio empresarial. No tiene par en `/educacion-financiera/` (que es solo para personas). Propuesta:
```
/empresas/educacion-financiera/      ← nueva sección (si hay más contenido previsto)
  /territorios
```

### 3.3 `/empresas/cuenta-en-dolares-pyme` (1.209w)
Producto de cuenta en dólares para pymes, suelto en la raíz de empresas. Debería estar:
```
/empresas/pyme/cuenta-en-dolares/
o
/empresas/inversion-y-liquidez/cuenta-en-dolares-pyme/
```

### 3.4 `/empresas/seguros-pyme` (985w)
Seguros para pymes, suelto. Debería estar:
```
/empresas/pyme/seguros/
```

### 3.5 `/empresas/soluciones-financiacion-estructurada` (255w)
255 palabras sobre financiación estructurada. Thin content para un servicio que es de alto valor. No tiene sección lógica actualmente. Probablemente pertenece a:
```
/empresas/productos-de-credito/financiacion-estructurada/
```

---

## 4. El patrón VTU: páginas de canal de venta sin contexto

`vtu` y `vtua` aparecen como subpáginas de varios productos sin ninguna explicación de qué son:

| URL | Palabras | Producto padre |
|---|---|---|
| `/personas/tarjetas-de-credito/clasica/vtu` | 164w | Tarjeta Clásica |
| `/personas/tarjetas-de-credito/aliada/vtu` | 163w | Tarjeta Aliada |
| `/personas/creditos/libre-inversion/vtu` | 847w | Crédito Libre Inversión |
| `/personas/creditos/crediservice/vtua` | 856w | Crediservice (variante `vtua`) |
| `/personas/cdt/tradicional/vtu` | 159w | CDT Tradicional |

Las páginas `/clasica/vtu` y `/aliada/vtu` son extremadamente thin (164 palabras). Las demás tienen contenido normal.

**Hipótesis:** VTU parece ser una abreviatura interna de "Venta Telefónica / Fuerza de Ventas" o de un canal de adquisición específico. Son landing pages de un mismo producto pensadas para un canal de venta diferente (teléfono, call center, vendedor), con una URL distinta para tracking de conversión.

**Problema:** Estas páginas son internas de canal pero están indexadas públicamente. Un usuario que navega a `/personas/tarjetas-de-credito/clasica/` ve como subpágina una opción llamada `vtu` que no significa nada para él.

**Propuesta:**
- Si son exclusivas para un canal de venta, no deberían ser URLs públicas indexadas
- Si tienen contenido válido, el slug debe ser descriptivo: `/clasica/solicitar-por-telefono` o `/clasica/oferta-especial`
- La nomenclatura `vtua` (variante de `vtu` en Crediservice) indica que no hay una convención estandarizada

---

## 5. El patrón Anderson / Hamilton: convenios institucionales sin contexto

Cuatro páginas nombradas con apellidos (Anderson, Hamilton) aparecen en distintos productos:

| URL | Palabras | Producto |
|---|---|---|
| `/personas/creditos/libre-inversion/li-anderson-g` | 297w | Crédito libre inversión |
| `/personas/creditos/libre-inversion/li-hamilton` | 290w | Crédito libre inversión |
| `/personas/cuenta-de-ahorros/ca-hamilton` | 276w | Cuenta de ahorros |
| `/personas/tarjetas-de-credito/tc-anderson` | 455w | Tarjeta de crédito |

`li-` (libre inversión), `ca-` (cuenta de ahorros), `tc-` (tarjeta de crédito) son prefijos del tipo de producto. Anderson y Hamilton parecen ser instituciones educativas o empleadores con convenio (universidades, empresas grandes con acuerdo comercial).

**Problema:** Los slugs usan nombres propios sin contexto (`li-anderson-g`, `ca-hamilton`) y mezclan prefijos de producto con nombres de convenio de forma no consistente. No existe una sección `/alianzas-institucionales/` o `/convenios/` que los agrupe.

**Propuesta:**
```
/personas/creditos/convenios/              ← nueva sección de convenios
  /anderson
  /hamilton
  /[otros-convenios]

o dentro del tipo de producto:
/personas/creditos/libre-inversion/convenio-anderson/
/personas/cuenta-de-ahorros/convenio-hamilton/
```

---

## 6. `/personas/bienvenida`: onboarding sin modelo

`/personas/bienvenida` tiene 3 subpáginas para clientes nuevos:

```
/personas/bienvenida/
  /credito-libre-inversion   [585w]
  /cuentas-de-ahorro         [1.088w]
  /tarjetas-credito          [1.075w]
```

Es el único intento de contenido de onboarding en el sitio. El problema es que existe como una sección paralela a los productos, en lugar de ser una capa dentro del ecosistema de cada producto.

Un cliente que acaba de activar su tarjeta de crédito debería llegar a:
```
/personas/tarjetas-de-credito/[su-tarjeta]/bienvenida    ← contextual al producto
```
No a:
```
/personas/bienvenida/tarjetas-credito    ← genérico, sin relación con su tarjeta específica
```

Esta sección también crea fragmentación con `/atencion-al-cliente/instructivos/`, que es la sección de operaciones post-activación.

---

## 7. `/personas/portafolios` y `/banca-personas/portafolios`: duplicidad de segmentación

Existe una tercera instancia de la segmentación por tipo de cliente, además de `/personas/portafolios` y `/banca-personas`:

| URL | Segmentos | Páginas |
|---|---|---|
| `/personas/portafolios/` | masivo, preferente, premium | 3 |
| `/banca-personas/portafolio-personas` | portafolio personas | 1 |
| `/banca-personas/portafolio-personas-alto` | portafolio alto | 1 |
| `/banca-personas/preferente/portafolio-integral-preferente` | integral preferente | 1 |
| `/banca-personas/premium/portafolio-integral-premium` | integral premium | 1 |
| `/banca-personas/joven/portafolio-integral-joven` | integral joven | 1 |
| `/banca-personas/portafolio-integral-basico` | integral básico | 1 |

Los portafolios "integrales" por segmento están tanto en `/personas/portafolios/` como en `/banca-personas/[segmento]/portafolio-integral-[segmento]`. Son la misma información de segmentación publicada en dos lugares distintos.

---

## 8. Programa de beneficios y lealtad: infradesarrollado

`/personas/beneficios/` tiene solo 2 páginas (303 palabras promedio):
```
/personas/beneficios/
  /plan-lealtad-mejores-puntos   [372w]
  /programa-lealtad-tuplus       [423w]
```

Además:
- `/personas/experiencias-aval` (419w) — acceso a experiencias del grupo Aval — está suelta en la raíz de personas
- `/BuscadordePuntosAval` (122w) — buscador de redención de puntos — está en la raíz del dominio

Los tres son parte del mismo ecosistema de fidelización, pero no están conectados. Un programa de lealtad completo requeriría:

```
/personas/programa-de-beneficios/
  /como-ganar-puntos
  /como-canjear-puntos
  /buscador-de-puntos             ← mover desde raíz
  /tuplus
  /mejores-puntos
  /experiencias-aval              ← mover desde /personas/
  /tiendas-y-aliados
```

---

## 9. `/personas/promociones`: slugs internos en producción

`/personas/promociones/` tiene 9 subpáginas con slugs que mezclan nomenclatura interna y de campañas activas:

| Slug | Palabras | Problema |
|---|---|---|
| `/exte-ca` | 799w | `exte-` = extensión interna de cuenta de ahorros |
| `/exte-tc` | 608w | `exte-` = extensión interna de tarjeta de crédito |
| `/ext-cuenta-facil` | 716w | Variante del mismo prefijo |
| `/productos-digitales-chf` | 534w | `chf` no tiene significado para el usuario |
| `/mas-de-una-vez-cashback` | 299w | Thin content (cashback) |
| `/mas-de-una-vez-millas` | 291w | Thin content (millas) |
| `/cuota-en-pausa` | 615w | Beneficio de alivio financiero — debería estar en gestión de crédito |
| `/oferta-instacupo` | 813w | Duplica `/personas/tarjetas-de-credito/instacupo` |
| `/preaprobado-tarjeta-credito` | 385w | Landing de producto preaprobado — debería estar en el ecosistema de TC |

`/cuota-en-pausa` es especialmente mal ubicado: es un programa de alivio para clientes con dificultad de pago, que debería estar en `/personas/gestiona-tu-credito/opciones-ponerte-al-dia/`, no en una sección de promociones.

---

## 10. Productos de personas sin ecosistema mínimo

Hay productos que existen como una sola página sin ningún satélite (ni variantes, ni tasas, ni FAQ):

| URL | Palabras | Problema |
|---|---|---|
| `/personas/cuenta-corriente` | 1.025w | Un solo producto sin variantes ni subpáginas. Empresas tiene 4 páginas para cuenta corriente. |
| `/personas/depositos` | 1.615w | CDT/depósitos como página única, a pesar de que existe `/personas/cdt/` con 4 páginas separadas. |
| `/personas/bienes-e-inmuebles` | 111w | 111 palabras para un producto de bienes raíces (very thin). No está en `/personas/leasing/` ni en ningún ecosistema. |
| `/personas/servicio-transfiya` | 942w | Servicio de transferencias inmediatas suelta en personas, sin relación con `/atencion-al-cliente/canales/transacciones/transferencias-utilizaciones` |

La coexistencia de `/personas/depositos` y `/personas/cdt` es un caso claro de contenido duplicado sin consolidar.

---

## 11. Sostenibilidad dentro de `/empresas/leasing`

Una página de sostenibilidad vive dentro del producto leasing empresarial:

```
/empresas/leasing/sostenibilidad   [1.058w]
```

Esta página tiene exactamente el mismo número de palabras (1.058) que `/empresas/leasing/` (la landing del producto), lo que sugiere que puede ser contenido compartido o duplicado de la sección institucional. No hay ninguna otra página de sostenibilidad dentro de ecosistemas de producto; esta es la única excepción.

**Propuesta:** Si el contenido es específico del leasing sostenible (financiamiento de activos verdes), debería renombrarse:
```
/empresas/leasing/leasing-sostenible/    ← ya existe como variante de producto
```
Si es contenido institucional reutilizado, debe reemplazarse por un enlace a `/sobre-el-banco/sostenibilidad/`.

---

## 12. Perfiles de beneficiarios de la Fundación como páginas web

La Fundación Banco de Bogotá publica **4 perfiles de personas** como páginas individuales dentro del árbol de contenido:

```
/sostenibilidad/fundacion-banco-de-bogota/educacion-y-bienestar-social/
  /alejandro-torres   [885w]
  /astrid-sarria      [808w]
  /cristian-ropero    [659w]
  /paola-monroy       [826w]
```

Estas son historias de impacto social (personas beneficiadas por programas de la Fundación). Es contenido con valor editorial, pero tiene tres problemas estructurales:

1. **No hay una plantilla de tipo**: todas son páginas únicas. Si el banco publica más historias, no hay un modelo de URL predecible.
2. **Están 4 niveles adentro**: `/sostenibilidad/fundacion/educacion-y-bienestar-social/[persona]` es la ruta más larga de la sección institucional.
3. **No hay índice de historias**: no hay una página `/educacion-y-bienestar-social/` que liste y permita explorar todos los perfiles.

**Propuesta de modelo:**
```
/sobre-el-banco/fundacion/historias-de-impacto/      ← índice
  /alejandro-torres
  /astrid-sarria
  /cristian-ropero
  /paola-monroy
  /[nuevas-historias]
```

---

## 13. Resumen: inventario de páginas no consideradas y su destino

| Página / patrón | Problema | Destino propuesto |
|---|---|---|
| `/empresas/soluciones-de-comercio-internacional-y-tesoreria` | Duplicado de `/empresas/comercio-internacional-y-tesoreria` | Fusionar, redirigir |
| `/empresas/negocio-de-divisas` | Duplicado singular/plural de `negocios-de-divisas` | Eliminar el menor, redirigir |
| `/empresas/soluciones-fiduciarias` | Duplicado parcial de `/inversion-y-liquidez/fiducias` | Fusionar |
| `/empresas/recaudo-y-pagos` | Duplicado de `recaudos-y-pagos` | Redirigir 301 |
| Sucursales internacionales (Miami, NY, Panamá, Nassau) | Dispersas en 2 secciones | `/sobre-el-banco/presencia-internacional/` |
| `panama` + `sucursal-panama` | Misma oficina, dos URLs | Conservar una, redirigir la otra |
| `confirming` (2 veces) | Mismo producto en dos secciones | Página canónica + referencia cruzada |
| `crecer` y `logros` (TC y débito) | Mismo nombre en dos tipos de tarjeta | Aclarar si son el mismo o distinto producto |
| `/empresas/login` | Función del sistema, no contenido | Eliminar del CMS; implementar como redirección |
| `/empresas/requerimientos-sistema` | Soporte técnico del portal | `/ayuda/portal-empresarial/requerimientos/` |
| `/empresas/flujo-solicitud-de-novedades` | Proceso interno con URL pública | `/ayuda/portal-empresarial/solicitar-novedades/` |
| `/empresas/enko` | Programa sin sección | `/empresas/pyme/enko/` |
| `/empresas/cuenta-en-dolares-pyme` | Producto suelto | `/empresas/pyme/cuenta-en-dolares/` |
| `/empresas/seguros-pyme` | Producto suelto | `/empresas/pyme/seguros/` |
| `/empresas/educacion-financiera-territorios` | Sin sección | `/empresas/educacion-financiera/territorios/` |
| Patrón VTU (5 páginas) | Slug de canal interno indexado públicamente | Hacer privadas o renombrar con significado |
| Patrón Anderson/Hamilton (4 páginas) | Convenios institucionales sin sección | `/personas/[producto]/convenios/[institución]` |
| `/personas/bienvenida` | Onboarding genérico sin relación al producto | Integrar en cada ecosistema de producto |
| `/personas/portafolios` | 3ª instancia de segmentación, duplica banca-personas | Fusionar con `/banca-personas/` |
| `/personas/beneficios` + `/experiencias-aval` + `/BuscadordePuntosAval` | Ecosistema de lealtad fragmentado | `/personas/programa-de-beneficios/` |
| Slugs técnicos en promociones (`exte-ca`, `exte-tc`, `chf`) | Nomenclatura interna pública | Renombrar con slugs descriptivos |
| `/personas/cuota-en-pausa` | En promociones; es alivio financiero | `/personas/gestiona-tu-credito/opciones-ponerte-al-dia/` |
| `/personas/oferta-instacupo` | Duplica `/personas/tarjetas-de-credito/instacupo` | Redirigir o fusionar |
| `/personas/depositos` | Duplica `/personas/cdt/` | Fusionar en un solo ecosistema CDT/depósitos |
| `/personas/bienes-e-inmuebles` | 111w, sin categoría | `/personas/leasing/` o eliminada |
| `/personas/servicio-transfiya` | Servicio suelto | `/personas/medios-de-pago/transfiya/` |
| `/empresas/leasing/sostenibilidad` | Página institucional dentro de producto | Reemplazar por link a `/sobre-el-banco/sostenibilidad/` |
| Perfiles de beneficiarios Fundación | Sin plantilla ni índice | `/sobre-el-banco/fundacion/historias-de-impacto/[persona]` |

---

*Ver también: [analisis-arquitectura-informacion.md](analisis-arquitectura-informacion.md), [tipos-de-pagina-y-ecosistemas.md](tipos-de-pagina-y-ecosistemas.md), [paginas-no-producto-estructura.md](paginas-no-producto-estructura.md)*
*Fecha: junio 2026.*
