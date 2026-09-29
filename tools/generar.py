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

TEL, TEL_VISIBLE = '+34921050483', '921 05 04 83'
DIRECCION = 'C/ Calixto del Río, 8 · 40480 Coca (Segovia)'
MAPA = 'https://www.google.com/maps/search/?api=1&query=Aut%C3%A9nticos+CyL+Calle+Calixto+del+R%C3%ADo+8+Coca+Segovia'
TIENDA_ONLINE = 'https://www.autenticoscyl.com/'
ALERGENOS = {1: 'Gluten', 2: 'Crustáceos', 3: 'Moluscos', 4: 'Pescado', 5: 'Huevos', 6: 'Soja', 7: 'Mostaza',
             8: 'Apio', 9: 'Frutos secos', 10: 'Cacahuetes', 11: 'Sésamo', 12: 'Sulfitos', 13: 'Lácteos', 14: 'Altramuces'}
NAV = [('index.html', 'Inicio'), ('carta.html', 'Carta'), ('noticias.html', 'Noticias'), ('reservas.html', 'Reservas')]

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
      <a href="index.html" class="min-w-0 leading-tight">
        <span class="block font-display text-xl font-semibold text-crema-100">Auténticos CyL</span>
        <span class="block text-[11px] font-semibold uppercase tracking-[.22em] text-oro-400">Bar Tapería · Tienda · Coca</span>
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
      </div>
      <div class="text-sm leading-relaxed text-crema-300">
        <p class="text-xs font-semibold uppercase tracking-[.22em] text-oro-400">Visítanos</p>
        <p class="mt-3">{e(DIRECCION)}</p>
        <p class="mt-1">Teléfono <a href="tel:{TEL}" class="font-semibold text-crema-100 hover:text-oro-300">{TEL_VISIBLE}</a></p>
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
    <p class="border-t border-white/5 px-5 py-5 text-center text-xs text-crema-500">© <span data-anio></span> Auténticos CyL · Coca (Segovia) · Web en modo demostración</p>
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


def tarjeta_noticia(n, grande=False):
    return f'''
        <article id="{n["id"]}" class="flex flex-col overflow-hidden rounded-3xl border border-white/5 bg-pizarra-900">
          <img src="{n["foto"]}" alt="" loading="lazy" class="{"aspect-[16/9]" if grande else "aspect-[4/3]"} w-full object-cover" />
          <div class="flex flex-1 flex-col p-6">
            <p class="text-[11px] font-semibold uppercase tracking-[.2em] text-oro-400">{e(n["fecha"])}</p>
            <h3 class="mt-2 font-display text-2xl font-semibold leading-snug">{e(n["titulo"])}</h3>
            <p class="mt-3 flex-1 leading-relaxed text-crema-300">{e(n["entradilla"])}</p>
            <a href="{n["enlace"][0]}" class="mt-5 font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">{e(n["enlace"][1])} →</a>
          </div>
        </article>'''


