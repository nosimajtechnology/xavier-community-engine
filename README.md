# Xavier Community Engine

Create recognizable Xavier fan art, lost-PS2 scenes, memes, storyboards, short-form concepts, and precise continuity repairs from an ordinary-language idea.

> **Unofficial community creation tool for original Xavier fan works. Not official show material. Nosimaj Media does not own or claim rights to _Xavier: Renegade Angel_ or the original series.**

The engine keeps Xavier's deliberately crude CGI construction intact while using inspected original-PlayStation 2 screenshots to control the surrounding environment, camera, lighting, texture limits, NPC economy, and capture feel. Its story system favors sincere intervention, one flawed semantic idea, causal escalation, and a readable reversal. Token promotion is optional and isolated to the campaign route.

## Try it

- `Xavier tries to help a cashier whose register is emotionally checked out.`
- `Make a captionless reaction meme where Xavier realizes the weekend has already ended.`
- `Create a 15-second lost-PS2 Xavier scene for a Shillz submission. Keep the token secondary.`

## Install

1. Download `xavier-community-engine.zip` from the latest GitHub release.
2. Do not unzip it.
3. In ChatGPT, open **Settings → Skills**, choose **Add skill**, and upload the ZIP.
4. Start with `$xavier-community-engine` and describe what you want in one sentence.

The repository root is for source and validation. The installable package is built only from [`skill/xavier-community-engine/`](skill/xavier-community-engine/).

## Supported modes

`REFERENCE`, `STILL`, `MEME`, `MINI`, `SCENE`, `BUMPER`, `FAKE_AD`, `RENEGADE_CLIP`, `EPISODE`, and `REPAIR`.

The skill chooses the smallest fitting mode, asks at most one material question, gates multi-shot work behind Genesis Frame approval, and waits for storyboard approval before producing a provider-specific motion prompt.

## Canonical reference

The bundled production sheet is the immutable authority for Xavier's identity and base construction. Its recorded SHA-256 is `589fbf61c98e861d76f5310cb39c2ebe2494a5fd8140c4bf9bbb013c8a8c4731`. See [`ASSET_PROVENANCE.md`](ASSET_PROVENANCE.md).

## Campaign route

Campaign behavior activates only when the request names Shillz, a campaign, a submission, token content, or an equivalent use. The story remains the A-plot; Xavier must carry the clip; any cashtag or end card is secondary. Ordinary fan requests receive no token branding.

## Validate and build

```bash
python scripts/validate_package.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

The build is deterministic, verifies both canonical asset copies byte-for-byte, updates `SHA256SUMS`, and produces `dist/xavier-community-engine-v1.0.0.zip` with one top-level folder.

Read [`START_HERE.md`](START_HERE.md) for the five-minute workflow and [`COMMUNITY_GUIDE.md`](COMMUNITY_GUIDE.md) for attribution, rights, campaign, and reporting guidance.

