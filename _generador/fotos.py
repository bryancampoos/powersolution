# -*- coding: utf-8 -*-
"""
Procesa las fotos reales para la web.

Toma lo que haya en assets/img/originales/ y produce, en assets/img/:
  - <nombre>.jpg   1600 px de ancho, recortado a 4:3, calidad 82
  - <nombre>.webp  lo mismo en WebP (pesa ~30 % menos)

Uso:
    python _generador/fotos.py            # lista lo que encuentra
    python _generador/fotos.py --procesar # genera las versiones web

El recorte por defecto es al centro. Para encuadrar distinto, añade el nombre
del archivo a ENCUADRE con un valor entre 0 (arriba/izquierda) y 1
(abajo/derecha); 0.5 es el centro.
"""
import io
import os
import sys
from PIL import Image, ImageOps

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "assets", "img", "originales")
DEST = os.path.join(RAIZ, "assets", "img")

ANCHO = 1600
CALIDAD = 82

W = "WhatsApp Image 2026-07-27 at "

# nombre que usa la web -> archivo original.
# Una misma foto puede alimentar varios destinos (aparece en secciones
# distintas), por eso el diccionario va destino -> origen y no al reves.
MAPA = {
    # portada y bloques principales
    "hero":              W + "2.20.57 PM.jpeg",          # sala con plafon iluminado
    "remodelacion":      W + "2.20.56 PM.jpeg",          # panel de TV terminado
    "equipo":            W + "2.20.57 PM (1).jpeg",      # obra en proceso

    # comparadores antes / despues
    "antes-1":           W + "2.20.57 PM (9).jpeg",      # panel electrico viejo
    "despues-1":         W + "2.20.57 PM (5).jpeg",      # panel Eaton nuevo
    "antes-2":           W + "2.20.57 PM (2).jpeg",      # valvula: cobre a la vista
    "despues-2":         W + "2.20.57 PM (7).jpeg",      # valvula instalada

    # cabecera de cada servicio
    "serv-plomeria":     W + "2.20.57 PM (7).jpeg",
    "serv-pintura":      W + "2.20.57 PM (4).jpeg",      # nicho pintado
    "serv-reparaciones": W + "2.20.57 PM (6).jpeg",      # estructura de repisas
    "serv-remodelacion": W + "2.20.57 PM (8).jpeg",      # repisas acabadas
    "serv-exterior":     W + "1.56.13 PM (1).jpeg",      # azotea sellada

    # galeria de trabajos
    "trabajo-1":         W + "2.20.57 PM (4).jpeg",      # nicho terminado
    "trabajo-2":         W + "1.56.12 PM (1).jpeg",      # azotea sellada
    "trabajo-3":         W + "2.20.57 PM (8).jpeg",      # repisas acabadas
    "trabajo-4":         W + "1.56.12 PM.jpeg",          # azotea con calentador solar
    "trabajo-5":         W + "2.20.57 PM (5).jpeg",      # panel electrico nuevo
    "trabajo-6":         W + "2.20.57 PM (7).jpeg",      # valvula instalada
}

# Sin usar por ahora (siguen en originales/):
#   1.56.12 PM (2) y 1.56.13 PM  -> azoteas casi identicas a las elegidas
#   2.20.57 PM (3)               -> techo con filtracion, foto de problema

# nombre de destino -> posicion del recorte (0 = arriba, 1 = abajo)
# Las fotos verticales pierden mucho al pasarlas a 4:3 horizontal, asi que
# se desplaza el encuadre hacia donde esta lo que interesa.
ENCUADRE = {
    "hero": 0.46,
    "remodelacion": 0.42,
    "serv-remodelacion": 0.45,
    "serv-reparaciones": 0.45,
    "equipo": 0.45,
    "trabajo-3": 0.45,
}

# destinos que van en 16:9 en vez de 4:3
PANORAMICAS = {"hero"}


def recortar(im, ratio, pos=0.5):
    """Recorta al ratio pedido sin deformar, desplazando el encuadre."""
    an, al = im.size
    objetivo = ratio
    actual = an / al
    if actual > objetivo:                      # sobra ancho
        nuevo_an = int(al * objetivo)
        x = int((an - nuevo_an) * pos)
        caja = (x, 0, x + nuevo_an, al)
    else:                                      # sobra alto
        nuevo_al = int(an / objetivo)
        y = int((al - nuevo_al) * pos)
        caja = (0, y, an, y + nuevo_al)
    return im.crop(caja)


def procesar(origen, destino, ratio, pos):
    im = Image.open(origen)
    im = ImageOps.exif_transpose(im)           # respeta la rotacion del movil
    im = im.convert("RGB")
    im = recortar(im, ratio, pos)
    if im.width > ANCHO:
        alto = round(im.height * ANCHO / im.width)
        im = im.resize((ANCHO, alto), Image.LANCZOS)
    jpg = os.path.join(DEST, destino + ".jpg")
    webp = os.path.join(DEST, destino + ".webp")
    im.save(jpg, "JPEG", quality=CALIDAD, optimize=True, progressive=True)
    im.save(webp, "WEBP", quality=CALIDAD, method=6)
    return im.size, os.path.getsize(jpg), os.path.getsize(webp)


def main():
    if not os.path.isdir(ORIG):
        print("No existe", ORIG)
        return
    archivos = sorted(
        f for f in os.listdir(ORIG)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".heic", ".webp"))
    )
    if not archivos:
        print(f"No hay fotos en {ORIG}\nCopia ahi las imagenes y vuelve a ejecutar.")
        return

    if "--procesar" not in sys.argv:
        print(f"{len(archivos)} fotos en originales/\n")
        for f in archivos:
            ruta = os.path.join(ORIG, f)
            try:
                im = ImageOps.exif_transpose(Image.open(ruta))
                orientacion = "horizontal" if im.width > im.height else "vertical"
                print(f"  {f:44} {im.width}x{im.height}  {orientacion}  "
                      f"{os.path.getsize(ruta)/1024:.0f} KB")
            except Exception as e:
                print(f"  {f:44} ERROR: {e}")
        print("\nSin MAPA definido todavia. Ejecuta con --procesar cuando lo este.")
        return

    if not MAPA:
        print("MAPA esta vacio: nada que procesar.")
        return

    print("Procesando\n")
    for destino, origen_nombre in MAPA.items():
        origen = os.path.join(ORIG, origen_nombre)
        if not os.path.exists(origen):
            print(f"  FALTA  {destino}  <- {origen_nombre}")
            continue
        ratio = 16 / 9 if destino in PANORAMICAS else 4 / 3
        pos = ENCUADRE.get(destino, 0.5)
        tam, kj, kw = procesar(origen, destino, ratio, pos)
        print(f"  {destino:22} {tam[0]}x{tam[1]}  "
              f"jpg {kj/1024:5.0f} KB   webp {kw/1024:5.0f} KB")
    print("\nListo.")


if __name__ == "__main__":
    main()
