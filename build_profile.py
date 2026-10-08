#!/usr/bin/env python3
"""Build the samragyi22 profile README assets.

Emits ONE combined profile.svg (so GitHub cannot insert paragraph gaps between
sections) plus four small link-card SVGs that get wrapped in <a> in the README
so they are genuinely clickable.

Theme: light is the base; a prefers-color-scheme:dark block re-skins every
surface. All transforms use transform-box:fill-box so they are element-local
and therefore independent of each section's y-offset in the tall canvas.
"""
import base64, io, os
from PIL import Image

W = 880
OUT = "assets"

# ---------------------------------------------------------------- illustration
def portrait_b64():
    src = Image.open("Images/Neon AI Engineer Portfolio Dashboard.png").convert("RGB")
    crop = src.crop((0, 58, 356, 386)).resize((520, 479), Image.LANCZOS)
    buf = io.BytesIO(); crop.save(buf, "JPEG", quality=86, optimize=True)
    return base64.b64encode(buf.getvalue()).decode()

# ---------------------------------------------------------------- theme + css
CSS = """
  .m{font-family:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace}
  .d{font-family:"Helvetica Neue",Helvetica,Arial,"Segoe UI",Roboto,sans-serif}
  .h{font-family:"Segoe Script","Bradley Hand","Brush Script MT","Comic Sans MS",cursive;font-style:italic}
  svg{--bg:#FFFFFF;--card:#F8FAFE;--chip:#F2F6FD;--code:#F4F8FD;--band:#F1F5FC;
      --bd:#DFE6F2;--bdc:#D9E2F0;--rule:#E6ECF6;--grid:#EFF4FB;--hair:#ECF0F7;
      --tx:#0A1020;--body:#46556F;--chiptx:#33435E;--mut:#68768F;--dim:#9AA8BF;
      --acc:#1668E3;--acc2:#D81E36;--acc3:#3F77DE;--ok:#0E9F6E;--glow:0.07;--sweep:0.16;--sweep2:0.10}
  /* Light only, by request. To make it follow the viewer's system theme again,
     re-add a @media (prefers-color-scheme:dark) block that redefines these same
     tokens -- nothing else in the file references a literal hex. */
  .f-tx{fill:var(--tx)}.f-body{fill:var(--body)}.f-chip{fill:var(--chiptx)}
  .f-mut{fill:var(--mut)}.f-dim{fill:var(--dim)}.f-acc{fill:var(--acc)}
  .f-acc2{fill:var(--acc2)}.f-acc3{fill:var(--acc3)}.f-ok{fill:var(--ok)}
  .sf-bg{fill:var(--bg)}.sf-band{fill:var(--band)}
  .sf-card{fill:var(--card);stroke:var(--bd)}
  .sf-chip{fill:var(--chip);stroke:var(--bdc)}
  .sf-code{fill:var(--code);stroke:var(--bd)}
  .st-rule{stroke:var(--rule);fill:none}.st-hair{stroke:var(--hair);fill:none}
  .st-bd{stroke:var(--bd);fill:none}.st-acc{stroke:var(--acc);fill:none}
  .st-dim{stroke:var(--dim);fill:none}
  .st-grid{stroke:var(--grid);fill:none}
  .cursor{fill:var(--card);stroke:var(--acc);stroke-width:1.2;stroke-linejoin:round}
  .gs-acc{stop-color:var(--acc)}.gs-acc2{stop-color:var(--acc2)}
  .glow-a{fill:url(#gA)}.glow-b{fill:url(#gB)}
  .fade{animation:fade .6s ease-out backwards}
  .rise{animation:rise .7s cubic-bezier(.2,.7,.3,1) backwards}
  .chip{animation:chip .55s cubic-bezier(.2,.7,.3,1) backwards}
  @keyframes fade{from{opacity:0}}
  @keyframes rise{from{opacity:0;transform:translateY(10px)}}
  @keyframes chip{from{opacity:0;transform:translateY(8px)}}
  @keyframes blink{0%,45%{opacity:1}50%,95%{opacity:0}100%{opacity:1}}
  @keyframes pulse{0%,100%{opacity:.35;transform:scale(1)}50%{opacity:1;transform:scale(1.45)}}
  @keyframes spin{to{transform:rotate(360deg)}}
  @keyframes spinR{to{transform:rotate(-360deg)}}
  @keyframes grow{from{transform:scaleX(0)}}
  @keyframes typeIn{from{transform:translateX(0)}}
  @keyframes draw{from{stroke-dashoffset:var(--len)}}
  @keyframes halo{0%{opacity:.7;transform:scale(1)}70%,100%{opacity:0;transform:scale(2.8)}}
  @keyframes glowPulse{0%,100%{opacity:.35}50%{opacity:.8}}
  @keyframes sweep{0%{opacity:0;transform:translateX(-260px)}6%,44%{opacity:1}52%,100%{opacity:0;transform:translateX(900px)}}
  @keyframes scan{0%{opacity:0;transform:translateX(-10px)}8%,44%{opacity:.8}52%,100%{opacity:0;transform:translateX(830px)}}
  @keyframes bob{0%,100%{transform:translate(0,0)}50%{transform:translate(-5px,8px)}}
  .dot{transform-box:fill-box;transform-origin:center;animation:pulse 2.4s ease-in-out infinite}
  .halo{transform-box:fill-box;transform-origin:center;animation:halo 2.6s ease-out 1.6s infinite}
  .orb{transform-box:fill-box;transform-origin:center;animation:spin 70s linear infinite}
  .orbR{transform-box:fill-box;transform-origin:center;animation:spinR 48s linear infinite}
  .bar{transform-box:fill-box;transform-origin:left center;animation:grow .9s cubic-bezier(.2,.7,.3,1) backwards}
  .cover1{transform:translateX(90px);animation:typeIn 1.0s steps(10) .25s backwards}
  .cover2{transform:translateX(304px);animation:typeIn 1.5s steps(34) 1.3s backwards}
  .caret{animation:blink 1.1s step-end infinite}
  .pglow{animation:glowPulse 3.6s ease-in-out infinite}
  .sweep{opacity:0;animation:sweep 6.5s ease-in-out 1.4s infinite}
  .scanline{opacity:0;animation:scan 6.5s ease-in-out 1.4s infinite}
  .bob{transform-box:fill-box;animation:bob 3.4s ease-in-out infinite}
  .trk{stroke-dasharray:var(--len);stroke-dashoffset:0;animation:draw 1.5s ease-out .5s backwards}
  .trail{opacity:.45;animation:glowPulse 3.4s ease-in-out infinite}
  @media (prefers-reduced-motion:reduce){
    .fade,.rise,.chip,.dot,.halo,.orb,.orbR,.bar,.caret,.pglow,.sweep,.scanline,.bob,.trk,.trail,
    .cover1,.cover2,.rule{animation:none}
  }
"""

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def T(x, y, s, cls="m f-body", size=10, anchor=None, weight=None, ls=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    w = f' font-weight="{weight}"' if weight else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    return f'<text class="{cls}" x="{x:g}" y="{y:g}" font-size="{size}"{w}{l}{a}{extra}>{s}</text>'

def header(y, title, meta):
    return (f'<g class="fade"><rect x="44" y="{y-13}" width="3" height="16" fill="url(#hg)"/>'
            + T(58, y, title, "m f-tx", 13, weight="700", ls="3.2")
            + T(836, y, meta, "m f-mut", 10, anchor="end", ls="2") + '</g>')

def chip_row(items, x0, y, h=26, gap=10, fs=10.5, pad=26, per=6.9, delay=0.3, step=0.045):
    """items: list of labels. returns (svg, end_x, next_delay)"""
    out, x, d = [], x0, delay
    for lab in items:
        w = round(len(lab) * per) + pad
        out.append(f'<g class="chip" style="animation-delay:{d:.2f}s">'
                   f'<rect class="sf-chip" x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2:g}"/>'
                   + T(x + w/2, y + h/2 + 3.5, esc(lab), "m f-chip", fs, anchor="middle", ls="0.6")
                   + '</g>')
        x += w + gap; d += step
    return "".join(out), x - gap, d

# ---------------------------------------------------------------- sections
def sec_hero(b64):
    H = 390
    o = [f'<rect class="sf-band" x="0" y="0" width="880" height="56"/>',
         '<path class="st-rule" d="M0 56H880"/>']
    # terminal
    o.append('<g class="fade">'
             + f'<text class="m" x="44" y="22" font-size="11"><tspan class="f-acc">samragyi@github</tspan>'
               f'<tspan class="f-mut">:~$ </tspan><tspan class="f-tx">whoami</tspan></text>'
             + '<g class="cover1"><rect class="sf-band" x="134" y="10" width="96" height="16"/>'
               '<rect class="f-acc" x="134" y="10" width="7" height="15"/></g>'
             + T(44, 42, "&gt; Building AI products for a better tomorrow...", "m f-body", 11)
             + '<g class="cover2"><rect class="sf-band" x="50" y="30" width="320" height="16"/>'
               '<rect class="caret f-acc" x="50" y="30" width="7" height="15"/></g></g>')
    # terminal window chrome (decorative -- deliberately not tab-shaped, since an
    # SVG rendered through <img> can never carry clickable regions)
    o.append('<g class="fade" style="animation-delay:.5s">'
             '<circle class="f-acc2" cx="700" cy="28" r="3.4" opacity="0.75"/>'
             '<circle class="f-dim" cx="712" cy="28" r="3.4"/>'
             '<circle class="f-dim" cx="724" cy="28" r="3.4"/>'
             + T(836, 32, "samragyi22 — zsh", "m f-mut", 9.5, anchor="end", ls="0.6") + '</g>')
    # portrait
    o.append('<g class="rise" style="animation-delay:.15s">'
             '<rect class="pglow" x="40" y="74" width="268" height="248" rx="16" fill="none" '
             'stroke="var(--acc)" stroke-opacity="0.45" stroke-width="2"/>'
             f'<image clip-path="url(#portrait)" x="44" y="78" width="260" height="240" '
             f'preserveAspectRatio="xMidYMid slice" xlink:href="data:image/jpeg;base64,{b64}"/>'
             '<rect clip-path="url(#portrait)" x="44" y="78" width="260" height="240" fill="url(#pFade)"/>'
             '<rect x="44" y="78" width="260" height="240" rx="12" fill="none" stroke="var(--bd)"/></g>')
    # identity
    o.append('<g class="fade" style="animation-delay:.3s">'
             '<rect class="st-bd" x="330" y="78" width="94" height="22" rx="4"/>'
             + T(340, 93, "Hi there! I&apos;m", "m f-chip", 9.5, ls="0.6") + '</g>')
    o.append(T(330, 142, "SAMRAGYI", "d f-tx rise", 42, weight="800", ls="0.5",
               extra=' textLength="248" lengthAdjust="spacing" style="animation-delay:.4s"'))
    o.append(f'<text class="d rise" x="330" y="186" font-size="42" font-weight="800" letter-spacing="0.5" '
             f'fill="url(#nameG)" textLength="186" lengthAdjust="spacing" style="animation-delay:.5s">SHARMA</text>')
    o.append('<rect class="rule bar" x="330" y="196" width="150" height="2.5" rx="1.2" fill="url(#hg)" '
             'style="animation-delay:1.5s"/>')
    o.append(T(330, 216, "AI-FOCUSED FULL-STACK ENGINEER", "m f-acc rise", 12.5, ls="3.2",
               extra=' style="animation-delay:.6s"'))
    # handwritten accent
    o.append('<g class="h f-mut" opacity="0.85" transform="rotate(-7 712 142)">'
             + T(660, 118, "turn ideas", "h fade", 20, extra=' style="animation-delay:1.1s"')
             + T(672, 146, "into impact", "h fade", 20, extra=' style="animation-delay:1.2s"')
             + T(700, 176, "&lt;/&gt;", "m f-acc2 fade", 13, extra=' style="animation-delay:1.3s"') + '</g>')
    pitch = ["I build real-world products at the intersection of AI and full-stack",
             "development — from FinTech analytics to e-commerce and career-tech",
             "platforms. Currently ranked in the top 1,500 of 50,000+ students",
             "nationally in Google&apos;s The Big Code 2026."]
    o.append('<g class="fade" style="animation-delay:.9s">'
             + "".join(T(330, 240 + i*17, l, "m f-body", 10.5) for i, l in enumerate(pitch)) + '</g>')
    # focus chips
    x = 330
    for i, (lab, acc) in enumerate([("AI / AGENTIC SYSTEMS", "f-acc"), ("FULL-STACK ENGINEERING", "f-acc"),
                                    ("PRODUCTION SOFTWARE", "f-acc2")]):
        w = round(len(lab) * 6.2) + 34
        o.append(f'<g class="rise" style="animation-delay:{1.9+i*0.12:.2f}s">'
                 f'<rect class="sf-chip" x="{x}" y="304" width="{w}" height="28" rx="14"/>'
                 f'<circle class="{acc}" cx="{x+13}" cy="318" r="2.6"/>'
                 + T(x + 23, 321.5, lab, "m f-chip", 9, ls="0.8") + '</g>')
        x += w + 8
    # status bar
    o.append('<g class="fade" style="animation-delay:2.3s">'
             '<rect class="sf-code" x="44" y="344" width="792" height="30" rx="6"/>'
             '<circle class="dot f-acc2" cx="62" cy="359" r="3.2"/>'
             + f'<text class="m f-mut" x="76" y="363" font-size="10.5" letter-spacing="1.5">STATUS: '
               f'<tspan class="f-tx">OPEN TO SOFTWARE ENGINEERING / AI OPPORTUNITIES</tspan></text>'
             + T(818, 363, "JAIPUR, INDIA", "m f-mut", 10.5, anchor="end", ls="1.5") + '</g>')
    return H, "".join(o)


def sec_metrics():
    H = 116
    tiles = [("50+", "Engineering Tickets", "Resolved", "f-acc"),
             ("3.2%", "Conversion Rate", "(1.5% &#8594; 3.2%)", "f-acc"),
             ("&lt;200ms", "API Response Time", "(500ms &#8594; &lt;200ms)", "f-acc3"),
             ("95%", "ATS Pass Rate", "(Resume Analysis)", "f-acc3"),
             ("Top 1,500", "Google Big Code 2026", "(50,000+ students)", "f-acc2")]
    o, x = [], 44
    for i, (v, l1, l2, c) in enumerate(tiles):
        o.append(f'<g class="rise" style="animation-delay:{0.1+i*0.08:.2f}s">'
                 f'<rect class="sf-card" x="{x}" y="18" width="152" height="80" rx="10"/>'
                 f'<rect class="{c}" x="{x}" y="18" width="152" height="2.5" rx="1.2" opacity="0.85"/>'
                 f'<rect class="{c}" x="{x+14}" y="34" width="3" height="14" rx="1.5"/>'
                 + T(x + 24, 48, v, "d f-tx", 19, weight="800", ls="0.2")
                 + T(x + 14, 72, l1, "m f-chip", 8.5, ls="0.5")
                 + T(x + 14, 85, l2, "m f-mut", 8.5, ls="0.5") + '</g>')
        x += 160
    return H, "".join(o)


def sec_about():
    H = 364
    o = [header(43, "ABOUT ME", "SYSTEM PROFILE")]
    body = ["AI-focused full-stack engineer with production",
            "experience across FinTech analytics, e-commerce",
            "and career-tech platforms — shipping features",
            "end-to-end using MERN, Next.js and modern AI",
            "tooling (Claude SDK, MCP, Groq API)."]
    o.append('<g class="rise" style="animation-delay:.1s">'
             '<rect class="sf-card" x="44" y="62" width="408" height="170" rx="10"/>'
             '<rect class="f-acc" x="44" y="62" width="408" height="2" rx="1" opacity="0.7"/>'
             + T(60, 88, "PROFILE", "m f-acc", 10, ls="2.2")
             + "".join(T(60, 110 + i*15, l, "m f-body", 10) for i, l in enumerate(body)))
    x = 60
    for lab, w, c in [("JAIPUR, INDIA", 99, "f-acc"), ("OPEN TO OPPORTUNITIES", 146, "f-ok"),
                      ("ALWAYS LEARNING", 111, "f-acc2")]:
        o.append(f'<rect class="sf-chip" x="{x}" y="186" width="{w}" height="24" rx="12"/>'
                 f'<circle class="{c}" cx="{x+13}" cy="198" r="2.4"/>'
                 + T(x + 23, 202, lab, "m f-chip", 8.5, ls="0.8"))
        x += w + 8
    o.append('</g>')
    code = [('<tspan class="f-acc2">const</tspan><tspan class="f-tx"> samragyi</tspan><tspan class="f-mut"> = {</tspan>'),
            ('<tspan class="f-acc">  role</tspan><tspan class="f-mut">: </tspan><tspan class="f-chip">"AI-Full Stack Engineer"</tspan><tspan class="f-mut">,</tspan>'),
            ('<tspan class="f-acc">  building</tspan><tspan class="f-mut">: [</tspan><tspan class="f-chip">"Scalable Products", "Agentic Systems"</tspan><tspan class="f-mut">],</tspan>'),
            ('<tspan class="f-acc">  learning</tspan><tspan class="f-mut">: [</tspan><tspan class="f-chip">"Better Systems", "Real World Impact"</tspan><tspan class="f-mut">],</tspan>'),
            ('<tspan class="f-acc">  interests</tspan><tspan class="f-mut">: [</tspan><tspan class="f-chip">"AI", "Product Thinking", "Open Source"</tspan><tspan class="f-mut">],</tspan>'),
            ('<tspan class="f-acc">  goal</tspan><tspan class="f-mut">: </tspan><tspan class="f-chip">"Turn ideas into products people love"</tspan>'),
            ('<tspan class="f-mut">}</tspan>'),
            ('<tspan class="f-dim">// still learning, always building...</tspan>')]
    o.append('<g class="rise" style="animation-delay:.22s">'
             '<rect class="sf-code" x="468" y="62" width="368" height="170" rx="10"/>'
             + T(484, 88, "&gt;", "m f-ok", 10)
             + T(498, 88, "current_focus.js", "m f-chip", 10, ls="0.6")
             + '<circle class="f-acc2" cx="800" cy="84" r="3.2" opacity="0.8"/>'
               '<circle class="f-dim" cx="812" cy="84" r="3.2"/><circle class="f-dim" cx="824" cy="84" r="3.2"/>'
               '<path class="st-rule" d="M468 98H836"/>'
             + "".join(T(486, 114 + i*14, str(i + 1), "m f-dim", 8.5, anchor="end")
                       + f'<text class="m" x="498" y="{114+i*14}" font-size="9">{ln}</text>'
                       for i, ln in enumerate(code)) + '</g>')
    x = 44
    for i, (lab, w) in enumerate([("AI ENGINEERING", 114), ("FULL-STACK DEVELOPMENT", 165),
                                  ("PRODUCTION ENGINEERING", 165), ("DEVELOPER EXPERIENCE", 152),
                                  ("PROBLEM SOLVING", 120)]):
        o.append(f'<g class="rise" style="animation-delay:{0.5+i*0.07:.2f}s">'
                 f'<rect class="sf-chip" x="{x}" y="246" width="{w}" height="26" rx="13"/>'
                 + T(x + w/2, 263, lab, "m f-chip", 9, anchor="middle", ls="1") + '</g>')
        x += w + 10
    o.append('<path class="st-rule" d="M44 288H836"/>'
             '<path class="st-bd" d="M100 326H760" stroke-width="1.5"/>'
             '<path class="trk" d="M100 326H760" stroke="url(#hg)" stroke-width="1.5" fill="none" style="--len:660"/>')
    for i, (nx, yr, lab, c, now) in enumerate([(140, "2025", "AI / Full-Stack Engineering", "acc", False),
                                               (430, "2026", "Production Software Engineering", "acc", False),
                                               (720, "NOW", "Building AI + Full-Stack Systems", "acc2", True)]):
        halo = f'<circle class="halo" cx="{nx}" cy="326" r="5.5" fill="none" stroke="var(--{c})" stroke-width="1.5"/>' if now else ""
        node = (f'<circle class="f-{c}" cx="{nx}" cy="326" r="5.5"/>' if now else
                f'<circle class="sf-bg" cx="{nx}" cy="326" r="5.5" stroke="var(--{c})" stroke-width="2"/>')
        o.append(f'<g class="fade" style="animation-delay:{0.9+i*0.12:.2f}s">{halo}{node}'
                 + T(nx, 310, yr, f"m f-{c}", 11, anchor="middle", weight="700", ls="2")
                 + T(nx, 350, lab, "m f-tx" if now else "m f-body", 10, anchor="middle") + '</g>')
    return H, "".join(o)


def sec_experience():
    H = 300
    roles = [dict(y=86, badge="E", title="Software Engineer Intern", org="Eternz", meta="E-commerce Marketplace",
                  date="May 2026 – Sep 2026", c="acc",
                  b=["Resolved 45+ engineering tickets across frontend and backend as a forward-deployed engineer.",
                     "Built the wallet module and shipped a new checkout feature — conversion 1.5% &#8594; 3.2% (113% increase).",
                     "Shipped bug fixes, performance optimizations and DB query caching to production."]),
             dict(y=196, badge="K", title="AI / Full-stack Engineer Intern", org="KalviumLabs", meta="AI · Full-Stack",
                  date="Sep 2025 – May 2026", c="acc2",
                  b=["Built an AI-powered FinTech analytics platform on Next.js 16, Claude Haiku 4.5 and an isolated MCP server.",
                     "Enabled natural-language queries with autonomous tool calling, streaming responses, SQL/Python analysis and PDF export.",
                     "Delivered production-ready MERN + PostgreSQL applications and scalable REST APIs.",
                     "Reduced response times from ~500ms to &lt;200ms through indexing."])]
    o = [header(43, "EXPERIENCE", "SHIPPED TO PRODUCTION"),
         '<path class="trk" d="M70 76V286" stroke="url(#spine)" stroke-width="1.5" opacity="0.55" style="--len:210"/>']
    for i, r in enumerate(roles):
        y, c = r["y"], r["c"]
        bul = "".join(f'<circle class="f-{c}" cx="102" cy="{y+26+j*15}" r="1.8" opacity="0.85"/>'
                      + T(112, y + 30 + j*15, b, "m f-body", 9.5) for j, b in enumerate(r["b"]))
        o.append(f'<g class="rise" style="animation-delay:{0.15+i*0.14:.2f}s">'
                 f'<circle class="sf-card" cx="70" cy="{y}" r="11" stroke="var(--{c})" stroke-width="2"/>'
                 + T(70, y + 4, r["badge"], f"m f-{c}", 10, anchor="middle", weight="700")
                 + T(96, y - 4, r["title"], "m f-tx", 12, weight="700")
                 + f'<text class="m" x="96" y="{y+13}" font-size="10"><tspan class="f-{c}">{r["org"]}</tspan>'
                   f'<tspan class="f-mut">  ·  {r["meta"]}</tspan></text>'
                 + T(836, y - 4, r["date"], "m f-mut", 9.5, anchor="end", ls="0.6") + bul + '</g>')
    return H, "".join(o)


def sec_stack():
    rows = [("LANGUAGES", ["Java", "JavaScript", "TypeScript", "Python", "SQL"], "f-acc", 10),
            ("AI / AGENTIC", ["Claude SDK", "MCP", "Groq API"], "f-acc", 10),
            ("FRONTEND", ["React", "Next.js", "Vite", "Tailwind", "Redux Toolkit"], "f-acc", 10),
            ("BACKEND &amp; APIs", ["Django", "Django Ninja", "DRF", "Node.js", "Express", "GraphQL", "REST", "Celery"], "f-acc", 10),
            ("DATABASES", ["PostgreSQL", "MongoDB", "ClickHouse", "DuckDB", "Redis", "Typesense", "pgvector"], "f-acc3", 10),
            ("DEVOPS / TESTING", ["Docker", "AWS", "GitHub Actions", "Pytest", "Jest", "Playwright", "Git", "Postman"], "f-acc2", 8)]
    H = 62 + len(rows) * 58 + 6
    o = [header(43, "TECH STACK", f"{len(rows)} DOMAINS"),
         '<g opacity="0.85"><circle class="orb st-grid" cx="812" cy="215" r="230" stroke-dasharray="1 9"/>'
         '<circle class="orbR st-bd" cx="812" cy="215" r="165" stroke-dasharray="40 160" opacity="0.6"/>'
         '<circle class="orb st-grid" cx="68" cy="340" r="130" stroke-dasharray="2 10"/></g>']
    d, widest = 0.3, 0
    for i, (lab, chips, c, gap) in enumerate(rows):
        ry = 62 + i * 58
        o.append(f'<g class="fade" style="animation-delay:{0.08+i*0.07:.2f}s">'
                 f'<rect class="{c}" x="44" y="{ry+14}" width="3" height="14" rx="1.5"/>'
                 + T(56, ry + 26, lab, "m f-mut", 10, ls="2") + '</g>')
        body, end, d = chip_row(chips, 200, ry + 12, gap=gap, delay=d)
        o.append(body); widest = max(widest, end)
        if i < len(rows) - 1:
            o.append(f'<path class="st-hair" d="M44 {ry+54}H836"/>')
    assert widest <= 836, widest
    return H, "".join(o)


def sec_projects():
    H = 244
    cards = [dict(x=44, tag="01 / CAREER AI", c="f-acc", g="barA", title="SCORIK", ts=17,
                  d=["AI-powered career and resume", "intelligence platform."],
                  m=["95% ATS pass rate", "50+ ATS-optimized templates", "Groq llama-3.3-70b analysis"]),
             dict(x=313, tag="02 / AGENTIC", c="f-acc3", g="barB", title="AI FINTECH ANALYTICS", ts=17,
                  d=["Natural-language financial", "analytics with AI tool calling."],
                  m=["Claude Haiku 4.5 + MCP", "SQL / Python analysis", "Streaming AI + PDF export"]),
             dict(x=582, tag="03 / FULL-STACK", c="f-acc2", g="barC", title="HACKTOK", ts=17,
                  d=["Dual-database MERN platform", "for sharing life hacks."],
                  m=["MongoDB + PostgreSQL", "50+ weekly users", "REST APIs · sync logic"])]
    o = [header(43, "FEATURED PROJECTS", "3 SYSTEMS")]
    for i, c in enumerate(cards):
        x = c["x"]
        o.append(f'<g class="rise" style="animation-delay:{0.1+i*0.12:.2f}s">'
                 f'<rect class="sf-card" x="{x}" y="62" width="254" height="164" rx="10"/>'
                 f'<rect class="bar" x="{x}" y="62" width="254" height="2.5" rx="1.2" fill="url(#{c["g"]})" '
                 f'style="animation-delay:{0.3+i*0.12:.2f}s"/>'
                 + T(x + 16, 86, c["tag"], f'm {c["c"]}', 9.5, ls="1.8")
                 + T(x + 16, 110, c["title"], "d f-tx", c["ts"], weight="800", ls="0.8")
                 + "".join(T(x + 16, 130 + j*15, l, "m f-body", 10.5) for j, l in enumerate(c["d"]))
                 + f'<path class="st-rule" d="M{x+16} 158H{x+238}"/>'
                 + "".join(f'<circle class="{c["c"]}" cx="{x+19}" cy="{175+j*17}" r="2"/>'
                           + T(x + 30, 178 + j*17, m, "m f-chip", 10) for j, m in enumerate(c["m"]))
                 + '</g>')
    return H, "".join(o)


def sec_achievements():
    H = 406
    def grid(items, y, h, d0):
        out, x = [], 44
        for i, (tag, l1, l2, c) in enumerate(items):
            out.append(f'<g class="rise" style="animation-delay:{d0+i*0.08:.2f}s">'
                       f'<rect class="sf-card" x="{x}" y="{y}" width="192" height="{h}" rx="9"/>'
                       + T(x + 14, y + 20, tag, f"m {c}", 8.5, ls="2")
                       + T(x + 14, y + 41, l1, "m f-tx", 10.5, weight="700", ls="0.4")
                       + T(x + 14, y + 58, l2, "m f-mut", 9) + '</g>')
            x += 200
        return "".join(out)
    o = [header(43, "ACHIEVEMENTS &amp; CREDENTIALS", "VERIFIED HIGHLIGHTS")]
    o.append('<g class="rise" style="animation-delay:.1s">'
             '<rect x="44" y="62" width="792" height="132" rx="12" fill="url(#heroCard)" stroke="var(--bd)"/>'
             '<g clip-path="url(#mainClip)">'
             '<rect class="sweep" x="-200" y="62" width="200" height="132" fill="url(#sweepG)"/>'
             '<rect class="scanline f-acc" x="40" y="62" width="1.6" height="132"/></g>'
             '<rect x="44" y="62" width="792" height="2.5" rx="1.2" fill="url(#hg)"/>'
             '<circle class="dot f-acc2" cx="74" cy="88" r="3"/>'
             + T(86, 92, "NATIONAL COMPETITION", "m f-acc2", 9.5, ls="2.4")
             + T(72, 128, "GOOGLE THE BIG CODE 2026", "d f-tx", 24, weight="800", ls="0.6")
             + T(72, 152, "Advanced to Round 2", "m f-body", 11)
             + T(72, 172, "Invited by Google India for SWE Internship", "m f-body", 11)
             + '<path class="st-bd" d="M640 86V174"/>'
             + T(812, 128, "TOP 1,500", "d f-tx", 34, weight="800", ls="0.5", anchor="end")
             + T(812, 152, "OF 50,000+ STUDENTS", "m f-acc", 10.5, ls="1.8", anchor="end")
             + T(812, 172, "NATIONALLY", "m f-mut", 10.5, ls="1.8", anchor="end") + '</g>')
    o.append(grid([("LEADERSHIP", "CLASS REPRESENTATIVE", "50+ students · 3+ workshops", "f-acc"),
                   ("COMPETITION", "AARUNYA 2023 TECH TALK", "First Runner Up · MITS Gwalior", "f-acc"),
                   ("PUBLIC SPEAKING", "PATRIKA MUN", "Top 10 speaker of 150+", "f-acc"),
                   ("VOLUNTEERING", "ISRO SCIENCE EXPO", "CR delegate · 1,500+ attendees", "f-acc2")], 206, 72, 0.3))
    o.append('<path class="st-rule" d="M44 300H836"/>'
             + T(44, 322, "CERTIFICATIONS &amp; EDUCATION", "m f-mut fade", 10, ls="2.4",
                 extra=' style="animation-delay:.6s"'))
    o.append(grid([("ORACLE", "Certified Foundations", "Associate — Agentic AI", "f-acc"),
                   ("WALMART · FORAGE", "Advanced Software", "Engineering Job Simulation", "f-acc"),
                   ("LEETCODE", "50 Days Badge 2026", "100 Days Badge 2026", "f-acc"),
                   ("EDUCATION", "B.Tech CSE (SPE) · 9.59", "JECRC · Kalvium · 2024–28", "f-acc2")], 332, 66, 0.66))
    return H, "".join(o)


def sec_principles():
    H = 172
    items = [(44, "01", "f-acc", "SHIP PRODUCTION SOFTWARE", ["Build things that actually", "reach users."]),
             (313, "02", "f-acc", "MEASURE PERFORMANCE", ["Use metrics to guide", "optimization."]),
             (582, "03", "f-acc2", "BUILD WITH AI, NOT AROUND IT", ["AI as an engineering", "capability, not decoration."])]
    o = [header(43, "ENGINEERING PRINCIPLES", "HOW I WORK")]
    for i, (x, n, c, title, body) in enumerate(items):
        o.append(f'<g class="rise" style="animation-delay:{0.1+i*0.1:.2f}s">'
                 f'<rect class="sf-card" x="{x}" y="62" width="254" height="86" rx="10"/>'
                 + T(x + 16, 84, n, f"m {c}", 10, ls="1.8")
                 + T(x + 16, 106, title, "m f-tx", 11.5, weight="700", ls="0.8")
                 + "".join(T(x + 16, 124 + j*14, l, "m f-body", 9.5) for j, l in enumerate(body)) + '</g>')
    return H, "".join(o)


def sec_connect():
    H = 118
    o = [header(36, "CONNECT", "LET&apos;S WORK TOGETHER"),
         '<path class="trail st-acc" d="M700 44q46 14 70 46" stroke-width="1.2" stroke-dasharray="3 6"/>',
         '<g transform="translate(772,46) scale(1.45)"><g class="bob">'
         '<path class="cursor" d="M0 0 L0 19 L5 14.6 L8.3 22 L12 20.3 L8.7 13.2 L14.6 12.9 Z"/></g></g>',
         T(44, 84, "LET&apos;S BUILD SOMETHING.", "d f-tx rise", 30, weight="800", ls="0.6",
           extra=' style="animation-delay:.08s"'),
         T(44, 106, "Open to software engineering and AI engineering opportunities — links below.",
           "m f-body fade", 11, extra=' style="animation-delay:.2s"')]
    return H, "".join(o)


# ---------------------------------------------------------------- assembly
def build_profile():
    b64 = portrait_b64()
    secs = [sec_hero(b64), sec_metrics(), sec_about(), sec_experience(), sec_stack(),
            sec_projects(), sec_achievements(), sec_principles(), sec_connect()]
    body, off, rules = [], 0, []
    for i, (h, svg) in enumerate(secs):
        if i:
            rules.append(f'<path class="st-rule" d="M0 {off}H880"/>')
        body.append(f'<g transform="translate(0,{off})">{svg}</g>')
        off += h
    H = off

    defs = f'''
  <linearGradient id="hg" x1="0" y1="0" x2="1" y2="0"><stop class="gs-acc" offset="0"/><stop class="gs-acc2" offset="1"/></linearGradient>
  <linearGradient id="nameG" x1="0" y1="0" x2="1" y2="0"><stop class="gs-acc" offset="0"/><stop class="gs-acc2" offset="1"/></linearGradient>
  <linearGradient id="spine" x1="0" y1="0" x2="0" y2="1"><stop class="gs-acc" offset="0"/><stop class="gs-acc2" offset="1"/></linearGradient>
  <linearGradient id="barA" x1="0" y1="0" x2="1" y2="0"><stop class="gs-acc" offset="0"/><stop class="gs-acc" offset="1" stop-opacity="0.15"/></linearGradient>
  <linearGradient id="barB" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="var(--acc3)"/><stop offset="1" stop-color="var(--acc3)" stop-opacity="0.15"/></linearGradient>
  <linearGradient id="barC" x1="0" y1="0" x2="1" y2="0"><stop class="gs-acc2" offset="0"/><stop class="gs-acc2" offset="1" stop-opacity="0.15"/></linearGradient>
  <linearGradient id="sweepG" x1="0" y1="0" x2="1" y2="0">
    <stop class="gs-acc" offset="0" stop-opacity="0"/><stop class="gs-acc" offset="0.45" stop-opacity="var(--sweep2)"/>
    <stop class="gs-acc" offset="0.5" stop-opacity="var(--sweep)"/><stop class="gs-acc" offset="0.55" stop-opacity="var(--sweep2)"/>
    <stop class="gs-acc" offset="1" stop-opacity="0"/></linearGradient>
  <linearGradient id="heroCard" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="var(--acc)" stop-opacity="0.07"/><stop offset="0.55" stop-color="var(--card)"/>
    <stop offset="1" stop-color="var(--acc2)" stop-opacity="0.07"/></linearGradient>
  <linearGradient id="pFade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0.5" stop-color="#091020" stop-opacity="0"/><stop offset="1" stop-color="#091020" stop-opacity="0.45"/></linearGradient>
  <radialGradient id="gA" cx="0.5" cy="0.5" r="0.5"><stop class="gs-acc" offset="0" stop-opacity="var(--glow)"/><stop class="gs-acc" offset="1" stop-opacity="0"/></radialGradient>
  <radialGradient id="gB" cx="0.5" cy="0.5" r="0.5"><stop class="gs-acc2" offset="0" stop-opacity="var(--glow)"/><stop class="gs-acc2" offset="1" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path class="st-grid" d="M44 0H0V44"/></pattern>
  <clipPath id="portrait"><rect x="44" y="78" width="260" height="240" rx="12"/></clipPath>
  <clipPath id="mainClip"><rect x="44" y="62" width="792" height="132" rx="12"/></clipPath>'''

    glows = (f'<ellipse class="glow-a" cx="180" cy="200" rx="420" ry="260"/>'
             f'<ellipse class="glow-b" cx="820" cy="360" rx="340" ry="210"/>'
             f'<ellipse class="glow-a" cx="700" cy="{secs[0][0]+secs[1][0]+secs[2][0]//2}" rx="460" ry="220"/>'
             f'<ellipse class="glow-b" cx="700" cy="{H-700}" rx="420" ry="230"/>')

    desc = ("Samragyi Sharma, AI-focused full-stack engineer based in Jaipur, India, open to software "
            "engineering and AI opportunities. Builds real-world products at the intersection of AI and "
            "full-stack development across FinTech analytics, e-commerce and career-tech. "
            "Impact: 50+ engineering tickets resolved; checkout conversion 1.5% to 3.2%; API response time "
            "500ms to under 200ms; 95% ATS pass rate; top 1,500 of 50,000+ students in Google The Big Code 2026. "
            "Experience: Software Engineer Intern at Eternz (May 2026 to Sep 2026) and AI/Full-stack Engineer "
            "Intern at KalviumLabs (Sep 2025 to May 2026). "
            "Stack: Java, JavaScript, TypeScript, Python, SQL; Claude SDK, MCP, Groq API; React, Next.js, Vite, "
            "Tailwind, Redux Toolkit; Django, Django Ninja, DRF, Node.js, Express, GraphQL, REST, Celery; "
            "PostgreSQL, MongoDB, ClickHouse, DuckDB, Redis, Typesense, pgvector; Docker, AWS, GitHub Actions, "
            "Pytest, Jest, Playwright, Git, Postman. "
            "Projects: SCORIK AI career platform, AI FinTech Analytics, HackTok. "
            "Credentials: Oracle Certified Foundations Associate Agentic AI; Walmart Advanced Software "
            "Engineering Job Simulation; LeetCode 50 and 100 Days badges 2026; B.Tech Computer Science "
            "Software Product Engineering, JECRC University Kalvium Program, CGPA 9.59.")

    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
           f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t ds">\n'
           f'<title id="t">Samragyi Sharma — AI-focused full-stack engineer</title>\n'
           f'<desc id="ds">{desc}</desc>\n<defs>{defs}\n</defs>\n<style>{CSS}</style>\n'
           f'<rect class="sf-bg" width="{W}" height="{H}"/>'
           f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.8"/>{glows}'
           + "".join(body) + "".join(rules) + '\n</svg>\n')
    open(f"{OUT}/profile.svg", "w").write(svg)
    return H, len(svg)


