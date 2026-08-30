# Modes

| Mode | Output | Default scope |
|---|---|---|
| `REFERENCE` | production character study | one image and explicit approval |
| `STILL` | composed screenshot/frame | one image |
| `MEME` | still plus optional caption | one image, one joke |
| `MINI` | micro-action motion brief | 4–8 seconds |
| `SCENE` | connected short scene | 8–15 seconds |
| `BUMPER` | ident, found clip, interstitial | 4–10 seconds |
| `FAKE_AD` | PSA, commercial, tutorial, guru pitch | 8–15 seconds |
| `RENEGADE_CLIP` | edited short-form story | 8–45 seconds, 60 maximum |
| `EPISODE` | progressive mini-episode | 30–60 seconds or four boards |
| `REPAIR` | smallest correction | failed layer only |

Infer the smallest fitting mode. A one-image request remains one image. `Shillz submission` routes to `RENEGADE_CLIP` plus the optional campaign reference. `Fix the snake arm` routes to `REPAIR`. `Lost PS2 episode` routes to `EPISODE`.

## Approval gates

- `REFERENCE`: inspect sources, generate one reference, explicitly approve before locking the hash.
- `STILL`/`MEME`: a single image may be the final output after QA.
- multi-shot modes: Genesis Frame approval before boarding.
- provider prompt: storyboard approval first unless the user explicitly requests prompt-only or supplies an already approved board.
- `EPISODE`: approve each progressive board before the next.