def bloque_reconocimientos():
    return ''.join(f'''
        <li class="rounded-3xl border border-oro-400/20 bg-oro-400/5 p-6">
          <p class="text-[11px] font-semibold uppercase tracking-[.2em] text-oro-400">{e(r["origen"])}</p>
          <p class="mt-2 font-display text-xl font-semibold leading-snug">{e(r["titulo"])}</p>
          <p class="mt-2 text-sm leading-relaxed text-crema-300">{e(r["texto"])}</p>
          {f'<a href="{r["enlace"]}" target="_blank" rel="noopener" class="mt-3 inline-block text-sm font-semibold text-oro-300 underline decoration-oro-400/40 underline-offset-4">Ver opiniones →</a>' if r.get("enlace") else ''}
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

    <!-- El restaurante -->
    <section id="restaurante" class="mx-auto grid max-w-6xl items-center gap-10 px-5 py-20 md:grid-cols-2 md:gap-16">
      <img src="img/local.webp" alt="Interior de la tapería: barra de madera con azulejos azules y mesas de madera" loading="lazy" class="aspect-[4/3] w-full rounded-3xl object-cover" />
      <div>
        <p class="text-xs font-semibold uppercase tracking-[.3em] text-oro-400">El restaurante</p>
        <h2 class="mt-3 font-display text-4xl font-semibold leading-tight">Tradición y creatividad en cada plato</h2>
        <p class="mt-5 leading-relaxed text-crema-300">Nuestra carta nace del mejor producto de temporada y de la cocina a la brasa. Respetamos el producto, el fuego y el tiempo para llevar cada ingrediente a su máxima expresión: platos memorables, honestos y sorprendentes.</p>
        <p class="mt-4 leading-relaxed text-crema-300">De día, los imprescindibles de siempre, las carnes maduradas al josper y el mar. Cuando cae el sol llegan <strong class="text-crema-100">Las noches de Auténticos</strong>: hamburguesas de autor y bocados para disfrutar sin prisas, solo en las cenas.</p>
        <div class="mt-8 flex flex-wrap gap-3">{boton('carta.html', 'Ver la carta')}{boton('reservas.html', 'Reservar', False)}</div>
      </div>
    </section>

    <!-- Destacados -->
    <section class="mx-auto max-w-6xl px-5 pb-20">
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
          <div><dt class="text-xs font-semibold uppercase tracking-[.2em] text-crema-500">Horario</dt><dd class="mt-1 text-crema-300">Llámanos para consultar el horario de cocina y de tienda.</dd></div>
        </dl>
        <div class="mt-8 flex flex-wrap gap-3">{boton('reservas.html', 'Reservar mesa')}<a href="{MAPA}" target="_blank" rel="noopener" class="inline-flex items-center justify-center rounded-full border border-crema-100/30 px-7 py-3.5 font-semibold text-crema-100 transition hover:bg-white/10">Cómo llegar</a></div>
      </div>
      <img src="img/fachada.webp" alt="Fachada de ladrillo y piedra de Auténticos CyL, con un barril de vino en la puerta" loading="lazy" class="aspect-[4/3] w-full rounded-3xl object-cover" />
    </section>
  </main>
''' + pie() + '</body>\n</html>\n'


# ---------------------------------------------------------------------------
# CARTA (solo consulta)
# ---------------------------------------------------------------------------
def plato(p):
    etiquetas = ''.join(f'<span class="rounded-full bg-vino-500/15 px-2.5 py-0.5 text-[11px] font-semibold text-vino-300">{e(t)}</span>' for t in p['etiquetas'])
    alerg = f'<span class="text-xs text-crema-500" title="Alérgenos: {e(", ".join(ALERGENOS[a] for a in p["alergenos"]))}">({", ".join(map(str, p["alergenos"]))})</span>' if p['alergenos'] else ''
    foto = f'<img src="{p["foto"]}" alt="{e(p["nombre"])}" loading="lazy" class="h-20 w-20 shrink-0 rounded-2xl object-cover sm:h-24 sm:w-24" />' if p.get('foto') else ''
    precio = euros(p['precio']) + (' /ud.' if p['unidad'] else '')
    return f'''
          <li class="flex gap-4 py-5">
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
    for p in s['platos']:
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
      <div class="no-scrollbar flex gap-2 overflow-x-auto">{chips}</div>
    </nav>
    {''.join(seccion_carta(s) for s in secciones)}
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
''' + pie() + '</body>\n</html>\n'


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
          <span>Acepto que Auténticos CyL use mis datos solo para gestionar esta reserva.</span></label>
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
        <p class="mt-2">Para grupos grandes o reservas para hoy, llámanos:</p>
        <a href="tel:{TEL}" class="mt-3 block text-2xl font-semibold text-oro-300">{TEL_VISIBLE}</a>
      </div>
      <div class="rounded-3xl border border-vino-400/30 bg-vino-500/10 p-6 text-sm leading-relaxed text-crema-300">
        <p class="font-semibold text-vino-300">Las noches de Auténticos</p>
        <p class="mt-1">Nuestras hamburguesas de autor solo se sirven en el turno de cenas.</p>
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
    function pintar() {
      $('#turnos').innerHTML = Object.entries(C.turnos).map(([k, t]) => `<button type="button" data-turno="${k}" aria-pressed="${k === turno}" class="${chip(k === turno)}">${t.nombre}<span class="block text-xs font-normal opacity-70">${t.horas[0]} – ${t.horas.at(-1)}</span></button>`).join('');
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


def main():
    for nombre, html in [('index.html', pagina_inicio()), ('carta.html', pagina_carta()),
                         ('noticias.html', pagina_noticias()), ('reservas.html', pagina_reservas())]:
        (RAIZ / nombre).write_text(html, encoding='utf-8')
        print('escrito', nombre)


if __name__ == '__main__':
    main()
