#!/usr/bin/env python3
"""Genera las páginas públicas de la web de Auténticos CyL.

    python3 tools/generar.py

Escribe index.html (inicio), carta.html, noticias.html y reservas.html con la
misma cabecera, menú y pie. La carta se edita en datos/carta.json y las noticias
y reconocimientos en datos/noticias.json. El área de propietarios
(gestor.html) es un archivo aparte y no se genera aquí.
"""
import json
from html import escape as e
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARTA = json.loads((RAIZ / 'datos' / 'carta.json').read_text(encoding='utf-8'))
NOTICIAS = json.loads((RAIZ / 'datos' / 'noticias.json').read_text(encoding='utf-8'))
EVENTO = json.loads((RAIZ / 'datos' / 'evento_especial.json').read_text(encoding='utf-8'))


TEL, TEL_VISIBLE = '+34647413186', '647 41 31 86'
WHATSAPP = 'https://wa.me/34647413186'
REPSOL = 'https://www.guiarepsol.com/es/fichas/solete/autenticos-cyl-334575/'
REDES = [('Instagram', 'https://www.instagram.com/autenticoscylbartaperia/', '@autenticoscylbartaperia'),
         ('Facebook', 'https://www.facebook.com/AutenticosCyLBarTaperia/', 'Auténticos CyL Bar Tapería'),
         ('Threads', 'https://www.threads.net/@autenticoscylbartaperia', '@autenticoscylbartaperia')]
ICONOS = {
    'Instagram': '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
    'Facebook': '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5H16l.4-3H13.5V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4a21 21 0 0 0-2.3-.1c-2.3 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3Z"/></svg>',
    'Threads': '<svg class="h-5 w-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path stroke-linecap="round" d="M16.5 11.2c-.5-2.4-2.3-3.6-4.6-3.6-2.8 0-4.4 2-4.4 4.6 0 3 1.9 4.9 4.8 4.9 2.3 0 3.9-1.2 3.9-3 0-2.9-4.9-3.3-6-1.4-.8 1.5.4 3 2 3 2.6 0 3.8-2.4 3.2-6.2M19 6.8C17.6 4.4 15.2 3 12.1 3 6.9 3 4 6.5 4 12s2.9 9 8.1 9c3.7 0 6.4-1.9 7.4-5"/></svg>'
}
HORARIO = [('Lunes', '9:00 – 14:00 · 17:00 – 20:00'), ('Martes', 'Cerrado'), ('Miércoles', 'Cerrado'),
           ('Jueves', '9:00 – 23:30'), ('Viernes', '9:00 – 23:30'), ('Sábado', '9:00 – 24:00'), ('Domingo', '9:00 – 24:00')]
DIRECCION = 'C/ Calixto del Río, 8 · 40480 Coca (Segovia)'
LEMA = 'Cocinamos con cabeza, trabajamos con el corazón'  # lema oficial de la casa
MAPA = 'https://www.google.com/maps/search/?api=1&query=Aut%C3%A9nticos+CyL+Calle+Calixto+del+R%C3%ADo+8+Coca+Segovia'
TIENDA_ONLINE = 'https://www.autenticoscyl.com/'
ALERGENOS = {1: 'Gluten', 2: 'Crustáceos', 3: 'Moluscos', 4: 'Pescado', 5: 'Huevos', 6: 'Soja', 7: 'Mostaza',
             8: 'Apio', 9: 'Frutos secos', 10: 'Cacahuetes', 11: 'Sésamo', 12: 'Sulfitos', 13: 'Lácteos', 14: 'Altramuces'}
NAV = [('index.html', 'Inicio'), ('carta.html', 'Carta'), ('para-llevar.html', 'Para llevar'), ('noticias.html', 'Noticias'), ('reservas.html', 'Reservas')]
LEGALES = [('aviso-legal.html', 'Aviso legal'), ('privacidad.html', 'Política de privacidad'), ('cookies.html', 'Política de cookies')]

# Datos del titular para los textos legales. Los que van entre corchetes los tiene
# que facilitar el cliente antes de publicar la web.
TITULAR = {
    'nombre': 'Alfonso Galindo',       # según el aviso legal de autenticoscyl.com
    'nif': '[NIF / CIF]',
    'domicilio': 'C/ Calixto del Río, 8 · 40480 Coca (Segovia)',
    'email': 'autenticoscyl@gmail.com',
    'telefono': '647 41 31 86',
    'registro': '[Si es una sociedad: datos de inscripción en el Registro Mercantil; si es autónomo, no aplica]',
    'dominio': 'www.autenticoscyl.com',
    'actualizado': 'septiembre de 2026',
}

ACTUAL = ' aria-current="page"'
CANDADO = '<svg class="h-4 w-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path stroke-linecap="round" d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'


def euros(n):
    return f'{n:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.') + ' €'


def cabeza(titulo, descripcion):
    return f'''<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  <title>{e(titulo)}</title>
  <meta name="description" content="{e(descripcion)}" />
  <meta name="theme-color" content="#121315" />
  <link rel="icon" type="image/png" href="img/favicon.png" />
  <link rel="apple-touch-icon" href="img/icono-192.png" />
  <meta property="og:title" content="{e(titulo)}" />
  <meta property="og:description" content="{e(descripcion)}" />
  <meta property="og:image" content="img/fachada.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            pizarra: {{ 950: '#121315', 900: '#1a1c1f', 800: '#24272b', 700: '#34383d', 600: '#4a4f55' }},
            vino:    {{ 600: '#6e1f2c', 500: '#8c2a3a', 400: '#b0455a', 300: '#d98c9b' }},
            oro:     {{ 500: '#b38d45', 400: '#c9a45c', 300: '#dcc08a' }},
            crema:   {{ 100: '#f4efe6', 300: '#d9d2c5', 500: '#a39c90' }}
          }},
          fontFamily: {{ display: ['Fraunces', 'Georgia', 'serif'], sans: ['Manrope', 'system-ui', 'sans-serif'] }}
        }}
      }}
    }};
  </script>
  <style>
    html {{ -webkit-tap-highlight-color: transparent; scroll-behavior: smooth; scroll-padding-top: 8rem; }}
    body {{ background: #121315; }}
    input, select, textarea {{ font-size: 16px; }}
    .no-scrollbar {{ scrollbar-width: none; }} .no-scrollbar::-webkit-scrollbar {{ display: none; }}
    :focus-visible {{ outline: 2px solid #c9a45c; outline-offset: 2px; }}
    @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
  </style>
</head>
<body class="min-h-screen font-sans text-crema-100 antialiased">
'''


def cabecera(actual):
    enlaces = ''.join(
        f'<a href="{h}" class="rounded-full px-4 py-2 text-sm font-semibold transition {"bg-white/10 text-crema-100" if h == actual else "text-crema-300 hover:text-crema-100"}"{ACTUAL if h == actual else ""}>{t}</a>'
        for h, t in NAV)
    movil = ''.join(
        f'<a href="{h}" class="block rounded-2xl px-4 py-3 text-lg font-semibold {"bg-white/10 text-crema-100" if h == actual else "text-crema-300"}">{t}</a>'
        for h, t in NAV)
    return f'''
  <header class="sticky top-0 z-40 border-b border-white/5 bg-pizarra-950/90 backdrop-blur">
    <div class="mx-auto flex max-w-6xl items-center justify-between gap-4 px-5 py-3">
      <a href="index.html" class="flex min-w-0 items-center gap-3 leading-tight">
        <img src="img/logo.webp" alt="" width="44" height="44" class="h-11 w-11 shrink-0 rounded-full" />
        <span class="min-w-0"><span class="block font-display text-xl font-semibold text-crema-100">Auténticos CyL</span>
        <span class="block truncate text-[11px] font-semibold uppercase tracking-[.22em] text-oro-400">Bar Tapería · Tienda · Coca</span></span>
      </a>
      <nav class="hidden items-center gap-1 md:flex" aria-label="Principal">
        {enlaces}
        <a href="gestor.html" class="ml-2 inline-flex items-center gap-2 rounded-full border border-oro-400/40 px-4 py-2 text-sm font-semibold text-oro-300 transition hover:bg-oro-400 hover:text-pizarra-950">{CANDADO}Propietarios</a>
      </nav>
      <button id="menuBtn" class="rounded-full p-2 text-crema-100 md:hidden" aria-controls="menuMovil" aria-expanded="false" aria-label="Abrir menú">
        <svg class="h-7 w-7" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24"><path stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
    <nav id="menuMovil" class="hidden border-t border-white/5 px-5 pb-5 pt-2 md:hidden" aria-label="Principal (móvil)">
      {movil}
      <a href="gestor.html" class="mt-2 flex items-center gap-2 rounded-2xl border border-oro-400/30 px-4 py-3 font-semibold text-oro-300">{CANDADO}Área de propietarios</a>
    </nav>
  </header>
'''


def pie():
    return f'''
  <footer class="border-t border-white/5 bg-pizarra-900">
    <div class="mx-auto grid max-w-6xl gap-10 px-5 py-12 md:grid-cols-3">
      <div>
        <p class="font-display text-2xl font-semibold">Auténticos CyL</p>
        <p class="mt-1 font-display italic text-oro-300">Sabores, Sensaciones y +</p>
        <p class="mt-4 text-sm leading-relaxed text-crema-500">Bar tapería y tienda de productos de Castilla y León, a los pies del castillo de Coca.</p>
        <div class="mt-5">{sello_solete()}</div>
        <div class="mt-4 flex gap-2">{''.join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}" title="{n}" class="grid h-10 w-10 place-items-center rounded-full border border-white/10 text-crema-300 transition hover:border-oro-400 hover:text-oro-300">{ICONOS[n]}</a>' for n, u, _ in REDES)}</div>
      </div>
      <div class="text-sm leading-relaxed text-crema-300">
        <p class="text-xs font-semibold uppercase tracking-[.22em] text-oro-400">Visítanos</p>
        <p class="mt-3">{e(DIRECCION)}</p>
        <p class="mt-1">Teléfono <a href="tel:{TEL}" class="font-semibold text-crema-100 hover:text-oro-300">{TEL_VISIBLE}</a></p>
        <p class="mt-1">WhatsApp <a href="{WHATSAPP}" target="_blank" rel="noopener" class="font-semibold text-crema-100 hover:text-oro-300">escríbenos</a></p>
        <p class="mt-1"><a href="{MAPA}" target="_blank" rel="noopener" class="underline decoration-oro-400/40 underline-offset-4 hover:text-oro-300">Cómo llegar</a> · <a href="{TIENDA_ONLINE}" target="_blank" rel="noopener" class="underline decoration-oro-400/40 underline-offset-4 hover:text-oro-300">Tienda online</a></p>
      </div>
      <div class="text-sm">
        <p class="text-xs font-semibold uppercase tracking-[.22em] text-oro-400">La web</p>
        <ul class="mt-3 space-y-1.5 text-crema-300">
          {''.join(f'<li><a href="{h}" class="hover:text-oro-300">{t}</a></li>' for h, t in NAV)}
          <li><a href="gestor.html" class="inline-flex items-center gap-1.5 hover:text-oro-300">{CANDADO}Área de propietarios</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-white/5 px-5 py-5 text-center text-xs text-crema-500">
      <nav class="flex flex-wrap justify-center gap-x-5 gap-y-2" aria-label="Textos legales">
        {''.join(f'<a href="{h}" class="hover:text-oro-300">{t}</a>' for h, t in LEGALES)}
      </nav>
      <p class="mt-3">© <span data-anio></span> Auténticos CyL · Coca (Segovia) · Web en modo demostración</p>
    </div>
  </footer>
  <script src="js/config.js"></script>
  <script>
    (() => {{
      const b = document.getElementById('menuBtn'), m = document.getElementById('menuMovil');
      b.addEventListener('click', () => {{ const abierto = m.classList.toggle('hidden') === false; b.setAttribute('aria-expanded', abierto); }});
      document.querySelectorAll('[data-anio]').forEach(el => el.textContent = new Date().getFullYear());
    }})();
  </script>
'''


