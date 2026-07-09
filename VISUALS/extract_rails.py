from PIL import Image
import numpy as np, os
V = os.path.dirname(os.path.abspath(__file__)) + '/'
OUT = V + 'frames/'
files = [('Black.png','black'), ('dark_wood.png','dark_wood'),
         ('med_oak.png','med_oak'), ('light_wood.png','light_wood'),
         ('white.png','white')]

def band_rows(gray, x0, x1):
    band = gray[:, x0:x1]
    std = band.std(axis=1)
    rows = np.where(std > 12)[0]
    if len(rows) == 0:  # white-on-white: fall back to edge gradient
        grad = np.abs(np.diff(band, axis=0)).mean(axis=1)
        rows = np.where(grad > 1.5)[0]
    return int(rows.min()), int(rows.max())

def longest_run(mask):
    best = cur = start = bs = 0
    for i, v in enumerate(mask):
        if v:
            if cur == 0: start = i
            cur += 1
            if cur > best: best, bs = cur, start
        else:
            cur = 0
    return bs, bs + best

for f, name in files:
    im = Image.open(V + f).convert('RGB')
    rot = im.rotate(-45, expand=True, resample=Image.BICUBIC,
                    fillcolor=(247, 246, 243))
    gray = np.asarray(rot.convert('L')).astype(float)
    W = rot.size[0]
    x0, x1 = int(W * 0.08), int(W * 0.45)
    r0, r1 = band_rows(gray, x0, x1)
    h = r1 - r0
    crop = rot.crop((x0, r0 + int(h*0.12), x1, r1 - int(h*0.12)))
    a = np.asarray(crop).astype(float)
    med = np.median(a.reshape(-1, 3), axis=0)
    dist = np.sqrt(((a - med) ** 2).sum(axis=2))
    tol = max(30.0, np.median(dist) * 3.5)
    colgood = (dist < tol).mean(axis=0) > 0.90
    rowgood = (dist < tol).mean(axis=1) > 0.90
    c0, c1 = longest_run(colgood)
    rr0, rr1 = longest_run(rowgood)
    if c1 - c0 > 60: c0 += 6; c1 -= 6
    else: c0, c1 = 0, crop.size[0]      # trim failed; keep axis whole
    if rr1 - rr0 > 30: rr0 += 3; rr1 -= 3
    else: rr0, rr1 = 0, crop.size[1]
    clean = crop.crop((c0, rr0, c1, rr1))
    clean.save(OUT + name + '_h.png')
    clean.transpose(Image.ROTATE_90).save(OUT + name + '_v.png')
    print(name, 'clean', clean.size, 'median RGB', med.astype(int).tolist())
print('done')
