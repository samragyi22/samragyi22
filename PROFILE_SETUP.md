# Profile README — setup & maintenance

How the GitHub profile for [github.com/samragyi22](https://github.com/samragyi22) is built,
and how to change it.

---

## 1. Why it is one SVG

GitHub sanitises README HTML and **strips `style` attributes**. That means separate `<img>`
tags can never be made to sit flush — the markdown renderer puts a paragraph gap between
each one, and in dark mode those gaps show as bands between the panels. The profile used to
be nine images and looked like a stack of disconnected cards.

So the entire visual profile is **one `assets/profile.svg`** (880 × 2526). Sections are
divided by hairline rules drawn inside the SVG, not by separate files. No gaps are possible.

The only separate images are the four link cards, because an SVG rendered through `<img>`
cannot contain clickable regions. Each card is its own small SVG wrapped in an `<a>` so it
genuinely navigates.

```
README.md              # one <img> + the clickable link row
build_profile.py       # generates every SVG — edit this, not the SVG
assets/
  profile.svg    (116 KB)  the whole dashboard, 880x2526
  link-github.svg     )
  link-leetcode.svg   )  194x64 each, wrapped in <a> in the README
  link-email.svg      )
  link-portfolio.svg  )
preview/index.html     # offline preview, follows your system light/dark setting
README-preview.png     # rendered snapshot
Images/                # source art: the dashboard reference + LeetCode badges
```

Regenerate everything after an edit:

```bash
python3 build_profile.py      # needs Pillow: pip3 install Pillow
```

---

## 2. Theme

The SVG is **theme-adaptive**. Light is the base; a `prefers-color-scheme: dark` block
re-skins every surface through CSS custom properties:

| token | light | dark |
| :--- | :--- | :--- |
| `--bg` page | `#FFFFFF` | `#070B16` |
| `--card` | `#F8FAFE` | `#0B1222` |
| `--chip` | `#F2F6FD` | `#0C1426` |
| `--code` code card | `#F4F8FD` | `#080D1A` |
| `--bd` border | `#DFE6F2` | `#1B2B45` |
| `--tx` primary text | `#0A1020` | `#F5F7FA` |
| `--body` | `#46556F` | `#A9B6CC` |
| `--mut` muted | `#68768F` | `#55657F` |
| `--acc` blue | `#1668E3` | `#247BFF` |
| `--acc2` red | `#D81E36` | `#FF354F` |

To change a colour, edit the `CSS` string near the top of `build_profile.py` and rebuild.
Both palettes are defined in one place; nothing else references a literal hex except the
fade over the illustration, which must stay dark in both themes.

The light accents are deepened versions of the `#247BFF` / `#FF354F` brand pair so small text
clears WCAG AA 4.5:1 on white: primary 18.9:1, body 7.5:1, chip 10.0:1, muted 4.6:1,
accents 5.1:1.

> `prefers-color-scheme` follows the viewer's **OS/browser** setting, not GitHub's own theme
> dropdown. If someone sets GitHub to dark while their OS is light they will see the light
> version. That is the same limitation GitHub's documented `<picture>` theme-switching has —
> there is no signal an image can read for the site-level toggle.

---

## 3. What is clickable

Clicking anywhere inside `profile.svg` does nothing — it is an image. The real links are:

- the four **link cards** under it (GitHub, LeetCode, Email, Portfolio)
- the text row below that (SCORIK repo, Repositories, Contribution activity)

The `/ about  / projects  / experience  / skills  / connect` pills in the hero are
**decorative section labels**, not navigation. They cannot be links — there is no image-map
equivalent that survives GitHub's sanitiser.

### Adding LinkedIn as a fifth card

1. Add `("linkedin", "LINKEDIN", "linkedin.com/in/", "<your-handle>", "f-acc")` to the
   `cards` list in `build_links()` and rebuild.
2. Drop the card width from `194` to `170` in the same function so five fit on one row
   (5 × 170 + margins = 870, inside GitHub's ~880px content width).
3. Add to `README.md`:
   ```html
   <a href="https://www.linkedin.com/in/YOUR-HANDLE/"><img src="assets/link-linkedin.svg" height="64" alt="LinkedIn" /></a>
   ```

---

## 4. Editing the layout

- **Canvas**: 880 wide. The content column runs `x = 44 → 836`. Keep new elements inside
  that and nothing clips at GitHub's README width.
- **Sections** are functions in `build_profile.py` (`sec_hero`, `sec_metrics`, `sec_about`,
  `sec_experience`, `sec_stack`, `sec_projects`, `sec_achievements`, `sec_principles`,
  `sec_connect`). Each returns `(height, svg)` in **local** coordinates starting at y=0;
  the assembler stacks them with `translate(0, offset)` and draws the dividing rules. To
  reorder sections, reorder the list in `build_profile()`.
- **Transforms** all use `transform-box: fill-box`, so every animation is element-local and
  stays correct no matter where its section lands in the tall canvas. Keep that if you add
  animated elements — a bare `transform-origin: center` would resolve against the 2526px
  viewBox and fling the element off-screen.
- **Chip widths** are computed as `round(len(label) * 6.9) + 26`. `sec_stack` asserts the
  widest row ends at or before `x = 836`, so an over-long row fails the build instead of
  clipping silently.
- **Fonts**: system stacks only — GitHub blocks webfonts in SVG. The name uses `textLength`
  so it occupies a fixed width whatever font the viewer has.

---

## 5. Animation

Inline CSS keyframes only; no SMIL, no scripts. They replay on every page load.

The contract: **every animated element's resting CSS state is its final state**, and
animations use `animation-fill-mode: backwards` to play *from* the hidden state. If animation
never runs — reduced motion, an old renderer, a static export — the profile is still
complete and fully legible. A `@media (prefers-reduced-motion: reduce)` block disables every
animation class; add new ones to that list.

GitHub proxies images through camo and caches them. After pushing, a hard refresh
(Cmd/Ctrl+Shift+R) may be needed before the new version appears.

---

## 6. Previewing

```bash
open preview/index.html     # follows your system light/dark setting
```

Regenerate `README-preview.png`:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --hide-scrollbars \
  --force-prefers-reduced-motion --force-device-scale-factor=1.25 \
  --virtual-time-budget=4000 --window-size=940,2672 \
  --screenshot="$PWD/README-preview.png" "file://$PWD/preview/index.html"
```

Headless Chrome follows the OS theme, so to check the *other* theme either flip macOS
appearance, or temporarily delete / unwrap the `@media (prefers-color-scheme:dark)` block in
a scratch copy of the SVG.

---

## 7. Facts used

Every figure traces to source material: 45+ tickets and 1.5% → 3.2% checkout conversion
(Eternz), ~500ms → <200ms (KalviumLabs), 95% ATS pass rate / 50+ templates / llama-3.3-70b
(SCORIK), 50+ weekly users (HackTok), Top 1,500 of 50,000+ and Round 2 (Google The Big Code
2026), CGPA 9.59, Jaipur.

No star counts, follower counts, commit counts, streak widgets, trophies or third-party stat
services. The activity links point at first-party GitHub pages only, so they can never show a
stale or invented number. The contribution heatmap from the design reference was deliberately
not reproduced — its "1,234 contributions" figure is invented, and a real heatmap cannot be
rendered without an external service.

The hero illustration is the artwork you supplied (`Images/Neon AI Engineer Portfolio
Dashboard.png`), cropped and embedded as an inline base64 JPEG. It is stylised art, **not a
photographic likeness** — no likeness was generated. `build_profile.py:portrait_b64()` does
the crop; point it at a different file to swap it.
