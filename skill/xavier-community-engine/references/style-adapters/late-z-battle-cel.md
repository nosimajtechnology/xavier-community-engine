# Late-Z Battle Cel Adapter v1.2

## Purpose and activation

Adapter ID: `late-z-battle-cel-v1`

Adapter version: `1.2`

Display signifier: `LATE-Z BATTLE CEL`

Use for Xavier images and cinematics that request Late-Z Battle Cel,
Buu-era-inspired, original mid-1990s broadcast battle anime, or an approved
project image in that treatment. This render-and-motion adapter replaces the
flagship PS2 build while active. Do not mix cel animation with 3D game
rendering unless the user explicitly requests a hybrid.

Borrow period production grammar only. Do not add franchise characters,
costumes, symbols, attacks, locations, logos, or story canon unless the user
separately requests them.

## Reference assignments

- `../../assets/xavier-canonical-reference.png` remains immutable authority for
  Xavier's face, body, asymmetry, costume, proportions, and underlying identity.
- `../../assets/xavier-leg-authority.png` remains the supplemental authority for
  lower-body joint direction, segment count, silhouette, and shoes whenever
  Xavier's legs may be visible.
- `../../assets/style-adapters/late-z-battle-cel/xavier-late-z-character-sheet-v1.png`
  is the bundled Late-Z translation authority for front, three-quarter,
  profile, rear, face, and snake-arm construction; warm umber cel palette;
  blond hair mass; beak, eye, snake, costume, and line treatment; and sheet-local
  surface simplification. Every visible face in this authority uses the
  closed-mouth `DEADPAN_CANONICAL` neutral expression. Its SHA-256 is
  `2ceee8b0607bf2ba1b387f088ee237f73138c538976ac5f0067ff3af89306706`.
- A user-approved project image controls current rendering, wardrobe,
  environment, lighting, pose, and continuity.
- Inspected original 1994-1996 television broadcast captures control line,
  paint, camera, motion, restrained analog softness, and period color behavior
  only. Reject promotional art, remasters, HD crops, fan redraws, and modern
  game art as grounding authority.

When image tooling accepts references, assign the canonical sheet to identity,
the leg asset to lower-body topology, and the bundled Late-Z sheet to
adapter-specific visual translation. Assign any approved project image to
current continuity. The adapter sheet never replaces the canonical or leg
authorities.

Exception for H3 Max R2V: upload only the bundled Late-Z Xavier sheet as `Image
1` by default. For that route, it is the consolidated authority for identity,
face, asymmetric anatomy, costume, proportions, palette, linework, cel shading,
and broadcast rendering. Do not also attach the canonical sheet, leg authority,
or raw broadcast captures unless the user requests them, the scene needs a
separate narrow authority, or a failed result needs a targeted repair.

## Reference-role firewall

Assign every supplied reference a primary role before generation:

- **IDENTITY:** canonical Xavier sheet or approved project Xavier
- **ANATOMY:** supplemental leg authority when legs may be visible
- **STYLE:** bundled Late-Z sheet, approved cel project image, and inspected
  target-era broadcast captures
- **PROJECT:** approved frame or storyboard controlling current continuity
- **MOTION:** clips controlling only timing, cuts, camera rhythm, pose cadence,
  performance, or effects behavior

A mixed-era, differently cropped, or off-target clip may guide cadence without
becoming style authority. Do not inherit its character design, anatomy,
palette, aura colors, location, costume, logo, crop, letterboxing, watermark,
caption, or audio. Reference audio is non-authoritative unless the user assigns
it an audio role.

## Broadcast-grounding gate

When grounding or refreshing this adapter, search and visually inspect ordinary
original-series 4:3 television frames from the 1994-1996 late-Z run. Prefer
identifiable broadcast captures or faithful original-frame sources. Reject
remastered, recolored, denoised, sharpened, widescreen-cropped, promotional,
key-art, game, fan-redrawn, and AI-generated material.

