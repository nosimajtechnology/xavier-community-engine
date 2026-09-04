# fal.ai MiniMax H3 Max Adapter

Use this adapter for `H3 Max`, `fal H3`, `I2V`, `T2V`, `R2V`, `Classic
Control`, `Direct Explore`, or `Character Lock`. Apply Xavier canon, leg
topology, the selected style adapter, approved continuity, and the model-neutral
motion brief first. This file changes route, prompt structure, reference
packaging, and verified fal.ai fields only.

## Live routes

| Creation route | fal.ai endpoint | Source authority |
| --- | --- | --- |
| CLASSIC CONTROL | `minimax/h3-max/image-to-video` | approved Genesis Frame |
| DIRECT EXPLORE | `minimax/h3-max/text-to-video` | text prompt only |
| CHARACTER LOCK | `minimax/h3-max/reference-to-video` | one selected Xavier sheet by default |

Do not ask for this choice when the user already requested the classic
first-frame-to-storyboard flow. If the user asks to explore or iterate freely,
recommend DIRECT EXPLORE. If they want recognizable Xavier without a fixed
opening frame, recommend CHARACTER LOCK. Ask the compact chooser from
`SKILL.md` only when video intent is ambiguous.

Because Xavier's asymmetry and leg rig are unusually fragile, describe DIRECT
EXPLORE as interpretive. Recommend CHARACTER LOCK for recognizable free staging
and CLASSIC CONTROL for the highest control over opening composition and
anatomy.

## Optimize the seed before prompting

Preserve the premise and every explicit non-negotiable. Improve only how the
idea is staged for H3 Max:

1. put a readable visual hook in the opening second
2. create a visible cause -> escalation -> payoff
3. use one dominant subject action and one camera purpose per beat
4. sequence actions that would be confusing or anatomically difficult if simultaneous
5. end on a resolved image, reaction, reveal, loop point, or intentional cliffhanger

For a 15-second action scene, prefer about four or five principal shots with
only brief impact or detail inserts. Do not give every shot equal duration.
Avoid passive openings, repetitive angles, slideshow pacing, impossible
contact, and an unresolved final beat.

For transformations, state `PRE-STATE -> physical impact or occlusion bridge ->
POST-STATE`. Never request continuous liquid morphing of Xavier's face, eyes,
beak, hair, snake arm, body, legs, or costume.

If the seed is loose and the route is DIRECT EXPLORE, offer at most three
meaningfully different T2V-ready concepts. If it is clear, silently optimize one
direction and continue.

## Model-aware staging

Exploit H3 Max for coherent short action, explicit camera movement,
chronological multi-shot prompting, physical transitions, and multimodal role
assignment. Reduce risk by simplifying crowded choreography, overlapping limb
actions, tiny continuity-dependent props, dense dialogue, frequent costume
changes, long cut chains, or conflicting camera commands.

Timecodes are narrative guidance, not guaranteed frame-accurate edit points.
Cover the full requested duration with non-overlapping blocks. Each block
contains camera, Xavier or subject action, environmental response, and the
physical transition into the next beat.

## Common prompt order

```text
[duration, aspect, one-line premise, selected rendering lock]

[R2V ONLY: REFERENCE ASSIGNMENTS]

IDENTITY AND ANATOMY INVARIANTS:
[protected Xavier traits, side mapping, leg topology, and current state]

0.0-[time]s — [camera]; [subject action]; [environment]; [transition]
[continue through the full duration]

AUDIO:
[dialogue, effects, ambience, music, NO MUSIC, or NO AUDIO]

CONTINUITY / DO NOT:
[short decisive failure prevention]
```

Use direct concrete verbs. Describe how cuts, wipes, impacts, occlusions, or
camera passes cause transitions. Do not stack contradictory aesthetic labels.
When Late-Z is active, use its exact broadcast-cel rendering and temporal rules,
not generic `modern anime`, `smooth animation`, or `glossy cinematic` language.

## CLASSIC CONTROL — I2V

Create and approve the Genesis Frame with GPT Image 2, then create and approve
the storyboard. Send only the Genesis Frame to `image_url` as the literal first
frame. The I2V output inherits its aspect ratio. Use `end_image_url` only when
the user deliberately approves an exact ending frame.

The storyboard is planning authority for shot order, composition, geography,
action states, rhythm, and transitions. Do not upload a contact sheet by
default: translate it into the chronological prompt. The canonical, leg, and
selected style sheets remain upstream authorities used to create and repair the
frame. Keep appearance wording compact and spend prompt budget on motion,
contact points, camera, continuity, and endpoint.

If the opening frame is wrong, repair it before video. If motion fails but the
frame is right, revise only the motion/camera language or simplify the failed
beat.

## DIRECT EXPLORE — T2V

Use `text-to-video` with no image, video, or audio references. The prompt must
describe Xavier completely enough to stand alone:

