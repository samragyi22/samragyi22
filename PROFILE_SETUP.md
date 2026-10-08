# Profile README — setup & maintenance

Everything needed to publish and maintain the GitHub profile README for
[github.com/samragyi22](https://github.com/samragyi22).

---

## 1. What's in here

```
README.md              # the profile README itself
assets/
  hero.svg        (77 KB)  terminal bar, section nav, illustration, name, pitch, focus chips, status
  metrics.svg     (4 KB)   5-tile impact strip (tickets, conversion, latency, ATS, Big Code)
  about.svg       (10 KB)  profile card + current_focus.js code card + capabilities + 2025/2026/NOW
  experience.svg  (6 KB)   vertical timeline — Eternz and KalviumLabs
  stack.svg       (14 KB)  6 tech domains
  projects.svg    (6 KB)   3 featured project cards
  achievement.svg (9 KB)   Google Big Code card + 4 achievements + certifications & education
  principles.svg  (3 KB)   3 engineering principles
  connect.svg     (5 KB)   LET'S BUILD SOMETHING. + 4 contact cards
preview/index.html     # offline preview that mimics GitHub's dark README styling
README-preview.png     # rendered snapshot of the whole README (light, static / no-animation state)
Images/                # source material — LeetCode badges + the dashboard reference art
```

Total asset weight: **156 KB**, of which 77 KB is the embedded illustration.

Every SVG is **self-contained**: no scripts, no `<foreignObject>`, no external fonts,
stylesheets or network calls. The only `href` anywhere in the assets is the illustration's
inline `data:image/jpeg;base64` payload, which travels inside the file. That matters because
GitHub renders README SVGs through `<img>`, where external subresources are blocked but
inline data URIs and inline CSS keyframes work.

---

## 2. Publish

Your profile README lives in the special repo `samragyi22/samragyi22`, which already exists.

```bash
# 1. Clone the existing profile repo somewhere clean
git clone https://github.com/samragyi22/samragyi22.git
cd samragyi22

# 2. Copy the new profile in (adjust the source path to wherever this folder lives)
SRC="$HOME/Desktop/Dishuuu github profile "       # note the trailing space in the folder name
cp    "$SRC/README.md" .
cp -R "$SRC/assets" .
cp -R "$SRC/preview" .
cp    "$SRC/PROFILE_SETUP.md" .
cp    "$SRC/README-preview.png" .

# 3. Review what changed before committing
git status
git diff --stat

# 4. Commit and push
git add README.md assets preview PROFILE_SETUP.md README-preview.png
git commit -m "Redesign profile README: self-contained animated SVG dashboard"
git push origin main
```

If `git push` is rejected because the remote moved on, run `git pull --rebase origin main` first.

> Nothing above touches any other repository. Only `samragyi22/samragyi22` is modified.

### If you'd rather not overwrite the old README yet

```bash
git checkout -b profile-redesign
# ...copy files, commit...
git push -u origin profile-redesign
```
Then open a PR and merge when you're happy with the GitHub-rendered result.

---

## 3. The illustration in the hero

`assets/hero.svg` embeds a cropped, JPEG-compressed version of the workstation scene from
`Images/Neon AI Engineer Portfolio Dashboard.png`, inlined as a base64 data URI so the SVG
stays a single self-contained file.

It is **stylised artwork you supplied, not a photographic likeness of you.** No likeness was
generated. If you ever want a real portrait or a traced avatar there instead, send a photo.

### Replacing it

```python
# run from the project root
from PIL import Image
import io, base64, re

src  = Image.open("Images/YOUR_NEW_IMAGE.png").convert("RGB")
crop = src.crop((left, top, right, bottom))      # pick a roughly 13:12 region
crop = crop.resize((520, 479), Image.LANCZOS)    # 2x the 260x240 display box

buf = io.BytesIO(); crop.save(buf, "JPEG", quality=86, optimize=True)
b64 = base64.b64encode(buf.getvalue()).decode()

s = open("assets/hero.svg").read()
s = re.sub(r'xlink:href="data:image/jpeg;base64,[^"]+"',
           f'xlink:href="data:image/jpeg;base64,{b64}"', s)
open("assets/hero.svg", "w").write(s)
```

Keep the payload under ~80 KB — drop `quality` to 74 or 68 if it grows. The frame is a
`260 x 240` box at `x=44, y=78`, clipped by `clipPath#portrait`; change both the `<image>`
and the clip rect together if you resize it.

---

## 4. Things only you can supply

| Item | Why it's missing | What to do |
| :--- | :--- | :--- |
| **LinkedIn URL** | Not provided, and fabricating one is worse than omitting it. | See §5 — the exact snippet is ready to paste. |
| **HackTok repo URL** | No public repo named HackTok on your account. | If it's public, add the link under the projects image. |
| **AI FinTech Analytics repo URL** | Built at KalviumLabs; likely private/company-owned. | Only link it if it's genuinely yours to share. |
| **SCORIK live demo URL** | Repo exists and is linked; no deployed URL given. | Add `· <a href="…">Live demo</a>` to the line under the projects image. |

---

## 5. Adding LinkedIn

**README.md** — add to the link row at the bottom:

```html
<a href="PUT_YOUR_LINKEDIN_URL_HERE"><strong>LinkedIn</strong></a> ·
```

**assets/connect.svg** — the four cards are currently `width="192"` at `x = 44, 244, 444, 644`
with an 8px gap. For five cards use `width="152"` at `x = 44, 204, 364, 524, 684`
(still ending exactly at 836). Each card's inner text sits at `x + 16`, and the arrow glyph
at `x + 168` → change that to `x + 128`. Then update the `<desc>` so screen readers list
LinkedIn too.

---

## 6. Editing the SVGs

- **Canvas**: every asset uses an `880 × H` viewBox. The content column runs `x = 44 → 836`.
  Keep new elements inside that and nothing will clip at GitHub's README width.
- **Colours (light theme)**: page `#FFFFFF`, card `#F8FAFE`, chip `#F2F6FD`,
  code card `#F4F8FD`, terminal band `#F1F5FC`, border `#DFE6F2`, chip border `#D9E2F0`,
  rule `#E6ECF6`, grid `#EFF4FB`. Text: primary `#0A1020`, body `#46556F`,
  chip `#33435E`, muted `#68768F`. Accents: blue `#1668E3`, mid blue `#3F77DE`,
  red `#D81E36`, status green `#0E9F6E`. The accents are deepened versions of the
  `#247BFF` / `#FF354F` brand pair so small text clears 4.5:1 on white.
- **Fonts**: system stacks only (`ui-monospace…monospace`, `Helvetica Neue…sans-serif`, and a
  `cursive` stack for the one handwritten accent, which degrades to italic). No webfonts —
  GitHub blocks them in SVG. The big name uses `textLength` so it occupies a fixed width
  whatever font a visitor has.
- **Animation contract**: every animated element's *resting* CSS state is its **final** state,
  and animations use `animation-fill-mode: backwards` to play *from* the hidden state. If
  animation never runs — reduced motion, an old renderer, a static export — everything is
  still fully visible. Keep this pattern if you add elements.
- **Reduced motion**: each file ends its `<style>` with a
  `@media (prefers-reduced-motion: reduce)` block setting `animation: none`. Add any new
  animation class to that list.
- **Chip widths** are computed as `round(len(label) * 6.9) + 26` for 10.5px mono. If you add a
  technology, recompute the row and confirm it still ends at or before `x = 836`.

---

## 7. Previewing and re-rendering

```bash
open preview/index.html        # offline preview, no server needed
```

Regenerate `README-preview.png` (static state) with headless Chrome:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --force-prefers-reduced-motion --force-device-scale-factor=1.25 \
  --virtual-time-budget=4000 --window-size=940,2870 \
  --screenshot="$PWD/README-preview.png" \
  "file://$PWD/preview/index.html"
```

Drop `--force-prefers-reduced-motion` to capture the animated state. To inspect a specific
moment, temporarily append
`svg *{animation-play-state:paused !important; animation-delay:-1.8s !important}`
inside each SVG's `<style>` and render — that freezes everything 1.8s into its animation.

---

## 8. Light mode

The whole profile is built for **GitHub light mode**: the SVG canvas is `#FFFFFF`, which is
exactly GitHub's light README background, so the panels sit flush on the page with no visible
seams or gaps between them.

It is a **single light theme** — there is no dark variant, by design. On GitHub's dark theme
the panels read as a clean white dashboard card, which is legible but high-contrast against
the dark page.

### If you later want it to follow the viewer's theme

Add a `prefers-color-scheme` block at the end of each asset's `<style>`, overriding only the
surface and text colours, e.g.:

```css
@media (prefers-color-scheme: dark){
  /* re-darken surfaces and lighten text here */
}
```

That keys off the viewer's OS/browser setting, which is the same signal GitHub's own
`<picture>`-based theme switching uses. Ask and it can be wired up across all nine assets.

### Accessibility

Every text colour was checked against the white page: primary text 18.9:1, body 7.5:1,
chip text 10.0:1, muted 4.6:1, accent blue 5.1:1, accent red 5.1:1 — all at or above the
WCAG AA 4.5:1 threshold for small text. The status-green dot is decorative only.

---

## 9. Facts used

Every number and claim traces back to what you supplied: 45+ tickets and 1.5% → 3.2% checkout
conversion (Eternz), ~500ms → <200ms (KalviumLabs), 95% ATS pass rate / 50+ templates /
llama-3.3-70b (SCORIK), 50+ weekly users (HackTok), Top 1,500 of 50,000+ and Round 2 (Google
The Big Code 2026), CGPA 9.59, Jaipur.

There are **no** star counts, follower counts, commit counts, streak widgets, trophies or
third-party stat services anywhere. The Activity section links to first-party GitHub pages
only, so it can never show a stale or invented number. The contribution heatmap from the
reference mockup was deliberately **not** reproduced — the "1,234 contributions" figure on it
is invented, and a real heatmap cannot be rendered without an external service.

The previous profile README's claims that weren't in your source material — RAG pipeline
diagnostics, LangGraph multi-agent DAG, cross-encoder reranker, anti-hallucination
architecture, PALADIN AI and FinLens — were **not** carried over. If those are real and you
want them back, send the supporting detail and they can be added properly.