def boton(href, texto, primario=True):
    clase = ('bg-vino-500 text-crema-100 hover:bg-vino-400' if primario
             else 'border border-crema-100/30 text-crema-100 hover:bg-white/10')
    return f'<a href="{href}" class="inline-flex items-center justify-center rounded-full px-7 py-3.5 font-semibold transition {clase}">{texto}</a>'


def sol(clase='h-10 w-10'):
    rayos = ''.join(f'<line x1="24" y1="3" x2="24" y2="9" transform="rotate({a} 24 24)" />' for a in range(0, 360, 30))
    return (f'<svg class="{clase}" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" aria-hidden="true">'
            f'{rayos}<circle cx="24" cy="24" r="10" fill="currentColor" stroke="none" /></svg>')


def sello_solete(tam='normal'):
    grande = tam == 'grande'
    return f'''<a href="{REPSOL}" target="_blank" rel="noopener" class="group inline-flex items-center gap-3 rounded-full border border-oro-400/40 bg-pizarra-950/60 py-2 pl-2 {"pr-6" if grande else "pr-5"} backdrop-blur transition hover:border-oro-300">
          <span class="grid {"h-12 w-12" if grande else "h-10 w-10"} place-items-center rounded-full bg-oro-400 text-pizarra-950">{sol("h-8 w-8" if grande else "h-7 w-7")}</span>
          <span class="leading-tight"><span class="block text-[11px] font-semibold uppercase tracking-[.2em] text-oro-300">Guía Repsol</span><span class="block font-display {"text-xl" if grande else "text-lg"} font-semibold text-crema-100">Solete 2025</span></span>
        </a>'''


def enlace(href, texto, clase):
    externo = href.startswith('http')
    destino = ' target="_blank" rel="noopener"' if externo else ''
    return f'<a href="{href}"{destino} class="{clase}">{e(texto)} →</a>'


def tarjeta_noticia(n, grande=False):
    return f'''
        <article id="{n["id"]}" class="flex flex-col overflow-hidden rounded-3xl border border-white/5 bg-pizarra-900">
          {f'<div class="{"aspect-[16/9]" if grande else "aspect-[4/3]"} grid w-full place-items-center bg-[radial-gradient(circle_at_50%_40%,rgba(201,164,92,.35),transparent_65%)]"><div class="text-center"><span class="mx-auto grid h-24 w-24 place-items-center rounded-full bg-oro-400 text-pizarra-950 shadow-[0_0_60px_rgba(201,164,92,.45)]">{sol("h-16 w-16")}</span><p class="mt-4 text-xs font-semibold uppercase tracking-[.25em] text-oro-300">Guía Repsol</p><p class="font-display text-3xl font-semibold">Solete</p></div></div>' if n.get("insignia") else f'<img src="{n["foto"]}" alt="" loading="lazy" class="{"aspect-[16/9]" if grande else "aspect-[4/3]"} w-full object-cover" />'}
          <div class="flex flex-1 flex-col p-6">
            <p class="text-[11px] font-semibold uppercase tracking-[.2em] text-oro-400">{e(n["fecha"])}</p>
            <h3 class="mt-2 font-display text-2xl font-semibold leading-snug">{e(n["titulo"])}</h3>
            <p class="mt-3 flex-1 leading-relaxed text-crema-300">{e(n["entradilla"])}</p>
            <div class="mt-5 flex flex-wrap gap-x-5 gap-y-2">{enlace(n["enlace"][0], n["enlace"][1], "font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4")}{enlace(n["prensa"][0], n["prensa"][1], "font-semibold text-crema-300 underline decoration-white/20 underline-offset-4") if n.get("prensa") else ""}</div>
          </div>
        </article>'''


def bloque_reconocimientos():
    return ''.join(f'''
        <li class="rounded-3xl border border-oro-400/20 bg-oro-400/5 p-6">
          {f'<span class="mb-3 grid h-12 w-12 place-items-center rounded-full bg-oro-400 text-pizarra-950">{sol("h-8 w-8")}</span>' if r.get("insignia") else ''}
          <p class="text-[11px] font-semibold uppercase tracking-[.2em] text-oro-400">{e(r["origen"])}</p>
          <p class="mt-2 font-display text-xl font-semibold leading-snug">{e(r["titulo"])}</p>
          <p class="mt-2 text-sm leading-relaxed text-crema-300">{e(r["texto"])}</p>
          {f'<a href="{r["enlace"]}" target="_blank" rel="noopener" class="mt-3 inline-block text-sm font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">{e(r.get("enlaceTexto", "Ver más"))} →</a>' if r.get("enlace") else ''}
        </li>''' for r in NOTICIAS['reconocimientos'])


# ---------------------------------------------------------------------------
# INICIO
# ---------------------------------------------------------------------------
DESTACADOS = [
    ('img/chipirones.webp', 'Chipirones en texturas', 'Nuestros imprescindibles', 'imprescindibles'),
    ('img/tabla-duroc.webp', 'Tabla de carnes Duroc a la brasa', 'A la brasa y el mar', 'brasa'),
    ('img/rabo-de-toro.webp', 'La Rabo de Toro', 'Las noches de Auténticos', 'noches'),
    ('img/croquetas.webp', 'Croquetas súper cremosas de jamón', 'Nuestros imprescindibles', 'imprescindibles'),
    ('img/torreznos.webp', 'Torrezno de Soria bien crujiente', 'Nuestros imprescindibles', 'imprescindibles'),
    ('img/huevo-de-corral.webp', 'Huevo de corral', 'La repostería de Auténticos', 'postres'),
]
TIENDA = ['Vinos de Castilla y León', 'Embutidos', 'Quesos', 'Patés', 'Mieles', 'Conservas artesanas de Segovia',
          'Licores y vermut', 'Dulces y chocolates artesanos', 'Recuerdos de Coca']


