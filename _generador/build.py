# -*- coding: utf-8 -*-
"""
Generador del sitio de Perfect Solution.

OPCIONAL. El sitio publicado son los .html sueltos de la raíz y de /en/: no
necesitan este script para funcionar. Esto existe solo para no tener que editar
la cabecera, el pie o el juego de iconos en diez archivos a mano.

    python _generador/build.py

Reescribe los 10 HTML. Si prefieres editar el HTML directamente, borra esta
carpeta y ya: nada más depende de ella.
"""
import io
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEL_HUMANO = "939-219-0979"
TEL_LINK = "+19392190979"
WA = "19392190979"
EMAIL = "pseltipo@gmail.com"
IG_USUARIO = "_2rivera"
IG_URL = f"https://www.instagram.com/{IG_USUARIO}/"
# URL donde vive el sitio publicado. Al conectar un dominio propio, cambiar
# esto y volver a ejecutar build.py: actualiza canonical, hreflang y og:url.
DOMINIO = "https://bryancampoos.github.io/powersolution"

PUEBLOS = [
    "San Juan", "Bayamón", "Guaynabo", "Carolina", "Trujillo Alto", "Cataño",
    "Toa Baja", "Toa Alta", "Dorado", "Caguas", "Ponce", "Juana Díaz",
    "Santa Isabel", "Coamo", "Salinas", "Guayama", "Villalba", "Peñuelas",
]

# Cada pagina: clave -> (archivo es, archivo en)
PAGINAS = {
    "home":      ("index.html",      "en/index.html"),
    "servicios": ("servicios.html",  "en/services.html"),
    "proyectos": ("proyectos.html",  "en/projects.html"),
    "nosotros":  ("nosotros.html",   "en/about.html"),
    "contacto":  ("contacto.html",   "en/contact.html"),
}

NAV = {
    "es": [("home", "Inicio"), ("servicios", "Servicios"), ("proyectos", "Proyectos"),
           ("nosotros", "Nosotros"), ("contacto", "Contacto")],
    "en": [("home", "Home"), ("servicios", "Services"), ("proyectos", "Projects"),
           ("nosotros", "About"), ("contacto", "Contact")],
}

WA_TEXTO = {
    "es": "Hola Michaell, vi su página y necesito ayuda con...",
    "en": "Hi Michaell, I saw your website and I need help with...",
}

T = {
    "saltar":      {"es": "Saltar al contenido", "en": "Skip to content"},
    "inicio_aria": {"es": "Perfect Solution — inicio", "en": "Perfect Solution — home"},
    "abrir_menu":  {"es": "Abrir menú", "en": "Open menu"},
    "principal":   {"es": "Principal", "en": "Main"},
    "wa_boton":    {"es": "Escríbenos por WhatsApp", "en": "Message us on WhatsApp"},
    "wa_aria":     {"es": "Escribir por WhatsApp", "en": "Message us on WhatsApp"},
    "llamar":      {"es": "Llamar", "en": "Call"},
    "nav_footer":  {"es": "Navegación", "en": "Navigation"},
    "serv_footer": {"es": "Servicios", "en": "Services"},
    "cont_footer": {"es": "Contacto", "en": "Contact"},
    "area":        {"es": "Área Metro y Sur, PR", "en": "San Juan Metro & Southern PR"},
    "hecho":       {"es": "Hecho en Puerto Rico 🇵🇷", "en": "Made in Puerto Rico 🇵🇷"},
    "footer_desc": {
        "es": "Contratista general en el Área Metro y Sur de Puerto Rico. "
              "Plomería, pintura, reparaciones y remodelación.",
        "en": "General contractor serving the San Juan metro area and southern "
              "Puerto Rico. Plumbing, painting, repairs and remodeling.",
    },
    "cta_titulo": {
        "es": "¿Tienes algo que arreglar o quieres remodelar?",
        "en": "Got something to fix, or ready to remodel?",
    },
    "cta_texto": {
        "es": "Escríbenos y coordinamos la visita. El presupuesto no te cuesta nada.",
        "en": "Message us and we'll set up the visit. The estimate costs you nothing.",
    },
    "firma": {
        "es": '"Si te digo que llego, llego." — Michaell J. Rivera',
        "en": '"If I say I\'ll be there, I\'ll be there." — Michaell J. Rivera',
    },
}

SERVICIOS_FOOTER = {
    "es": [("plomeria", "Plomería"), ("pintura", "Pintura"),
           ("reparaciones", "Reparaciones"), ("remodelacion", "Remodelación"),
           ("exterior", "Techos y exterior")],
    "en": [("plomeria", "Plumbing"), ("pintura", "Painting"),
           ("reparaciones", "Repairs"), ("remodelacion", "Remodeling"),
           ("exterior", "Roofing & exterior")],
}

# --- iconos ---------------------------------------------------------------
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
  <symbol id="i-tel" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.2-1.7-.9-2-1-.3-.1-.5-.2-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1-.3-.2-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5 0-.2 0-.4 0-.5 0-.2-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.2.2 2.1 3.2 5.1 4.4.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"/><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3a8.2 8.2 0 1 1 7.2 3.9z"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></symbol>
  <symbol id="i-gota" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5S5.5 9.6 5.5 14a6.5 6.5 0 0 0 13 0c0-4.4-6.5-11.5-6.5-11.5z"/></symbol>
  <symbol id="i-brocha" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18.4 2.6a2 2 0 0 1 2.8 2.8L12 14.6 8.4 11z"/><path d="M8.4 11 5 14.4c-1 1-1 3.6-2.5 5.1 0 0 3.5.9 5.4-1a3.5 3.5 0 0 0 1-2.4"/></symbol>
  <symbol id="i-llave" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4.5 4.5 0 0 0 6 5.9l-8.5 8.5a2.4 2.4 0 0 1-3.4-3.4l8.5-8.5a4.5 4.5 0 0 0-5.9-6L14 6.4 11.9 8.6 8.7 5.4 10.9 3.2z"/></symbol>
  <symbol id="i-bano" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h18v3a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4z"/><path d="M6 12V5.5A2.5 2.5 0 0 1 8.5 3c1 0 1.8.6 2.2 1.4"/><path d="M6 19.5 5 22M18 19.5 19 22"/></symbol>
  <symbol id="i-cocina" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 11h18M7 7h.01M11 7h.01M7 15h4"/></symbol>
  <symbol id="i-techo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 11 12 3l10 8"/><path d="M5 10.5V20h14v-9.5"/><path d="M9.5 20v-5h5v5"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h5M9 13h6M9 17h4"/></symbol>
  <symbol id="i-reloj" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 1.8"/></symbol>
  <symbol id="i-mapa" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10.5c0 5.5-8 12-8 12s-8-6.5-8-12a8 8 0 1 1 16 0z"/><circle cx="12" cy="10.3" r="2.8"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="4.5" width="19" height="15" rx="2"/><path d="m3 6.5 9 6 9-6"/></symbol>
  <symbol id="i-flecha" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-escudo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5 4.5 5.5V11c0 5 3.2 9 7.5 10.5 4.3-1.5 7.5-5.5 7.5-10.5V5.5z"/><path d="m9 11.8 2.2 2.2 4-4"/></symbol>
  <symbol id="i-ventana" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M12 3.5v17M3.5 12h17"/></symbol>
  <symbol id="i-regla" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15.6 2.6 21.4 8.4a2 2 0 0 1 0 2.8L11.2 21.4a2 2 0 0 1-2.8 0L2.6 15.6a2 2 0 0 1 0-2.8L12.8 2.6a2 2 0 0 1 2.8 0z"/><path d="m7 11 2 2M10 8l2 2M13 5l2 2"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.6" y="2.6" width="18.8" height="18.8" rx="5.4"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.5" cy="6.5" r="1.15" fill="currentColor" stroke="none"/></symbol>
