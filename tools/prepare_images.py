"""One-time image preparation from the PDF extraction staging folder.
Usage: python -I tools/prepare_images.py <staging_dir> <site_img_dir> <manifest_json>
Not needed to edit the site; kept for reference."""
import sys, json, os, glob
from PIL import Image
stg, out, man = sys.argv[1:4]
crops, emb, social, film = [os.path.join(stg, d) for d in ('crops','emb','social','film')]
plan = {
 'al-centro': [f'{crops}/al-centro-2.png', f'{crops}/al-centro-1.png', f'{crops}/al-centro-3.png', f'{emb}/x201.png', f'{crops}/al-centro-5.png'],
 'energizar': ['ENERGIZAR_LOGO', f'{crops}/energizar-1.png', f'{crops}/energizar-3.png', f'{emb}/x231.png', f'{crops}/energizar-5.png'],
 'jca': [f'{crops}/jca-1.png', f'{crops}/jca-2.png', f'{crops}/jca-3.png', f'{emb}/x255.png', f'{crops}/jca-5.png'],
 'fornatta': [f'{crops}/fornatta-1.png', f'{crops}/fornatta-3.png', f'{crops}/fornatta-2.png', f'{crops}/fornatta-4.png', f'{emb}/x303.png', f'{emb}/x305.png'],
 'mandato-centro': [f'{crops}/mandato-centro-5.png', f'{crops}/mandato-centro-1.png', f'{crops}/mandato-centro-2.png', f'{crops}/mandato-centro-3.png', f'{emb}/x329.png'],
 'accountability-report-2024': [f'{crops}/accountability-2024-{i}.png' for i in (4,1,2,3,5,6)],
 'accountability-report-2025': [f'{crops}/accountability-2025-{i}.png' for i in (4,1,2,3,5)],
 'music-film-events': [f'{crops}/music-film-{i}.png' for i in (1,2,3,4,5)],
 'cali-film-commission': [f'{film}/laptop.png', f'{film}/site-a.png', f'{film}/site-b.png'],
 'about': [f'{emb}/x139.png'],
}
for g in ('andina-dental','la-colina','cali-city-hall','pets-services','pulpas-rico','edison-giraldo','youth-council'):
    plan['social-'+g] = sorted(glob.glob(f'{social}/{g}-*.png'))
manifest = {}
for slug, files in plan.items():
    os.makedirs(f'{out}/{slug}', exist_ok=True); manifest[slug] = []
    for i, f in enumerate(files, 1):
        if f == 'ENERGIZAR_LOGO':
            src = Image.open(f'{crops}/energizar-2.png').convert('RGB')
            w, h = src.size; k = w / 458
            bg = src.getpixel((int(w*0.5), int(h*0.06)))
            src.paste(bg, (0, int(390*k), int(70*k), int(420*k)))
            box = (int(30*k), int(52*k), int(428*k), int(450*k))
            core = src.crop(box)
            pad = int(core.width * 0.18)
            im = Image.new('RGB', (core.width + 2*pad, core.height + 2*pad), bg)
            im.paste(core, (pad, pad))
            W = im.width; im.paste(bg, (int(W*0.08), int(W*0.76), int(W*0.22), int(W*0.92)))
        else:
            im = Image.open(f)
        alpha = im.mode in ('RGBA', 'LA', 'P') and slug == 'about'
        im = im.convert('RGBA' if alpha else 'RGB')
        cap = 700 if slug.startswith('social-') else (1100 if slug == 'about' else 1800)
        im.thumbnail((cap, cap), Image.LANCZOS)
        name = f'{i:02d}.webp'
        im.save(f'{out}/{slug}/{name}', 'WEBP', quality=82, method=6)
        manifest[slug].append({'src': f'img/{slug}/{name}', 'w': im.width, 'h': im.height})
json.dump(manifest, open(man, 'w'), indent=1)
print({k: len(v) for k, v in manifest.items()})

# Social media cover collage (4 x 3 square crops across clients)
picks = ['social-cali-city-hall/08', 'social-youth-council/01', 'social-andina-dental/03', 'social-pulpas-rico/02',
         'social-edison-giraldo/02', 'social-la-colina/03', 'social-pets-services/05', 'social-cali-city-hall/11',
         'social-pulpas-rico/03', 'social-youth-council/09', 'social-edison-giraldo/06', 'social-la-colina/12']
cell, gap, cols, rows = 340, 10, 4, 3
W, H = cols*cell + (cols+1)*gap, rows*cell + (rows+1)*gap
canvas = Image.new('RGB', (W, H), (31, 84, 59))
for n, pk in enumerate(picks):
    im = Image.open(f'{out}/{pk}.webp').convert('RGB')
    s = min(im.size); l = (im.width - s)//2; t = (im.height - s)//2
    im = im.crop((l, t, l+s, t+s)).resize((cell, cell), Image.LANCZOS)
    canvas.paste(im, (gap + (n % cols)*(cell+gap), gap + (n//cols)*(cell+gap)))
os.makedirs(f'{out}/social-media', exist_ok=True)
canvas.save(f'{out}/social-media/cover.webp', 'WEBP', quality=84, method=6)
manifest['social-media'] = [{'src': 'img/social-media/cover.webp', 'w': W, 'h': H}]
json.dump(manifest, open(man, 'w'), indent=1)
