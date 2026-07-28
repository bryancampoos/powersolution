# BRIEF — Sitio web Perfect Solution

> Documento de trabajo. Todo lo marcado con `⚠️ PENDIENTE` necesita confirmación del cliente
> antes de construir. Nada marcado así debe inventarse en el sitio final.

---

## 1. Identidad

| Campo | Valor |
|---|---|
| Nombre comercial | **Perfect Solution** |
| Firma / autoría | *by Michaell J. Rivera* |
| Apodo de marca | **"El Tipo"** |
| Descriptor del logo | Plomería · Pintura · Reparaciones Generales |
| Posicionamiento acordado | **Contratista general y remodelaciones**, con los servicios del logo como base |
| Mercado | Área Metro y región Sur de Puerto Rico |
| Teléfono / WhatsApp | 939-219-0979 |
| Correo | pseltipo@outlook.com |
| Trayectoria | 2 años |

### Paleta (medida sobre el logo, no estimada)

Extraída por cuantificación de los píxeles del JPEG original. Son los cinco colores
reales del logo; el sitio no usa ningún otro color de marca.

```
--naranja    #EF6C33   Acentos, íconos, números, detalles. 3.06:1 sobre blanco:
                       NO usar para texto pequeño, solo para elementos gráficos.
--terracota  #BB4817   Botones primarios y enlaces. 5.19:1 con texto blanco (AA).
--marron     #6B2F15   Titulares, footer, fondos oscuros. 9.64:1 sobre el crema.
--crema      #FFF6ED   Fondo base del sitio. Es el fondo del propio logo.
--negro      #080303   Detalles de la ilustración.
```

Derivados que usa el CSS: `--marron-oscuro #4A2010` (texto de cuerpo y hero),
`--crema-2 #FBEADC` (secciones alternas), `--borde #E8D5C4`.

> El botón primario es **terracota, no naranja**. El naranja con texto blanco da 3.06:1
> y no cumple AA para texto pequeño; el terracota da 5.19:1. Es la razón de que el
> naranja quede reservado a íconos y acentos.

Regla: el crema es el fondo, **no** el blanco puro. Es lo que amarra el sitio al logo y lo
diferencia de la plantilla genérica de constructora.

### Tipografía (Google Fonts)

- **Titulares:** `Archivo` 800/900 — sans robusta y ancha, hace eco del lettering del logo.
- **Cuerpo:** `Inter` 400/500/600 — legible, neutra, no compite.
- **Acento manuscrito:** `Caveat` 600 — **solo** para "El Tipo" y frases cortas de firma.
  Nunca para párrafos ni botones.

---

## 2. Público y promesa

**Quién llega al sitio:**
1. Dueño de casa con un problema urgente (fuga, filtración, algo roto) → quiere resolverlo *hoy*.
2. Dueño de casa planificando una remodelación de baño o cocina → compara, quiere ver trabajos.
3. Negocio pequeño o administrador de propiedades → quiere un contratista confiable y recurrente.

**Promesa central:** un solo contratista que resuelve desde la reparación pequeña hasta la
remodelación completa — sin subcontratar el problema, sin desaparecer a mitad de obra.

**Tono:** cercano y directo, de oficio, primera persona. Nada de lenguaje corporativo inflado.
El sitio debe sonar a Michaell hablando, no a un folleto.

---

## 3. Arquitectura del sitio

Multipágina ligera (mejor para SEO que una sola página larga):

```
/                Home
/servicios       Todos los servicios en detalle
/proyectos       Galería de trabajos + antes/después
/nosotros        Michaell, historia, licencias, seguro
/contacto        Formulario + WhatsApp + área de servicio
```

Bilingüe: español en la raíz, inglés bajo `/en/` con las mismas rutas, `hreflang` cruzado y
selector **ES | EN** en el header que preserva la página actual.

### Home — secciones en orden

1. **Header** — logo, nav, selector de idioma, teléfono visible, botón "Cotiza gratis".
   Sticky al hacer scroll, con fondo sólido crema.
2. **Hero** — imagen de un trabajo real a pantalla ancha, overlay marrón oscuro.
   Titular + subtítulo + dos botones: *WhatsApp* (primario) y *Ver trabajos* (secundario).
3. **Barra de confianza** — 4 datos duros en fila: años de experiencia · proyectos completados ·
   licenciado y asegurado · presupuesto sin costo. ⚠️ PENDIENTE: números reales.
4. **Servicios** — grid de 6 tarjetas con ícono, título y una línea. Enlace a `/servicios`.
5. **Remodelaciones** — bloque destacado a dos columnas (baños y cocinas), el gancho de
   mayor ticket. Foto grande + bullets + CTA.
