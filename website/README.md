# Kavach-AI — Website

A static marketing website for **Kavach-AI**: *AI & MCP Security for the Agentic Era*.

The site is a product-marketing page modeled on the layout, section flow and visual
language of the **Upwind security platform** (dark "Inside-Out" hero, three operating
pillars, capability/feature grids, recognition band, testimonial grid, demo CTA),
while the product narrative is grounded in the **kavach-mcp** open-source middleware
in this repo (`kavach_mcp-0.1.11/`).

## Why this pairing

- **Upwind** provides the *structure*: live inventory → high-signal exposures → real-time
  protection, Inside-Out positioning, enterprise trust/CTA sections.
- **Kavach** provides the *substance*: the detection engine and its 11 rule families
  (prompt injection, secret leakage, PII, SQL injection, path traversal, cloud
  destruction, tool abuse, …) are the hero of the site.

## Project structure

```
website/
├── index.html                  # Home — hero, pillars, rules grid, testimonials, CTA
├── css/
│   └── style.css               # Full design system (Upwind-inspired tokens)
├── js/
│   └── main.js                 # Nav, mobile menu, reveal-on-scroll, demo form
├── pages/
│   ├── platform.html           # "Inside-Out Platform" — architecture + capability matrix
│   ├── detection-rules.html    # The 11 detection rule families + code integration
│   ├── mcp-security.html       # MCP guardrail layer — why MCP is the attack surface
│   └── demo.html               # Demo request form + what-you'll-see tour
└── assets/                     # (placeholder for future images/branding)
```

## Design tokens (from Upwind's palette)

| Token | Value | Use |
|-------|-------|-----|
| `--bg-dark` | `#141217` | Hero / footer / dark sections |
| `--bg-dark-2` | `#18202d` | Dark platform sections |
| `--bg-light` | `#fafafa` | Base light background |
| `--accent` | `#f2583c` | Primary CTA / highlights |
| `--accent-2` | `#9fe870` | Trust metrics / secondary accent |
| `--accent-3` | `#57c1fe` | Info / tertiary |
| `--danger` | `#ff5950` | Blocked detections |

Typography: **Inter** (Google Fonts, with a system fallback stack).

## Run it

No build step — serve the folder statically:

```bash
cd website
python3 -m http.server 8080
# open http://localhost:8080
```

## Files still to add (optional)

- `assets/` — real logo, dashboard screenshots, favicon
- More product pages: AI Security Posture (AI-SPM), API Security, Cloud Posture (CSPM)
- An interactive rule-demo playground page wiring the actual `kavach` engine (Pyodide)

## Credit

- Product content derived from the **kavach-mcp** package (`kavach/engine.py`,
  `kavach/rules.py`, `kavach/middleware.py`).
- Layout/structure benchmarked against **Upwind** (`upwind.io`), a cloud & AI security
  platform. All copy is original to this project.