# La Tapería de Auténticos CyL · Carta digital

Carta digital interactiva para móvil de **La Tapería de Auténticos CyL** (C/ Calixto del Río, 8 · Coca, Segovia), pensada para abrirse escaneando un código QR en la mesa.

> **Modo demostración:** los platos y precios son orientativos y se ajustarán a la carta real del local.

## Qué incluye

- **Carta por pestañas**, sin recargar la página: Tapas y Raciones (filtros Tradición / Vanguardia), Hamburguesas Gourmet, Vinoteca · Bodega de CyL y Postres Artesanales. También se cambia de sección deslizando el dedo.
- **Ficha de cada plato**: descripción, etiquetas, alérgenos, formato (tapa, media, ración, copa, botella…), cantidad e indicaciones para cocina.
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
- **Enlace directo a una sección:** `index.html#bodega` (también `#tapas`, `#hamburguesas` y `#postres`).

La carta está en el bloque `SECCIONES`. Cada plato tiene nombre, descripción, formatos con precio, alérgenos y etiquetas.

Un solo archivo HTML con Tailwind CSS por CDN, sin dependencias ni compilación.
