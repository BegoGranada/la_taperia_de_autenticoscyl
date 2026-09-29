# Auténticos CyL · Web del bar tapería y tienda

Web de **Auténticos CyL** (C/ Calixto del Río, 8 · Coca, Segovia): bar tapería y tienda de productos de Castilla y León, a los pies del castillo de Coca.

> **Modo demostración:** las reservas se guardan en el navegador (no hay base de datos todavía).

## Páginas

| Página | Qué es |
|---|---|
| `index.html` | **Inicio**: el restaurante, platos destacados, la tienda, Las noches de Auténticos, noticias y dónde estamos. |
| `carta.html` | **Carta** de verano, solo para consultar: imprescindibles, brasa y mar, Las noches de Auténticos (solo cenas), repostería y bodega. Incluye precios, alérgenos (1–14) y suplemento de pan. |
| `noticias.html` | **Noticias y reconocimientos**. |
| `reservas.html` | **Reservas**: formulario de solicitud (día, turno, hora, personas y datos de contacto). |
| `gestor.html` | **Área de propietarios**: agenda por día y turno, aforo, solicitudes pendientes (confirmar o rechazar), llegadas y no presentados, reservas a mano, llamada y WhatsApp con mensaje de confirmación preparado. |

Todas las páginas públicas tienen el mismo menú: Inicio · Carta · Noticias · Reservas · Propietarios.

## Editar el contenido

Las páginas públicas se generan con `python3 tools/generar.py`. Para cambiar el contenido:

- **Carta:** `datos/carta.json` (secciones, platos, precios, alérgenos y fotos).
- **Noticias y reconocimientos:** `datos/noticias.json`.
- **Teléfono, WhatsApp, horas y días de servicio:** `js/config.js`. Lo usan la web y el área de propietarios. El horario del bar y la tienda está en `HORARIO`, dentro de `tools/generar.py`.
- **Fotos:** `img/` (webp optimizado para móvil).

Después de editar, vuelve a ejecutar `python3 tools/generar.py`.

## Cómo funciona la demo de reservas

1. El cliente envía una solicitud en `reservas.html`.
2. La solicitud se guarda en el navegador.
3. Al entrar en `gestor.html` desde el mismo navegador, aparece como **pendiente** en *Solicitudes*.
4. Al confirmarla, el gestor ofrece avisar al cliente por WhatsApp con el mensaje ya escrito.

Para usarlo de verdad hay que sustituir el guardado en el navegador por una base de datos, como se hizo en el gestor de Cabañas Los Pinos.
