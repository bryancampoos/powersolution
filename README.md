# Perfect Solution — sitio web

Sitio estático bilingüe (ES / EN). HTML, CSS y JavaScript puros: **no hay que compilar
nada**. Se sube tal cual a cualquier hosting o se arrastra la carpeta a Netlify.

Para verlo en local, basta con abrir `index.html` en el navegador.

---

## Qué hay aquí

```
index.html  servicios.html  proyectos.html  nosotros.html  contacto.html   ← español
en/index.html  en/services.html  en/projects.html  en/about.html  en/contact.html  ← inglés

assets/css/styles.css    todo el diseño (colores, tipografía, componentes)
assets/js/main.js        menú móvil, animaciones, slider antes/después, formulario
assets/img/              fotos del sitio  ← AQUÍ VAN LAS FOTOS REALES
assets/logo/             el logo vectorizado en todas sus versiones

favicon.ico  apple-touch-icon.png  site.webmanifest  robots.txt  sitemap.xml
BRIEF.md                 el documento de decisiones y lo que falta
_generador/              opcional, ver más abajo
```

---

## Lo primero que hay que hacer

### 1. Poner las fotos reales

En `assets/img/` hay 11 archivos `.svg` que son marcadores: dicen "pendiente de sustituir
por una foto real". Para reemplazarlos, guarda tus fotos con **el mismo nombre pero en
`.jpg`** y cambia la extensión en el HTML donde aparezca.

| Archivo | Dónde sale | Qué debe ser |
|---|---|---|
| `hero.svg` | fondo de la portada | foto ancha de una obra o de ti trabajando (1600×900) |
| `remodelacion.svg` | bloque de remodelación | un baño o cocina terminados |
| `equipo.svg` | página *Nosotros* | Michaell en obra |
| `trabajo-1..6.svg` | galerías | seis trabajos terminados (4:3) |
| `antes.svg` / `despues.svg` | slider comparador | el mismo espacio antes y después, **desde el mismo ángulo** |

Consejos: horizontal, con luz de día, sin filtros. Para el antes/después, lo importante
es que las dos fotos estén tomadas desde el mismo punto — si no, el slider no funciona.

Guarda las fotos a un ancho máximo de 1600 px y en calidad ~80 %. Una foto de 4 MB
recién salida del celular hace que la página tarde en cargar.

### 2. Cambiar el dominio

Ahora mismo el sitio usa `perfectsolutionpr.com` como marcador. Cuando tengas el dominio
real, busca y reemplaza esa cadena en:

- los 10 archivos `.html` (etiquetas `canonical`, `hreflang` y `og:`)
- `sitemap.xml`
- `robots.txt`

### 3. Revisar lo que quedó pendiente

Está listado al final de [BRIEF.md](BRIEF.md): licencias, seguro, reseñas, horario,
redes sociales y la lista definitiva de pueblos.

---

## Cambios frecuentes

**Teléfono, WhatsApp o correo:** aparecen en varios sitios de cada página. Busca y
reemplaza `939-219-0979`, `19392190979` (el del enlace de WhatsApp) y `pseltipo@outlook.com`.

**Colores:** están todos al principio de `assets/css/styles.css`, en el bloque `:root`.
Cambiando ahí un valor, cambia en todo el sitio.

---

## El formulario de contacto

El visitante llena los campos una sola vez y elige cómo mandarlo:

- **Enviar por WhatsApp** — abre el chat con el mensaje ya redactado.
- **Enviar por correo** — abre el gestor de correo del visitante (Gmail, Outlook, la app
  del teléfono…) con destinatario, asunto y cuerpo escritos. Solo tiene que darle a enviar.

Ninguna de las dos necesita servidor, así que no hay coste ni nada que mantener.

### Cómo llega el correo

El botón de correo usa **Web3Forms**, ya configurado y probado. El mensaje se envía
directo a `pseltipo@outlook.com` sin que el visitante salga de la página.

La clave está en `assets/js/main.js`, en `WEB3FORMS_KEY`. Es visible en el código y eso
es correcto: Web3Forms la diseñó para usarse desde el navegador, va ligada al dominio
registrado y no da acceso a nada de la cuenta.

Si algún día el servicio no respondiera, el formulario no deja al visitante colgado:
abre su gestor de correo con el mensaje ya escrito, como respaldo.

**Panel de mensajes:** entrando en [web3forms.com](https://web3forms.com) con
`pseltipo@outlook.com` se ven todos los envíos recibidos, por si algún correo se
perdiera o cayera en no deseado.

### El día que cambies de hosting

Esto no depende de GitHub, sino de que el sitio sea estático: son archivos que el
servidor entrega tal cual, sin ejecutar nada. Enviar un correo necesita algo corriendo
en el servidor. Según dónde acabe el sitio:

| Destino | Qué hacer |
|---|---|
| Hosting con **PHP** (Hostinger, GoDaddy, SiteGround, cPanel…) | Lo mejor. Un `enviar.php` de unas 15 líneas envía directo, sin servicios externos ni límite de envíos. Ya no hace falta Web3Forms |
| **Netlify** | Trae formularios integrados: se activan con un atributo en el `<form>`. 100 envíos al mes gratis y quedan guardados en un panel |
| **Cloudflare Pages** o **Vercel** | Funcionan, pero hay que escribir una función serverless |
| Otro hosting **estático** | Igual que ahora: Web3Forms es la vía |

Web3Forms sirve en todos los casos, así que es la opción segura mientras no esté decidido.
Cambiar después a la solución propia del hosting es cuestión de minutos.

---

## El logo

`assets/logo/original.jpeg` es el archivo que se recibió. El resto está vectorizado a
partir de él, así que se puede ampliar a cualquier tamaño sin perder nitidez —
sirve igual para el sitio que para una rotulación de guagua o un letrero.

| Archivo | Para qué |
|---|---|
| `logo.svg` | el logo completo a color, fondo transparente |
| `logo-light.svg` | sobre fondos oscuros (es el que va en el pie de página) |
| `isotipo.svg` | solo la casita, sin el texto — para la cabecera y el favicon |
| `avatar.png` | foto de perfil de Facebook, Instagram o WhatsApp Business |
| `logo-1024/512/256.png` | por si algún sitio no acepta SVG |

---

## _generador/ (opcional)

La cabecera, el pie y los iconos son idénticos en las diez páginas. Editarlos a mano
significa repetir el mismo cambio diez veces, y es fácil que se descuadre el español
con el inglés.

`_generador/build.py` reconstruye las diez páginas de una vez:

```
python _generador/build.py
```

**No hace falta para nada más.** El sitio funciona sin él. Si prefieres editar el HTML
directamente, borra la carpeta y no pasa nada — pero entonces recuerda hacer cada cambio
de cabecera o pie en los diez archivos.