</defs></svg>'''


def icono(nombre, extra=""):
    return f'<svg aria-hidden="true"{extra}><use href="#i-{nombre}"/></svg>'


def wa_url(idioma):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(WA_TEXTO[idioma])}"


# --- piezas comunes -------------------------------------------------------
def head(idioma, clave, titulo, descripcion, jsonld=""):
    p = "../" if idioma == "en" else ""
    es_file, en_file = PAGINAS[clave]
    url_es = f"{DOMINIO}/{es_file}".replace("/index.html", "/")
    url_en = f"{DOMINIO}/{en_file}".replace("/index.html", "/")
    canonical = url_en if idioma == "en" else url_es
    lang = "en" if idioma == "en" else "es-PR"
    og_locale = "en_US" if idioma == "en" else "es_PR"

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="es-pr" href="{url_es}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="x-default" href="{url_es}">

<meta property="og:type" content="website">
<meta property="og:locale" content="{og_locale}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMINIO}/assets/logo/logo-512.png">
<meta name="theme-color" content="#6B2F15">

<link rel="icon" href="{p}favicon.ico" sizes="any">
<link rel="icon" href="{p}assets/logo/isotipo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="manifest" href="{p}site.webmanifest">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Caveat:wght@600&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{p}assets/css/styles.css">
<script>document.documentElement.classList.add('js')</script>
{jsonld}</head>
<body>

<a class="saltar" href="#principal">{T["saltar"][idioma]}</a>

{SPRITE}
'''


def cabecera(idioma, activa):
    p = "../" if idioma == "en" else ""
    i = 0 if idioma == "es" else 1
    otro = 1 - i
    otro_idioma = "en" if idioma == "es" else "es"

    def ruta(clave, lang_idx):
        archivo = PAGINAS[clave][lang_idx]
        if lang_idx == i:
            return p + archivo if idioma == "es" else archivo.replace("en/", "")
        # enlace al otro idioma
        return ("" if idioma == "en" else "") + (
            archivo if idioma == "es" else "../" + archivo)

    enlaces = ""
    for clave, etiqueta in NAV[idioma]:
        href = PAGINAS[clave][i]
        if idioma == "en":
            href = href.replace("en/", "")
        actual = ' aria-current="page"' if clave == activa else ""
        enlaces += f'        <li><a href="{href}"{actual}>{etiqueta}</a></li>\n'

    href_otro = PAGINAS[activa][otro]
    href_otro = href_otro if idioma == "es" else "../" + href_otro
    href_este = PAGINAS[activa][i]
    href_este = href_este.replace("en/", "") if idioma == "en" else href_este

    es_link = href_este if idioma == "es" else href_otro
    en_link = href_otro if idioma == "es" else href_este

    return f'''<header class="header">
  <div class="contenedor header__fila">
    <a class="marca" href="{PAGINAS["home"][i].replace("en/", "") if idioma == "en" else "index.html"}" aria-label="{T["inicio_aria"][idioma]}">
      <img src="{p}assets/logo/isotipo.svg" alt="" width="44" height="44">
      <span class="marca__texto">
        <span class="marca__apodo">"El Tipo"</span>
        <span class="marca__nombre">Perfect <span>Solution</span></span>
      </span>
    </a>

    <button class="hamburguesa" type="button" aria-expanded="false" aria-controls="menu" aria-label="{T["abrir_menu"][idioma]}">
      <span></span>
    </button>

    <nav class="nav" id="menu" aria-label="{T["principal"][idioma]}">
      <ul>
{enlaces}      </ul>
    </nav>

    <div class="header__acciones">
      <a class="tel-header" href="tel:{TEL_LINK}">
        {icono("tel")}
        <span>{TEL_HUMANO}</span>
      </a>
      <div class="idioma">
        <a href="{es_link}"{' aria-current="true"' if idioma == "es" else ""} hreflang="es">ES</a>
        <a href="{en_link}"{' aria-current="true"' if idioma == "en" else ""} hreflang="en">EN</a>
      </div>
    </div>
  </div>
</header>

<main id="principal">
'''


def cta_cierre(idioma):
    return f'''
  <section class="seccion cta-cierre">
    <div class="contenedor">
      <h2>{T["cta_titulo"][idioma]}</h2>
      <p>{T["cta_texto"][idioma]}</p>
      <div class="grupo-btn">
        <a class="btn btn--claro" href="tel:{TEL_LINK}">
          {icono("tel")}
          {TEL_HUMANO}
        </a>
        <a class="btn btn--wa" href="{wa_url(idioma)}" target="_blank" rel="noopener">
          {icono("wa")}
          WhatsApp
        </a>
      </div>
      <p class="firma">{T["firma"][idioma]}</p>
    </div>
  </section>
'''


def pie(idioma):
    p = "../" if idioma == "en" else ""
    i = 0 if idioma == "es" else 1

    nav_items = ""
    for clave, etiqueta in NAV[idioma]:
        href = PAGINAS[clave][i]
        if idioma == "en":
            href = href.replace("en/", "")
        nav_items += f'          <li><a href="{href}">{etiqueta}</a></li>\n'

    serv_pagina = PAGINAS["servicios"][i]
    if idioma == "en":
        serv_pagina = serv_pagina.replace("en/", "")
    serv_items = ""
    for ancla, etiqueta in SERVICIOS_FOOTER[idioma]:
        serv_items += f'          <li><a href="{serv_pagina}#{ancla}">{etiqueta}</a></li>\n'

    return f'''</main>

<footer class="footer">
  <div class="contenedor">
    <div class="footer__rejilla">
      <div>
        <img class="footer__logo" src="{p}assets/logo/logo-light.svg" alt="Perfect Solution by Michaell J. Rivera" width="190" height="244">
        <p style="font-size:.94rem">{T["footer_desc"][idioma]}</p>
      </div>

      <div>
        <h3>{T["nav_footer"][idioma]}</h3>
        <ul>
{nav_items}        </ul>
      </div>

      <div>
        <h3>{T["serv_footer"][idioma]}</h3>
        <ul>
{serv_items}        </ul>
      </div>

      <div>
        <h3>{T["cont_footer"][idioma]}</h3>
        <ul>
          <li><a href="tel:{TEL_LINK}">{TEL_HUMANO}</a></li>
          <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="{IG_URL}" target="_blank" rel="noopener">Instagram @{IG_USUARIO}</a></li>
          <li>{T["area"][idioma]}</li>
        </ul>
      </div>
    </div>

    <div class="footer__pie">
      <p>© <span data-anio>2026</span> Perfect Solution by Michaell J. Rivera.</p>
      <p>{T["hecho"][idioma]}</p>
    </div>
  </div>
</footer>

<a class="wa-flotante" href="{wa_url(idioma)}" target="_blank" rel="noopener" aria-label="{T["wa_aria"][idioma]}">
  {icono("wa")}
</a>

<div class="barra-movil">
  <a href="tel:{TEL_LINK}">{icono("tel")} {T["llamar"][idioma]}</a>
  <a href="{wa_url(idioma)}" target="_blank" rel="noopener">{icono("wa")} WhatsApp</a>
</div>

<script src="{p}assets/js/main.js" defer></script>
</body>
</html>
'''


