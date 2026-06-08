# MobileTrans Affiliate Site — build.py v2

A complete, production-ready affiliate marketing website for [MobileTrans by Wondershare](https://mobiletrans.wondershare.com), built for GitHub Pages at:

**`https://brightlane.github.io/mobiletransonline/`**

---

## Quick Start

```bash
python3 build.py
```

Outputs 49 files into `mobiletrans-site/` next to `build.py`. Zero dependencies — pure Python 3 stdlib only.

---

## Deployment

Your repo needs exactly three files:

```
mobiletransonline/          ← your GitHub repo
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

**One-time GitHub setup:**
1. Go to `Settings → Pages → Source` → set to **GitHub Actions**
2. Push to `main` — the workflow builds and deploys automatically in ~30 seconds

Every subsequent push to `main` rebuilds all 22 pages and redeploys live.

---

## Config (top of build.py)

```python
BASE      = Path(__file__).parent / "mobiletrans-site"          # Output folder — always relative
SITE_ROOT = "/mobiletransonline"                                 # Must match your GitHub repo name exactly
SITE_URL  = "https://brightlane.github.io/mobiletransonline"    # Full canonical base URL
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048399004532&atid=mobiletransweb"
YEAR      = date.today().year                                    # Auto-updates on every build
```

⚠️ **Critical:** `SITE_ROOT` must exactly match your GitHub repo name. If your repo is `mobiletransonline`, `SITE_ROOT` must be `/mobiletransonline`. Getting this wrong causes 404s — it was the exact issue that broke the AllMyTube site.

---

## All 22 Pages

| Page | URL | Target Keywords | Schema |
|---|---|---|---|
| Homepage | `/` | MobileTrans download, phone transfer | SoftwareApp + Breadcrumb |
| Features | `/features/` | MobileTrans features, WhatsApp transfer | SoftwareApp + ItemList |
| How It Works | `/how-it-works/` | how to transfer phone data | SoftwareApp + HowTo |
| Supported Devices | `/supported-devices/` | MobileTrans compatible phones | SoftwareApp + Breadcrumb |
| Pricing | `/pricing/` | MobileTrans price, cost, discount | SoftwareApp + FAQPage |
| Review | `/review/` | MobileTrans review, is it worth it | SoftwareApp + Review |
| FAQ | `/faq/` | MobileTrans safe, free, WhatsApp | SoftwareApp + FAQPage |
| Download | `/download/` | download MobileTrans Windows Mac | SoftwareApp + Breadcrumb |
| Blog | `/blog/` | phone transfer guides | SoftwareApp + Breadcrumb |
| Android to iPhone | `/android-to-iphone/` | Android to iPhone transfer | SoftwareApp + Article |
| iPhone to Android | `/iphone-to-android/` | iPhone to Android, WhatsApp transfer | SoftwareApp + Article |
| WhatsApp Transfer | `/whatsapp-transfer/` | WhatsApp Android iPhone, both ways | SoftwareApp + Article |
| Phone Backup | `/phone-backup/` | back up phone to PC | SoftwareApp + Article |
| Samsung to iPhone | `/samsung-to-iphone/` | Samsung Galaxy to iPhone | SoftwareApp + Article |
| iCloud to Android | `/icloud-to-android/` | iCloud contacts photos to Android | SoftwareApp + Article |
| Alternatives | `/alternatives/` | best phone transfer software | SoftwareApp + Breadcrumb |
| vs Smart Switch | `/vs-smart-switch/` | MobileTrans vs Smart Switch | SoftwareApp + Breadcrumb |
| vs iMazing | `/vs-imazing/` | MobileTrans vs iMazing | SoftwareApp + Breadcrumb |
| vs dr.fone | `/vs-drfone/` | MobileTrans vs dr.fone | SoftwareApp + Breadcrumb |
| Privacy Policy | `/privacy/` | — | — |
| Disclaimer | `/disclaimer/` | — | — |
| 404 | `/404.html` | — | — |

---

## SEO Files

| File | Purpose |
|---|---|
| `sitemap.xml` | 21 URLs with `lastmod`, priority and changefreq — submit to Google & Bing |
| `robots.txt` | Allows all crawlers, points to sitemap |
| `llms.txt` | Structured summary for AI crawlers (Perplexity, ChatGPT, Claude, etc.) |
| `feed.xml` | RSS feed with 5 blog articles |
| `assets/favicon.svg` | Phone-transfer branded SVG icon (purple/cyan) |
| `.nojekyll` | Prevents GitHub Pages Jekyll from processing HTML files |

**After deploying, submit your sitemap:**
```
https://brightlane.github.io/mobiletransonline/sitemap.xml
```
→ **Google Search Console** → Add property → Submit sitemap URL
→ **Bing Webmaster Tools** → Import from Google or submit directly

---

## Schema Markup — What's on Each Page

Every page includes `SoftwareApplication` + `BreadcrumbList` as a baseline. Additional schemas:

| Page | Extra Schema |
|---|---|
| `/how-it-works/` | `HowTo` — 4 steps with names and descriptions |
| `/features/` | `ItemList` — 5 key features listed |
| `/review/` | `Review` — rating 9.1/10, datePublished, author |
| `/faq/` | `FAQPage` — 12 questions and full answers |
| `/pricing/` | `FAQPage` — 5 pricing-specific questions |
| All guide pages | `og:type = article` for better social sharing |

---

## SEO Built Into Every Page

- Unique `<title>` (under 60 chars) and `<meta description>` (under 160 chars) per page
- `<link rel="canonical">` on every page
- Full Open Graph tags: `og:title`, `og:description`, `og:url`, `og:type`, `og:image`, `og:locale`, `og:site_name`
- Twitter Card: `summary_large_image` on every page
- RSS feed link (`<link rel="alternate">`) on every page
- Mobile-responsive with accessible hamburger nav
- Semantic HTML throughout (`<nav>`, `<section>`, `<footer>`, `<details>`, `<summary>`)
- `aria-label` on nav toggle button
- `rel="noopener sponsored"` on all affiliate links (correct per Google guidelines)

---

## Affiliate Link

Every CTA and download button uses:
```
https://www.linkconnector.com/ta.php?lc=007949048399004532&atid=mobiletransweb
```

To update, change the `AFF` variable at the top of `build.py` and re-run.

All affiliate links include `rel="noopener sponsored"` as required by Google's guidelines for paid/affiliate links.

---

## Design System

Deep navy/purple theme — distinct from other sites.

| Variable | Value | Usage |
|---|---|---|
| `--acc` | `#7c6bff` | Primary purple — CTAs, headings, links |
| `--acc2` | `#ff4f82` | Pink/red — logo dot, warnings, accents |
| `--acc3` | `#00f0ff` | Cyan — code text, highlights, success |
| `--gold` | `#fbbf24` | Gold — star ratings, warnings |
| `--green` | `#22c55e` | Green — checkmarks, success states |
| `--bg` | `#030512` | Deep near-black background |
| `--txt` | `#eef0f8` | Primary text |
| `--muted` | `#7a86a0` | Body / secondary text |

Gradient text is used for stat numbers and the score badge via `-webkit-background-clip: text`. The hero badge uses a pulsing dot animation. CTAs use a `glow-pulse` keyframe animation.

The entire CSS lives in one `CSS` string variable near the top of `build.py`. Edit once to restyle all 22 pages simultaneously.

---

## MobileTrans Product Facts (for content updates)

| Fact | Value |
|---|---|
| Publisher | Wondershare Software Ltd (publicly listed, est. 2003) |
| Product launched | 2012 |
| Users | 50M+ worldwide |
| Supported devices | 6,000+ |
| Data types | 18+ |
| Transfer speed | 30 MB/s average — 200× faster than Bluetooth |
| 1 GB video transfer | ~30 seconds |
| Full phone switch | 3–15 minutes (USB) |
| Wireless | Up to 8 data types via QR code over Wi-Fi |
| Platforms | Windows 7–11, macOS 10.12+ (Intel + Apple Silicon) |
| Mobile app | iOS and Android (wireless transfers without PC) |
| Pricing | Free trial (5 contacts) · $35.99/yr · $44.99 lifetime · Up to 60% off |
| Key differentiator | WhatsApp in BOTH directions including iPhone → Android |
| Also supports | WeChat, Line, Kik, GBWhatsApp, WhatsApp Business |
| Privacy | Zero server upload — all transfers direct device-to-device |

---

## Adding a New Page

1. Write a `pg_mypage()` function following the same pattern as existing ones
2. Use `page(title, desc, path, body, kw, extras, article)` to wrap it
3. Call `write("my-page/index.html", pg_mypage())` inside `main()`
4. Add the URL to `mk_sitemap()` inside the `pages = [...]` list
5. Add a link in `foot()` under the right footer column

---

## v2 Improvements over v1

| Area | v1 | v2 |
|---|---|---|
| Pages | 19 | 22 (+ Samsung→iPhone, iCloud→Android, vs dr.fone) |
| Schema types | 2 | 6 (+ HowTo, ItemList, Review, FAQPage) |
| FAQ answers | 10 | 12 full detailed answers |
| Review categories | 7 | 7 + separate pros/cons boxes |
| Testimonials | 6 | 6 with avatar initials + detailed attribution |
| Pricing | Basic cards | Strikethrough prices, 5-item FAQ, promotion callout |
| Blog cards | Date only | Date + read time |
| Steps | Basic | Steps with tip chips |
| Hero | Simple trust line | Pulsing badge dot + trust items row |
| Stat numbers | Plain text | Gradient text via background-clip |
| Internal linking | Minimal | hbox callouts with direct links on homepage |
| Competitor coverage | 2 vs pages | 3 vs pages + richer alternatives page |
| CSS | ~250 lines | ~400 lines — more component coverage |
| Content depth | Short paragraphs | Full explanatory paragraphs on every feature |

---

## File Structure After Build

```
mobiletrans-site/
├── .nojekyll
├── index.html
├── 404.html
├── sitemap.xml
├── robots.txt
├── llms.txt
├── feed.xml
├── assets/
│   └── favicon.svg
├── features/index.html
├── how-it-works/index.html
├── supported-devices/index.html
├── pricing/index.html
├── review/index.html
├── faq/index.html
├── download/index.html
├── blog/index.html
├── android-to-iphone/index.html
├── iphone-to-android/index.html
├── whatsapp-transfer/index.html
├── phone-backup/index.html
├── samsung-to-iphone/index.html
├── icloud-to-android/index.html
├── alternatives/index.html
├── vs-smart-switch/index.html
├── vs-imazing/index.html
├── vs-drfone/index.html
├── privacy/index.html
└── disclaimer/index.html
```

---

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Generator | Python 3 stdlib only | Zero dependencies, runs on any machine or CI |
| HTML/CSS/JS | Vanilla — no frameworks | Instant load, no build step, no versioning issues |
| Fonts | Google Fonts CDN | Bebas Neue + Inter — bold and professional |
| Hosting | GitHub Pages | Free, HTTPS, global CDN |
| CI/CD | GitHub Actions | Auto-deploy on every `git push` to `main` |

---

## License

Independent affiliate guide. MobileTrans is a product of Wondershare Software Ltd. This site is not affiliated with or endorsed by Wondershare.