def pagina_inicio():
    tarjetas = ''.join(f'''
        <a href="carta.html#{sec}" class="group block overflow-hidden rounded-3xl border border-white/5 bg-pizarra-900">
          <img src="{src}" alt="{e(nombre)}" loading="lazy" class="aspect-[4/3] w-full object-cover transition duration-500 group-hover:scale-[1.03]" />
          <div class="p-5">
            <p class="text-[11px] font-semibold uppercase tracking-[.2em] text-oro-400">{e(seccion)}</p>
            <p class="mt-1 font-display text-xl font-semibold leading-snug">{e(nombre)}</p>
          </div>
        </a>''' for src, nombre, seccion, sec in DESTACADOS)
    chips = ''.join(f'<li class="rounded-full border border-white/10 px-4 py-2 text-sm text-crema-300">{e(t)}</li>' for t in TIENDA)
    return cabeza('Auténticos CyL · Bar Tapería y tienda en Coca (Segovia)',
                  'Bar tapería y tienda de productos de Castilla y León a los pies del castillo de Coca: cocina a la brasa, producto de temporada y más de 500 vinos de nuestra tierra.') + cabecera('index.html') + f'''
  <main>
    <!-- Portada -->
    <section class="relative isolate overflow-hidden">
      <img src="img/fachada.webp" alt="Fachada de Auténticos CyL en Coca, con los carteles de bar, comidas, tapería y tienda" class="absolute inset-0 -z-10 h-full w-full object-cover" />
      <div class="absolute inset-0 -z-10 bg-gradient-to-b from-pizarra-950/70 via-pizarra-950/75 to-pizarra-950"></div>
      <div class="mx-auto max-w-6xl px-5 pb-20 pt-24 sm:pb-28 sm:pt-32">
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Coca · Segovia · a los pies del castillo</p>
        <h1 class="mt-4 max-w-3xl font-display text-5xl font-semibold leading-[1.02] sm:text-7xl">Auténticos CyL</h1>
        <p class="mt-3 font-display text-2xl italic text-oro-300 sm:text-3xl">Sabores, Sensaciones y +</p>
        <p class="mt-6 max-w-xl text-lg leading-relaxed text-crema-300">Bar tapería y tienda de productos de Castilla y León. Cocina a la brasa, producto de temporada y una bodega con más de 500 vinos de nuestra tierra.</p>
        <div class="mt-9 flex flex-wrap gap-3">{boton('reservas.html', 'Reservar mesa')}{boton('carta.html', 'Ver la carta', False)}</div>
        <div class="mt-10">{sello_solete('grande')}</div>
      </div>
    </section>

    <!-- Datos -->
    <section class="border-y border-white/5 bg-pizarra-900">
      <dl class="mx-auto grid max-w-6xl grid-cols-1 divide-y divide-white/5 px-5 sm:grid-cols-3 sm:divide-x sm:divide-y-0">
        <div class="py-6 sm:px-6"><dt class="text-xs font-semibold uppercase tracking-[.2em] text-oro-400">Desde 2014</dt><dd class="mt-1 text-crema-300">En Coca, junto a uno de los castillos más bonitos de España.</dd></div>
        <div class="py-6 sm:px-6"><dt class="text-xs font-semibold uppercase tracking-[.2em] text-oro-400">Castilla y León</dt><dd class="mt-1 text-crema-300">Productos artesanos de las nueve provincias.</dd></div>
        <div class="py-6 sm:px-6"><dt class="text-xs font-semibold uppercase tracking-[.2em] text-oro-400">+500 referencias</dt><dd class="mt-1 text-crema-300">De vino, en nuestra bodega y tienda.</dd></div>
      </dl>
    </section>

    <!-- Fechas especiales y eventos -->
    <section id="eventos" class="mx-auto max-w-6xl px-5 pt-16">
      <div class="overflow-hidden rounded-3xl border border-oro-400/30 bg-gradient-to-br from-vino-600/30 via-pizarra-900 to-pizarra-900 p-8 md:p-12">
        <div class="grid items-center gap-8 md:grid-cols-2">
          <div>
            <div class="inline-flex items-center gap-2 rounded-full border border-oro-400/40 bg-oro-400/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-oro-300">
              <svg class="h-4 w-4 fill-oro-400" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
              <span>Fechas especiales y eventos</span>
            </div>
            <h2 class="mt-4 font-display text-3xl font-semibold leading-tight sm:text-4xl" data-evento-titulo>{e(EVENTO['titulo'])}</h2>
            <p class="mt-2 text-sm font-semibold uppercase tracking-widest text-oro-400" data-evento-fecha>{e(EVENTO['fecha'])}</p>
            <p class="mt-4 text-base leading-relaxed text-crema-300" data-evento-desc>{e(EVENTO['descripcion'])}</p>
            <ul class="mt-5 space-y-2 text-sm font-semibold text-crema-100">
              <li class="flex items-center gap-2.5"><span class="h-2 w-2 rounded-full bg-oro-400"></span>Servicio únicamente de cenas esa noche</li>
              <li class="flex items-center gap-2.5"><span class="h-2 w-2 rounded-full bg-oro-400"></span>Hamburguesas de autor solo para llevar</li>
            </ul>
            <div class="mt-8 flex flex-wrap gap-3">
              {boton('reservas.html', 'Reservar para esta fecha')}
            </div>
          </div>
          <div class="flex items-center justify-center p-2">
            <div class="relative w-full max-w-[300px] aspect-[9/16] overflow-hidden rounded-2xl border border-white/10 bg-black shadow-2xl">
              <video id="videoEventoSeccion" src="{EVENTO['videoUrl']}" controls autoplay loop muted playsinline class="h-full w-full rounded-2xl object-cover"></video>
            </div>
          </div>
        </div>
      </div>
    </section>
        </div>
      </div>
    </section>

    <!-- El restaurante -->
    <section id="restaurante" class="mx-auto grid max-w-6xl items-center gap-10 px-5 py-20 md:grid-cols-2 md:gap-16">
      <img src="img/local.webp" alt="Interior de la tapería: barra de madera con azulejos azules y mesas de madera" loading="lazy" class="aspect-[4/3] w-full rounded-3xl object-cover" />
      <div>
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">El restaurante</p>
        <h2 class="mt-3 font-display text-4xl font-semibold leading-tight">Tradición y creatividad en cada plato</h2>
        <ul class="mt-4 flex flex-wrap gap-2 text-sm font-semibold"><li class="rounded-full bg-oro-400/10 px-4 py-1.5 text-oro-300">Calidad</li><li class="rounded-full bg-oro-400/10 px-4 py-1.5 text-oro-300">Innovación</li></ul>
        <p class="mt-5 leading-relaxed text-crema-300">Nuestra carta nace del mejor producto de temporada y de la cocina a la brasa. Respetamos el producto, el fuego y el tiempo para llevar cada ingrediente a su máxima expresión: platos memorables, honestos y sorprendentes.</p>
        <p class="mt-4 leading-relaxed text-crema-300">De día, los imprescindibles de siempre, las carnes maduradas al josper y el mar. Cuando cae el sol llegan <strong class="text-crema-100">Las noches de Auténticos</strong>: hamburguesas de autor y bocados para disfrutar sin prisas, solo en las cenas.</p>
        <div class="mt-8 flex flex-wrap gap-3">{boton('carta.html', 'Ver la carta')}{boton('reservas.html', 'Reservar', False)}</div>
      </div>
    </section>

    <!-- Lema de la casa -->
    <section aria-label="Nuestro lema" class="border-y border-white/5 bg-pizarra-900">
      <figure class="mx-auto max-w-4xl px-5 py-16 text-center sm:py-20">
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Nuestro lema</p>
        <blockquote class="mt-5 font-display text-3xl font-semibold italic leading-tight text-crema-100 sm:text-5xl">«{LEMA}»</blockquote>
        <figcaption class="mt-5 text-sm uppercase tracking-[.25em] text-crema-500">Auténticos CyL · Coca</figcaption>
      </figure>
    </section>

    <!-- Destacados -->
    <section class="mx-auto max-w-6xl px-5 py-20">
      <div class="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">De nuestra cocina</p>
          <h2 class="mt-3 font-display text-4xl font-semibold">Para abrir boca</h2>
        </div>
        <a href="carta.html" class="font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">Toda la carta →</a>
      </div>
      <div class="mt-8 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">{tarjetas}
      </div>
    </section>

    <!-- La tienda -->
    <section id="tienda" class="border-y border-white/5 bg-pizarra-900">
      <div class="mx-auto grid max-w-6xl items-center gap-10 px-5 py-20 md:grid-cols-2 md:gap-16">
        <div class="md:order-2"><img src="img/tienda.webp" alt="La tienda: estanterías con vinos, conservas y productos de Castilla y León junto a la barra" loading="lazy" class="aspect-[4/3] w-full rounded-3xl object-cover" /></div>
        <div>
          <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">La tienda</p>
          <h2 class="mt-3 font-display text-4xl font-semibold leading-tight">Lo mejor de Castilla y León, para llevar</h2>
          <p class="mt-5 leading-relaxed text-crema-300">Un espacio gastronómico con productos artesanos de Segovia, Valladolid, Soria, Palencia, Burgos, Ávila, Zamora, Salamanca y León. Lo que pruebas en la mesa lo puedes llevar a casa.</p>
          <ul class="mt-6 flex flex-wrap gap-2">{chips}</ul>
          <p class="mt-6 text-sm text-crema-500">¿No puedes venir? Tenemos <a href="{TIENDA_ONLINE}" target="_blank" rel="noopener" class="font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">tienda online</a> con envíos a toda España.</p>
        </div>
      </div>
    </section>

    <!-- Las noches -->
    <section class="relative isolate overflow-hidden">
      <img src="img/rabo-de-toro.webp" alt="" loading="lazy" class="absolute inset-0 -z-10 h-full w-full object-cover" />
      <div class="absolute inset-0 -z-10 bg-pizarra-950/80"></div>
      <div class="mx-auto max-w-6xl px-5 py-20 text-center">
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Solo en servicio de cenas</p>
        <h2 class="mt-3 font-display text-4xl font-semibold sm:text-5xl">Las noches de Auténticos</h2>
        <p class="mx-auto mt-4 max-w-xl leading-relaxed text-crema-300">La Bestia Castellana, Rock &amp; Rolla, Deluxe Macarra, La Castiza… Hamburguesas de buey 100 % certificado y bocados para compartir.</p>
        <div class="mt-8 flex justify-center">{boton('carta.html#noches', 'Descubrir Las Noches')}</div>
      </div>
    </section>

    <!-- Otros servicios -->
    <section class="mx-auto max-w-6xl px-5 pt-20">
      <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Además</p>
      <h2 class="mt-3 font-display text-4xl font-semibold">También te lo preparamos</h2>
      <div class="mt-8 grid gap-5 md:grid-cols-3">
        <div class="rounded-3xl border border-white/5 bg-pizarra-900 p-6"><p class="font-display text-2xl font-semibold">Comida para llevar</p><p class="mt-2 leading-relaxed text-crema-300">Nuestra cocina para disfrutar en casa. Encárgala por teléfono o WhatsApp y pásate a recogerla.</p></div>
        <div class="rounded-3xl border border-white/5 bg-pizarra-900 p-6"><p class="font-display text-2xl font-semibold">Menús de empresa y grupos</p><p class="mt-2 leading-relaxed text-crema-300">Comidas y cenas de empresa, celebraciones y grupos con menús a medida.</p></div>
        <div class="rounded-3xl border border-white/5 bg-pizarra-900 p-6"><p class="font-display text-2xl font-semibold">Encargos de Navidad</p><p class="mt-2 leading-relaxed text-crema-300">Esta Navidad no vas a cocinar: platos por encargo y cestas con productos de Castilla y León.</p></div>
      </div>
      <div class="mt-6 flex flex-wrap gap-3"><a href="tel:{TEL}" class="inline-flex items-center justify-center rounded-full bg-vino-500 px-7 py-3.5 font-semibold text-crema-100 transition hover:bg-vino-400">Llamar al {TEL_VISIBLE}</a><a href="{WHATSAPP}" target="_blank" rel="noopener" class="inline-flex items-center justify-center rounded-full border border-crema-100/30 px-7 py-3.5 font-semibold text-crema-100 transition hover:bg-white/10">Escribir por WhatsApp</a></div>
    </section>

    <!-- Instagram -->
    <section class="mx-auto max-w-6xl px-5 pt-20">
      <a href="{REDES[0][1]}" target="_blank" rel="noopener" class="group flex flex-col items-start gap-5 rounded-3xl border border-white/5 bg-gradient-to-br from-vino-600/40 via-pizarra-900 to-pizarra-900 p-8 sm:flex-row sm:items-center sm:justify-between">
        <span class="flex min-w-0 items-center gap-4"><img src="img/logo.webp" alt="" class="h-16 w-16 shrink-0 rounded-full" loading="lazy" />
          <span class="min-w-0"><span class="block text-xs font-semibold uppercase tracking-[.25em] text-oro-400">Síguenos</span><span class="block break-all font-display text-xl font-semibold sm:text-2xl">@autenticoscylbartaperia</span><span class="block text-sm text-crema-300">Platos del día, novedades y horarios especiales.</span></span></span>
        <span class="inline-flex items-center gap-2 rounded-full bg-crema-100 px-6 py-3 font-semibold text-pizarra-950">{ICONOS['Instagram']}Ver Instagram</span>
      </a>
    </section>

    <!-- Noticias -->
    <section class="mx-auto max-w-6xl px-5 pt-20">
      <div class="flex flex-wrap items-end justify-between gap-4">
        <div>
          <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Noticias y reconocimientos</p>
          <h2 class="mt-3 font-display text-4xl font-semibold">Lo último en Auténticos</h2>
        </div>
        <a href="noticias.html" class="font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">Todas las noticias →</a>
      </div>
      <div class="mt-8 grid gap-5 md:grid-cols-3">{''.join(tarjeta_noticia(n) for n in NOTICIAS['noticias'][:3])}
      </div>
      <ul class="mt-5 grid gap-5 md:grid-cols-2">{bloque_reconocimientos()}
      </ul>
    </section>

    <!-- Dónde estamos -->
    <section id="contacto" class="mx-auto grid max-w-6xl gap-10 px-5 py-20 md:grid-cols-2 md:gap-16">
      <div>
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Dónde estamos</p>
        <h2 class="mt-3 font-display text-4xl font-semibold leading-tight">En el corazón de Coca</h2>
        <p class="mt-5 leading-relaxed text-crema-300">A unos pasos del castillo de Coca, joya del mudéjar castellano. Ven a comer, a cenar o a tomar algo en la barra, y llévate un trocito de Castilla y León.</p>
        <dl class="mt-8 space-y-4">
          <div><dt class="text-xs font-semibold uppercase tracking-[.2em] text-crema-500">Dirección</dt><dd class="mt-1">{e(DIRECCION)}</dd></div>
          <div><dt class="text-xs font-semibold uppercase tracking-[.2em] text-crema-500">Teléfono</dt><dd class="mt-1"><a href="tel:{TEL}" class="text-lg font-semibold hover:text-oro-300">{TEL_VISIBLE}</a></dd></div>
          <div><dt class="text-xs font-semibold uppercase tracking-[.2em] text-crema-500">Horario</dt><dd><table class="mt-2 w-full max-w-sm text-sm"><tbody>{''.join(f'<tr class="border-b border-white/5"><th scope="row" class="py-1.5 pr-4 text-left font-medium text-crema-300">{d}</th><td class="py-1.5 text-right tabular-nums text-crema-100">{h}</td></tr>' for d, h in HORARIO)}</tbody></table><p class="mt-2 text-xs text-crema-500">Martes y miércoles cerrado, salvo festivos. Horarios especiales en fiestas: los publicamos en Instagram.</p></dd></div>
        </dl>
        <div class="mt-8 flex flex-wrap gap-3">{boton('reservas.html', 'Reservar mesa')}<a href="{WHATSAPP}" target="_blank" rel="noopener" class="inline-flex items-center justify-center rounded-full border border-crema-100/30 px-7 py-3.5 font-semibold text-crema-100 transition hover:bg-white/10">WhatsApp</a><a href="{MAPA}" target="_blank" rel="noopener" class="inline-flex items-center justify-center rounded-full border border-crema-100/30 px-7 py-3.5 font-semibold text-crema-100 transition hover:bg-white/10">Cómo llegar</a></div>
      </div>
      <img src="img/fachada.webp" alt="Fachada de ladrillo y piedra de Auténticos CyL, con un barril de vino en la puerta" loading="lazy" class="aspect-[4/3] w-full rounded-3xl object-cover" />
    </section>

    <!-- Modal / Pop-up Fechas especiales y eventos -->
    <div id="modalEventoEspecial" class="fixed inset-0 z-50 hidden items-center justify-center bg-pizarra-950/80 p-4 backdrop-blur-md" role="dialog" aria-modal="true" aria-labelledby="tituloEventoModal">
      <div class="relative max-h-[90vh] w-full max-w-xl overflow-y-auto rounded-3xl border border-oro-400/40 bg-pizarra-900 p-6 shadow-2xl sm:p-8">
        <button onclick="cerrarModalEvento()" class="absolute right-4 top-4 grid h-9 w-9 place-items-center rounded-full bg-white/10 text-crema-300 transition hover:bg-white/20 hover:text-white" aria-label="Cerrar modal">
          <svg class="h-5 w-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" d="M6 6l12 12M18 6 6 18"/></svg>
        </button>
        
        <div class="inline-flex items-center gap-2 rounded-full border border-oro-400/40 bg-oro-400/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-oro-300">
          <svg class="h-4 w-4 fill-oro-400" viewBox="0 0 24 24"><path d="M12 2L15.09 8.26L22 9.27L17 14.14L18.18 21.02L12 17.77L5.82 21.02L7 14.14L2 9.27L8.91 8.26L12 2Z"/></svg>
          <span data-evento-etiqueta>Fechas especiales y eventos</span>
        </div>
        
        <h2 id="tituloEventoModal" class="mt-4 font-display text-3xl font-semibold leading-snug sm:text-4xl" data-evento-titulo>{e(EVENTO['titulo'])}</h2>
        <p class="mt-1 text-sm font-semibold uppercase tracking-widest text-oro-400" data-evento-fecha>{e(EVENTO['fecha'])}</p>
        
        <p class="mt-4 leading-relaxed text-crema-300" data-evento-desc>{e(EVENTO['descripcion'])}</p>
        
        <div class="mt-5 flex justify-center">
          <div class="relative w-full max-w-[260px] sm:max-w-[300px] aspect-[9/16] overflow-hidden rounded-2xl border border-white/10 bg-black shadow-2xl">
            <video id="videoEventoModal" src="{EVENTO['videoUrl']}" controls autoplay loop muted playsinline class="h-full w-full rounded-2xl object-cover"></video>
          </div>
        </div>

        <div class="mt-7 flex flex-wrap gap-3">
          <a href="reservas.html" class="flex-1 inline-flex items-center justify-center rounded-full bg-vino-500 px-6 py-3.5 font-semibold text-crema-100 transition hover:bg-vino-400">Reservar mesa</a>
          <button onclick="cerrarModalEvento()" class="rounded-full border border-crema-100/30 px-6 py-3.5 font-semibold text-crema-100 transition hover:bg-white/10">Entendido / Cerrar</button>
        </div>
      </div>
    </div>
  </main>
  <script>
    function cerrarModalEvento() {{
      const m = document.getElementById('modalEventoEspecial');
      if (m) {{ m.classList.replace('flex', 'hidden'); document.body.style.overflow = ''; }}
    }}
    function abrirModalEvento(evData) {{
      const m = document.getElementById('modalEventoEspecial');
      if (!m) return;
      document.querySelectorAll('[data-evento-titulo]').forEach(el => el.textContent = evData.titulo);
      document.querySelectorAll('[data-evento-fecha]').forEach(el => el.textContent = evData.fecha);
      document.querySelectorAll('[data-evento-desc]').forEach(el => el.textContent = evData.descripcion);
      if (evData.videoUrl) {{
        const v1 = document.getElementById('videoEventoSeccion');
        if (v1 && v1.getAttribute('src') !== evData.videoUrl) v1.src = evData.videoUrl;
        const v2 = document.getElementById('videoEventoModal');
        if (v2 && v2.getAttribute('src') !== evData.videoUrl) v2.src = evData.videoUrl;
      }}
      m.classList.replace('hidden', 'flex');
      document.body.style.overflow = 'hidden';
    }}
    function initEventoModal() {{
      let evData = null;
      try {{
        const local = localStorage.getItem('taperia-evento-especial');
        if (local) evData = JSON.parse(local);
      }} catch(e) {{}}
      if (!evData && window.TAPERIA) evData = window.TAPERIA.eventoEspecial;
      if (evData && evData.activo) {{
        abrirModalEvento(evData);
      }}
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', initEventoModal);
    }} else {{
      initEventoModal();
    }}
  </script>
''' + pie() + '</body>\n</html>\n'


