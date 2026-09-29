/* =============================================================================
   Configuración común de la web y del área de propietarios
   ============================================================================= */
window.TAPERIA = {
  nombre: 'Auténticos CyL · Bar Tapería',
  telefono: '34647413186',          // formato internacional sin "+"
  telefonoVisible: '647 41 31 86',
  whatsapp: '34647413186',          // WhatsApp del local
  direccion: 'C/ Calixto del Río, 8 · 40480 Coca (Segovia)',
  // Horas que se ofrecen en el formulario de reservas
  turnos: {
    comida: { nombre: 'Comida', horas: ['13:30', '14:00', '14:30', '15:00', '15:30'] },
    cena:   { nombre: 'Cena',   horas: ['20:30', '21:00', '21:30', '22:00', '22:30'] }
  },
  // Días con servicio de cada turno (0 = domingo … 6 = sábado), según el horario
  // publicado: martes solo mañana (sin comidas ni cenas); lunes y miércoles cierra
  // a las 20:00 (sin cenas); de jueves a domingo abre hasta la noche.
  diasServicio: {
    comida: [0, 1, 3, 4, 5, 6],
    cena:   [0, 4, 5, 6]
  },
  maxPersonasWeb: 12,               // grupos mayores: por teléfono
  // Demostración: las solicitudes de la web se guardan en este navegador y el área
  // de propietarios las recoge de aquí. Con una base de datos se sustituye por una API.
  claveSolicitudes: 'taperia-solicitudes-web'
};
