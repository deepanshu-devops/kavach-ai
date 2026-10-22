# Kavach-AI

**AI & MCP Security for the Agentic Era — Cloud & AI Security from the Inside-Out.**

Kavach-AI is a static marketing site for Kavach-AI, a security platform that protects
AI agents, LLM tool calls, MCP infrastructure and multi-cloud workloads (AWS, Azure, GCP).
The site pairs the layout and operating model of modern cloud-security platforms with the
detection engine of the open-source **kavach-mcp** middleware.

🌐 [kavach-ai.com](https://kavach-ai.com) · ✉️ [corporate@kavach-ai.com](mailto:corporate@kavach-ai.com)

---

## Table of Contents

- [Why Kavach-AI](#why-kavach-ai)
- [Company realism](#company-realism)
- [Documentation sync](#documentation-sync)
- [Site structure](#site-structure)
- [Pages](#pages)
- [Design system](#design-system)
- [Detection engine](#detection-engine)
- [Tech stack](#tech-stack)
- [Run locally](#run-locally)
- [Deploy](#deploy)
- [Contact](#contact)

## Why Kavach-AI

AI and MCP infrastructure now change in real time. Manual inventories and periodic scans
can't keep up. Kavach-AI follows an **Inside-Out** operating model:

| Pillar | What it does |
|--------|--------------|
| **Live inventory** | Know what agents, tools, MCP servers, data flows and non-human identities run, connect and expose — refreshed every 30 seconds |
| **Fix high-signal exposures** | Use live exposure and activity to separate real risk from theoretical risk and cut alert noise |
| **Real-time protection** | Detect and stop prompt attacks, tool abuse, secrets leakage and cloud destruction while they happen |

The platform content builds on the rule families shipped in `kavach-mcp` (prompt
injection, data exfiltration, PII, secret leakage, SQL injection, path traversal,
filesystem/cloud destruction, shell injection, tool abuse).

The presentation is a **light theme** — airy surfaces, deep ink text and a coral /
green / blue accent set — with the dark console mock kept as the single deliberately
dark element, because it is a product screenshot of a terminal.

## Company realism

The site is a presentation of a fictional company, modelled on how a real cloud & AI
security vendor (**Upwind Security**) presents itself — a light "Inside-Out" hero, three
operating pillars, capability/feature grids, customer logos, analyst recognition, a
Trust/Security page, Newsroom, Careers and Partners — while the product narrative is
grounded in the `kavach-mcp` open-source middleware in this repo.

To keep the company believable and self-consistent (and to avoid impersonation), **all
customer names, testimonials, funding, investors, leadership, offices, awards and dates
are original illustrative placeholders**, not claims about any real person or firm. When
the site goes live, replace them with verified facts:

- `pages/about.html` — founders, mission, funding, investors, offices
- `pages/newsroom.html` — press releases, research, dates
- `pages/careers.html` — open roles and locations
- `pages/partners.html` — partner program and integrations
- `pages/trust.html` — certifications and security controls
- `pages/customers.html` and the home/testimonial sections — customer names & quotes

No page references Upwind or its real awards/customers; the layout is merely the
benchmark. See [docs/README.md](docs/README.md) for the design-language notes.

## Documentation sync

[`instruction.md`](instruction.md) is the agent-facing twin of this README and carries the
same facts plus the working rules for this repo. **Whenever `README.md` is updated, update
`instruction.md` in the same change** — and the other way round. If the site itself changes
(new page, new token, new asset, new route), update all of:

| File | What it holds |
|------|---------------|
| `README.md` | Root documentation for humans |
| `instruction.md` | Working instructions for agents — same facts, same order |
| `docs/README.md` | Documentation for the publish root (`docs/`) |
| `docs/readme.html` | HTML twin of `docs/README.md`, served at `/readme.html` |
| `docs/sitemap.xml` | Every public route |

## Site structure

```
kavach-ai/
├── README.md                       # this file
├── instruction.md                  # agent instructions — mirrors this file
├── .gitignore
├── kavach_mcp-0.1.11/              # open-source detection middleware (reference)
├── tools/
│   └── generate_logo.py            # regenerates docs/assets/logo.png from the SVG geometry
└── docs/                           # the GitHub Pages site root
    ├── index.html                  # home — hero, pillars, rules grid, testimonials, CTA
    ├── home.html                   # legacy alias → redirects to index.html
    ├── readme.html                 # rendered copy of docs/README.md
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

## Design system

All tokens live in the `:root` block of `docs/css/style.css` — never hard-code a colour in a
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

## Detection engine

The 11 rule families featured on the site come from the `KAVACH_RULES` set in
`kavach/rules.py`:

Prompt Injection · Data Exfiltration · PII Detection · Secret Leakage · Dangerous
Execution · SQL Injection · Path Traversal · Filesystem Destruction · Cloud Destruction
· Shell Injection · Tool Abuse — plus fully custom rules.

## Tech stack

- **Static site** — no build step, no dependencies
- HTML5 + CSS3 custom design system (CSS variables, grid, reveal-on-scroll)
- Vanilla JavaScript (sticky nav, mobile menu, IntersectionObserver, form handling)
- Inter (Google Fonts) with a system fallback stack
- Brand assets generated as SVG / PNG — `tools/generate_logo.py` rebuilds `docs/assets/logo.png`
  from the same geometry as `docs/assets/logo.svg`

## Run locally

```bash
cd docs
python3 -m http.server 8080
# open http://localhost:8080
```

Or use any static server (`npx serve`, Vercel, Netlify, GitHub Pages…).
No server-side logic — the whole site deploys as-is.

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

Remove any old parking A record. After DNS propagates, GitHub auto-issues TLS and
`https://kavach-ai.com/` serves the home page.

## Contact

- Website: [https://kavach-ai.com](https://kavach-ai.com)
- Email: [corporate@kavach-ai.com](mailto:corporate@kavach-ai.com)
- Security: [security@kavach-ai.com](mailto:security@kavach-ai.com)
- LinkedIn: `https://linkedin.com/company/kavach-ai`

---

© 2026 Kavach-AI. Built on the kavach-mcp open-source middleware.
