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

  /* --- formulario -> WhatsApp --------------------------------------------- *
   * El negocio atiende por WhatsApp, así que el formulario arma el mensaje y
   * abre el chat: no hace falta backend ni servicio de correo. Para recibirlo
   * por email en su lugar, quitar este bloque y poner en el <form> un
   * action="https://formspree.io/f/TU_ID" con method="post".
   * ----------------------------------------------------------------------- */
  var form = document.querySelector('[data-form-whatsapp]');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      /* honeypot: si viene lleno, es un bot */
      var miel = form.querySelector('[name="apellido2"]');
      if (miel && miel.value) return;

      var datos = new FormData(form);
      var etiquetas = JSON.parse(form.getAttribute('data-etiquetas') || '{}');
      var lineas = [etiquetas.saludo || 'Hola Michaell, le escribo desde la página web.', ''];

      datos.forEach(function (valor, clave) {
        if (clave === 'apellido2' || !String(valor).trim()) return;
        lineas.push((etiquetas[clave] || clave) + ': ' + valor);
      });

      var url = 'https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(lineas.join('\n'));
      window.open(url, '_blank', 'noopener');

      var ok = form.querySelector('[data-form-ok]');
      if (ok) ok.hidden = false;
    });
  }

  /* --- año en el pie ------------------------------------------------------ */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