```text
Xavier is a tall awkward brown-furred humanoid with long slab-like blond hair,
a yellow bird-like beak instead of a nose, a cyan anatomical-right eye and a
brown anatomical-left eye, six nipples when visible, a bright-green snake that
replaces his anatomical-left forearm and hand from the elbow, and one ordinary
black-gloved anatomical-right hand. He wears his small decorated loincloth,
pendant, single shoulder accessory, bead-and-feather hair detail, and normal
flat white sneakers. Each leg has one thigh, one true knee hinging backward,
one lower leg, and one ankle; no human forward knees or animal hocks. Preserve
his deliberate asymmetry, awkward proportions, exact sides, and limb count.
```

Then state the selected style's rendering, capture, cadence, camera, and
exclusions. T2V is for breadth, not canonical certainty; label identity as
interpretive. If Xavier drifts, recommend CHARACTER LOCK or CLASSIC CONTROL
rather than making the prompt longer and more conflicted.

## CHARACTER LOCK — R2V

When Late-Z is active, use this default package:

```text
Image 1 = ../../assets/style-adapters/late-z-battle-cel/xavier-late-z-character-sheet-v1.png;
sole default reference for Xavier identity, face, eye mapping, beak, hair,
snake arm, costume, proportions, leg construction, palette, line, shading, and
Late-Z era treatment.
```

Begin every default Late-Z R2V prompt with:

```text
#Image1 is the sole visual reference and complete authority for the character's
identity, facial construction, anatomy, costume, proportions, palette, linework
and Late-Z rendering. Preserve the same character throughout every angle. Do
not show the sheet, turnaround layout, white background or multiple copies of
the character.
```

Do not also upload the canonical Xavier sheet or leg authority for a default
Late-Z R2V request, and do not upload raw broadcast frames or other internal
construction assets. The Late-Z sheet is already their approved translation.
Add another reference only when the user explicitly requests it, the scene
requires another character, prop, vehicle, environment, motion, or audio
authority, or a failed generation needs a narrow identity or anatomy repair.
Keep the Late-Z sheet as `Image 1`, assign every addition one narrow role, never
say to blend all references, and mention only reference slots actually used.

Outside Late-Z, use this default order:

```text
Image 1 = ../../assets/xavier-canonical-reference.png; Xavier identity and
underlying construction.
Image 2 = ../../assets/xavier-leg-authority.png when legs may be visible;
lower-body topology only.
Next Image = selected adapter-specific Xavier sheet when needed.
```

For either package, add optional sources only when the scene materially needs
them:

```text
Next Image = secondary character identity, environment, prop, vehicle, or
wardrobe authority; one narrow role per file.
Video 1 = motion, performance timing, camera, or edit rhythm only; never
identity, anatomy, rendering, palette, wardrobe, or audio authority.
Audio 1 = voice or sound authority only.
```

If an outside-Late-Z scene is guaranteed to remain waist-up, the leg authority
may be omitted and the remaining image order closes up.

In the copy-paste prompt, call inputs `Image 1`, `Image 2`, `Image 3`, `Video
1`, and `Audio 1` according to their actual list order. Do not mention unused
reference slots. A host UI may display the same
tokens with `#` or `@`; preserve ordering and roles.

Use the fewest references that fully define the scene. Never say `blend all
references`. Reference images, videos, and audio together may total at most 12
files in the current fal.ai schema. Reference videos must each be 2-15 seconds
with at most 15 seconds combined. Reference audio must be 2-15 seconds with at
most 15 seconds combined and cannot be the only reference modality.

## Verified fal.ai fields

- `duration`: integer seconds; current H3 Max range is 5-15
- `resolution`: `768P` default; use `480P` only for cheaper/faster drafts
- `prompt_expansion_mode`: `balanced` for iteration; offer `quality` for finals
- `aspect_ratio` for T2V: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, or `9:16`
- `aspect_ratio` for R2V: the same choices plus `adaptive`
- I2V aspect follows `image_url`; `end_image_url` is optional
- keep `enable_safety_checker: true`

Prefer `4:3` for Late-Z T2V or R2V unless the project requires another format.
Do not claim 2K, a hidden camera control, or another field not present in the
current endpoint schema.

## Delivery

Return exactly the useful layers:

```text
ROUTE: [CLASSIC CONTROL / DIRECT EXPLORE / CHARACTER LOCK]
SETUP: [endpoint and what to upload, or NO REFERENCES]
REFERENCES: [ordered narrow roles; omit for T2V]
PROMPT: [copy-paste prompt]
FIELDS: [duration, resolution, expansion mode, ratio when applicable]
RISK / NEXT MOVE: [one short note only when useful]
```

For repair, keep the seed premise, route, reference order, identity, anatomy,
approved state, and style locked. Change only the failed action, camera,
transition, audio, or continuity clause. A route change is explicit: T2V -> R2V
for identity or anatomy drift; R2V -> CLASSIC CONTROL when opening composition
or exact geography must be locked.