# ---------------------------------------------------------------------------
# CARTA (solo consulta)
# ---------------------------------------------------------------------------
def plato(p):
    if p.get('estado') == 'oculto':
        return ''
    agotado = p.get('estado') == 'agotado'
    etiquetas = ('<span class="rounded-full bg-white/10 px-2.5 py-0.5 text-[11px] font-semibold text-crema-100">Agotado hoy</span>' if agotado else '') + ''.join(f'<span class="rounded-full bg-vino-500/15 px-2.5 py-0.5 text-[11px] font-semibold text-vino-300">{e(t)}</span>' for t in p['etiquetas'])
    alerg = f'<span class="text-xs text-crema-500" title="Alérgenos: {e(", ".join(ALERGENOS[a] for a in p["alergenos"]))}">({", ".join(map(str, p["alergenos"]))})</span>' if p['alergenos'] else ''
    foto = f'<img src="{p["foto"]}" alt="{e(p["nombre"])}" loading="lazy" class="h-20 w-20 shrink-0 rounded-2xl object-cover sm:h-24 sm:w-24" />' if p.get('foto') else ''
    precio = euros(p['precio']) + (' /ud.' if p['unidad'] else '')
    return f'''
          <li class="flex gap-4 py-5{" opacity-50" if agotado else ""}">
            {foto}
            <div class="min-w-0 flex-1">
              <div class="flex items-baseline justify-between gap-4">
                <h3 class="font-display text-[1.2rem] font-semibold leading-snug">{e(p["nombre"])}</h3>
                <p class="shrink-0 font-semibold tabular-nums text-oro-300">{precio}</p>
              </div>
              {f'<p class="mt-1 text-sm leading-relaxed text-crema-500">{e(p["desc"])}</p>' if p['desc'] else ''}
              {f'<div class="mt-2 flex flex-wrap items-center gap-1.5">{etiquetas} {alerg}</div>' if etiquetas or alerg else ''}
            </div>
          </li>'''


def seccion_carta(s):
    filas, grupo = [], None
    for p in (x for x in s['platos'] if x.get('estado') != 'oculto'):
        if p.get('grupo') and p['grupo'] != grupo:
            filas.append(f'</ul><h3 class="mt-8 flex items-center gap-3 text-xs font-semibold uppercase tracking-[.22em] text-oro-400">{e(p["grupo"])}<span class="h-px flex-1 bg-oro-400/25"></span></h3><ul class="divide-y divide-white/5">')
        grupo = p.get('grupo')
        filas.append(plato(p))
    foto = f'<img src="{s["foto"][0]}" alt="{e(s["foto"][1])}" loading="lazy" class="mb-8 h-56 w-full rounded-3xl object-cover object-[center_40%] sm:h-72" />' if s.get('foto') else ''
    return f'''
      <section id="{s["id"]}" class="pt-14">
        {foto}
        <p class="text-[11px] font-semibold uppercase tracking-[.3em] text-oro-400">{e(s["lema"])}</p>
        <h2 class="mt-2 font-display text-4xl font-semibold leading-tight">{e(s["nombre"])}</h2>
        <p class="mt-3 max-w-2xl italic leading-relaxed text-crema-500">{e(s["intro"])}</p>
        {f'<p class="mt-4 inline-block rounded-full border border-vino-400/40 bg-vino-500/15 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-vino-300">{e(s["aviso"])}</p>' if s.get('aviso') else ''}
        <ul class="mt-4 divide-y divide-white/5">{''.join(filas)}
        </ul>
        {f'<p class="mt-6 text-center font-display text-lg italic text-oro-300">{e(s["cierre"])}</p>' if s.get('cierre') else ''}
      </section>'''


def pagina_carta():
    secciones = CARTA['secciones']
    chips = ''.join(f'<a href="#{s["id"]}" class="shrink-0 rounded-full border border-white/10 px-4 py-2 text-sm font-semibold text-crema-300 transition hover:border-oro-400 hover:text-oro-300">{e(s["corto"])}</a>' for s in secciones)
    chips += '<a href="#bodega" class="shrink-0 rounded-full border border-white/10 px-4 py-2 text-sm font-semibold text-crema-300 transition hover:border-oro-400 hover:text-oro-300">Bodega</a>'
    leyenda = ' · '.join(f'<span><b class="text-oro-300">{n}</b> {a}</span>' for n, a in ALERGENOS.items())
    return cabeza('Carta · Auténticos CyL, Coca',
                  'Carta de Auténticos CyL: imprescindibles, carnes a la brasa y pescados, hamburguesas de autor para las cenas y repostería. Precios y alérgenos.') + cabecera('carta.html') + f'''
  <main class="mx-auto max-w-3xl px-5 pb-20">
    <header class="pt-14">
      <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Carta de {e(CARTA["temporada"].lower())}</p>
      <h1 class="mt-3 font-display text-5xl font-semibold">La carta</h1>
      <p class="mt-4 max-w-xl leading-relaxed text-crema-300">Producto de temporada, cocina a la brasa y una forma de entender la gastronomía donde tradición y creatividad se encuentran en cada plato.</p>
    </header>
    <nav class="sticky top-[61px] z-30 -mx-5 mt-8 border-y border-white/5 bg-pizarra-950/95 px-5 py-3 backdrop-blur" aria-label="Secciones de la carta">
      <div id="chipsCarta" class="no-scrollbar flex gap-2 overflow-x-auto">{chips}</div>
    </nav>
    <div id="secciones">{''.join(seccion_carta(s) for s in secciones)}
    </div>
    <section id="bodega" class="pt-14">
      <img src="img/tienda.webp" alt="Estanterías de vinos y productos de Castilla y León junto a la barra" loading="lazy" class="mb-8 h-56 w-full rounded-3xl object-cover sm:h-72" />
      <p class="text-[11px] font-semibold uppercase tracking-[.3em] text-oro-400">Vinos de Castilla y León</p>
      <h2 class="mt-2 font-display text-4xl font-semibold">Nuestra bodega</h2>
      <p class="mt-3 max-w-2xl leading-relaxed text-crema-300">Más de 500 referencias de Castilla y León en nuestra bodega y tienda: Ribera del Duero, Rueda, Toro, Bierzo, Cigales, León y muchas más. Pregúntanos y te recomendamos el vino perfecto para cada plato.</p>
    </section>
    <section class="mt-14 rounded-3xl border border-white/10 bg-pizarra-900 p-6 text-sm leading-relaxed text-crema-300">
      <p>Se cobrará un suplemento de <strong class="text-crema-100">1,50 €</strong> por servicio de pan y comensal. IVA incluido.</p>
      <p class="mt-3">Si tienes alguna alergia o intolerancia, pregunta a nuestro equipo. Los números junto a cada plato indican sus alérgenos:</p>
      <p class="mt-2 flex flex-wrap gap-x-3 gap-y-1 text-crema-500">{leyenda}</p>
    </section>
    <div class="mt-10 flex flex-wrap justify-center gap-3">{boton('reservas.html', 'Reservar mesa')}</div>
  </main>
''' + pie() + '''  <!-- Modo demostración: si el propietario ha publicado cambios desde su área, se muestran aquí -->
  <script src="js/carta-datos.js"></script>
  <script src="js/carta-render.js"></script>
</body>
</html>
'''


