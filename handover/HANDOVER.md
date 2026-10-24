# Entrega del portafolio de Alejandra Rico

Sitio en vivo: https://alejandra-rico-portfolio.vercel.app
Repositorio: https://github.com/mashaincanada-beep/alejandra-rico-portfolio
Archivo listo para publicar: `alejandra-rico-portfolio-site.zip` (contiene la carpeta `site/` completa)

El sitio es estático (HTML, CSS e imágenes). No usa base de datos ni servidor, así que funciona en cualquier hosting y no tiene costo mensual en los planes gratuitos de Vercel o Netlify.

## Opción 1: Transferir el repositorio de GitHub y publicarlo en su propio Vercel (recomendada)

1. Alejandra crea una cuenta gratuita en https://github.com si no la tiene y le pasa su usuario a Masha.
2. Masha entra al repositorio en GitHub: Settings > General > Danger Zone > Transfer ownership, escribe el usuario de Alejandra y confirma.
3. Alejandra acepta la transferencia desde el correo que le llega de GitHub.
4. Alejandra crea una cuenta gratuita en https://vercel.com usando "Continue with GitHub".
5. En Vercel: Add New > Project > importa `alejandra-rico-portfolio` > Deploy. No hay que cambiar ninguna configuración: el archivo `vercel.json` ya indica que se publica la carpeta `site/`.
6. Cuando el sitio de Alejandra esté en línea, Masha puede borrar el proyecto de su propio Vercel para liberar el nombre.

Ventaja: cada cambio que Alejandra haga en el repositorio se publica solo.

## Opción 2: Transferir el proyecto de Vercel

1. Alejandra crea una cuenta gratuita en https://vercel.com.
2. Masha abre el proyecto `alejandra-rico-portfolio` en Vercel: Settings > General > Transfer Project, y elige la cuenta o el equipo de Alejandra (Vercel le enviará una invitación si es necesario).
3. Alejandra acepta. La dirección `alejandra-rico-portfolio.vercel.app` se mantiene.
4. Recomendado: hacer también la Opción 1 para que el código quede en el GitHub de Alejandra y volver a conectar el repositorio en Settings > Git.

## Opción 3: Arrastrar el ZIP a Netlify Drop o a cualquier hosting

1. Descomprimir `alejandra-rico-portfolio-site.zip`. Aparece una carpeta con `index.html`, `assets/`, `img/` y `work/`.
2. Ir a https://app.netlify.com/drop y arrastrar esa carpeta. En segundos el sitio queda publicado con una dirección de Netlify; creando una cuenta gratuita se puede conservar y cambiar el nombre.
3. Para cualquier otro hosting (Hostinger, GoDaddy, cPanel, GitHub Pages, Cloudflare Pages): subir el contenido de la carpeta a la raíz pública del sitio (`public_html` o similar).

## Dominio propio (opcional)

En Vercel o Netlify: Settings > Domains > agregar el dominio (por ejemplo `alejandrarico.com`) y seguir las instrucciones de DNS del proveedor donde se compró.

## Cómo editar textos

Todo el texto está en `content/site.mjs`. Después de editar, ejecutar `node build.mjs` (requiere Node 18 o superior) y publicar de nuevo. Más detalles en `README.md`.

## Pendiente por confirmar con Alejandra

- Fechas de cada empleo: sus documentos no coinciden, por eso el sitio muestra los cargos sin meses ni años.
- Si quiere agregar más trabajo de video o motion (el PDF no incluye piezas de video).
- La página de redes sociales de JCA en el PDF repite las mismas imágenes de Andina Dental, por eso no se incluyó.
