# Xavier Community Engine

An easy creative tool for making original Xavier images, memes, PS2-style scenes, storyboards, fake commercials, and short videos.

You do not need to know prompting.

Tell the Engine what Xavier is doing. It uses locked references and validation rules to keep him recognizable, finds the right old-game visual references, creates the first image, keeps scenes consistent, and prepares the animation prompt when you want video. Backward-hinged leg anatomy remains a known generator limitation; see [Current leg limitation](#current-leg-limitation).

> **Unofficial community creation tool for original Xavier fan works. Not official show material. Nosimaj Media does not own or claim rights to _Xavier: Renegade Angel_ or the original series.**

## What you need

- **A paid ChatGPT plan with Skills available.** Managed workspaces may require admin approval.
- **ChatGPT image generation** for images and storyboards.
- **A separate video tool** if you want animation. The Engine prepares the prompt, but tools such as Seedance, Kling, or Sora are separate products.

## Install in ChatGPT

1. Download [xavier-community-engine-v1.0.2.zip](https://github.com/nosimajtechnology/xavier-community-engine/releases/latest/download/xavier-community-engine-v1.0.2.zip). **Do not unzip it.**
2. In ChatGPT, open **Plugins** → **Skills** → **Create** → **Upload from your computer**.
3. Select the ZIP and start a new chat.

Start with:

```text
@Xavier Community Engine
```

Then describe Xavier doing one clear thing in one location:

```text
Xavier meditating beside a desert road at sunset.
```

If the first image looks right, reply `Approved.` If one detail is wrong, name only that problem:

```text
The snake arm is on the wrong side. Fix only that.
```

## What you can make

- **STILL** — one finished image
- **MEME** — a quick visual joke or reaction image
- **MINI** — one short animated moment
- **SCENE** — a connected 8–15 second story
- **BUMPER** — a strange ident, loop, or found clip
- **FAKE AD** — a fictional commercial or public-service message
- **EPISODE** — a story built across several connected storyboards
- **REPAIR** — fix only what drifted

Name a mode or just describe your idea and let the Engine choose.

## Canonical Xavier reference

This is the Engine's visual authority for Xavier. It keeps his face, eye colors, snake arm, hair, body, clothing, accessories, and deliberately crude 3D construction consistent.

![Xavier canonical character reference](./assets/xavier-canonical-reference.png)

Scenes, poses, expressions, props, and settings may change. The Engine should not smooth Xavier into polished modern CGI or redesign him as a different fantasy character.

## Supplemental leg authority

Xavier's legs use one thigh, one true knee hinging backward, one lower leg, one ankle, and one normal flat sneaker. This second reference enlarges the approved strict side-profile construction without changing the canonical sheet.

![Xavier supplemental leg authority](./skill/xavier-community-engine/assets/xavier-leg-authority.png)

The Engine instructs the image generator to use this asset only for lower-body topology and to reject standard forward human knees, animal hocks, extra segments, and exaggerated curved legs. This improves the guidance and makes failures easier to identify, but it does not guarantee that the generator will follow the topology.

## Current leg limitation

Current image generators often normalize Xavier's backward-hinged knees into standard human legs even when both authority images, explicit topology rules, negative constraints, and a narrow repair prompt are supplied. In testing, correct results have been intermittent rather than controllable. Prompting and reference images alone are therefore not reliable enough for guaranteed, leg-critical production.

For any frame where the legs are visible:

1. Inspect the knee direction before approving the frame.
2. Reject forward human knees, animal hocks, extra joints, curved segments, or mismatched leg rigs.
3. Allow one narrow leg-only repair while preserving the rest of a passing image.
4. If that repair fails, stop the attempt instead of repeatedly regenerating or describing the result as canonical.

Do not crop or hide an incorrect leg merely to pass the identity check. Dependable leg consistency will likely require stronger structural pose conditioning or a controlled rigged Xavier asset, neither of which is provided by v1.0.2.

Other identity, visual-style, composition, scene, and continuity features remain useful. Treat leg-visible output as experimental until the underlying generator can consistently obey the reversed-knee construction.

## Need an idea?

- Xavier walking through a quiet suburban street at night.
- Xavier sitting alone at a diner counter.
- Xavier waiting at a bus stop before sunrise.
- Xavier dancing alone in a dark nightclub.
- Xavier standing on a mountain summit in heavy wind.

More simple starters are available in [EXAMPLE_IDEAS.md](EXAMPLE_IDEAS.md).

## Community use

Community creations are unofficial by default. The Engine does not make new work official show canon.

Suggested credit:

> Unofficial Xavier fan work created with the Xavier Community Engine by Nosimaj Media.

_Xavier: Renegade Angel_ and related character names, designs, imagery, footage, audio, trademarks, and original material belong to their respective rights holders. This project is not affiliated with, sponsored by, or endorsed by Adult Swim, Cartoon Network, Williams Street, Warner Bros. Discovery, PFFR, or other applicable rights holders.

Do not upload or redistribute full episodes, ripped dialogue, show music, scripts, or artwork you do not have permission to use. This tool does not provide financial advice, price targets, or return promises.

Learn more about [Nosimaj Media](https://nosimaj.com).
