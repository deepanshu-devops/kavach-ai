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
- [Site structure](#site-structure)
- [Pages](#pages)
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

## Site structure

```
kavach-ai/
├── README.md                       # this file
├── .gitignore
├── kavach_mcp-0.1.11/              # open-source detection middleware (reference)
└── docs/                           # the GitHub Pages site root
    ├── index.html                  # home — hero, pillars, rules grid, testimonials, CTA
    ├── css/
    │   └── style.css               # full design system (dark Inside-Out theme)
    ├── js/
    │   └── main.js                 # sticky nav, mobile menu, reveal, demo form
    ├── pages/
    │   ├── platform.html           # Inside-Out platform + architecture + capabilities
    │   ├── cloud-security.html     # AWS · Azure · GCP multi-cloud security
    │   ├── data-protection.html    # AI data protection: discover → policy → insight
    │   ├── detection-rules.html    # the 11 detection rule families
    │   ├── mcp-security.html       # protecting Model Context Protocol tool calls
    │   └── demo.html               # demo request form + tour
    └── assets/
        ├── logo.svg / logo.png     # brand logo (also used as favicon)
        └── linkedin-cover.png      # LinkedIn company page cover (1584×396)
```

## Pages

| Route | Purpose |
|-------|---------|
| `/` | Landing: Inside-Out positioning, 3 pillars, detection-engine demo, rules grid, testimonials, CTA |
| `/pages/platform.html` | The platform: live discovery, attack-path exposure, realtime D&R, architecture |
| `/pages/cloud-security.html` | AWS / Azure / GCP coverage, posture, AI & data protection in the cloud |
| `/pages/data-protection.html` | Discover → Policy → Insight loop, AI safety controls, editions |
| `/pages/detection-rules.html` | Rule families with regex examples + FastMCP integration snippet |
| `/pages/mcp-security.html` | Why MCP is the new attack surface; tool inventory, guardrails, audit |
| `/pages/demo.html` | Demo request form (client-side), what-you'll-see tour |

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
- Brand assets generated as SVG / PNG

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
`https://kavach-ai.com/` serves the Data Protection landing page.

## Contact

- Website: [https://kavach-ai.com](https://kavach-ai.com)
- Email: [corporate@kavach-ai.com](mailto:corporate@kavach-ai.com)
- LinkedIn: `https://linkedin.com/company/kavach-ai`

---

© 2026 Kavach-AI. Built on the kavach-mcp open-source middleware.