def cabecera_pagina(idioma, activa, titulo, bajada):
    i = 0 if idioma == "es" else 1
    home = "index.html"
    inicio = "Inicio" if idioma == "es" else "Home"
    actual = dict(NAV[idioma])[activa]
    return f'''
  <section class="cabecera-pagina">
    <div class="contenedor">
      <p class="miga"><a href="{home}">{inicio}</a> / {actual}</p>
      <h1>{titulo}</h1>
      <p>{bajada}</p>
    </div>
  </section>
'''


def pueblos_html(idioma, centrado=True):
    lis = "".join(f"<li>{x}</li>" for x in PUEBLOS)
    estilo = ' style="justify-content:center"' if centrado else ""
    return f'<ul class="pueblos revelar"{estilo}>{lis}</ul>'


def imagen(base, alt, prefijo, ancho=1200, alto=900, prioridad=False):
    """Devuelve el <img> de una foto.

    Si existen el .webp y el .jpg (los que produce fotos.py) usa <picture> para
    servir WebP con JPG de respaldo. Si solo hay un .svg, es todavia un
    marcador de posicion y se emite un <img> normal. Asi el mismo generador
    sirve antes y despues de tener las fotos reales, sin tocar el HTML.
    """
    carpeta = os.path.join(RAIZ, "assets", "img")
    carga = ' fetchpriority="high"' if prioridad else ' loading="lazy"'
    tag = (f'<img src="{prefijo}assets/img/{base}.%s" alt="{alt}" '
           f'width="{ancho}" height="{alto}"{carga}>')

    if (os.path.exists(os.path.join(carpeta, base + ".webp"))
            and os.path.exists(os.path.join(carpeta, base + ".jpg"))):
        return ('<picture>'
                f'<source srcset="{prefijo}assets/img/{base}.webp" type="image/webp">'
                + (tag % "jpg") + '</picture>')
    if os.path.exists(os.path.join(carpeta, base + ".jpg")):
        return tag % "jpg"
    return tag % "svg"


def tarjeta(ico, titulo, texto):
    return f'''        <article class="tarjeta revelar">
          <div class="tarjeta__icono">{icono(ico)}</div>
          <h3>{titulo}</h3>
          <p>{texto}</p>
        </article>
'''


def comparador(n, antes, despues, p, clases=""):
    """Slider antes/despues del par n. Las dos fotos deben estar tomadas
    desde el mismo angulo o el efecto no funciona.

    El "despues" va de fondo y el "antes" es la capa recortada por la
    izquierda: asi el orden en pantalla es antes -> despues, que es como se
    lee, y coincide con las etiquetas de cada lado."""
    cls = f" {clases}" if clases else ""
    return f'''<div class="comparador{cls}">
          {imagen(f"despues-{n}", despues, p)}
          <div class="comparador__frente">
            {imagen(f"antes-{n}", antes, p)}
          </div>
          <div class="comparador__tirador" aria-hidden="true"></div>
          <span class="comparador__etiqueta comparador__etiqueta--a">{antes}</span>
          <span class="comparador__etiqueta comparador__etiqueta--b">{despues}</span>
          <input type="range" min="0" max="100" value="50" aria-label="{antes} / {despues}">
        </div>'''


def escribir(ruta_rel, contenido):
    destino = os.path.join(RAIZ, ruta_rel)
    carpeta = os.path.dirname(destino)
    if carpeta:
        os.makedirs(carpeta, exist_ok=True)
    with io.open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(contenido)
    print(f"  {ruta_rel}  ({len(contenido)/1024:.1f} KB)")


