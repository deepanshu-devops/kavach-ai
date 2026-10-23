# Kavach-AI — Instructions

**AI & MCP Security for the Agentic Era — Cloud & AI Security from the Inside-Out.**

Working instructions for this repository. This file is the **agent-facing twin of
[`README.md`](README.md)** and carries the same facts, plus the rules for changing them.

> ### ⚠️ Sync rule — read this first
>
> **`README.md` and `instruction.md` are one document in two forms.**
> **Every time `README.md` is updated, update `instruction.md` in the same change** — and
> the other way round. They must never drift.
>
> When the site itself changes (new page, new token, new asset, new route), update **all** of:
>
> | File | What it holds |
> |------|---------------|
> | `README.md` | Root documentation for humans |
> | `instruction.md` | This file — same facts, plus the working rules |
> | `docs/README.md` | Documentation for the publish root (`docs/`) |
> | `docs/readme.html` | HTML twin of `docs/README.md`, served at `/readme.html` |
> | `docs/sitemap.xml` | Every public route |
>
> Keep the heading order and the table of contents aligned across all five so a diff shows
> the same change in every file.

---

## Table of contents

- [1. What this repo is](#1-what-this-repo-is)
- [2. Hard rules](#2-hard-rules)
- [3. Repo map](#3-repo-map)
- [4. Pages](#4-pages)
- [5. Design system — light theme](#5-design-system--light-theme)
- [6. Brand assets](#6-brand-assets)
- [7. Detection engine](#7-detection-engine)
- [8. Run locally](#8-run-locally)
- [9. Deploy](#9-deploy)
- [10. Task checklists](#10-task-checklists)
- [11. Contact](#11-contact)

---

## 1. What this repo is

Kavach-AI is a **static marketing site** for Kavach-AI, a security platform that protects AI
agents, LLM tool calls, MCP infrastructure and multi-cloud workloads (AWS, Azure, GCP). The site
pairs the layout and operating model of modern cloud-security platforms with the detection engine
of the open-source **kavach-mcp** middleware in this repo.

The site is **light-themed**: airy surfaces, deep ink text, coral/green/blue accents. The hero,
inner-page heroes, the CTA band and the footer are all light; the only deliberate dark element is
the **console mock** (`.console`), which is a product screenshot of a terminal.

🌐 [kavach-ai.com](https://kavach-ai.com) · ✉️ [corporate@kavach-ai.com](mailto:corporate@kavach-ai.com)

---

## 2. Hard rules

### 2.1 README ⇄ instruction.md

- Change **one** → change **the other**, in the same commit.
- Mirror content, not prose: same sections, same tables, same numbers, same route lists.
- If you add a section to `README.md`, add the counterpart here and extend the table of contents
  in both files.

### 2.2 Fictional company — no real claims

The site presents a fictional but plausible vendor. **All customer names, testimonials, funding,
investors, leadership, offices, awards and dates are original illustrative placeholders** — they
are not claims about any real person or firm. When the site goes live, replace the placeholders
with verified facts:

- `docs/pages/about.html` — founders, mission, funding, investors, offices
- `docs/pages/newsroom.html` — press releases, research, dates
- `docs/pages/careers.html` — open roles and locations
- `docs/pages/partners.html` — partner program and integrations
- `docs/pages/trust.html` — certifications and security controls
- `docs/pages/customers.html` and the home/testimonial sections — customer names & quotes

**Never name a third-party company in the site or the docs.** Describe layouts generically
("a conventional security-vendor pattern"); do not cite a real vendor, its domain, customers
or awards, and keep no downloaded third-party pages in the repo. Structural inspiration is
fine; attribution and copied assets are not.

### 2.3 Static site, no build step

- HTML + one CSS file + one vanilla-JS file. **No frameworks, no bundler, no npm dependencies.**
- Pages are hand-written; every page repeats the same nav and the same four-column footer.
- Only the optional asset generator uses Python (`tools/generate_logo.py`).

### 2.4 Accessibility

- Text on light surfaces must meet **WCAG AA** (4.5:1 for body text, 3:1 for ≥ 24px or bold
  ≥ 18.66px). The palette in §5 is tuned for this — do not lighten the accent tokens.
- **Text on a gradient is checked against the lightest stop of that gradient**, not against the
  page background. Avatar chips and the CTA band are gradients — keep white text on the
  AA-safe `--accent` (`#c13c26`), `--accent-2` (`#356b1c`), `--accent-3` (`#0f6b9f`),
  `--accent-4` (`#7c3aed`) or `--accent-5` (`#c026d3`), never on `--accent-glow`.
- Every page declares `<meta name="theme-color" content="#f6f8fc" />` for the browser chrome.
- Icons are inline SVG with `stroke="currentColor"` so they inherit the text colour.

---

## 3. Repo map

```
kavach-ai/
├── README.md                       # root documentation (mirrors this file)
├── instruction.md                  # this file — agent instructions, mirrors README.md
├── .gitignore
├── kavach_mcp-0.1.11/              # open-source detection middleware (reference)
├── tools/
│   └── generate_logo.py            # regenerates docs/assets/logo.png from the SVG geometry
└── docs/                           # the GitHub Pages site root
    ├── index.html                  # home — hero, pillars, rules grid, testimonials, CTA
    ├── home.html                   # legacy alias → redirects to index.html
    ├── readme.html                 # rendered copy of docs/README.md
    ├── README.md                   # documentation for the publish root
    ├── robots.txt                  # crawler directives + sitemap pointer
    ├── sitemap.xml                 # all public routes
    ├── CNAME                       # custom domain (kavach-ai.com)
    ├── css/
    │   └── style.css               # full design system (light theme)
    ├── js/
    │   └── main.js                 # sticky nav, mobile menu, reveal, demo form
    ├── pages/
    │   ├── platform.html           # Inside-Out platform + architecture + capabilities
    │   ├── cloud-security.html     # AWS · Azure · GCP multi-cloud security
    │   ├── data-protection.html    # AI data protection: discover → policy → insight
    │   ├── detection-rules.html    # the 11 detection rule families
    │   ├── mcp-security.html       # protecting Model Context Protocol tool calls
    │   ├── customers.html          # logo band + case studies
    │   ├── about.html              # mission, story, leadership, investors
    │   ├── trust.html              # Trust & Security: certifications, controls, disclosure
    │   ├── newsroom.html           # news, research, press kit
    │   ├── careers.html            # values, benefits, open roles, hiring process
    │   ├── partners.html           # partner programs and ecosystem
    │   ├── privacy.html            # Privacy Policy
    │   ├── terms.html              # Terms of Use
    │   └── demo.html               # demo request form + tour
    └── assets/
        ├── logo.svg / logo.png     # brand logo (also used as favicon)
        └── linkedin-cover.png      # LinkedIn company page cover (1584×396)
```

---

## 4. Pages

| Route | Purpose |
|-------|---------|
| `/` | Landing: Inside-Out positioning, 3 pillars, detection-engine demo, rules grid, testimonials, recognition, CTA |
| `/pages/platform.html` | The platform: live discovery, attack-path exposure, realtime D&R, architecture |
| `/pages/cloud-security.html` | AWS / Azure / GCP coverage, posture, AI & data protection in the cloud |
| `/pages/data-protection.html` | Discover → Policy → Insight loop, AI safety controls, editions |
| `/pages/detection-rules.html` | Rule families with regex examples + FastMCP integration snippet |
| `/pages/mcp-security.html` | Why MCP is the new attack surface; tool inventory, guardrails, audit |
| `/pages/customers.html` | Customer logos and three case-study spotlights |
| `/pages/about.html` | Company mission, story timeline, leadership, investors |
| `/pages/trust.html` | Certifications, security controls, data handling, responsible disclosure |
| `/pages/newsroom.html` | Press releases, threat research and a media kit |
| `/pages/careers.html` | Culture, benefits, open roles and hiring process |
| `/pages/partners.html` | Cloud alliances, technology and reseller/MSSP programs |
| `/pages/privacy.html` · `/pages/terms.html` | Legal |
| `/pages/demo.html` | Demo request form (client-side), what-you'll-see tour |

---

## 5. Design system — light theme

All tokens live in the `:root` block of `docs/css/style.css`. **Never hard-code a colour in a
component rule** — add or reuse a token.

### Surfaces

| Token | Value | Use |
|-------|-------|-----|
| `--page` | `#f6f8fc` | Page background, default sections, footer |
| `--surface` | `#ffffff` | Cards, panels, `.section.alt`, tables, forms |
| `--surface-2` | `#f8fafc` | Inset surfaces: table heads, code blocks, inputs |
| `--tint` | `#eef2f9` | Tinted bands (`<section class="section tint">`) |

### Lines & text

| Token | Value | Use |
|-------|-------|-----|
| `--border` | `#e2e8f0` | Hairlines, card borders |
| `--border-strong` | `#cbd5e1` | Input borders, ghost buttons |
| `--text` | `#0f172a` | Headings and body copy |
| `--text-muted` | `#56637a` | Secondary copy, labels |
| `--text-inverse` | `#ffffff` | Text on solid accent buttons |

### Accents & status

| Token | Value | Use |
|-------|-------|-----|
| `--accent` | `#c13c26` | Primary CTA, eyebrows, links — AA-safe on light |
| `--accent-glow` | `#f2583c` | Gradients and glows only, never small text |
| `--accent-soft` | `#fdece7` | Coral tint backgrounds |
| `--accent-2` | `#356b1c` | Trust metrics, green highlights |
| `--accent-3` | `#0f6b9f` | Info, kickers, footer links |
| `--accent-4` / `--accent-5` | `#7c3aed` / `#c026d3` | Violet / magenta accents |
| `--danger` / `--warning` / `--safe` | `#c0271d` / `#b45309` / `#356b1c` | Status text on their `-soft` tints |

### Section variants

| Class | Look |
|-------|------|
| `section` | Transparent — inherits `--page` |
| `section alt` | White (`--surface`) |
| `section tint` | Soft blue-grey band (`--tint`) — used for platform, trust, newsroom bands |
| `hero` / `page-hero` | White → `#eef3fb` gradient with soft colour radials |
| `cta-band` | Coral → violet → blue tint gradient |
| `footer` | `--page` with a top hairline |
| `.console` | **Intentionally dark** (`--console-bg`) — a terminal mock, not the theme |

Other type tokens: `--radius-lg/md/sm` (24/16/10), `--shadow-soft`, `--shadow-strong`,
`--shadow-dark`, `--maxw: 1200px`, and `--font` (Inter with a system fallback stack).

---

## 6. Brand assets

- `docs/assets/logo.svg` — the source of truth for the mark: a light rounded tile with a soft
  brand edge, a gradient armour shield (`#2f9fe0 → #7c3aed → #c026d3`) and a green verified check.
- `docs/assets/logo.png` — 512×512 raster fallback, generated from the same geometry.
- Regenerate the PNG after editing the SVG:

  ```bash
  python tools/generate_logo.py
  ```

  It needs Pillow + NumPy and reproduces the SVG faithfully (verified against a Chromium render).
- The logo is the favicon: every page links `assets/logo.svg` and `assets/logo.png`
  (`../assets/…` from `docs/pages/`).
- **Cache-busting.** Every logo/favicon reference carries one shared version query:
  `assets/logo.svg?v=2` and `assets/logo.png?v=2`. Browsers keep favicons in a separate store
  that ignores `Cache-Control`, so a changed mark can otherwise stay stale for days. After
  editing either asset, bump the number on every page in one pass:

  ```powershell
  Get-ChildItem docs -Recurse -Include *.html | ForEach-Object {
    $t = [IO.File]::ReadAllText($_.FullName)
    $t = $t -replace 'assets/logo\.(svg|png)\?v=\d+', 'assets/logo.$1?v=3'
    [IO.File]::WriteAllText($_.FullName, $t, (New-Object Text.UTF8Encoding($false)))
  }
  ```

  Keep the same number on `/logo.svg` and `/logo.png`, and never change the mark without
  bumping it — that is the only reliable way to refresh a cached favicon.
- The mark must stay legible on white: never put the logo on a dark fill without checking it.

---

## 7. Detection engine

The 11 rule families featured on the site come from the `KAVACH_RULES` set in
`kavach/rules.py`:

Prompt Injection · Data Exfiltration · PII Detection · Secret Leakage · Dangerous
Execution · SQL Injection · Path Traversal · Filesystem Destruction · Cloud Destruction
· Shell Injection · Tool Abuse — plus fully custom rules.

---

## 8. Run locally

```bash
cd docs
python3 -m http.server 8080
# open http://localhost:8080
```

Or use any static server (`npx serve`, Vercel, Netlify, GitHub Pages…).
No server-side logic — the whole site deploys as-is.

---

## 9. Deploy

Deployed on GitHub Pages with a custom domain (`docs/` folder, `main` branch).
`index.html` is the home page; `home.html` is kept only as a redirect.

DNS records to set at Hostinger → hPanel → Domains → `kavach-ai.com` → DNS:

| Type | Name/Host | Value |
|------|-----------|-------|
| A    | `@`       | `185.199.108.153` |
| A    | `@`       | `185.199.109.153` |
| A    | `@`       | `185.199.110.153` |
| A    | `@`       | `185.199.111.153` |
| CNAME | `www`    | `deepanshu-devops.github.io` (optional) |
| CAA  | `@`       | `0 issue "letsencrypt.org"` (optional) |

Remove any old parking A record. After DNS propagates, GitHub auto-issues TLS and
`https://kavach-ai.com/` serves the home page.

---

## 10. Task checklists

### Adding a page

1. Create `docs/pages/<name>.html` — copy the nav + footer from an existing page.
2. Add `<meta name="theme-color" content="#f6f8fc" />` under the viewport meta.
3. Link it from the nav (product pages) or the footer (company/legal pages).
4. Add the route to `docs/sitemap.xml`.
5. Update `README.md`, **this file**, `docs/README.md` and `docs/readme.html`.

### Changing a colour

1. Edit the token in `:root` of `docs/css/style.css` — never a component rule.
2. Re-check contrast (AA) for text on every surface that uses it — including the lightest
   stop of any gradient it lands on.
3. If the accent palette changed, regenerate `docs/assets/logo.png` if the logo colours moved.
4. Update the token tables in `README.md`, this file, `docs/README.md` and `docs/readme.html`.

### Changing the logo

1. Edit `docs/assets/logo.svg`.
2. Run `python tools/generate_logo.py`.
3. Update §6 of this file and the asset list in `README.md` if the file names changed.

### Any documentation change

1. `README.md` **and** `instruction.md`, in the same change.
2. If the site facts changed → `docs/README.md` and `docs/readme.html` too.

---

## 11. Contact

- Website: [https://kavach-ai.com](https://kavach-ai.com)
- Email: [corporate@kavach-ai.com](mailto:corporate@kavach-ai.com)
- Security: [security@kavach-ai.com](mailto:security@kavach-ai.com)
- LinkedIn: `https://linkedin.com/company/kavach-ai`

---

© 2026 Kavach-AI. Built on the kavach-mcp open-source middleware.