6. **Trabajos recientes** — 6 fotos en mosaico, al menos 2 en formato antes/después con slider.
7. **Cómo trabajamos** — 4 pasos numerados: *Llamas → Visitamos y evaluamos → Cotización
   escrita → Ejecutamos y entregamos limpio*.
8. **Testimonios** — 3 reseñas con nombre y pueblo. ⚠️ PENDIENTE: reseñas reales.
9. **Área de servicio** — lista de pueblos cubiertos. Es señal fuerte de SEO local.
10. **CTA de cierre** — franja naranja: "¿Tienes algo que arreglar o quieres remodelar?"
    + teléfono + WhatsApp.
11. **Footer** — logo en versión clara sobre marrón, nav, contacto, horario, redes, © año.

### Elementos permanentes

- **Botón flotante de WhatsApp** abajo a la derecha, en todas las páginas, con mensaje
  predefinido: *"Hola Michaell, vi su página y necesito ayuda con…"*
- **Barra de llamada en móvil**: franja fija abajo con *Llamar* | *WhatsApp*.

---

## 4. Servicios

⚠️ PENDIENTE — confirmar cuáles ofrece realmente. Borrador según el logo y el posicionamiento:

**Base (del logo)**
- Plomería — fugas, destape, calentadores, instalación de piezas
- Pintura — interior, exterior, sellado
- Reparaciones generales — el "llámame para lo que sea"


**Remodelación**
- Baños completos
- Cocinas completas
- Losa, azulejo y pisos
- Drywall, plafón y molduras
- Gabinetes y closets

**Exterior / estructura**
- Impermeabilización y sellado de techos
- Ventanas y puertas
- Verjas, portones y terrazas
- Ampliaciones y cuartos anexos

> **Nota legal:** en Puerto Rico la plomería y la electricidad requieren perito licenciado, y la
> obra de cierta escala requiere contratista registrado. El sitio no debe afirmar licencias,
> certificaciones ni seguro que no existan. Si algo se subcontrata a un licenciado, se puede
> decir así — es honesto y sigue vendiendo.

---

## 5. Copy — borrador

Todo el copy final va en dos idiomas. Esto es el punto de partida en español;
el inglés se traduce de forma natural, no literal.

**Hero**
> ### Lo arreglamos. Lo remodelamos. Lo dejamos perfecto.
> Plomería, pintura, reparaciones y remodelación completa de baños y cocinas.
> Presupuesto sin costo y trabajo garantizado.
> `[ Escríbenos por WhatsApp ]` `[ Ver trabajos ]`

**Remodelaciones**
> ### Tu baño o tu cocina, completos
> Demolición, plomería, electricidad, losa, gabinetes y pintura — un solo contratista
> de principio a fin. Tú no tienes que coordinar a nadie.

**Cómo trabajamos**
> 1. **Nos escribes** — cuéntanos qué necesitas, con fotos si las tienes.
> 2. **Visitamos y evaluamos** — vamos a verlo en persona, sin cargo.
> 3. **Cotización escrita** — precio claro, sin sorpresas a mitad de obra.
> 4. **Ejecutamos y entregamos** — terminamos a tiempo y dejamos el área limpia.

**CTA de cierre**
> ### ¿Tienes algo que arreglar o quieres remodelar?
> Llama a "El Tipo". Contesta él, no una máquina.

**Firma de marca** — usar `Caveat` en el bloque de *Nosotros*:
> *"Si te digo que llego, llego."* — Michaell J. Rivera

---

## 6. Sistema de diseño

**Layout:** ancho máximo 1200px, canalón 24px móvil / 48px escritorio.
Escala de espaciado en múltiplos de 8. Secciones a 96px de padding vertical (64px en móvil).

**Bordes:** radio de 12px en tarjetas, 8px en botones, 999px en píldoras.
El logo es redondeado — el sitio no debe ser de esquinas vivas.

**Botones**
- Primario: fondo naranja, texto blanco, hover a naranja oscuro, transición 150ms.
- Secundario: borde marrón 2px, fondo transparente, hover invierte a marrón sólido.
- Ambos con área táctil mínima de 44px de alto.

**Tarjetas:** fondo blanco sobre crema, sombra suave `0 2px 12px rgba(74,35,18,.08)`,
elevación en hover con `translateY(-4px)`.

**Íconos:** línea de 2px, un solo estilo consistente en todo el sitio, en naranja.
SVG inline — sin librería de íconos externa.

**Fotografía:** obligatoriamente trabajos reales. Nada de banco de imágenes con obreros
sonrientes de cascos amarillos — mata la credibilidad en un negocio local.
⚠️ PENDIENTE: recibir fotos.