# ===========================================================================
#  CONTENIDO
# ===========================================================================
JSONLD_HOME = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HomeAndConstructionBusiness",
  "name": "Perfect Solution",
  "alternateName": "Perfect Solution by Michaell J. Rivera",
  "description": "Contratista general: plomeria, pintura, reparaciones generales y remodelacion de banos y cocinas en Puerto Rico.",
  "image": "%(d)s/assets/logo/logo-512.png",
  "logo": "%(d)s/assets/logo/logo.svg",
  "url": "%(d)s/",
  "telephone": "+1-939-219-0979",
  "email": "%(e)s",
  "priceRange": "$$",
  "sameAs": [ "%(ig)s" ],
  "founder": { "@type": "Person", "name": "Michaell J. Rivera" },
  "address": { "@type": "PostalAddress", "addressRegion": "PR", "addressCountry": "US" },
  "areaServed": [
    { "@type": "AdministrativeArea", "name": "Area Metropolitana de San Juan, Puerto Rico" },
    { "@type": "AdministrativeArea", "name": "Region Sur de Puerto Rico" }
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios",
    "itemListElement": [
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Plomeria" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Pintura interior y exterior" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Reparaciones generales" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Remodelacion de banos" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Remodelacion de cocinas" } },
      { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Impermeabilizacion y sellado de techos" } }
    ]
  }
}
</script>
''' % {"d": DOMINIO, "e": EMAIL, "ig": IG_URL}

META = {
    "home": {
        "es": ("Perfect Solution | Contratista general, plomería y remodelación en Puerto Rico",
               "Contratista general en el Área Metro y Sur de Puerto Rico. Plomería, pintura, "
               "reparaciones generales y remodelación completa de baños y cocinas. Presupuesto "
               "sin costo. WhatsApp 939-219-0979."),
        "en": ("Perfect Solution | General Contractor, Plumbing & Remodeling in Puerto Rico",
               "General contractor serving the San Juan metro area and southern Puerto Rico. "
               "Plumbing, painting, general repairs and full bathroom and kitchen remodeling. "
               "Free estimates. WhatsApp 939-219-0979."),
    },
    "servicios": {
        "es": ("Servicios | Perfect Solution — plomería, pintura, reparaciones y remodelación",
               "Plomería, pintura interior y exterior, reparaciones generales, remodelación de "
               "baños y cocinas, impermeabilización de techos. Área Metro y Sur de Puerto Rico."),
        "en": ("Services | Perfect Solution — plumbing, painting, repairs and remodeling",
               "Plumbing, interior and exterior painting, general repairs, bathroom and kitchen "
               "remodeling, roof sealing. San Juan metro area and southern Puerto Rico."),
    },
    "proyectos": {
        "es": ("Proyectos | Perfect Solution — trabajos antes y después",
               "Galería de trabajos terminados: remodelación de baños y cocinas, pintura, "
               "reparaciones e impermeabilización en Puerto Rico."),
        "en": ("Projects | Perfect Solution — before and after",
               "Gallery of finished work: bathroom and kitchen remodels, painting, repairs and "
               "roof sealing in Puerto Rico."),
    },
    "nosotros": {
        "es": ("Nosotros | Perfect Solution by Michaell J. Rivera",
               "Perfect Solution es Michaell J. Rivera, \"El Tipo\": contratista general en el "
               "Área Metro y Sur de Puerto Rico. Trabajo directo, sin intermediarios."),
        "en": ("About | Perfect Solution by Michaell J. Rivera",
               "Perfect Solution is Michaell J. Rivera, \"El Tipo\": a general contractor "
               "serving metro and southern Puerto Rico. You deal with him directly."),
    },
    "contacto": {
        "es": ("Contacto | Perfect Solution — presupuesto sin costo",
               "Pide tu presupuesto sin costo. WhatsApp o llamada al 939-219-0979. "
               "Área Metro y Sur de Puerto Rico."),
        "en": ("Contact | Perfect Solution — free estimate",
               "Request your free estimate. WhatsApp or call 939-219-0979. "
               "San Juan metro area and southern Puerto Rico."),
    },
}


# --- HOME ------------------------------------------------------------------
def home(idioma):
    es = idioma == "es"
    p = "../" if not es else ""
    proyectos = PAGINAS["proyectos"][0 if es else 1].replace("en/", "")
    servicios = PAGINAS["servicios"][0 if es else 1].replace("en/", "")
    contacto = PAGINAS["contacto"][0 if es else 1].replace("en/", "")

    if es:
        h1 = 'Lo arreglamos. Lo remodelamos. <em>Lo dejamos perfecto.</em>'
        bajada = ("Plomería, pintura, reparaciones generales y remodelación completa de baños y "
                  "cocinas en el Área Metro y Sur de Puerto Rico. Un solo contratista de principio a fin.")
        sellos = ["Presupuesto sin costo", "Cotización por escrito", "Área Metro y Sur"]
        conf = [("doc", "Cotización clara y por escrito"),
                ("llave", "Desde una fuga hasta un baño completo"),
                ("reloj", "Te contesta Michaell, no una máquina"),
                ("escudo", "Entregamos el área limpia")]
        serv_ante, serv_h2 = "Lo que hacemos", "Un solo contratista para toda la casa"
        serv_p = ("No hay que llamar a cinco personas distintas. Nos encargamos del trabajo "
                  "pequeño que nadie quiere hacer y también del proyecto completo.")
        servicios_lista = [
            ("gota", "Plomería", "Fugas de agua, destapes, calentadores, cambio de piezas y llaves, instalación de inodoros y lavamanos."),
            ("brocha", "Pintura", "Interior y exterior. Preparación de superficie, sellado de grietas, masilla y acabado parejo."),
            ("llave", "Reparaciones generales", "Puertas que no cierran, closets, gabinetes, molduras, drywall roto. Eso que llevas meses posponiendo."),
            ("bano", "Remodelación de baños", "Demolición, plomería, losa, vanity, ducha y pintura. Coordinado de principio a fin."),
            ("cocina", "Remodelación de cocinas", "Gabinetes, tope, salpicadero, pisos y acabados. Te entregamos la cocina lista para usar."),
            ("techo", "Impermeabilización", "Sellado de techos y control de filtraciones, que en Puerto Rico es medio trabajo de toda casa."),
        ]
        ver_todos = "Ver todos los servicios"
        rem_ante, rem_h2 = "Remodelación", "Tu baño o tu cocina, completos"
        rem_p = ("Demolición, plomería, losa, gabinetes, pintura y acabados. Todo con el mismo "
                 "contratista, así que tú no tienes que coordinar a nadie ni perseguir a cuatro "
                 "personas para que aparezcan el mismo día.")
        rem_lista = ["Visita y evaluación sin costo", "Cotización por escrito antes de empezar",
                     "Un solo interlocutor durante toda la obra", "Área limpia al terminar cada jornada"]
        rem_btn = "Pedir cotización"
        rem_alt = "Baño remodelado por Perfect Solution"
        tra_ante, tra_h2 = "Trabajos", "Antes y después"
        tra_p = "La mejor forma de explicar lo que hacemos es enseñarlo."
        comp_h3 = "Arrastra para comparar"
        comp_p = ("Cada proyecto empieza con una casa que tenía un problema y termina con un "
                  "espacio que la familia vuelve a usar. Esa es la parte del trabajo que nos gusta.")
        comp_btn = "Ver la galería completa"
        antes, despues = "Antes", "Después"
        cap = ["Remodelación de baño", "Pintura exterior", "Cocina completa"]
        proc_ante, proc_h2 = "Cómo trabajamos", "Cuatro pasos, sin sorpresas"
        pasos = [
            ("Nos escribes", "Cuéntanos qué necesitas por WhatsApp. Si tienes fotos, mándalas — adelantan mucho."),
            ("Visitamos y evaluamos", "Vamos a verlo en persona, sin cargo. Nadie cotiza bien una obra por teléfono."),
            ("Cotización por escrito", "Precio claro con lo que incluye y lo que no. Sin cambios a mitad del trabajo."),
            ("Ejecutamos y entregamos", "Trabajamos con la fecha acordada y te devolvemos el área limpia y lista para usar."),
        ]
        area_ante, area_h2 = "Dónde trabajamos", "Área Metro y Sur de Puerto Rico"
        area_p = "Si tu pueblo no aparece en la lista, escríbenos igual y te decimos si llegamos."
        ver_trabajos = "Ver trabajos"
    else:
        h1 = 'We fix it. We remodel it. <em>We leave it perfect.</em>'
        bajada = ("Plumbing, painting, general repairs and full bathroom and kitchen remodels "
                  "across metro and southern Puerto Rico. One contractor from start to finish.")
        sellos = ["Free estimates", "Written quote", "Metro & South PR"]
        conf = [("doc", "A clear, written quote"),
                ("llave", "From a leak to a full bathroom"),
                ("reloj", "Michaell answers, not a machine"),
                ("escudo", "We leave the area clean")]
        serv_ante, serv_h2 = "What we do", "One contractor for the whole house"
        serv_p = ("No need to call five different people. We handle the small job nobody wants "
                  "to take, and the full project too.")
        servicios_lista = [
            ("gota", "Plumbing", "Leaks, clogged drains, water heaters, fixture and faucet replacement, toilet and sink installs."),
            ("brocha", "Painting", "Interior and exterior. Surface prep, crack sealing, patching and an even finish."),
            ("llave", "General repairs", "Doors that won't close, closets, cabinets, trim, damaged drywall. The stuff you keep putting off."),
            ("bano", "Bathroom remodels", "Demo, plumbing, tile, vanity, shower and paint. Coordinated end to end."),
            ("cocina", "Kitchen remodels", "Cabinets, countertops, backsplash, flooring and finishes. Handed over ready to use."),
            ("techo", "Roof sealing", "Roof waterproofing and leak control — half the work on any house in Puerto Rico."),
        ]
        ver_todos = "See all services"
        rem_ante, rem_h2 = "Remodeling", "Your bathroom or kitchen, done right"
        rem_p = ("Demo, plumbing, tile, cabinets, paint and finishes. All with the same "
                 "contractor, so you don't have to coordinate anyone or chase four people to "
                 "show up on the same day.")
        rem_lista = ["Free visit and assessment", "Written quote before we start",
                     "One point of contact for the whole job", "Clean area at the end of every day"]
        rem_btn = "Request a quote"
        rem_alt = "Bathroom remodeled by Perfect Solution"
        tra_ante, tra_h2 = "Our work", "Before and after"
        tra_p = "The best way to explain what we do is to show it."
        comp_h3 = "Drag to compare"
        comp_p = ("Every project starts with a house that had a problem and ends with a space "
                  "the family uses again. That's the part of the job we like.")
        comp_btn = "See the full gallery"
        antes, despues = "Before", "After"
        cap = ["Bathroom remodel", "Exterior painting", "Full kitchen"]
        proc_ante, proc_h2 = "How we work", "Four steps, no surprises"
        pasos = [
            ("You message us", "Tell us what you need on WhatsApp. Send photos if you have them — they help a lot."),
            ("We visit and assess", "We come see it in person, at no charge. Nobody quotes a job properly over the phone."),
            ("Written quote", "A clear price with what's included and what isn't. No changes halfway through."),
            ("We build and hand over", "We work to the agreed date and give the area back clean and ready to use."),
        ]
        area_ante, area_h2 = "Where we work", "Metro and southern Puerto Rico"
        area_p = "If your town isn't on the list, message us anyway and we'll tell you if we get there."
        ver_trabajos = "See our work"

    sellos_html = "".join(f'        <li>{icono("check")} {s}</li>\n' for s in sellos)
    conf_html = "".join(f'        <li>{icono(i)} {t}</li>\n' for i, t in conf)
    serv_html = "".join(tarjeta(i, t, d) for i, t, d in servicios_lista)
    rem_lista_html = "".join(f"          <li>{x}</li>\n" for x in rem_lista)
    pasos_html = "".join(
        f'        <li class="revelar">\n          <h3>{t}</h3>\n          <p>{d}</p>\n        </li>\n'
        for t, d in pasos)
    galeria_html = "".join(
        f'        <figure class="revelar">{imagen(f"trabajo-{n}", c, p)}'
        f'<figcaption>{c}</figcaption></figure>\n'
        for n, c in enumerate(cap, start=1))

    return head(idioma, "home", *META["home"][idioma], jsonld=JSONLD_HOME) \
        + cabecera(idioma, "home") + f'''
  <section class="hero">
    <div class="hero__fondo">
      {imagen("hero", "", p, 1600, 900, prioridad=True)}
    </div>
    <div class="contenedor">
     <div class="hero__contenido">
      <p class="hero__apodo">"El Tipo"</p>
      <h1>{h1}</h1>
      <p class="hero__bajada">{bajada}</p>
      <div class="grupo-btn">
        <a class="btn btn--wa" href="{wa_url(idioma)}" target="_blank" rel="noopener">
          {icono("wa")}
          {T["wa_boton"][idioma]}
        </a>
        <a class="btn btn--fantasma-claro" href="{proyectos}">{ver_trabajos}</a>
      </div>
      <ul class="hero__sellos">
{sellos_html}      </ul>
     </div>
    </div>
  </section>

  <section class="confianza">
    <div class="contenedor">
      <ul>
{conf_html}      </ul>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <p class="antetitulo">{serv_ante}</p>
        <h2>{serv_h2}</h2>
        <p>{serv_p}</p>
      </div>

      <div class="rejilla rejilla--3">
{serv_html}      </div>

      <div class="grupo-btn revelar" style="margin-top:40px;justify-content:center">
        <a class="btn btn--secundario" href="{servicios}">
          {ver_todos}
          {icono("flecha")}
        </a>
      </div>
    </div>
  </section>

  <section class="seccion seccion--alt">
    <div class="contenedor dos-col">
      <div class="revelar">
        <p class="antetitulo">{rem_ante}</p>
        <h2>{rem_h2}</h2>
        <p>{rem_p}</p>
        <ul class="lista-marcas">
{rem_lista_html}        </ul>
        <div class="grupo-btn" style="margin-top:32px">
          <a class="btn btn--primario" href="{contacto}">{rem_btn}</a>
        </div>
      </div>
      <div class="dos-col__media revelar">
        {imagen("remodelacion", rem_alt, p)}
      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <p class="antetitulo">{tra_ante}</p>
        <h2>{tra_h2}</h2>
        <p>{tra_p}</p>
      </div>

      <div class="dos-col revelar" style="margin-bottom:48px">
        {comparador(1, antes, despues, p)}
        <div>
          <h3>{comp_h3}</h3>
          <p>{comp_p}</p>
          <div class="grupo-btn" style="margin-top:24px">
            <a class="btn btn--secundario" href="{proyectos}">
              {comp_btn}
              {icono("flecha")}
            </a>
          </div>
        </div>
      </div>

      <div class="galeria">
{galeria_html}      </div>
    </div>
  </section>

  <section class="seccion seccion--marron">
    <div class="contenedor">
      <div class="encabezado-seccion revelar">
        <p class="antetitulo">{proc_ante}</p>
        <h2>{proc_h2}</h2>
      </div>
      <ol class="pasos">
{pasos_html}      </ol>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <p class="antetitulo">{area_ante}</p>
        <h2>{area_h2}</h2>
        <p>{area_p}</p>
      </div>
      {pueblos_html(idioma)}
    </div>
  </section>