def build_links():
    cards = [("github",    "GITHUB",    "github.com/",     "samragyi22",        "f-acc"),
             ("leetcode",  "LEETCODE",  "leetcode.com/u/", "Samragyi_22",       "f-acc"),
             ("email",     "EMAIL",     "samragyisharma.2226", "@gmail.com",    "f-acc"),
             ("portfolio", "PORTFOLIO", "samragyiportfolio",   ".netlify.app",  "f-acc2")]
    w, h = 194, 64
    for name, label, l1, l2, acc in cards:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
               f'role="img" aria-label="{label}: {l1}{l2}">\n<style>{CSS}</style>\n'
               f'<rect class="sf-bg" width="{w}" height="{h}"/>'
               f'<rect class="sf-card" x="1" y="1" width="{w-2}" height="{h-2}" rx="10"/>'
               f'<rect class="{acc}" x="1" y="1" width="{w-2}" height="2" rx="1" opacity="0.85"/>'
               + T(16, 25, label, f"m {acc}", 9, ls="2.2")
               + '<path class="st-dim" d="M{0} 25l10-10M{1} 15h7v7" stroke-width="1.3" stroke-linecap="round"/>'
                 .format(w - 30, w - 27)
               + T(16, 45, l1, "m f-tx", 9.5) + T(16, 58, l2, "m f-chip", 9.5)
               + '\n</svg>\n')
        open(f"{OUT}/link-{name}.svg", "w").write(svg)
    return len(cards)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    H, size = build_profile()
    n = build_links()
    print(f"profile.svg   {W}x{H}  {size/1024:.1f} KB")
    print(f"link cards    {n} files")