Derive only general production grammar. Do not bundle, redistribute, trace, or
copy third-party frames, characters, costumes, attacks, locations, or exact
compositions into Xavier output.

## Rendering lock

- original 4:3 mid-1990s television-cel presentation
- confident dark brown-black contours, thicker on the outer silhouette and
  thinner on sparse face, hair, fur, clothing, and anatomy marks
- clean simplified forms with two opaque cel values and an occasional third
  highlight; hard-edged shadow shapes and no soft character gradients
- dark-brown fur translated into warm umber base and muted chocolate shadow
  planes with sparse short contour marks, never dense strand rendering
- long blond hair rendered as broad stable ochre-gold clumps with amber-brown
  shadows and sparse pale-yellow highlights, never individual simulated hair
- yellow beak remains a simple angular paint shape; cyan right eye and brown
  left eye remain distinct under every expression
- the anatomical-left snake forearm stays bright green with one darker green
  shadow family and a complete readable snake head instead of fingers
- loincloth, pendant, shoulder accessory, bead/feather detail, black right glove,
  and normal flat white sneakers retain their canonical construction
- hand-painted backgrounds use broad opaque shapes, sparse detail, and
  atmospheric color recession rather than dense digital rendering
- very light fine cel-photography grain, restrained broadcast softness, minute
  color bleed, and subtly imperfect registration; no obvious aging effect
- in animation, grain remains a stable finish rather than crawling, boiling, or
  redrawing independently

## Xavier identity and anatomy translation

Preserve the exact awkward brown-furred humanoid: long blond slab-like hair;
yellow bird-like beak; cyan anatomical-right eye and brown anatomical-left eye;
bright-green snake replacing the anatomical-left forearm and hand from the
elbow; one ordinary black-gloved anatomical-right hand; six nipples when
visible; canonical loincloth, pendant, shoulder accessory, white shoes, and
asymmetry.

Each leg remains plantigrade with exactly one thigh, one true knee hinging
backward, one lower leg, one ankle, and one normal flat white sneaker. In side
profile, the knee is the restrained rearward apex behind the hip-to-ankle axis.
Front and rear views may look nearly straight, but must never invent a forward
human knee. Do not translate Xavier into a generic human, satyr, faun, bird-man,
or heroic anime fighter.

## Expression presets

### DEADPAN_CANONICAL

Default to Xavier's awkward neutral sincerity: uneven eyes, relaxed beak/mouth,
minimal brow movement, slight head tilt, and a rigid but off-balance posture.
Preserve the cyan-right/brown-left mapping and do not beautify the face.

### BATTLE_INTENSE

Use only for confrontation or when requested. Compress the visible eyelid
apertures into firmer angular shapes, add one or two short tension creases, and
set the jaw. Preserve eye color, eye size and spacing, beak, hairline, facial
asymmetry, age, and head-to-body ratio. Do not add transformation irises,
oversized white sclera, giant teeth, spiked hair, or a permanent angry redesign.

## Camera and composition

Favor original-TV-anime framing: uncomfortable medium close-ups for monologue;
tight eye, beak, snake, or pendant inserts; low three-quarter confrontation
views; restrained dutch angles; wide aftermath frames holding Xavier against
painted terrain; strong asymmetry; foreground shapes; practical pans; short
push-ins; snap reframes; and decisive cuts.

Create dynamism through contrast between compositions instead of constant
camera motion. Keep 4:3 unless the user requests another ratio. Avoid modern
shallow depth of field, glossy lens effects, floating drone motion, and
continuous orbiting.

## Temporal rhythm

For animated work:

- use held key poses with limited secondary motion, then brief decisive bursts
- let principal shots breathe; do not assign every panel equal time
- tag each beat `HOLD`, `BURST`, `INSERT`, or `REVEAL`
- use visibly stepped pose changes and repeated drawings instead of perfectly
  smooth interpolation; effects may update faster than Xavier
- give each shot one dominant motion channel: subject, camera, or effects
- during a hold, use only restrained hair tips, snake-head reaction, mouth
  movement, weather, or one short optical push-in as needed