''' + cta_cierre(idioma) + pie(idioma)


# --- SERVICIOS -------------------------------------------------------------
GRUPOS_SERVICIOS = {
    "es": [
        ("plomeria", "gota", "Plomería", "serv-plomeria",
         "Lo que más nos llaman a resolver, y casi siempre corriendo. Atendemos la "
         "avería y también la causa, para que no vuelva en tres meses.",
         ["Detección y reparación de fugas", "Destape de desagües y tuberías",
          "Calentadores: instalación y reemplazo", "Llaves, mezcladoras y piezas de baño",
          "Instalación de inodoros, lavamanos y fregaderos", "Cambio de tubería dañada"]),
        ("pintura", "brocha", "Pintura", "serv-pintura",
         "El acabado se nota, pero lo que dura es la preparación. Sellamos, resanamos "
         "y damos las manos que haga falta.",
         ["Pintura interior completa", "Pintura exterior y fachadas",
          "Sellado de grietas y resane", "Masilla y nivelación de paredes",
          "Puertas, marcos y molduras", "Pintura de techos y aleros"]),
        ("reparaciones", "llave", "Reparaciones generales", "serv-reparaciones",
         "El trabajo pequeño que nadie quiere tomar. Si lleva meses en tu lista, "
         "probablemente es de los nuestros.",
         ["Puertas que no cierran o rozan", "Closets, gabinetes y estantes",
          "Drywall roto y plafón", "Molduras y zócalos",
          "Instalación de abanicos de techo y accesorios", "Ajustes y mantenimiento general"]),
        ("remodelacion", "bano", "Remodelación", "serv-remodelacion",
         "Baños y cocinas completos, coordinados por una sola persona. Tú decides el "
         "acabado; nosotros nos encargamos del orden de los trabajos.",
         ["Remodelación completa de baños", "Remodelación completa de cocinas",
          "Losa, azulejo y pisos", "Gabinetes, topes y salpicadero",
          "Drywall, plafón y molduras", "Closets y espacios de almacenaje"]),
        ("exterior", "techo", "Techos y exterior", "serv-exterior",
         "En Puerto Rico el techo y el exterior son la mitad del mantenimiento de "
         "cualquier casa. Mejor atenderlo antes de la temporada de lluvia.",
         ["Impermeabilización y sellado de techos", "Control de filtraciones",
          "Ventanas y puertas", "Verjas, portones y terrazas",
          "Ampliaciones y cuartos anexos", "Mantenimiento de fachada"]),
    ],
    "en": [
        ("plomeria", "gota", "Plumbing", "serv-plomeria",
         "What we get called for most, and usually in a hurry. We fix the failure and "
         "the cause behind it, so it doesn't come back in three months.",
         ["Leak detection and repair", "Drain and pipe unclogging",
          "Water heaters: install and replace", "Faucets, mixers and bathroom fixtures",
          "Toilet, sink and basin installation", "Damaged pipe replacement"]),
        ("pintura", "brocha", "Painting", "serv-pintura",
         "The finish is what you see, but prep is what lasts. We seal, patch and put on "
         "as many coats as the job needs.",
         ["Full interior painting", "Exterior and façade painting",
          "Crack sealing and patching", "Skim coating and wall levelling",
          "Doors, frames and trim", "Ceilings and eaves"]),
        ("reparaciones", "llave", "General repairs", "serv-reparaciones",
         "The small job nobody wants to take. If it's been on your list for months, "
         "it's probably one of ours.",
         ["Doors that stick or won't close", "Closets, cabinets and shelving",
          "Damaged drywall and ceilings", "Trim and baseboards",
          "Ceiling fans and fixture installs", "General adjustments and upkeep"]),
        ("remodelacion", "bano", "Remodeling", "serv-remodelacion",
         "Full bathrooms and kitchens, coordinated by one person. You pick the finishes; "
         "we handle the order the trades come in.",
         ["Full bathroom remodels", "Full kitchen remodels",
          "Tile and flooring", "Cabinets, countertops and backsplash",
          "Drywall, ceilings and trim", "Closets and storage"]),
        ("exterior", "techo", "Roofing & exterior", "serv-exterior",
         "In Puerto Rico the roof and exterior are half the upkeep of any house. Better "
         "handled before the rainy season, not during it.",
         ["Roof waterproofing and sealing", "Leak control",
          "Windows and doors", "Fences, gates and terraces",
          "Additions and extra rooms", "Façade maintenance"]),
    ],
}


def servicios(idioma):
    es = idioma == "es"
    p = "" if es else "../"
    contacto = PAGINAS["contacto"][0 if es else 1].replace("en/", "")

    titulo = "Servicios" if es else "Services"
    bajada = ("Desde una fuga a las once de la noche hasta un baño completo. "
              "Esto es todo lo que resolvemos." if es else
              "From a leak at eleven at night to a full bathroom. "
              "Here's everything we take on.")
    pedir = "Pedir cotización" if es else "Request a quote"
    nota_t = "¿No ves lo que necesitas?" if es else "Don't see what you need?"
    nota_p = ("Escríbenos igual. Si es trabajo de construcción o mantenimiento de casa, "
              "lo más probable es que lo hagamos o que sepamos quién lo hace bien."
              if es else
              "Message us anyway. If it's construction or home maintenance, chances are "
              "we do it — or we know who does it well.")

    bloques = ""
    for n, (ancla, ico, nombre, img, desc, items) in enumerate(GRUPOS_SERVICIOS[idioma]):
        alt = " seccion--alt" if n % 2 else ""
        inv = " dos-col--inverso" if n % 2 else ""
        lista = "".join(f"            <li>{x}</li>\n" for x in items)
        bloques += f'''
  <section class="seccion{alt}" id="{ancla}">
    <div class="contenedor dos-col{inv}">
      <div class="revelar">
        <div class="tarjeta__icono">{icono(ico)}</div>
        <h2>{nombre}</h2>
        <p>{desc}</p>
        <ul class="lista-marcas">
{lista}        </ul>
        <div class="grupo-btn" style="margin-top:30px">
          <a class="btn btn--primario" href="{contacto}">{pedir}</a>
        </div>
      </div>
      <div class="dos-col__media revelar">
        {imagen(img, nombre, p)}
      </div>
    </div>
  </section>
