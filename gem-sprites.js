// Root Jewels: sprite slots are stable across weekly vocabulary changes.
// Keep root labels as live text, not baked into artwork.
const GEM_SPRITES = Array.from({length:10},(_,i)=>`sprites/gem-${String(i+1).padStart(2,"0")}.png`);