- favor hard cuts and a very brief impact cel only when contact or state change
  needs punctuation
- keep face, eye mapping, beak, hair mass, snake attachment, leg rig, contours,
  cel shadows, and grain stable; no line boil, anatomy drift, elastic zoom, or
  costume crawling

## Motion profiles

### SURREAL_MONOLOGUE

Hold a rigid pose, use economical mouth/beak movement and one small head-angle
change, let the snake head make one restrained independent reaction, insert one
brief symbolic or environmental cutaway when useful, then return to a dry
aftermath hold. Dialogue density must not force continuous facial redrawing.

### POWER_UP_TRANSFORM

Use discrete states: intact pre-state; held strain pose with escalating weather,
dust, debris, aura pressure, or environmental response; tighter hard cuts or
one restrained push-in; one brief silhouette or impact insert; hard cut to the
completed post-state; held reveal and reaction or aftermath.

```text
PRE-STATE:
CHANGE ONLY:
POST-STATE:
```

The delta controls only named changes. Preserve face, mismatched eyes, beak,
hair, snake arm, leg rig, anatomy, proportions, costume, position, and
environment unless named. Never continuously morph Xavier's body or anatomy.

### IMPACT_MELEE

Use a readable chain: launch or approach, one strike, very brief contact insert,
follow-through, opponent reaction, aftermath. Use one attack path per principal
shot. Do not request prolonged overlapping limbs or an extended exchange. Keep
one head, one torso, one black-gloved right hand, one left snake forearm, and
two backward-knee legs.

For 8-15 seconds, prefer four or five principal shots plus no more than two
brief inserts. Written durations guide rhythm rather than guaranteeing
frame-accurate control.

## Exclusions

- no glossy modern digital-anime finish, promotional illustration polish,
  remaster coloring, airbrushed gradients, volumetric light, lens flare, or
  cinematic depth of field
- no 3D, CGI, PS2 render, photoreal fur, strand hair, PBR skin, or plastic toy
  rendering while the adapter is active
- no heavy grain, VHS noise, scanlines, scratches, film burns, chromatic
  aberration, sepia cast, vignette, CRT border, or compression blocks
- no normal human nose or muzzle, two ordinary hands, detached/duplicated snake,
  wrong-side snake, symmetric eyes, forward human knees, digitigrade hocks,
  extra leg bends, missing/extra limbs, generic fantasy species, heroic
  beautification, franchise traits, logos, subtitles, HUD, or watermark
- no constant camera motion, equal-duration montage rhythm, smooth
  transformation morph, crawling grain, line boil, or fluid modern interpolation

## Repair checks

- **too clean or remastered:** add only very light fine cel-photography grain,
  restrained broadcast softness, minute color bleed, and slightly muted cel
  paint; do not add VHS artifacts or change composition
- **too painterly:** remove soft blends and dense hair/fur marks; restore opaque
  planes, hard shadows, broad hair masses, and economical interior lines
- **identity drifts:** restore canonical face, beak, eye mapping, hair, snake
  arm, black glove, six nipples, costume, proportions, and asymmetry
- **snake becomes a hand:** remove fingers and restore a complete snake head at
  the anatomical-left forearm terminus without changing the pose
- **leg rig drifts:** restore one thigh, one backward-hinging knee, one lower
  leg, one ankle, and one flat sneaker per leg; reject forward knees and hocks
- **generic heroic redesign:** restore awkward canonical proportions and facial
  asymmetry before decorative style
- **camera feels stiff:** add shot-scale contrast, one restrained push-in, or a
  decisive cut; never constant orbiting or random handheld movement
- **transformation morphs:** restore locked pre- and post-states and bridge them
  only with effects plus one brief impact insert
- **held drawing crawls:** stabilize face, eyes, beak, hair, snake, leg rig,
  contours, cel shadows, and grain; animate only the dominant motion channel
- **melee duplicates anatomy:** reduce to one readable strike and attack path;
  restore exact limbs and sides before adding effects