# ---------------------------------------------------------------------------
# NOTICIAS Y RECONOCIMIENTOS
# ---------------------------------------------------------------------------
def pagina_noticias():
    return cabeza('Noticias y reconocimientos · Auténticos CyL, Coca',
                  'Novedades de la carta, Las noches de Auténticos y reconocimientos del bar tapería Auténticos CyL en Coca (Segovia).') + cabecera('noticias.html') + f'''
  <main class="mx-auto max-w-6xl px-5 pb-20 pt-14">
    <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Noticias y reconocimientos</p>
    <h1 class="mt-3 font-display text-5xl font-semibold">Lo que pasa en Auténticos</h1>
    <p class="mt-4 max-w-xl leading-relaxed text-crema-300">Novedades de la carta, propuestas de temporada y lo que dicen de nosotros.</p>
    <section class="mt-12" aria-labelledby="tNoticias">
      <h2 id="tNoticias" class="sr-only">Noticias</h2>
      <div class="grid gap-6 md:grid-cols-2">{''.join(tarjeta_noticia(n, i == 0) for i, n in enumerate(NOTICIAS['noticias']))}
      </div>
    </section>
    <section class="mt-20" aria-labelledby="tReconocimientos">
      <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Reconocimientos</p>
      <h2 id="tReconocimientos" class="mt-3 font-display text-4xl font-semibold">Lo que dicen de nosotros</h2>
      <ul class="mt-8 grid gap-5 md:grid-cols-2">{bloque_reconocimientos()}
      </ul>
    </section>
    <div class="mt-14 flex flex-wrap gap-3">{boton('reservas.html', 'Reservar mesa')}{boton('carta.html', 'Ver la carta', False)}</div>
  </main>
''' + pie() + '</body>\n</html>\n'


# ---------------------------------------------------------------------------
# RESERVAS (solicitud)
# ---------------------------------------------------------------------------
def pagina_reservas():
    campo = 'mt-2 w-full rounded-2xl border border-white/10 bg-pizarra-800 px-4 py-3 text-crema-100 placeholder:text-crema-500 focus:border-oro-400 focus:outline-none'
    etiqueta = 'text-xs font-semibold uppercase tracking-[.2em] text-crema-500'
    return cabeza('Reservas · Auténticos CyL, Coca',
                  'Reserva mesa en Auténticos CyL, bar tapería en Coca (Segovia). Elige día, turno y número de personas y te confirmamos la reserva.') + cabecera('reservas.html') + f'''
  <main class="mx-auto grid max-w-6xl gap-12 px-5 pb-20 pt-14 lg:grid-cols-[1fr_22rem]">
    <div>
      <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Reservas</p>
      <h1 class="mt-3 font-display text-5xl font-semibold">Reserva tu mesa</h1>
      <p class="mt-4 max-w-xl leading-relaxed text-crema-300">Envíanos tu solicitud y te confirmamos la reserva por teléfono o WhatsApp lo antes posible.</p>

      <form id="formReserva" class="mt-10 grid gap-5 sm:grid-cols-2" novalidate>
        <label class="block"><span class="{etiqueta}">Día</span>
          <input name="fecha" type="date" required class="{campo}" /></label>
        <label class="block"><span class="{etiqueta}">Personas</span>
          <select name="personas" required class="{campo}"></select></label>
        <fieldset class="sm:col-span-2">
          <legend class="{etiqueta}">Turno</legend>
          <div class="mt-2 grid grid-cols-2 gap-3" id="turnos"></div>
        </fieldset>
        <fieldset class="sm:col-span-2">
          <legend class="{etiqueta}">Hora</legend>
          <div class="mt-2 flex flex-wrap gap-2" id="horas"></div>
        </fieldset>
        <label class="block"><span class="{etiqueta}">Nombre</span>
          <input name="nombre" required autocomplete="name" class="{campo}" /></label>
        <label class="block"><span class="{etiqueta}">Teléfono</span>
          <input name="telefono" type="tel" required autocomplete="tel" placeholder="600 000 000" class="{campo}" /></label>
        <label class="block sm:col-span-2"><span class="{etiqueta}">Email (opcional)</span>
          <input name="email" type="email" autocomplete="email" class="{campo}" /></label>
        <label class="block sm:col-span-2"><span class="{etiqueta}">Comentarios (opcional)</span>
          <textarea name="notas" rows="3" maxlength="300" placeholder="Alergias, trona, celebración, terraza…" class="{campo}"></textarea></label>
        <label class="flex items-start gap-3 text-sm text-crema-300 sm:col-span-2">
          <input name="privacidad" type="checkbox" required class="mt-1 h-5 w-5 accent-vino-500" />
          <span>He leído la <a href="privacidad.html" target="_blank" class="font-semibold text-oro-300 underline underline-offset-4">política de privacidad</a> y acepto que Auténticos CyL use mis datos solo para gestionar esta reserva.</span></label>
        <p class="-mt-2 text-xs leading-relaxed text-crema-500 sm:col-span-2"><b class="text-crema-300">Información básica sobre protección de datos.</b> Responsable: {e(TITULAR["nombre"])}. Finalidad: gestionar tu reserva y avisarte de su confirmación. Legitimación: tu solicitud de reserva. Destinatarios: no se ceden datos a terceros salvo obligación legal. Derechos: acceso, rectificación, supresión y demás derechos en {e(TITULAR["email"])}. Más información en la <a href="privacidad.html" class="underline underline-offset-4">política de privacidad</a>.</p>
        <p id="errorReserva" class="hidden rounded-2xl bg-vino-500/15 px-4 py-3 text-sm text-vino-300 sm:col-span-2" role="alert"></p>
        <button type="submit" class="rounded-full bg-vino-500 py-4 font-semibold text-crema-100 transition hover:bg-vino-400 sm:col-span-2">Solicitar reserva</button>
      </form>

      <div id="reservaOk" class="mt-10 hidden rounded-3xl border border-oro-400/30 bg-pizarra-900 p-7" role="status" tabindex="-1">
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Solicitud recibida</p>
        <h2 class="mt-2 font-display text-3xl font-semibold">¡Gracias, <span id="okNombre"></span>!</h2>
        <p id="okResumen" class="mt-3 leading-relaxed text-crema-300"></p>
        <p class="mt-3 text-sm text-crema-500">Te confirmaremos la reserva por teléfono o WhatsApp. Si necesitas cambiar algo, llámanos al <a href="tel:{TEL}" class="font-semibold text-crema-100">{TEL_VISIBLE}</a>.</p>
        <p class="mt-4 rounded-2xl bg-oro-400/10 px-4 py-3 text-xs leading-relaxed text-oro-300">Modo demostración: la solicitud se ha guardado en este navegador y ya aparece en el área de propietarios.</p>
        <button id="otraReserva" class="mt-6 rounded-full border border-crema-100/30 px-6 py-3 text-sm font-semibold">Hacer otra reserva</button>
      </div>
    </div>

    <aside class="space-y-5 lg:pt-28">
      <div class="rounded-3xl border border-white/10 bg-pizarra-900 p-6">
        <p class="font-display text-xl font-semibold">Cómo funciona</p>
        <ol class="mt-4 space-y-3 text-sm leading-relaxed text-crema-300">
          <li><b class="text-oro-300">1.</b> Elige día, turno, hora y número de personas.</li>
          <li><b class="text-oro-300">2.</b> Recibimos tu solicitud al momento.</li>
          <li><b class="text-oro-300">3.</b> Te confirmamos por teléfono o WhatsApp.</li>
        </ol>
      </div>
      <div class="rounded-3xl border border-white/10 bg-pizarra-900 p-6 text-sm leading-relaxed text-crema-300">
        <p class="font-display text-xl font-semibold text-crema-100">¿Prefieres llamar?</p>
        <p class="mt-2">Para grupos grandes o reservas para hoy, llámanos o escríbenos:</p>
        <a href="tel:{TEL}" class="mt-3 block text-2xl font-semibold text-oro-300">{TEL_VISIBLE}</a>
        <a href="{WHATSAPP}" target="_blank" rel="noopener" class="mt-3 inline-flex rounded-full border border-white/15 px-4 py-2 font-semibold text-crema-100">Escribir por WhatsApp</a>
      </div>
      <div class="rounded-3xl border border-vino-400/30 bg-vino-500/10 p-6 text-sm leading-relaxed text-crema-300">
        <p class="font-semibold text-vino-300">Las noches de Auténticos</p>
        <p class="mt-1">Nuestras hamburguesas de autor solo se sirven en el turno de cenas.</p>
        <p class="mt-3 text-crema-500">Cenas de jueves a domingo. Martes y miércoles cerrado, salvo festivos.</p>
      </div>
    </aside>
  </main>
''' + pie() + r'''
  <script>
  (() => {
    const C = window.TAPERIA, F = document.getElementById('formReserva'), $ = s => document.querySelector(s);
    const hoy = new Date(); const iso = d => new Date(d.getTime() - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
    F.fecha.min = iso(hoy); F.fecha.value = iso(hoy);
    F.personas.innerHTML = Array.from({ length: C.maxPersonasWeb }, (_, i) => `<option value="${i + 1}" ${i === 1 ? 'selected' : ''}>${i + 1} ${i ? 'personas' : 'persona'}</option>`).join('');
    let turno = 'cena', hora = '';
    const chip = (sel, extra = '') => `rounded-2xl border px-4 py-3 text-sm font-semibold transition ${sel ? 'border-oro-400 bg-oro-400/10 text-oro-300' : 'border-white/10 text-crema-300 hover:border-white/30'} ${extra}`;
    const hay = k => F.fecha.value && C.diasServicio[k].includes(new Date(F.fecha.value + 'T12:00').getDay());
    function pintar() {
      if (!hay(turno)) turno = Object.keys(C.turnos).find(hay) || turno;
      const ninguno = !Object.keys(C.turnos).some(hay);
      $('#turnos').innerHTML = Object.entries(C.turnos).map(([k, t]) => hay(k)
        ? `<button type="button" data-turno="${k}" aria-pressed="${k === turno}" class="${chip(k === turno)}">${t.nombre}<span class="block text-xs font-normal opacity-70">${t.horas[0]} – ${t.horas.at(-1)}</span></button>`
        : `<button type="button" disabled class="rounded-2xl border border-white/5 px-4 py-3 text-sm font-semibold text-crema-500/50">${t.nombre}<span class="block text-xs font-normal">Sin servicio este día</span></button>`).join('');
      if (ninguno) { hora = ''; $('#horas').innerHTML = '<p class="rounded-2xl bg-white/5 px-4 py-3 text-sm text-crema-300">Ese día no hay servicio de comidas ni cenas. Elige otro día.</p>'; return; }
      // Hoy no se ofrecen horas que ya han pasado (margen de 30 minutos)
      const ahora = new Date(Date.now() + 30 * 6e4), limite = F.fecha.value === iso(hoy) ? ahora.toTimeString().slice(0, 5) : '';
      const pasada = h => limite && h < limite;
      if (!C.turnos[turno].horas.includes(hora) || pasada(hora)) hora = '';
      $('#horas').innerHTML = C.turnos[turno].horas.map(h => pasada(h)
        ? `<button type="button" disabled class="min-w-[5.5rem] rounded-2xl border border-white/5 px-4 py-3 text-sm tabular-nums text-crema-500/40 line-through">${h}</button>`
        : `<button type="button" data-hora="${h}" aria-pressed="${h === hora}" class="${chip(h === hora, 'min-w-[5.5rem] tabular-nums')}">${h}</button>`).join('');
    }
    $('#turnos').addEventListener('click', ev => { const b = ev.target.closest('[data-turno]'); if (b) { turno = b.dataset.turno; pintar(); } });
    $('#horas').addEventListener('click', ev => { const b = ev.target.closest('[data-hora]'); if (b) { hora = b.dataset.hora; pintar(); } });
    F.fecha.addEventListener('change', pintar);
    pintar();
    const fechaLarga = s => new Date(s + 'T12:00').toLocaleDateString('es-ES', { weekday: 'long', day: 'numeric', month: 'long' });
    F.addEventListener('submit', ev => {
      ev.preventDefault();
      const f = Object.fromEntries(new FormData(F)), err = $('#errorReserva');
      const tel = (f.telefono || '').replace(/[\s.-]/g, '');
      const msg = !f.fecha || f.fecha < iso(hoy) ? 'Elige un día a partir de hoy.'
        : !hay(turno) ? 'Ese día no hay servicio: elige otro día.'
        : !hora ? 'Elige la hora a la que quieres venir.'
        : !f.nombre.trim() ? 'Escribe tu nombre.'
        : !/^\+?\d{9,15}$/.test(tel) ? 'Escribe un teléfono válido para poder confirmarte.'
        : f.email && !/^\S+@\S+\.\S+$/.test(f.email) ? 'El email no parece correcto.'
        : !f.privacidad ? 'Acepta el uso de tus datos para gestionar la reserva.' : '';
      if (msg) { err.textContent = msg; err.classList.remove('hidden'); return; }
      err.classList.add('hidden');
      const sol = { id: 'web-' + Date.now().toString(36), fecha: f.fecha, turno, hora, personas: +f.personas, nombre: f.nombre.trim(),
        telefono: tel, email: f.email.trim(), notas: f.notas.trim(), origen: 'web', estado: 'pendiente', creado: new Date().toISOString() };
      try { const l = JSON.parse(localStorage.getItem(C.claveSolicitudes) || '[]'); l.push(sol); localStorage.setItem(C.claveSolicitudes, JSON.stringify(l)); } catch (e) {}
      $('#okNombre').textContent = sol.nombre.split(' ')[0];
      $('#okResumen').textContent = `Has solicitado mesa para ${sol.personas} ${sol.personas === 1 ? 'persona' : 'personas'} el ${fechaLarga(sol.fecha)} a las ${sol.hora} (${C.turnos[turno].nombre.toLowerCase()}).`;
      F.classList.add('hidden'); const ok = $('#reservaOk'); ok.classList.remove('hidden'); ok.focus(); ok.scrollIntoView({ block: 'center' });
    });
    $('#otraReserva').addEventListener('click', () => { F.reset(); F.fecha.value = iso(hoy); F.personas.value = 2; hora = ''; pintar(); $('#reservaOk').classList.add('hidden'); F.classList.remove('hidden'); });
  })();
  </script>
</body>
</html>
'''


