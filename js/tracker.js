// =============================================================================
// Monitorización de Actividad y Pruebas del Cliente - Auténticos CyL
// Granada IAtech CRM Telemetry
// =============================================================================
(function() {
    try {
        const path = window.location.pathname;
        const file = path.split('/').pop() || 'index.html';
        const pageTitle = document.title || 'Auténticos CyL';

        const sections = {
            'index.html': '🏠 Portada Principal',
            'carta.html': '🍷 Carta de Platos y Vinos',
            'reservas.html': '📅 Motor de Reservas Online',
            'gestor.html': '🔐 Panel de Gestión / Propietarios',
            'para-llevar.html': '🥡 Carta Para Llevar / Take Away',
            'noticias.html': '📰 Noticias y Novedades'
        };
        const friendlyName = sections[file] || ('📄 ' + file);

        const API = (window.TAPERIA && window.TAPERIA.apiUrl) ? window.TAPERIA.apiUrl : 'https://granadaiatech.com/api/taperia';
        fetch(`${API}/track`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                page: friendlyName,
                file: file,
                title: pageTitle,
                referrer: document.referrer || null,
                screen: `${window.innerWidth}x${window.innerHeight}`
            })
        }).catch(function() {});
    } catch(e) {}
})();
