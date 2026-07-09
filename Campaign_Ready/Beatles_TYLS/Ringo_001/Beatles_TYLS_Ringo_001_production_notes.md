# Beatles TYLS Ringo 001 - Production Notes

Approved image:

- `Beatles_TYLS_Ringo_001_approved_image.png`

QA crop:

- `Beatles_TYLS_Ringo_001_frame_crop_QA.png`

Reusable blank scene:

- `Beatles_TYLS_Ringo_001_reusable_blank_scene.png`

Source image:

- `/home/Phil/Codex-Projects/Pickart_Website_Redesign/CAMPAIGN_ASSETS/Beatles_TYLS/enhanced/ringo-starr_landscape.jpg`

Workflow that worked:

1. Generate a strong room-context image with a clean blank framed aperture.
2. Save the blank scene for reuse.
3. Phil marks four visible aperture corners in GIMP with magenta dots.
4. Detect the dot coordinates and use them as the true frame opening.
5. Crop the source print to remove its campaign border and let the mat visually cover a little of the image edge.
6. Perspective-map the exact source pixels into the marked aperture.
7. Export both the full mockup and a 100% frame crop for QA.

Phil-approved aperture dots for this image:

- Top-left: approximately `(992,190)`
- Top-right: approximately `(1194,181)`
- Bottom-right: approximately `(1194,366)`
- Bottom-left: approximately `(993,368)`

Important rule:

Do not ask AI to regenerate recognisable Beatles faces inside the frame. AI can generate the room and blank frame; the product image must be inserted from exact source pixels, with any AI blend pass limited to mat/frame/glass edges only.