# ---------------------------------------------------------------------------
# TEXTOS LEGALES (LSSI-CE, RGPD y LOPDGDD)
# Texto base: el titular debe completar los datos entre corchetes y revisarlo
# con su asesoría antes de publicar.
# ---------------------------------------------------------------------------
def pagina_legal(archivo, titulo, descripcion, cuerpo):
    T = TITULAR
    return cabeza(f'{titulo} · Auténticos CyL', descripcion) + cabecera(archivo) + f'''
  <main class="mx-auto max-w-3xl px-5 pb-20 pt-14">
    <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Información legal</p>
    <h1 class="mt-3 font-display text-5xl font-semibold">{e(titulo)}</h1>
    <p class="mt-3 text-sm text-crema-500">Última actualización: {e(T["actualizado"])}</p>
    <p class="mt-6 rounded-2xl border border-oro-400/30 bg-oro-400/10 px-4 py-3 text-sm leading-relaxed text-oro-300">Web en modo demostración: los datos entre corchetes los tiene que completar el titular, y conviene que su asesoría revise el texto antes de publicar la web.</p>
    <div class="legal mt-10 space-y-4 leading-relaxed text-crema-300">{cuerpo}</div>
    <nav class="mt-14 flex flex-wrap gap-3 border-t border-white/5 pt-6 text-sm" aria-label="Otros textos legales">
      {''.join(f'<a href="{h}" class="rounded-full border border-white/10 px-4 py-2 {"text-oro-300" if h == archivo else "text-crema-300 hover:text-oro-300"}">{t}</a>' for h, t in LEGALES)}
    </nav>
  </main>
''' + pie() + '</body>\n</html>\n'


def h2(t):
    return f'<h2 class="pt-6 font-display text-2xl font-semibold text-crema-100">{t}</h2>'


def lista(items):
    return '<ul class="list-disc space-y-1.5 pl-6">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


def pagina_aviso_legal():
    T = TITULAR
    cuerpo = f'''
      {h2('1. Datos del titular')}
      <p>En cumplimiento del artículo 10 de la Ley 34/2002, de Servicios de la Sociedad de la Información y de Comercio Electrónico (LSSI-CE), estos son los datos del titular de esta web:</p>
      {lista([f'<b>Titular:</b> {e(T["nombre"])}', f'<b>NIF / CIF:</b> {e(T["nif"])}', f'<b>Nombre comercial:</b> Auténticos CyL · Bar Tapería y tienda',
              f'<b>Domicilio:</b> {e(T["domicilio"])}', f'<b>Correo electrónico:</b> <a class="text-oro-300 underline underline-offset-4" href="mailto:{T["email"]}">{e(T["email"])}</a>',
              f'<b>Teléfono:</b> <a class="text-oro-300 underline underline-offset-4" href="tel:{TEL}">{e(T["telefono"])}</a>', f'<b>Datos registrales:</b> {e(T["registro"])}',
              '<b>Actividad:</b> bar, restaurante y tienda de productos de alimentación de Castilla y León.'])}
      {h2('2. Objeto y condiciones de uso')}
      <p>Esta web informa sobre el restaurante y la tienda: carta, noticias, horario, ubicación y la posibilidad de solicitar una reserva. Al navegar por ella aceptas usarla de buena fe y conforme a la ley, sin dañar la web ni a terceros.</p>
      {h2('3. Reservas')}
      <p>El formulario de reservas envía una <b>solicitud</b>. La reserva queda hecha cuando el restaurante la confirma por teléfono o WhatsApp. Si no puedes venir, avísanos cuanto antes en el {e(T["telefono"])}. La reserva no tiene coste.</p>
      {h2('4. Carta, precios y alérgenos')}
      <p>La carta y los precios publicados son informativos y pueden cambiar según la temporada y el producto disponible. Los precios incluyen IVA. La información sobre alérgenos se ofrece según el Reglamento (UE) 1169/2011; si tienes alguna alergia o intolerancia, consúltalo siempre con nuestro equipo antes de pedir.</p>
      {h2('5. Propiedad intelectual e industrial')}
      <p>Los textos, las fotografías, el logotipo, el diseño de esta web y el nombre de dominio {e(T["dominio"])} pertenecen al titular o se usan con permiso, y no pueden reproducirse sin autorización. Se permite enlazar a esta web y citar sus contenidos sin ánimo de lucro, indicando la fuente. «Guía Repsol» y «Solete» son marcas de sus titulares; se citan solo para informar del reconocimiento recibido. El resto de marcas mencionadas pertenecen a sus respectivos propietarios.</p>
      {h2('6. Enlaces a otras webs')}
      <p>La web enlaza a servicios de terceros (Instagram, Facebook, Threads, WhatsApp, Google Maps, Tripadvisor, Guía Repsol, medios de comunicación y nuestra tienda online). El titular no se hace responsable de sus contenidos ni de sus políticas, que puedes consultar en cada uno.</p>
      {h2('7. Responsabilidad')}
      <p>El titular procura que la información sea correcta y esté al día, pero no garantiza la ausencia de errores ni la disponibilidad continua de la web, y no responde de los daños que pudieran derivarse de su uso indebido.</p>
      {h2('8. Legislación aplicable')}
      <p>Este aviso se rige por la legislación española. Para cualquier controversia con consumidores serán competentes los juzgados y tribunales del domicilio del consumidor.</p>'''
    return pagina_legal('aviso-legal.html', 'Aviso legal', 'Aviso legal de la web de Auténticos CyL, bar tapería y tienda en Coca (Segovia).', cuerpo)


def pagina_privacidad():
    T = TITULAR
    cuerpo = f'''
      <p>En Auténticos CyL tratamos tus datos personales con cuidado y solo para lo que nos pides. Esta política explica cómo, conforme al Reglamento (UE) 2016/679 (RGPD) y a la Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales (LOPDGDD).</p>
      {h2('1. Responsable del tratamiento')}
      {lista([f'<b>Responsable:</b> {e(T["nombre"])} · NIF / CIF {e(T["nif"])}', f'<b>Dirección:</b> {e(T["domicilio"])}',
              f'<b>Contacto:</b> <a class="text-oro-300 underline underline-offset-4" href="mailto:{T["email"]}">{e(T["email"])}</a> · {e(T["telefono"])}'])}
      {h2('2. Qué datos tratamos')}
      <p>Cuando solicitas una reserva: nombre, teléfono, email (si lo indicas), día, hora y número de personas, y los comentarios que quieras añadir. Si en los comentarios nos cuentas alergias o intolerancias, las usaremos solo para preparar tu visita; es voluntario y lo tratamos con tu consentimiento expreso.</p>
      <p>Si nos escribes por WhatsApp, teléfono, email o redes sociales, tratamos los datos que nos facilites para responderte.</p>
      <p><b>Asistente automático de WhatsApp.</b> Si nos escribes por WhatsApp, puede responderte primero un asistente automático con inteligencia artificial, que te lo indicará al empezar la conversación. Usa lo que le cuentes (nombre, teléfono, día, hora, número de personas y comentarios) solo para contestar tus preguntas sobre la carta, el horario y las reservas, y para dejarnos tu solicitud de reserva. No toma decisiones por nosotros: cada reserva la revisa y confirma una persona del equipo, y puedes pedir hablar con una persona en cualquier momento.</p>
      {h2('3. Para qué los usamos y con qué base legal')}
      {lista(['<b>Gestionar tu reserva</b> y contactarte para confirmarla, cambiarla o avisarte de cualquier incidencia. Base legal: la aplicación de medidas precontractuales a petición tuya (art. 6.1.b RGPD).',
              '<b>Tener en cuenta alergias o necesidades especiales</b> que nos indiques. Base legal: tu consentimiento explícito (art. 9.2.a RGPD), que puedes retirar cuando quieras.',
              '<b>Responder a tus consultas.</b> Base legal: tu consentimiento al escribirnos (art. 6.1.a RGPD).'])}
      <p>No usamos tus datos para enviarte publicidad ni tomamos decisiones automatizadas sobre ti.</p>
      {h2('4. Cuánto tiempo los guardamos')}
      <p>Durante el tiempo necesario para gestionar la reserva y, después, hasta un año como máximo, salvo que una obligación legal exija conservarlos más tiempo. Pasado ese plazo se borran.</p>
      {h2('5. Con quién los compartimos')}
      <p>No cedemos tus datos a terceros, salvo obligación legal. Pueden acceder a ellos los proveedores que nos prestan servicios técnicos (alojamiento de la web, WhatsApp y el proveedor de inteligencia artificial del asistente automático, si nos escribes por ese canal), siempre con las garantías que exige el RGPD. Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo, amparados en decisiones de adecuación o en cláusulas contractuales tipo de la Comisión Europea.</p>
      {h2('6. Tus derechos')}
      <p>Puedes pedir el acceso, la rectificación o la supresión de tus datos, la limitación u oposición a su tratamiento y su portabilidad, y retirar el consentimiento dado. Escríbenos a <a class="text-oro-300 underline underline-offset-4" href="mailto:{T["email"]}">{e(T["email"])}</a> indicando qué derecho quieres ejercer. Si crees que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos (<a class="text-oro-300 underline underline-offset-4" href="https://www.aepd.es" target="_blank" rel="noopener">www.aepd.es</a>).</p>
      {h2('7. Menores de edad')}
      <p>El formulario de reservas está pensado para mayores de 14 años. Si eres menor, pide a tu madre, padre o tutor que haga la reserva.</p>
      {h2('8. Seguridad')}
      <p>Aplicamos medidas técnicas y organizativas razonables para proteger tus datos frente a pérdidas, accesos no autorizados o usos indebidos.</p>'''
    return pagina_legal('privacidad.html', 'Política de privacidad', 'Cómo trata Auténticos CyL los datos personales de las reservas y consultas.', cuerpo)


