# Root Jewels 💎

A Greek and Latin roots match-three game for classroom practice.

## Game
The playable game belongs in `index.html`. GitHub Pages can serve it directly, including when embedded on Google Sites.

## Artwork
The `sprites/` folder is reserved for **ten reusable gemstones**, named `gem-01.png` through `gem-10.png`. Sprite names are independent of vocabulary roots so the weekly list can change.

Each gem should be a 128×128 transparent PNG with an uncluttered center for a dynamically rendered root label (up to seven letters). The game should use a fallback shape until a sprite is available.

Special effects (silver/gold borders and blast icons) should be overlays, not baked into the gem images.

## Next steps
1. Add the current game as `index.html`.
2. Move weekly root data into `roots.js`.
3. Update tile rendering to load `sprites/gem-01.png` ... `gem-10.png`, with existing CSS jewels as fallback.
4. Enable GitHub Pages: Settings → Pages → Deploy from a branch → main / (root).