**Movimiento:** aparición suave al entrar en viewport (`IntersectionObserver`, fade + 16px de
subida). Nada de parallax ni carruseles automáticos. Respetar `prefers-reduced-motion`.

**Modo oscuro:** no. El sitio vive en el crema del logo.

---

## 7. Entrega técnica

**Stack:** HTML5 + CSS3 + JavaScript vanilla. Cero frameworks, cero build, cero dependencias
de npm. Se sube por FTP a cualquier hosting o se arrastra a Netlify.

```
perfect-solution/
├── index.html
├── servicios.html
├── proyectos.html
├── nosotros.html
├── contacto.html
├── en/
│   └── (mismas 5 páginas en inglés)
├── assets/
│   ├── css/styles.css
│   ├── js/main.js          nav móvil, scroll, animaciones, slider antes/después
│   ├── img/
│   └── logo/
├── favicon.ico
├── robots.txt
└── sitemap.xml
```

**Requisitos no negociables**
- Responsive real desde 320px. Diseñado móvil primero — la mayoría del tráfico llega del
  celular tras ver el logo en una guagua o una tarjeta.
- Lighthouse ≥ 95 en Performance, Accesibilidad y SEO.
- Imágenes en WebP con `loading="lazy"`, `width` y `height` declarados para evitar saltos.
- HTML semántico, `alt` descriptivo en todo, contraste AA verificado, navegable por teclado.
- **SEO local:** JSON-LD de tipo `LocalBusiness` con nombre, teléfono, dirección, horario,
  área de servicio y redes. `<title>` y `meta description` únicos por página. Open Graph
  para que el enlace se vea bien al compartirlo por WhatsApp.
- Formulario de contacto: **resuelto sin backend, con dos vías de envío**. El visitante
  llena los campos una vez y elige botón:
  - *Enviar por WhatsApp* → abre el chat con el mensaje redactado.
  - *Enviar por correo* → abre el gestor de correo del visitante con todo escrito.

  Lleva honeypot antispam. Ninguna de las dos vías tiene coste ni mantenimiento.

  El botón de correo entrega directo vía **Web3Forms** (configurado y probado): el mensaje
  llega a `pseltipo@outlook.com` sin que el visitante salga de la página. Si el servicio
  fallara, el formulario abre el gestor de correo del visitante como respaldo, así que
  nunca se queda sin vía de contacto.

  Al mover el sitio a un hosting con PHP conviene sustituirlo por un `enviar.php` propio:
  quita la dependencia externa y el límite de envíos. Ver la tabla del README.

---

## 8. Estado de los datos

**Confirmado y ya puesto en el sitio**

- [x] Teléfono y WhatsApp — 939-219-0979
- [x] Correo — pseltipo@outlook.com
- [x] Región — Área Metro y Sur
- [x] Trayectoria — 2 años
- [x] Lista de servicios (sin eléctrico, según tu corrección del brief)
- [x] Logo vectorial — trazado desde el JPEG, en `assets/logo/`

**Todavía pendiente**

- [ ] **Fotos de trabajos** — lo más urgente. Mínimo 8, idealmente 2 o 3 pares de
      antes/después. Ahora mismo hay 11 placeholders que dicen "pendiente".
- [ ] ¿Licenciado? ¿Asegurado? ¿Número de registro de contratista?
      *El sitio no afirma ninguna de las tres cosas mientras no se confirmen.*
- [ ] Reseñas reales (Google, Facebook o por escrito con permiso).
      *No hay sección de testimonios: no se inventan reseñas.*
- [ ] Horario de servicio · ¿atiende emergencias fuera de horario?
- [ ] Facebook / Instagram
- [ ] Lista definitiva de pueblos — ahora hay 18 del Área Metro y Sur puestos por
      criterio geográfico, conviene que los revise y quite los que no cubra
- [ ] Dominio y hosting — el sitio usa `perfectsolutionpr.com` como marcador en las
      URLs canónicas, `sitemap.xml` y `robots.txt`. Hay que sustituirlo por el real.

### Notas sobre decisiones tomadas

- **Los 2 años no se usan como argumento de venta.** Un contratista con dos años no
  compite por veteranía, así que la barra de confianza vende lo que sí es verificable:
  cotización por escrito, un solo interlocutor, contesta el dueño, se entrega limpio.
  El dato aparece con naturalidad en *Nosotros*, sin inflarlo.
- **No hay sección de testimonios** hasta que haya reseñas reales.
- **El sitio no dice "licenciado y asegurado"** hasta que se confirme.
