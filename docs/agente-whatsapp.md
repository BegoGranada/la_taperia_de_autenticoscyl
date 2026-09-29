# Asistente IA por WhatsApp · Auténticos CyL

El asistente atiende el WhatsApp del bar (647 41 31 86) a cualquier hora:

- contesta dudas sobre la carta, los alérgenos, el horario, la tienda y cómo llegar;
- recoge solicitudes de reserva;
- pasa a una persona todo lo que no le corresponde.

**Nunca confirma una reserva.** Deja la solicitud **pendiente** y los propietarios la confirman desde el área de propietarios, como las que llegan desde la web.

```
Cliente escribe por WhatsApp
      │
      ▼
Asistente (n8n + modelo de IA) ── lee ──► datos/asistente.json  (horario, turnos, carta, alérgenos, servicios)
      │
      ├─ pregunta resuelta ─────────────► responde
      ├─ quiere reservar ──── crea ─────► solicitud "pendiente" · origen "agente"
      │                                        │
      │                                        ▼
      │                           gestor.html › Solicitudes (etiqueta 🤖 Agente IA)
      │                                        │ Confirmar / Rechazar
      │                                        ▼
      │                           «Avisar por WhatsApp» al cliente
      └─ grupo grande, queja, encargo… ► aviso a los propietarios (pasa a una persona)
```

## 1. Conocimiento: `datos/asistente.json`

`tools/generar.py` genera este archivo junto con el resto de la web, a partir de:

- `datos/carta.json`;
- `js/config.js`;
- las constantes del propio generador: horario, dirección, redes y datos del titular.

Así, el asistente dice siempre lo mismo que la web. El archivo contiene:

| Clave | Contenido |
|---|---|
| `negocio` | Nombre, dirección, enlace de Google Maps, teléfono, email, web, tienda online, Solete y redes |
| `horario` | Horario de apertura por día. Nota: martes y miércoles cerrado, salvo festivos |
| `reservas.turnos` | Días y horas que se pueden reservar para comida y cena (los mismos que el formulario de la web) |
| `reservas.max_personas` | 12. A partir de ahí, lo gestiona una persona |
| `reservas.reglas` | Reglas de negocio que el asistente debe respetar |
| `servicios` | Comida para llevar, menús de grupo, encargos de Navidad y productos de la tienda |
| `carta` | Secciones y platos con precio, alérgenos (por nombre), etiquetas y si están agotados. No incluye lo oculto |
| `alergenos_aviso` | Texto que el asistente debe dar ante cualquier alergia |

En n8n se descarga con un nodo *HTTP Request*:

```
GET https://www.autenticoscyl.com/datos/asistente.json
```

Conviene guardarlo en caché unos minutos.

> Cuando la carta se guarde en una base de datos (el botón **Publicar** del editor de propietarios), el asistente leerá esa misma fuente. Así sabrá al momento si un plato está **agotado hoy**.

## 2. Herramientas del agente

| Herramienta | Qué hace | Cuándo |
|---|---|---|
| `info_local()` | Devuelve `negocio`, `horario`, `servicios` | Horario, dirección, cómo llegar, tienda, parking… |
| `consultar_carta(texto?, alergeno?)` | Filtra `carta` por nombre, sección o sin un alérgeno | «¿Qué tenéis sin gluten?», «¿Cuánto cuestan las croquetas?» |
| `turnos_disponibles(fecha)` | Aplica `reservas.turnos` a la fecha: devuelve comida/cena y horas o «cerrado» | Antes de proponer hora |
| `crear_solicitud(fecha, turno, hora, personas, nombre, telefono, notas)` | Registra la solicitud **pendiente** con `origen: "agente"` | El cliente quiere reservar y ha dado todos los datos |
| `avisar_propietarios(motivo, resumen)` | Mensaje al WhatsApp o email de los propietarios | Grupos de más de 12, menús de empresa, encargos, quejas, o cuando el cliente pide hablar con una persona |

Cómo funciona `crear_solicitud`:

- **Hoy, en la demo:** las solicitudes se guardan en el navegador, así que el agente todavía no tiene dónde escribir.
- **En producción:** se usa el mismo esquema que en Cabañas Los Pinos, con Supabase:
  - una tabla `reservas`;
  - una función pública `rpc/crear_solicitud` que valida día, turno, hora y aforo, y devuelve el `id` o un error en español;
  - el origen: `p_origen = "agente"`.
- El gestor ya muestra estas solicitudes con la etiqueta **🤖 Agente IA**.

## 3. Instrucciones para el agente (prompt de sistema sugerido)

```
Eres el asistente de WhatsApp de Auténticos CyL, bar tapería y tienda de productos de
Castilla y León en Coca (Segovia), Solete Guía Repsol 2025.

- En tu primer mensaje di que eres un asistente automático y que, si lo prefieren,
  pueden hablar con una persona.
- Tutea con cercanía, frases cortas, en el idioma del cliente. Sin inventar: si no está en
  tus datos, dilo y ofrece pasar el mensaje al equipo.
- Horario y turnos: usa solo info_local() y turnos_disponibles(). Martes y miércoles
  cerrado salvo festivos.
- Reservas: pide día, comida o cena, hora, personas, nombre y teléfono. Comprueba el turno
  y crea la solicitud. Di siempre: «Te la confirmamos por WhatsApp en cuanto la revisemos».
  Nunca digas que está confirmada.
- Más de 12 personas, menús de empresa, encargos de Navidad o comida para llevar: recoge
  los datos y usa avisar_propietarios().
- Alérgenos: informa de los que figuran en la carta y añade siempre que avisen al
  personal al llegar; no garantices la ausencia de trazas.
- Si el cliente está molesto o pide una persona: avisar_propietarios() y díselo.
- No pidas datos que no necesites (nada de DNI ni datos bancarios). Si preguntan por sus
  datos, enlaza la política de privacidad.
```

## 4. Requisitos legales

- **Transparencia (Reglamento UE 2024/1689 de IA, art. 50):** el cliente debe saber que habla con un sistema automático. El prompt obliga a decirlo en el primer mensaje.
- **Protección de datos:** la política de privacidad (`privacidad.html`) ya explica el asistente, para qué usa los datos, que una persona revisa cada reserva y que el proveedor de IA trata los datos.
  - Hay que firmar el contrato de encargado del tratamiento con los proveedores: n8n o VPS, proveedor del modelo de IA y WhatsApp Business.
- **Sin decisiones automatizadas:** el asistente no acepta ni rechaza reservas. Lo hace siempre una persona (art. 22 RGPD).

## 5. Qué hace falta para ponerlo en marcha

1. Número de WhatsApp Business del bar conectado a la API de WhatsApp Cloud (Meta).
2. El flujo de n8n del asistente: el disparador de WhatsApp, el agente con las herramientas de la sección 2 y el modelo de IA.
3. La base de datos de reservas (sección 2), para que las solicitudes del agente lleguen al gestor.
4. Publicar la web, para que `datos/asistente.json` esté accesible.
5. Probar conversaciones reales con los propietarios antes de abrirlo al público.