def pagina_cookies():
    T = TITULAR
    cuerpo = f'''
      <p>Esta política explica qué cookies y tecnologías parecidas usa esta web, conforme al artículo 22.2 de la LSSI-CE y a la guía sobre cookies de la Agencia Española de Protección de Datos.</p>
      {h2('1. ¿Usamos cookies de seguimiento?')}
      <p><b>No.</b> Esta web no usa cookies de análisis, de publicidad ni de redes sociales, por eso no te mostramos un aviso para aceptarlas.</p>
      {h2('2. Almacenamiento técnico')}
      <p>La web guarda en tu navegador (almacenamiento local) solo lo necesario para que funcione lo que tú pides, por ejemplo la solicitud de reserva que envías o el acceso al área de propietarios. Es almacenamiento técnico, exento de consentimiento, y puedes borrarlo desde la configuración de tu navegador.</p>
      {h2('3. Servicios de terceros')}
      <p>Para mostrar la web cargamos las tipografías desde Google Fonts y una librería de estilos desde un servidor externo (CDN). Estos servicios reciben tu dirección IP para poder enviarte los archivos, pero no instalamos con ellos cookies de seguimiento.</p>
      <p>Los enlaces a Instagram, Facebook, Threads, WhatsApp, Google Maps, Tripadvisor o Guía Repsol te llevan a sus webs, que tienen sus propias políticas de cookies. Solo se aplican si pulsas el enlace.</p>
      {h2('4. Cómo gestionar las cookies')}
      <p>Puedes ver, bloquear o borrar las cookies y los datos guardados desde la configuración de tu navegador: Chrome, Safari, Firefox o Edge. Si en el futuro la web incorpora cookies no técnicas (por ejemplo, de estadísticas), te pediremos antes tu consentimiento y actualizaremos esta política.</p>
      {h2('5. Contacto')}
      <p>Si tienes cualquier duda, escríbenos a <a class="text-oro-300 underline underline-offset-4" href="mailto:{T["email"]}">{e(T["email"])}</a>.</p>'''
    return pagina_legal('cookies.html', 'Política de cookies', 'Política de cookies de la web de Auténticos CyL.', cuerpo)


def pagina_para_llevar():
    noches_sec = next((s for s in CARTA['secciones'] if s['id'] == 'noches'), CARTA['secciones'][0])
    hamburguesas = [p for p in noches_sec['platos'] if p.get('estado') != 'oculto']
    
    campo = 'mt-2 w-full rounded-2xl border border-white/10 bg-pizarra-800 px-4 py-3 text-crema-100 placeholder:text-crema-500 focus:border-oro-400 focus:outline-none'
    etiqueta = 'text-xs font-semibold uppercase tracking-[.2em] text-crema-500'
    
    platos_html = []
    for i, p in enumerate(hamburguesas):
        precio_str = euros(p['precio'])
        foto = f'<img src="{p["foto"]}" alt="{e(p["nombre"])}" loading="lazy" class="h-20 w-20 shrink-0 rounded-2xl object-cover sm:h-24 sm:w-24" />' if p.get('foto') else '<div class="h-20 w-20 shrink-0 rounded-2xl bg-white/5 grid place-items-center text-oro-400 font-display text-2xl font-semibold">🍔</div>'
        etiquetas = ''.join(f'<span class="rounded-full bg-vino-500/15 px-2.5 py-0.5 text-[11px] font-semibold text-vino-300">{e(t)}</span>' for t in p.get('etiquetas', []))
        alerg = f'<span class="text-xs text-crema-500">({", ".join(map(str, p["alergenos"]))})</span>' if p.get('alergenos') else ''
        
        platos_html.append(f'''
          <li class="flex flex-col gap-4 rounded-3xl border border-white/5 bg-pizarra-900 p-5 sm:flex-row sm:items-center sm:justify-between">
            <div class="flex items-start gap-4 min-w-0 flex-1">
              {foto}
              <div class="min-w-0 flex-1">
                <div class="flex flex-wrap items-baseline justify-between gap-2">
                  <h3 class="font-display text-xl font-semibold leading-snug">{e(p["nombre"])}</h3>
                  <p class="font-semibold tabular-nums text-oro-300">{precio_str}</p>
                </div>
                {f'<p class="mt-1 text-sm leading-relaxed text-crema-500">{e(p["desc"])}</p>' if p.get('desc') else ''}
                {f'<div class="mt-2 flex flex-wrap items-center gap-1.5">{etiquetas} {alerg}</div>' if etiquetas or alerg else ''}
              </div>
            </div>
            <div class="flex items-center justify-end gap-3 border-t border-white/5 pt-3 sm:border-t-0 sm:pt-0">
              <span class="text-xs text-crema-500 sm:hidden">Cantidad:</span>
              <div class="inline-flex items-center rounded-2xl border border-white/10 bg-pizarra-800 p-1">
                <button type="button" onclick="cambiarCant({i}, -1)" class="grid h-9 w-9 place-items-center rounded-xl bg-white/5 text-lg font-bold text-crema-100 hover:bg-white/10" aria-label="Restar una unidad">-</button>
                <input type="number" id="cant_{i}" data-nombre="{e(p['nombre'])}" data-precio="{p['precio']}" value="0" min="0" max="20" readonly class="w-12 text-center font-display text-lg font-semibold text-oro-300 bg-transparent focus:outline-none" />
                <button type="button" onclick="cambiarCant({i}, 1)" class="grid h-9 w-9 place-items-center rounded-xl bg-white/5 text-lg font-bold text-crema-100 hover:bg-white/10" aria-label="Sumar una unidad">+</button>
              </div>
            </div>
          </li>''')

    return cabeza('Para llevar · Auténticos CyL, Coca',
                  'Encarga tus hamburguesas de autor y bocados de Auténticos CyL para llevar en Coca (Segovia). Pedido online directo para recogida.') + cabecera('para-llevar.html') + f'''
  <main class="mx-auto max-w-4xl px-5 pb-20 pt-14">
    <header>
      <div class="inline-flex items-center gap-2 rounded-full border border-oro-400/40 bg-oro-400/10 px-3.5 py-1 text-xs font-semibold uppercase tracking-wider text-oro-300">
        <span>🍔 Servicio de recogida en local</span>
      </div>
      <h1 class="mt-3 font-display text-5xl font-semibold">Hamburguesas para llevar</h1>
      <p class="mt-4 max-w-2xl leading-relaxed text-crema-300">Haz tu pedido online y ven a recoger tus hamburguesas de autor y bocados de <strong class="text-crema-100">Las Noches de Auténticos</strong> recién hechos.</p>
    </header>

    <form id="formPedido" class="mt-10 space-y-8" novalidate>
      <section>
        <h2 class="font-display text-2xl font-semibold text-crema-100">1. Selecciona tus hamburguesas y bocados</h2>
        <p class="mt-1 text-sm text-crema-500">Elige la cantidad de cada plato que deseas encargar.</p>
        <ul class="mt-5 space-y-4">
          {''.join(platos_html)}
        </ul>
      </section>

      <section class="rounded-3xl border border-oro-400/30 bg-pizarra-900 p-6 sm:p-8">
        <h2 class="font-display text-2xl font-semibold text-crema-100">2. Datos de recogida y contacto</h2>
        <p class="mt-1 text-sm text-crema-500">Indica cuándo vienes a recoger tu pedido y cómo contactarte.</p>
        
        <div class="mt-6 grid gap-5 sm:grid-cols-2">
          <label class="block"><span class="{etiqueta}">Día de recogida</span>
            <input name="fecha" type="date" required class="{campo}" /></label>
          <label class="block"><span class="{etiqueta}">Hora aproximada de recogida</span>
            <select name="hora" required class="{campo}">
              <option value="20:30">20:30 h</option>
              <option value="21:00">21:00 h</option>
              <option value="21:30" selected>21:30 h</option>
              <option value="22:00">22:00 h</option>
              <option value="22:30">22:30 h</option>
              <option value="23:00">23:00 h</option>
            </select></label>
          <label class="block"><span class="{etiqueta}">Nombre completo</span>
            <input name="nombre" required autocomplete="name" placeholder="Tu nombre" class="{campo}" /></label>
          <label class="block"><span class="{etiqueta}">Teléfono de contacto</span>
            <input name="telefono" type="tel" required autocomplete="tel" placeholder="600 000 000" class="{campo}" /></label>
          <label class="block sm:col-span-2"><span class="{etiqueta}">Comentarios u observaciones (opcional)</span>
            <textarea name="notas" rows="2" placeholder="Punto de la carne, intolerancias, cebolla aparte..." class="{campo}"></textarea></label>
        </div>

        <!-- Resumen del pedido -->
        <div class="mt-8 rounded-2xl border border-white/10 bg-pizarra-800 p-5">
          <div class="flex items-center justify-between font-display text-xl font-semibold">
            <span>Total del pedido:</span>
            <span id="lblTotalPedido" class="tabular-nums text-oro-300">0,00 €</span>
          </div>
          <p id="lblResumenCant" class="mt-1 text-xs text-crema-500">0 productos seleccionados</p>
        </div>

        <label class="mt-6 flex items-start gap-3 text-sm text-crema-300">
          <input name="privacidad" type="checkbox" required class="mt-1 h-5 w-5 accent-vino-500" />
          <span>Acepto la <a href="privacidad.html" target="_blank" class="font-semibold text-oro-300 underline underline-offset-4">política de privacidad</a> para la gestión de este pedido para llevar.</span></label>

        <p id="errorPedido" class="mt-4 hidden rounded-2xl bg-vino-500/15 px-4 py-3 text-sm text-vino-300" role="alert"></p>

        <button type="submit" class="mt-6 w-full rounded-full bg-vino-500 py-4 font-semibold text-crema-100 transition hover:bg-vino-400">Confirmar y realizar pedido para llevar</button>
      </section>
    </form>

    <div id="pedidoOk" class="mt-10 hidden rounded-3xl border border-oro-400/40 bg-pizarra-900 p-8 text-center" role="status">
      <div class="mx-auto grid h-16 w-16 place-items-center rounded-full bg-oro-400 text-pizarra-950 font-display text-3xl font-bold">✓</div>
      <p class="mt-4 text-xs font-semibold uppercase tracking-[.3em] text-oro-400">Pedido registrado</p>
      <h2 class="mt-2 font-display text-3xl font-semibold">¡Muchas gracias, <span id="okCliente"></span>!</h2>
      <p id="okResumenPedido" class="mt-3 text-lg leading-relaxed text-crema-300"></p>
      <div id="okDetalleItems" class="mx-auto mt-4 max-w-md rounded-2xl border border-white/10 bg-pizarra-800 p-4 text-left text-sm text-crema-300"></div>
      <p class="mt-5 text-sm text-crema-500">Te confirmaremos la recogida por teléfono o WhatsApp. Si necesitas modificar tu pedido, llámanos al <a href="tel:{TEL}" class="font-semibold text-crema-100">{TEL_VISIBLE}</a>.</p>
      <a href="index.html" class="mt-8 inline-block rounded-full bg-vino-500 px-8 py-3.5 font-semibold text-crema-100 transition hover:bg-vino-400">Volver al inicio</a>
    </div>
  </main>

  <script src="js/config.js"></script>
  <script>
    function cambiarCant(idx, delta) {{
      const el = document.getElementById('cant_' + idx);
      if (!el) return;
      let val = (parseInt(el.value) || 0) + delta;
      if (val < 0) val = 0;
      if (val > 20) val = 20;
      el.value = val;
      actualizarTotal();
    }}

    function actualizarTotal() {{
      let total = 0, cantTotal = 0;
      document.querySelectorAll('[id^="cant_"]').forEach(el => {{
        const c = parseInt(el.value) || 0;
        const p = parseFloat(el.dataset.precio) || 0;
        total += c * p;
        cantTotal += c;
      }});
      const totalFmt = total.toFixed(2).replace('.', ',') + ' €';
      document.getElementById('lblTotalPedido').textContent = totalFmt;
      document.getElementById('lblResumenCant').textContent = cantTotal === 1 ? '1 producto seleccionado' : cantTotal + ' productos seleccionados';
    }}

    (() => {{
      const hoy = new Date();
      const iso = d => new Date(d.getTime() - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10);
      const F = document.getElementById('formPedido');
      if (F && F.fecha) {{
        F.fecha.min = iso(hoy);
        F.fecha.value = iso(hoy);
      }}

      F.addEventListener('submit', ev => {{
        ev.preventDefault();
        const err = document.getElementById('errorPedido');
        const items = [];
        let total = 0;

        document.querySelectorAll('[id^="cant_"]').forEach(el => {{
          const cantidad = parseInt(el.value) || 0;
          if (cantidad > 0) {{
            const nombre = el.dataset.nombre;
            const precio = parseFloat(el.dataset.precio) || 0;
            const subtotal = cantidad * precio;
            total += subtotal;
            items.push({{ nombre, cantidad, precio, subtotal }});
          }}
        }});

        const f = Object.fromEntries(new FormData(F));
        const tel = (f.telefono || '').replace(/[\\s.-]/g, '');

        let msg = '';
        if (items.length === 0) msg = 'Por favor, selecciona al menos 1 hamburguesa o bocado para llevar.';
        else if (!f.fecha) msg = 'Selecciona el día de recogida.';
        else if (!f.nombre.trim()) msg = 'Escribe tu nombre.';
        else if (!/^[0-9+]{{9,15}}$/.test(tel)) msg = 'Escribe un número de teléfono válido para contactarte.';
        else if (!f.privacidad) msg = 'Debes aceptar la política de privacidad para realizar el pedido.';

        if (msg) {{
          err.textContent = msg;
          err.classList.remove('hidden');
          return;
        }}
        err.classList.add('hidden');

        const pedidoObj = {{
          id: 'ped-' + Date.now().toString(36),
          fecha: f.fecha,
          hora: f.hora,
          cliente: f.nombre.trim(),
          telefono: tel,
          notas: (f.notas || '').trim(),
          items: items,
          total: total,
          estado: 'pendiente',
          origen: 'web',
          creado: new Date().toISOString()
        }};

        // Guardar pedido en localStorage
        try {{
          const key = (window.TAPERIA && window.TAPERIA.clavePedidos) || 'taperia-pedidos-web';
          const prev = JSON.parse(localStorage.getItem(key) || '[]');
          prev.push(pedidoObj);
          localStorage.setItem(key, JSON.stringify(prev));
        }} catch(e) {{}}

        // Mostrar pantalla de confirmación
        F.classList.add('hidden');
        document.getElementById('okCliente').textContent = pedidoObj.cliente.split(' ')[0];
        document.getElementById('okResumenPedido').textContent = `Tu pedido de ${{items.reduce((a,b)=>a+b.cantidad,0)}} productos (${{total.toFixed(2).replace('.', ',')}} €) ha sido registrado para recogida el ${{pedidoObj.fecha}} a las ${{pedidoObj.hora}} h.`;
        
        let htmlItems = '<p class="font-semibold text-oro-300 border-b border-white/10 pb-2 mb-2">Resumen de productos:</p><ul class="space-y-1">';
        items.forEach(it => {{
          htmlItems += `<li class="flex justify-between"><span>${{it.cantidad}}x ${{it.nombre}}</span><span class="tabular-nums font-semibold">${{it.subtotal.toFixed(2).replace('.', ',')}} €</span></li>`;
        }});
        htmlItems += '</ul>';
        document.getElementById('okDetalleItems').innerHTML = htmlItems;

        const okBox = document.getElementById('pedidoOk');
        okBox.classList.remove('hidden');
        okBox.scrollIntoView({{ block: 'center' }});
      }});
    }})();
  </script>
''' + pie() + '</body>\n</html>\n'