'''

    return head(idioma, "servicios", *META["servicios"][idioma]) \
        + cabecera(idioma, "servicios") \
        + cabecera_pagina(idioma, "servicios", titulo, bajada) \
        + bloques + f'''
  <section class="seccion seccion--alt">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar" style="margin-bottom:0">
        <h2>{nota_t}</h2>
        <p>{nota_p}</p>
      </div>
    </div>
  </section>
''' + cta_cierre(idioma) + pie(idioma)


# --- PROYECTOS -------------------------------------------------------------
def proyectos(idioma):
    es = idioma == "es"
    p = "" if es else "../"

    if es:
        titulo = "Proyectos"
        bajada = ("Trabajos terminados en el Área Metro y Sur. Baños, cocinas, pintura, "
                  "techos y reparaciones.")
        antes, despues = "Antes", "Después"
        h2_comp = "Antes y después"
        p_comp = "Arrastra el control para ver el cambio."
        caps = ["Remodelación de baño", "Pintura exterior", "Cocina completa",
                "Sellado de techo", "Reparación de drywall", "Instalación de piso"]
        h2_gal = "Galería de trabajos"
        p_gal = "Cada foto es un trabajo real entregado a una familia del área."
    else:
        titulo = "Projects"
        bajada = ("Finished work across metro and southern Puerto Rico. Bathrooms, kitchens, "
                  "painting, roofs and repairs.")
        antes, despues = "Before", "After"
        h2_comp = "Before and after"
        p_comp = "Drag the handle to see the change."
        caps = ["Bathroom remodel", "Exterior painting", "Full kitchen",
                "Roof sealing", "Drywall repair", "Floor installation"]
        h2_gal = "Work gallery"
        p_gal = "Every photo is a real job handed over to a family in the area."

    comparadores = "".join(
        f'        {comparador(n, antes, despues, p, "revelar")}\n' for n in (1, 2))

    galeria = "".join(
        f'        <figure class="revelar">{imagen(f"trabajo-{n}", c, p)}'
        f'<figcaption>{c}</figcaption></figure>\n'
        for n, c in enumerate(caps, start=1))

    return head(idioma, "proyectos", *META["proyectos"][idioma]) \
        + cabecera(idioma, "proyectos") \
        + cabecera_pagina(idioma, "proyectos", titulo, bajada) + f'''
  <section class="seccion">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <h2>{h2_comp}</h2>
        <p>{p_comp}</p>
      </div>
      <div class="rejilla rejilla--2">
{comparadores}      </div>
    </div>
  </section>

  <section class="seccion seccion--alt">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <h2>{h2_gal}</h2>
        <p>{p_gal}</p>
      </div>
      <div class="galeria">
{galeria}      </div>
    </div>
  </section>
