/* =============================================================================
   Carta publicada desde el área de propietarios (modo demostración)

   carta.html se genera con la carta de datos/carta.json. Si el propietario ha
   publicado cambios desde su área (gestor.html → Carta), esos cambios están en
   este navegador y se pintan aquí encima. Con una base de datos, este archivo
   leería la carta publicada del servidor en lugar de localStorage.
   ============================================================================= */
(function () {
  const CLAVE_PUBLICADA = 'taperia-carta-publicada';
  const ALERGENOS = { 1: 'Gluten', 2: 'Crustáceos', 3: 'Moluscos', 4: 'Pescado', 5: 'Huevos', 6: 'Soja', 7: 'Mostaza',
    8: 'Apio', 9: 'Frutos secos', 10: 'Cacahuetes', 11: 'Sésamo', 12: 'Sulfitos', 13: 'Lácteos', 14: 'Altramuces' };
  const esc = t => String(t ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const euros = n => Number(n).toLocaleString('es-ES', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + ' €';

  function leerPublicada() {
    try { const d = JSON.parse(localStorage.getItem(CLAVE_PUBLICADA)); if (d && Array.isArray(d.secciones)) return d; } catch (e) {}
    return null;
  }
  window.CartaDemo = { CLAVE_PUBLICADA, ALERGENOS, leerPublicada, euros, esc };

  function plato(p) {
    if (p.estado === 'oculto') return '';
    const agotado = p.estado === 'agotado';
    const etiquetas = (agotado ? '<span class="rounded-full bg-white/10 px-2.5 py-0.5 text-[11px] font-semibold text-crema-100">Agotado hoy</span>' : '')
      + (p.etiquetas || []).map(t => `<span class="rounded-full bg-vino-500/15 px-2.5 py-0.5 text-[11px] font-semibold text-vino-300">${esc(t)}</span>`).join('');
    const al = p.alergenos || [];
    const alerg = al.length ? `<span class="text-xs text-crema-500" title="Alérgenos: ${esc(al.map(a => ALERGENOS[a]).join(', '))}">(${al.join(', ')})</span>` : '';
    const foto = p.foto ? `<img src="${esc(p.foto)}" alt="${esc(p.nombre)}" loading="lazy" class="h-20 w-20 shrink-0 rounded-2xl object-cover sm:h-24 sm:w-24" />` : '';
    return `
          <li class="flex gap-4 py-5${agotado ? ' opacity-50' : ''}">
            ${foto}
            <div class="min-w-0 flex-1">
              <div class="flex items-baseline justify-between gap-4">
                <h3 class="font-display text-[1.2rem] font-semibold leading-snug">${esc(p.nombre)}</h3>
                <p class="shrink-0 font-semibold tabular-nums text-oro-300">${euros(p.precio)}${p.unidad ? ' /ud.' : ''}</p>
              </div>
              ${p.desc ? `<p class="mt-1 text-sm leading-relaxed text-crema-500">${esc(p.desc)}</p>` : ''}
              ${etiquetas || alerg ? `<div class="mt-2 flex flex-wrap items-center gap-1.5">${etiquetas} ${alerg}</div>` : ''}
            </div>
          </li>`;
  }
  function seccion(s) {
    let grupo = null;
    const filas = s.platos.filter(p => p.estado !== 'oculto').map(p => {
      let cab = '';
      if (p.grupo && p.grupo !== grupo) cab = `</ul><h3 class="mt-8 flex items-center gap-3 text-xs font-semibold uppercase tracking-[.22em] text-oro-400">${esc(p.grupo)}<span class="h-px flex-1 bg-oro-400/25"></span></h3><ul class="divide-y divide-white/5">`;
      grupo = p.grupo || null;
      return cab + plato(p);
    }).join('');
    const foto = s.foto ? `<img src="${esc(s.foto[0])}" alt="${esc(s.foto[1] || '')}" loading="lazy" class="mb-8 h-56 w-full rounded-3xl object-cover object-[center_40%] sm:h-72" />` : '';
    return `
      <section id="${esc(s.id)}" class="pt-14">
        ${foto}
        ${s.lema ? `<p class="text-[11px] font-semibold uppercase tracking-[.3em] text-oro-400">${esc(s.lema)}</p>` : ''}
        <h2 class="mt-2 font-display text-4xl font-semibold leading-tight">${esc(s.nombre)}</h2>
        ${s.intro ? `<p class="mt-3 max-w-2xl italic leading-relaxed text-crema-500">${esc(s.intro)}</p>` : ''}
        ${s.aviso ? `<p class="mt-4 inline-block rounded-full border border-vino-400/40 bg-vino-500/15 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-vino-300">${esc(s.aviso)}</p>` : ''}
        <ul class="mt-4 divide-y divide-white/5">${filas}
        </ul>
        ${s.cierre ? `<p class="mt-6 text-center font-display text-lg italic text-oro-300">${esc(s.cierre)}</p>` : ''}
      </section>`;
  }

  const cont = document.getElementById('secciones'), chips = document.getElementById('chipsCarta');
  const d = cont && leerPublicada();
  if (!d) return;
  const visibles = d.secciones.filter(s => !s.oculta);
  cont.innerHTML = visibles.map(seccion).join('');
  const clase = 'shrink-0 rounded-full border border-white/10 px-4 py-2 text-sm font-semibold text-crema-300 transition hover:border-oro-400 hover:text-oro-300';
  chips.innerHTML = visibles.map(s => `<a href="#${esc(s.id)}" class="${clase}">${esc(s.corto || s.nombre)}</a>`).join('') + `<a href="#bodega" class="${clase}">Bodega</a>`;
  if (location.hash) { const el = document.getElementById(location.hash.slice(1)); if (el) el.scrollIntoView(); }
})();