def datos_asistente():
    """Conocimiento para el asistente IA de WhatsApp: un único JSON que el agente (n8n)
    descarga de la web publicada. Se regenera con el resto de la web, así que siempre
    coincide con lo que ve el cliente. Ver docs/agente-whatsapp.md."""
    import re
    conf = (RAIZ / 'js' / 'config.js').read_text(encoding='utf-8')
    dias = {k: json.loads(v) for k, v in re.findall(r'(comida|cena):\s*(\[[0-9,\s]*\])', conf)}
    horas = {k: json.loads(v.replace("'", '"')) for k, v in re.findall(r'(comida|cena):\s*\{[^}]*horas:\s*(\[[^\]]*\])', conf)}
    nombres_dia = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
    carta = []
    for s in CARTA['secciones']:
        if s.get('estado') == 'oculto':
            continue
        carta.append({'seccion': s['nombre'], 'aviso': s.get('aviso') or None, 'platos': [
            {'nombre': pl['nombre'], 'descripcion': pl.get('desc') or None, 'precio': pl['precio'],
             'por_unidad': bool(pl.get('unidad')), 'alergenos': [ALERGENOS[a] for a in pl.get('alergenos', [])],
             'etiquetas': pl.get('etiquetas', []), 'agotado': pl.get('estado') == 'agotado'}
            for pl in s['platos'] if pl.get('estado') != 'oculto']})

    hamburguesas_para_llevar = []
    noches = next((s for s in CARTA['secciones'] if s['id'] == 'noches'), None)
    if noches:
        hamburguesas_para_llevar = [
            {'nombre': pl['nombre'], 'descripcion': pl.get('desc'), 'precio': pl['precio']}
            for pl in noches['platos'] if pl.get('estado') != 'oculto'
        ]

    return {
        'generado': 'tools/generar.py',
        'negocio': {'nombre': 'Auténticos CyL · Bar Tapería y Tienda', 'lema': LEMA, 'direccion': DIRECCION, 'como_llegar': MAPA,
                    'telefono': TEL_VISIBLE, 'whatsapp': TEL, 'email': TITULAR['email'], 'web': 'https://' + TITULAR['dominio'],
                    'tienda_online': TIENDA_ONLINE, 'reconocimientos': ['Solete Guía Repsol 2025'],
                    'redes': {n: u for n, u, _ in REDES}},
        'horario': {d: h for d, h in HORARIO}, 'horario_nota': 'Martes y miércoles cerrado, salvo festivos.',
        'reservas': {
            'turnos': {t: {'dias': [nombres_dia[d] for d in dias.get(t, [])], 'horas': horas.get(t, [])} for t in ('comida', 'cena')},
            'max_personas': 12,
            'reglas': ['El asistente nunca confirma una reserva: deja una solicitud pendiente y los propietarios la confirman por WhatsApp.',
                       'Grupos de más de 12 personas, menús de empresa y encargos: pasar el caso a una persona.',
                       'Para reservas en el mismo día, recomendar llamar al ' + TEL_VISIBLE + '.',
                       'Las noches de Auténticos (hamburguesas de autor) solo en servicio de cenas.']},
        'pedidos_para_llevar': {
            'disponible': True,
            'hacer_pedido_web': 'https://' + TITULAR['dominio'] + '/para-llevar.html',
            'instrucciones_agente': 'El asistente debe ofrecer activamente las hamburguesas de autor para llevar. Puede facilitar el enlace a la web para-llevar.html o recoger el pedido del cliente directamente por WhatsApp (productos deseados, día y hora de recogida, nombre y teléfono).',
            'hamburguesas_y_bocados': hamburguesas_para_llevar
        },
        'servicios': ['Hamburguesas y bocados de autor para llevar (pedido online en para-llevar.html o por WhatsApp/teléfono)',
                      'Comida para llevar (encargo por teléfono o WhatsApp)', 'Menús de empresa y grupos', 'Encargos de Navidad',
                      'Tienda de productos de Castilla y León: ' + ', '.join(TIENDA)],
        'alergenos_aviso': 'Informamos de los 14 alérgenos de declaración obligatoria (Reglamento UE 1169/2011). '
                           'Ante una alergia o intolerancia, avisar al personal: el asistente no puede garantizar la ausencia de trazas.',
        'carta': {'temporada': CARTA.get('temporada'), 'secciones': carta},
        'privacidad': 'https://' + TITULAR['dominio'] + '/privacidad.html'}


def main():
    for nombre, html in [('index.html', pagina_inicio()), ('carta.html', pagina_carta()),
                         ('para-llevar.html', pagina_para_llevar()),
                         ('noticias.html', pagina_noticias()), ('reservas.html', pagina_reservas()),
                         ('aviso-legal.html', pagina_aviso_legal()), ('privacidad.html', pagina_privacidad()),
                         ('cookies.html', pagina_cookies())]:
        (RAIZ / nombre).write_text(html, encoding='utf-8')
        print('escrito', nombre)
    # La carta base, para el editor de propietarios y para la carta de la demo
    (RAIZ / 'js' / 'carta-datos.js').write_text(
        '/* Generado por tools/generar.py a partir de datos/carta.json: no editar a mano */\n'
        'window.CARTA_BASE = ' + json.dumps(CARTA, ensure_ascii=False, indent=1) + ';\n', encoding='utf-8')
    print('escrito js/carta-datos.js')
    (RAIZ / 'datos' / 'asistente.json').write_text(json.dumps(datos_asistente(), ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('escrito datos/asistente.json')


if __name__ == '__main__':
    main()

