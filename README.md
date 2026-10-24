# Alejandra Rico, portfolio

Static portfolio site for Alejandra Rico Gómez, graphic designer. Plain HTML, CSS and images: no framework, no server code, runs on any static host.

## Structure

- `site/` the complete, ready-to-publish website (this folder is what gets hosted)
- `content/site.mjs` all text: bio, experience, projects, captions, links
- `content/images.json` image sizes used for layout
- `build.mjs` regenerates the HTML in `site/` from `content/site.mjs`
- `site/assets/styles.css` all styling
- `site/img/<project>/` project images (WebP)
- `tools/prepare_images.py` one-time script used to extract images from the PDF portfolio (not needed for edits)

## Edit text or projects

1. Edit `content/site.mjs`.
2. Run `node build.mjs` (Node 18 or newer).
3. Open `site/index.html` in a browser, or publish the `site/` folder.

## Add or replace images

Put WebP or JPG files in `site/img/<project-slug>/` named `01.webp`, `02.webp`, ... and update the width and height for that project in `content/images.json`. Then set the `gallery` rows in `content/site.mjs` and run `node build.mjs`.

## Hosting

- Vercel: `vercel.json` publishes the `site/` folder, no build step.
- Netlify, GitHub Pages, Cloudflare Pages or any web host: upload the contents of `site/`.
