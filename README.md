# La Tapería de Auténticos CyL · Carta digital

Carta digital interactiva para móvil de **La Tapería de Auténticos CyL** (C/ Calixto del Río, 8 · Coca, Segovia), pensada para abrirse escaneando un código QR en la mesa.

> Carta real del local (verano): imprescindibles, brasa y mar, «Las noches de Auténticos» (solo cenas) y repostería, con sus precios y la numeración de alérgenos (1–14). **Modo demostración:** el pedido por WhatsApp está simulado y la selección de vinos es de ejemplo, a la espera de la carta de vinos.

## Qué incluye

- **Carta por pestañas**, sin recargar la página: Imprescindibles, Brasa y mar, Las Noches (hamburguesas de autor, solo cenas), Bodega CyL y Repostería. También se cambia de sección deslizando el dedo.
- **Ficha de cada plato**: descripción, etiquetas, alérgenos, formato (tapa, media, ración, copa, botella…), cantidad e indicaciones para cocina.
- **Suplemento de pan**: 1,50 € por comensal, que se indica en la comanda.
- **Comanda en tiempo real**: barra flotante con el número de artículos y el total, y un desglose donde se cambian cantidades, mesa, nombre y comentario. Se guarda en el navegador.
- **Envío por WhatsApp**: prepara un mensaje limpio con platos, cantidades y total, muestra cómo llegará y abre WhatsApp con el texto listo.

## Configuración

En `index.html`, bloque `CONFIG`:

```js
const CONFIG = {
  local: 'La Tapería de Auténticos CyL',
  whatsapp: ''   // móvil del WhatsApp del local, p. ej. '34600123456'
};
```

- Sin número (modo demostración), el botón abre WhatsApp con el mensaje escrito para elegir el contacto.
- **QR por mesa:** `index.html?mesa=5` muestra «Mesa 5» y la pone en la comanda.
- **Enlace directo a una sección:** `index.html#bodega` (también `#imprescindibles`, `#brasa`, `#noches` y `#postres`).

La carta está en el bloque `SECCIONES`. Cada plato tiene nombre, descripción, formatos con precio, alérgenos, etiquetas y, si hay, `foto`. Cada sección puede llevar una `foto` de cabecera. Las imágenes están en `img/` (webp, recortadas y optimizadas para móvil).

Un solo archivo HTML con Tailwind CSS por CDN, sin dependencias ni compilación.
