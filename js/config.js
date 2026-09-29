/* =============================================================================
   Configuración común de la web y del área de propietarios
   ============================================================================= */
window.TAPERIA = {
  nombre: 'Auténticos CyL · Bar Tapería',
  telefono: '34921050483',          // formato internacional sin "+"
  telefonoVisible: '921 05 04 83',
  whatsapp: '',                     // móvil de WhatsApp del local, p. ej. '34600123456' (vacío = sin configurar)
  direccion: 'C/ Calixto del Río, 8 · 40480 Coca (Segovia)',
  // Horas que se ofrecen en el formulario de reservas (orientativas: ajustar al horario real)
  turnos: {
    comida: { nombre: 'Comida', horas: ['13:30', '14:00', '14:30', '15:00', '15:30'] },
    cena:   { nombre: 'Cena',   horas: ['20:30', '21:00', '21:30', '22:00', '22:30'] }
  },
  maxPersonasWeb: 12,               // grupos mayores: por teléfono
  // Demostración: las solicitudes de la web se guardan en este navegador y el área
  // de propietarios las recoge de aquí. Con una base de datos se sustituye por una API.
  claveSolicitudes: 'taperia-solicitudes-web'
};
