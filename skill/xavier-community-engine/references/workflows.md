# Workflows

## Resolve visual style first

Before the first creative stage, resolve `FLAGSHIP PS2` or a registered adapter
using `style-adapters.md`. A registered adapter replaces PS2 rendering, camera,
and motion rules while active unless the user explicitly requests a hybrid.
Keep Xavier's canonical sheet as identity authority and the leg asset as
lower-body topology authority whenever the legs may be visible. Exception:
Late-Z H3 Max R2V uses only the bundled Late-Z Xavier sheet as its default
uploaded reference because that sheet already carries the approved identity,
leg construction, and style translation.

## Quick Mode

1. Parse the idea and intended use.
2. Infer mode and authority sources.
3. Resolve the visual style and assign identity, anatomy, style, project, and motion reference roles.
4. Attach the canonical identity asset; attach the leg authority whenever
   Xavier's legs may be visible; attach the selected style sheet only for its
   translation role. For Late-Z H3 Max R2V, instead attach only the Late-Z
   Xavier sheet by default.
5. Verify PS2 grounding only when the flagship build is active, or run the selected adapter's grounding gate.
6. Write a compact Scene Lock, including the neutral-expression default,
   full-body head-to-body scale, and exact leg rig when visible.
7. Create the Genesis Frame prompt or image when the selected route requires it.
8. Run identity, anatomy, selected-style render, premise, continuity, and rights QA.
9. Ask for Genesis Frame approval for Classic Control multi-shot work.
10. Build connected boards or a motion brief after approval.
11. Ask for storyboard approval before provider-specific compression when a storyboard is part of the route.
12. Deliver the final prompt package.

Ask no more than one question when a missing answer materially changes the output.

## Director Mode

Expose only requested controls: aspect ratio/social crop, camera/lens feel, shots/duration, dialogue density, tone, PS2 source roles, captions, audio, end card, provider, and verified character limit.

## Reference-First Mode

Use for canonical assets, new identity-sensitive subjects, close-ups, and ambiguous supplied references. Inspect the images, state exact locks, and do not generate until conflicts are resolved. Approval freezes the asset and its hash.

## Fidelity Repair Mode

Diagnose before changing anything. Preserve approved identity, framing, geography, and unaffected beats. Repair only the failed layer. For standard-human-leg drift, attach both authority assets and use the dedicated repair in `repair.md`. If an entire render stack is modern, preserve composition/action and rebuild materials, light, environment density, and capture limits together.

## Genesis Frame gate

Lock Xavier's orientation, scene geography, opening action, camera, rendering sources and roles, palette/time, supporting subjects/props, must-not-change constraints, crop safety, neutral-expression default, full-body head-to-body scale, and leg construction when visible.

Prefer a side or three-quarter Genesis Frame when the full legs must establish anatomy. Front and back views may be used when composition requires them, but cannot serve as the sole proof of the backward hinge.

A leg-visible Genesis Frame automatically fails for standard forward human knees, animal hocks, extra segments, mismatched left/right rigs, or ambiguous joint direction in side/three-quarter view. One isolated issue may receive one narrow automatic repair. Do not board a failed frame.

## Video creation routes

Resolve this after mode and style, before developing concepts or generating a
video source. Skip the chooser when intent already makes the route clear.

### CLASSIC CONTROL

Use for a polished scene whose opening composition, continuity, and edit need
approval.

```text
SEED IDEA -> STYLE -> OPTIMIZED CONCEPT -> GPT IMAGE 2 GENESIS FRAME
-> SELECTED-STYLE GATE -> APPROVAL -> GPT IMAGE 2 STORYBOARD -> APPROVAL
-> MODEL-NEUTRAL MOTION BRIEF -> H3 MAX I2V PROMPT
```

Upload the approved Genesis Frame as the literal I2V opening frame. The
storyboard remains planning and editorial authority; do not upload the contact
sheet to H3 Max by default. Translate its shot order, geography, action states,
and transitions into the prompt. The canonical, leg, and selected style sheets
remain upstream authorities used to create and repair the frame.

### DIRECT EXPLORE

Use for fast free concept iteration. Send no image, video, or audio reference.
The T2V prompt must fully describe Xavier, his asymmetric anatomy, the selected
rendering style, setting, action, camera, continuity, and ending. Identity and
leg accuracy are interpretive rather than canon-locked. After drift, recommend
CHARACTER LOCK or CLASSIC CONTROL instead of bloating the text prompt.

If a seed idea is loose, offer no more than three distinct T2V-ready concepts.
If it is clear, refine one direction and continue without forcing a choice.

### CHARACTER LOCK

Use when Xavier must remain recognizable but the opening frame should stay
free. For Late-Z, the bundled Late-Z Xavier sheet is the sole default R2V
reference and is uploaded as `Image 1`; do not also upload the canonical or leg
assets or raw broadcast frames. Add another reference only when the user
explicitly requests it, the scene materially requires a secondary character,
prop, vehicle, environment, wardrobe, motion, or audio authority, or a failed
generation needs a narrow identity or anatomy repair. Keep the Late-Z sheet as
`Image 1` and assign every addition one narrow role. Outside Late-Z, use the
canonical Xavier sheet as the primary R2V reference and add the leg authority
when legs may be visible. A
compact shot plan may guide the prompt, but a Genesis Frame and storyboard are
not required.

For fal.ai H3 Max packaging, use `model-adapters/fal-h3-max.md`.
