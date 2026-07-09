from PIL import Image
import numpy as np, os
V = os.path.dirname(os.path.abspath(__file__)) + '/'
OUT = V + 'frames/'
im = Image.open(V + 'white.png').convert('RGB')
rot = im.rotate(-45, expand=True, resample=Image.BICUBIC,
                fillcolor=(247, 246, 243))
a = np.asarray(rot.convert('L')).astype(float)
W = rot.size[0]
x0, x1 = int(W * 0.08), int(W * 0.42)
band = a[:, x0:x1]
# vertical gradient: rail edges show as horizontal lines even on white
grad = np.abs(np.diff(band, axis=0)).mean(axis=1)
rows = np.where(grad > 1.5)[0]
print('edge rows found:', len(rows), rows.min() if len(rows) else '-',
      rows.max() if len(rows) else '-')
r0, r1 = int(rows.min()), int(rows.max())
h = r1 - r0
r0i, r1i = r0 + int(h * 0.16), r1 - int(h * 0.16)
crop = rot.crop((x0, r0i, x1, r1i))
crop.save(OUT + 'white_h.png')
crop.transpose(Image.ROTATE_90).save(OUT + 'white_v.png')
print('white band rows', r0, r1, 'crop', crop.size)