''' + cta_cierre(idioma) + pie(idioma)


# --- NOSOTROS --------------------------------------------------------------
def nosotros(idioma):
    es = idioma == "es"
    p = "" if es else "../"
    contacto = PAGINAS["contacto"][0 if es else 1].replace("en/", "")

    if es:
        titulo = "Nosotros"
        bajada = 'Perfect Solution es Michaell J. Rivera. La gente le dice "El Tipo".'
        h2 = "El que cotiza es el que trabaja"
        parrafos = [
            "Perfect Solution nació de algo sencillo: mucha gente tiene un problema en su "
            "casa y no consigue a nadie que llegue, cotice claro y termine lo que empezó.",
            "Llevamos dos años trabajando en el Área Metro y Sur, y en ese tiempo el negocio "
            "creció de reparaciones sueltas a remodelaciones completas de baños y cocinas. "
            "Lo que no ha cambiado es cómo trabajamos: quien va a tu casa a cotizar es quien "
            "va a hacer el trabajo.",
            "No somos una compañía grande con centro de llamadas. Somos el contratista que "
            "contesta el teléfono, llega el día que dijo y te devuelve el área limpia.",
        ]
        h2_val = "Lo que puedes esperar"
        valores = [
            ("doc", "Cotización por escrito",
             "Antes de mover un dedo sabes el precio, qué incluye y qué no. Sin cambios "
             "sorpresa a mitad de obra."),
            ("reloj", "Te contestamos",
             "Si escribes por WhatsApp, te responde una persona. Si acordamos una fecha, "
             "esa es la fecha."),
            ("llave", "Un solo interlocutor",
             "No tienes que coordinar plomero, pintor y albañil por separado. Lo coordinamos "
             "nosotros."),
            ("escudo", "Entregamos limpio",
             "El trabajo no termina cuando se instala la última pieza, sino cuando puedes "
             "usar el espacio."),
        ]
        h2_area = "Dónde trabajamos"
        p_area = "Cubrimos el Área Metro y la región Sur. Si tu pueblo no está, pregúntanos."
        cita = '"Si te digo que llego, llego."'
        autor = "— Michaell J. Rivera"
        btn = "Hablemos de tu proyecto"
        alt_foto = "Obra de Perfect Solution en proceso"
    else:
        titulo = "About"
        bajada = 'Perfect Solution is Michaell J. Rivera. People call him "El Tipo".'
        h2 = "The person who quotes is the person who works"
        parrafos = [
            "Perfect Solution started from something simple: plenty of people have a problem "
            "at home and can't find anyone who shows up, quotes clearly and finishes what "
            "they started.",
            "We've been working across metro and southern Puerto Rico for two years, and in "
            "that time the business grew from one-off repairs into full bathroom and kitchen "
            "remodels. What hasn't changed is how we work: whoever comes to your house to "
            "quote is the one who does the job.",
            "We're not a big company with a call center. We're the contractor who answers the "
            "phone, shows up on the day he said, and gives the area back clean.",
        ]
        h2_val = "What you can expect"
        valores = [
            ("doc", "A written quote",
             "Before anything moves you know the price, what's included and what isn't. "
             "No surprise changes halfway through."),
            ("reloj", "We answer",
             "Message us on WhatsApp and a person replies. If we agree on a date, that's "
             "the date."),
            ("llave", "One point of contact",
             "You don't have to coordinate a plumber, a painter and a mason separately. "
             "We do that."),
            ("escudo", "We hand it over clean",
             "The job isn't done when the last fixture goes in — it's done when you can "
             "use the space."),
        ]
        h2_area = "Where we work"
        p_area = "We cover the San Juan metro area and the south. If your town isn't listed, just ask."
        cita = '"If I say I&rsquo;ll be there, I&rsquo;ll be there."'
        autor = "— Michaell J. Rivera"
        btn = "Let's talk about your project"
        alt_foto = "A Perfect Solution job in progress"

    parr = "".join(f"        <p>{x}</p>\n" for x in parrafos)
    vals = "".join(tarjeta(i, t, d) for i, t, d in valores)

    return head(idioma, "nosotros", *META["nosotros"][idioma]) \
        + cabecera(idioma, "nosotros") \
        + cabecera_pagina(idioma, "nosotros", titulo, bajada) + f'''
  <section class="seccion">
    <div class="contenedor dos-col">
      <div class="revelar">
        <h2>{h2}</h2>
{parr}        <p class="firma" style="margin-top:24px">{cita}<br>{autor}</p>
        <div class="grupo-btn" style="margin-top:30px">
          <a class="btn btn--primario" href="{contacto}">{btn}</a>
        </div>
      </div>
      <div class="dos-col__media revelar">
        {imagen("equipo", alt_foto, p)}
      </div>
    </div>
  </section>

  <section class="seccion seccion--alt">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <h2>{h2_val}</h2>
      </div>
      <div class="rejilla rejilla--4">
{vals}      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <h2>{h2_area}</h2>
        <p>{p_area}</p>
      </div>
      {pueblos_html(idioma)}
    </div>
  </section>
