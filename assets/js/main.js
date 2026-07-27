/* Perfect Solution — comportamiento del sitio. Sin dependencias. */
(function () {
  'use strict';

  var WHATSAPP = '19392190979';

  /* --- menú móvil --------------------------------------------------------- */
  var boton = document.querySelector('.hamburguesa');
  var nav = document.querySelector('.nav');

  if (boton && nav) {
    boton.addEventListener('click', function () {
      var abierto = nav.getAttribute('data-abierto') === 'true';
      nav.setAttribute('data-abierto', String(!abierto));
      boton.setAttribute('aria-expanded', String(!abierto));
    });

    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.setAttribute('data-abierto', 'false');
        boton.setAttribute('aria-expanded', 'false');
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.getAttribute('data-abierto') === 'true') {
        nav.setAttribute('data-abierto', 'false');
        boton.setAttribute('aria-expanded', 'false');
        boton.focus();
      }
    });
  }

  /* --- revelado al entrar en pantalla ------------------------------------- */
  var revelables = document.querySelectorAll('.revelar');
  var sinMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!revelables.length) {
    /* nada que hacer */
  } else if (sinMovimiento || !('IntersectionObserver' in window)) {
    revelables.forEach(function (el) { el.classList.add('visible'); });
  } else {
    var observador = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (entrada) {
        if (!entrada.isIntersecting) return;
        entrada.target.classList.add('visible');
        observador.unobserve(entrada.target);
      });
    }, { rootMargin: '0px 0px -4% 0px', threshold: 0.02 });

    revelables.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + 'ms';
      observador.observe(el);
    });
  }

  /* --- comparador antes / después ----------------------------------------- */
  document.querySelectorAll('.comparador').forEach(function (comp) {
    var rango = comp.querySelector('input[type="range"]');
    var frente = comp.querySelector('.comparador__frente');
    var tirador = comp.querySelector('.comparador__tirador');
    if (!rango || !frente || !tirador) return;

    function pintar() {
      frente.style.width = rango.value + '%';
      tirador.style.left = rango.value + '%';
    }
    rango.addEventListener('input', pintar);
    window.addEventListener('resize', pintar);
    pintar();
  });

  /* --- formulario de contacto --------------------------------------------- *
   * El mismo formulario se envía por WhatsApp o por correo, según el botón.
   *
   * WhatsApp  -> abre el chat con el mensaje ya redactado.
   * Correo    -> si hay clave de Web3Forms, lo manda de verdad y el visitante
   *              no sale de la página. Sin clave, cae en `mailto:`, que abre
   *              el gestor de correo del visitante con todo escrito.
   *
   * Para que el correo llegue solo, saca una clave gratuita en web3forms.com
   * (piden el email de destino y la mandan ahí; no hay que crear cuenta) y
   * pégala abajo en WEB3FORMS_KEY. Es la única línea que hay que tocar.
   * ----------------------------------------------------------------------- */
  var WEB3FORMS_KEY = '';

  var form = document.querySelector('[data-form-contacto]');

  if (form) {
    var mensajes = leerJson(form, 'data-mensajes');
    var etiquetas = leerJson(form, 'data-etiquetas');
    var ultimaVia = 'whatsapp';

    /* e.submitter no existe en navegadores viejos: se guarda el botón pulsado */
    form.querySelectorAll('[data-via]').forEach(function (b) {
      b.addEventListener('click', function () { ultimaVia = b.getAttribute('data-via'); });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* honeypot: si viene lleno, es un bot */
      var miel = form.querySelector('[name="apellido2"]');
      if (miel && miel.value) return;

      var via = (e.submitter && e.submitter.getAttribute('data-via')) || ultimaVia;
      var campos = recogerCampos();

      if (via === 'email') enviarPorCorreo(campos);
      else enviarPorWhatsapp(campos);
    });
  }

  function leerJson(el, attr) {
    try { return JSON.parse(el.getAttribute(attr) || '{}'); } catch (err) { return {}; }
  }

  function mostrar(texto) {
    var aviso = form.querySelector('[data-form-aviso]');
    if (!aviso) return;
    aviso.textContent = texto;
    aviso.hidden = false;
  }

  function recogerCampos() {
    var datos = new FormData(form);
    var pares = [];
    datos.forEach(function (valor, clave) {
      if (clave === 'apellido2' || !String(valor).trim()) return;
      pares.push({ clave: clave, etiqueta: etiquetas[clave] || clave, valor: valor });
    });
    return pares;
  }

  function cuerpoTexto(campos) {
    var lineas = [etiquetas.saludo || '', ''];
    campos.forEach(function (c) { lineas.push(c.etiqueta + ': ' + c.valor); });
    return lineas.join('\n');
  }

  function enviarPorWhatsapp(campos) {
    var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(cuerpoTexto(campos));
    window.open(url, '_blank', 'noopener');
    mostrar(mensajes.wa || '');
  }

  function enviarPorCorreo(campos) {
    var asunto = form.getAttribute('data-asunto') || 'Contacto';
    var nombre = campos.filter(function (c) { return c.clave === 'nombre'; })[0];
    if (nombre) asunto += ' — ' + nombre.valor;

    if (!WEB3FORMS_KEY) {
      var destino = form.getAttribute('data-email') || '';
      window.location.href = 'mailto:' + destino
        + '?subject=' + encodeURIComponent(asunto)
        + '&body=' + encodeURIComponent(cuerpoTexto(campos));
      mostrar(mensajes.mail || '');
      return;
    }

    var carga = { access_key: WEB3FORMS_KEY, subject: asunto, from_name: 'Web Perfect Solution' };
    campos.forEach(function (c) { carga[c.etiqueta] = c.valor; });

    var boton = form.querySelector('[data-via="email"]');
    if (boton) boton.disabled = true;

    fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(carga)
    })
      .then(function (r) { return r.json(); })
      .then(function (r) {
        if (r && r.success) { mostrar(mensajes.enviado || ''); form.reset(); }
        else { mostrar(mensajes.error || ''); }
      })
      .catch(function () { mostrar(mensajes.error || ''); })
      .then(function () { if (boton) boton.disabled = false; });
  }

  /* --- año en el pie ------------------------------------------------------ */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
