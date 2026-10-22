# Kavach-AI — Website

The GitHub Pages site for **Kavach-AI**: *AI & MCP Security for the Agentic Era*.

`docs/` is the publish root. It is a plain static site — HTML, one CSS design system and a
small vanilla-JS file — with no build step and no dependencies. The home page is
`index.html`; `home.html` is kept only as a redirect for old links.

The layout and section flow are benchmarked against how a modern cloud & AI security vendor
(**Upwind Security**) presents itself — a light "Inside-Out" hero, three operating pillars,
capability/feature grids, customer logos, recognition band, Trust/Security, Newsroom and
Careers — while the product narrative is grounded in the **kavach-mcp** open-source
middleware in this repo (`kavach_mcp-0.1.11/`).

The site is **light-themed**: airy surfaces, deep ink text, coral/green/blue accents. The
console mock (`.console`) is the one deliberately dark element — it is a product screenshot
of a terminal.

## Company realism

The company is fictional and presented as a plausible, self-consistent business so the site
reads like a real vendor. **All customer names, testimonials, funding, investors,
leadership, offices, awards and dates are original illustrative placeholders** — they are
not claims about any real person or firm, and no page names Upwind or its real
awards/customers. Replace the placeholders with verified facts before anything goes live:

- `pages/about.html` — founders, mission, funding, investors, offices
- `pages/newsroom.html` — press releases, research, dates
- `pages/careers.html` — open roles and locations
- `pages/partners.html` — partner program and integrations
- `pages/trust.html` — certifications and security controls
- `pages/customers.html` and the home/testimonial sections — customer names & quotes

See the root [README.md](../README.md) for the full company-facts list.

Documentation is kept in sync across five files — `README.md`, [`../instruction.md`](../instruction.md)
(the agent-facing twin), this file, `readme.html` (the HTML twin of this file) and
`sitemap.xml`. Update them together whenever the site changes.

## Site structure

```
docs/                             # GitHub Pages publish root
├── index.html                    # Home — hero, pillars, rules grid, testimonials, CTA
├── home.html                     # legacy alias → meta-refresh redirect to index.html
├── readme.html                   # HTML twin of this file (served at /readme.html)
├── README.md                     # this file
├── robots.txt                    # crawler directives + sitemap pointer
├── sitemap.xml                   # all public routes
├── CNAME                         # custom domain (kavach-ai.com)
├── css/
│   └── style.css                 # full design system (light theme)
├── js/
│   └── main.js                   # sticky nav, mobile menu, reveal-on-scroll, demo form
├── pages/
│   ├── platform.html             # Inside-Out platform + architecture + capabilities
│   ├── cloud-security.html       # AWS · Azure · GCP multi-cloud security
│   ├── data-protection.html      # AI data protection: discover → policy → insight
│   ├── detection-rules.html      # the 11 detection rule families
│   ├── mcp-security.html         # protecting Model Context Protocol tool calls
│   ├── customers.html            # logo band + case studies
│   ├── about.html                # mission, story, leadership, investors
│   ├── trust.html                # Trust & Security: certifications, controls, disclosure
│   ├── newsroom.html             # news, research, press kit
│   ├── careers.html              # values, benefits, open roles, hiring process
│   ├── partners.html             # partner programs and ecosystem
│   ├── privacy.html              # Privacy Policy
│   ├── terms.html                # Terms of Use
│   └── demo.html                 # demo request form + tour
└── assets/
    ├── logo.svg / logo.png       # brand logo (also used as favicon)
    └── linkedin-cover.png        # LinkedIn company page cover (1584×396)
```

## Pages

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

## Navigation & branding

- The top nav carries the six product links: Platform, Cloud Security, Data Protection,
  Detection Rules, MCP Security, Customers.
- The company pages (About, Trust, Newsroom, Careers, Partners) and legal links live in the
  footer's **Company**, **Resources** and bottom bar — matching how real vendors separate
  product navigation from corporate navigation.
- Brand markup is consistently `Kavach<span class="ai">AI</span>` and the footer is the same
  four-column block (brand + Platform + Company + Resources) on every page.

## Design tokens

All tokens live in the `:root` block of `css/style.css` — never hard-code a colour in a
component rule. The palette is tuned so every text/background pair meets WCAG AA on the light
theme.

| Token | Value | Use |
|-------|-------|-----|
| `--page` | `#f6f8fc` | Page background, default sections, footer |
| `--surface` | `#ffffff` | Cards, panels, `.section.alt`, tables, forms |
| `--surface-2` | `#f8fafc` | Inset surfaces: table heads, code blocks, inputs |
| `--tint` | `#eef2f9` | Tinted bands (`<section class="section tint">`) |
| `--border` / `--border-strong` | `#e2e8f0` / `#cbd5e1` | Hairlines, card and input borders |
| `--text` / `--text-muted` | `#0f172a` / `#56637a` | Headings and body / secondary copy |
| `--accent` | `#c13c26` | Primary CTA, eyebrows, links — AA-safe on light |
| `--accent-glow` | `#f2583c` | Gradients and glows only, never small text |
| `--accent-2` | `#356b1c` | Trust metrics, green highlights |
| `--accent-3` | `#0f6b9f` | Info, kickers, footer links |
| `--danger` / `--warning` / `--safe` | `#c0271d` / `#b45309` / `#356b1c` | Status text on their `-soft` tints |

Section variants: `section` (transparent → `--page`), `section alt` (white), `section tint`
(soft blue-grey band), `hero` / `page-hero` (white → `#eef3fb` gradient with colour radials),
`cta-band` (coral → violet → blue tint gradient), `footer` (`--page` with a top hairline).
The `.console` block is intentionally dark — it is a terminal mock, not the theme.

Typography: **Inter** (Google Fonts, with a system fallback stack).

## Brand assets

- `assets/logo.svg` — source of truth for the mark: a light rounded tile with a soft brand
  edge, a gradient armour shield (`#2f9fe0 → #7c3aed → #c026d3`) and a green verified check.
- `assets/logo.png` — 512×512 raster fallback, generated from the same geometry.
- Regenerate the PNG after editing the SVG (needs Pillow + NumPy), from the repo root:

  ```bash
  python tools/generate_logo.py
  ```

- The logo doubles as the favicon: every page links `assets/logo.svg` and `assets/logo.png`
  (`../assets/…` from `pages/`). The mark must stay legible on white.
- Both references carry a shared cache-busting query (`?v=2`). Browsers keep favicons in a
  separate cache that ignores `Cache-Control`, so bump that number on every page whenever
  either asset changes.

## Detection engine

The 11 rule families featured on the site come from the `KAVACH_RULES` set in
`kavach/rules.py`:

Prompt Injection · Data Exfiltration · PII Detection · Secret Leakage · Dangerous
Execution · SQL Injection · Path Traversal · Filesystem Destruction · Cloud Destruction
· Shell Injection · Tool Abuse — plus fully custom rules.

## Run locally

No build step — serve the folder statically:

```bash
cd docs
python3 -m http.server 8080
# open http://localhost:8080
```

Or use any static server (`npx serve`, Vercel, Netlify, GitHub Pages…).

## Deploy

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

After DNS propagates, GitHub auto-issues TLS and `https://kavach-ai.com/` serves the home
page.

## Credit

- Product content derived from the **kavach-mcp** package (`kavach/engine.py`,
  `kavach/rules.py`, `kavach/middleware.py`).
- Layout/structure benchmarked against **Upwind** (`upwind.io`), a cloud & AI security
  platform. All copy, names and facts are original to this project.

---

© 2026 Kavach-AI. Built on the kavach-mcp open-source middleware.