''' + cta_cierre(idioma) + pie(idioma)


# --- CONTACTO --------------------------------------------------------------
def contacto(idioma):
    es = idioma == "es"

    if es:
        titulo = "Contacto"
        bajada = ("Cuéntanos qué necesitas y coordinamos la visita. "
                  "El presupuesto no te cuesta nada.")
        h2_form = "Pide tu cotización"
        p_form = ("Llena esto y se abre WhatsApp con tu mensaje ya escrito. "
                  "También puedes escribirnos directo o llamar.")
        etiquetas = {
            "saludo": "Hola Michaell, le escribo desde la página web.",
            "nombre": "Nombre", "telefono": "Teléfono", "pueblo": "Pueblo",
            "servicio": "Servicio", "mensaje": "Detalles",
        }
        campos = {
            "nombre": "Nombre", "telefono": "Teléfono", "pueblo": "Pueblo",
            "servicio": "¿Qué necesitas?", "mensaje": "Cuéntanos los detalles",
        }
        opciones = ["Plomería", "Pintura", "Reparaciones generales",
                    "Remodelación de baño", "Remodelación de cocina",
                    "Techo e impermeabilización", "Otro / no estoy seguro"]
        elegir = "Elige una opción"
        ayuda_msg = ("Mientras más detalles, mejor la cotización. Si tienes fotos, "
                     "puedes enviarlas por WhatsApp después.")
        enviar = "Enviar por WhatsApp"
        ok = ("Se abrió WhatsApp con tu mensaje. Si no se abrió, escríbenos directo "
              "al 939-219-0979.")
        h2_datos = "Escríbenos directo"
        d_tel, d_wa, d_mail, d_area = "Teléfono", "WhatsApp", "Correo", "Área de servicio"
        v_area = "Área Metro y región Sur de Puerto Rico"
        h2_pueblos = "Pueblos que cubrimos"
        p_pueblos = "Si el tuyo no aparece, pregúntanos igual."
        obligatorio = "obligatorio"
    else:
        titulo = "Contact"
        bajada = ("Tell us what you need and we'll set up the visit. "
                  "The estimate costs you nothing.")
        h2_form = "Request your quote"
        p_form = ("Fill this in and WhatsApp opens with your message ready to send. "
                  "You can also message or call us directly.")
        etiquetas = {
            "saludo": "Hi Michaell, I'm writing from your website.",
            "nombre": "Name", "telefono": "Phone", "pueblo": "Town",
            "servicio": "Service", "mensaje": "Details",
        }
        campos = {
            "nombre": "Name", "telefono": "Phone", "pueblo": "Town",
            "servicio": "What do you need?", "mensaje": "Tell us the details",
        }
        opciones = ["Plumbing", "Painting", "General repairs",
                    "Bathroom remodel", "Kitchen remodel",
                    "Roofing & waterproofing", "Something else / not sure"]
        elegir = "Choose an option"
        ayuda_msg = ("The more detail, the better the quote. If you have photos, you can "
                     "send them over WhatsApp afterwards.")
        enviar = "Send via WhatsApp"
        ok = ("WhatsApp opened with your message. If it didn't, message us directly "
              "at 939-219-0979.")
        h2_datos = "Reach us directly"
        d_tel, d_wa, d_mail, d_area = "Phone", "WhatsApp", "Email", "Service area"
        v_area = "San Juan metro area and southern Puerto Rico"
        h2_pueblos = "Towns we cover"
        p_pueblos = "If yours isn't listed, ask us anyway."
        obligatorio = "required"

    import json
    et_json = json.dumps(etiquetas, ensure_ascii=False).replace('"', "&quot;")
    ops = "".join(f'            <option>{o}</option>\n' for o in opciones)

    return head(idioma, "contacto", *META["contacto"][idioma]) \
        + cabecera(idioma, "contacto") \
        + cabecera_pagina(idioma, "contacto", titulo, bajada) + f'''
  <section class="seccion">
    <div class="contenedor dos-col dos-col--arriba">
      <div class="revelar">
        <h2>{h2_form}</h2>
        <p style="margin-bottom:28px">{p_form}</p>

        <form class="formulario" data-form-whatsapp data-etiquetas="{et_json}">
          <div class="formulario__fila">
            <div class="campo">
              <label for="nombre">{campos["nombre"]} <span aria-label="{obligatorio}">*</span></label>
              <input type="text" id="nombre" name="nombre" autocomplete="name" required>
            </div>
            <div class="campo">
              <label for="telefono">{campos["telefono"]} <span aria-label="{obligatorio}">*</span></label>
              <input type="tel" id="telefono" name="telefono" autocomplete="tel" required>
            </div>
          </div>

          <div class="campo">
            <label for="pueblo">{campos["pueblo"]}</label>
            <input type="text" id="pueblo" name="pueblo" autocomplete="address-level2">
          </div>

          <div class="campo">
            <label for="servicio">{campos["servicio"]}</label>
            <select id="servicio" name="servicio">
              <option value="">{elegir}</option>
{ops}            </select>
          </div>

          <div class="campo">
            <label for="mensaje">{campos["mensaje"]}</label>
            <textarea id="mensaje" name="mensaje"></textarea>
            <p class="campo__ayuda">{ayuda_msg}</p>
          </div>

          <div class="campo campo--miel" aria-hidden="true">
            <label for="apellido2">No llenar</label>
            <input type="text" id="apellido2" name="apellido2" tabindex="-1" autocomplete="off">
          </div>

          <div class="grupo-btn">
            <button class="btn btn--wa" type="submit">
              {icono("wa")}
              {enviar}
            </button>
          </div>

          <p class="aviso" data-form-ok hidden>{ok}</p>
        </form>
      </div>

      <div class="revelar">
        <h2>{h2_datos}</h2>
        <ul class="datos" style="margin-top:26px">
          <li>
            {icono("tel")}
            <div><strong>{d_tel}</strong><a href="tel:{TEL_LINK}">{TEL_HUMANO}</a></div>
          </li>
          <li>
            {icono("wa")}
            <div><strong>{d_wa}</strong><a href="{wa_url(idioma)}" target="_blank" rel="noopener">{TEL_HUMANO}</a></div>
          </li>
          <li>
            {icono("mail")}
            <div><strong>{d_mail}</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          </li>
          <li>
            {icono("ig")}
            <div><strong>Instagram</strong><a href="{IG_URL}" target="_blank" rel="noopener">@{IG_USUARIO}</a></div>
          </li>
          <li>
            {icono("mapa")}
            <div><strong>{d_area}</strong>{v_area}</div>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <section class="seccion seccion--alt">
    <div class="contenedor">
      <div class="encabezado-seccion centrado revelar">
        <h2>{h2_pueblos}</h2>
        <p>{p_pueblos}</p>
      </div>
      {pueblos_html(idioma)}
    </div>
  </section>
''' + cta_cierre(idioma) + pie(idioma)


# ===========================================================================
if __name__ == "__main__":
    generadores = {
        "home": home, "servicios": servicios, "proyectos": proyectos,
        "nosotros": nosotros, "contacto": contacto,
    }
    print("Generando sitio Perfect Solution\n")
    for idioma, idx in (("es", 0), ("en", 1)):
        print(f"[{idioma}]")
        for clave, fn in generadores.items():
            escribir(PAGINAS[clave][idx], fn(idioma))
    print("\nListo.")
