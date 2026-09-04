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
| `EPISODE` | progressive mini-episode | 30–60 seconds or four boards |
| `REPAIR` | smallest correction | failed layer only |

Infer the smallest fitting mode. A one-image request remains one image. `Fix the snake arm` routes to `REPAIR`. `Lost PS2 episode` routes to `EPISODE`.

Honor explicit production commands such as `one image only`, `no video`,
`prompt only`, `Genesis Frame`, `classic`, `explore`, `H3 Max`, `I2V`, `T2V`,
`R2V`, `Seedance`, `Kling`, `under 3500 characters`, `NO music`, and `use only
this storyboard`.

For video work, resolve the creation route after mode and style:

- a Genesis Frame, exact opening image, or classic approval flow uses
  `CLASSIC CONTROL`
- text-only exploration uses `DIRECT EXPLORE`
- recognizable Xavier with free opening composition uses `CHARACTER LOCK`

Use the compact chooser in `SKILL.md` only when video intent is ambiguous.

## Approval gates

- `REFERENCE`: inspect sources, generate one reference, explicitly approve before locking the hash.
- `STILL`/`MEME`: a single image may be the final output after QA.
- Classic Control multi-shot modes: Genesis Frame approval before boarding.
- provider prompt: storyboard approval first when the selected route includes a storyboard, unless the user explicitly requests prompt-only or supplies an already approved board.
- `EPISODE`: approve each progressive board before the next.
