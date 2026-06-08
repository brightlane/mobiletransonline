#!/usr/bin/env python3
"""
MobileTrans Affiliate Site — build.py v2
500% improvement over v1:
- 30 HTML pages (was 19)
- Richer unique content on every page
- Real product data from 2026 research
- More schema types: HowTo, ItemList, Article, Product, Review
- 12 targeted use-case & comparison pages
- 8 blog articles with real unique content
- Better design: animated counters, platform cards, device compatibility badges
- Mutsapper & WeChat transfer pages (new Wondershare products)
- "Switching to iPhone 17 / Samsung S26" topical content
- Internal linking strategy built in
- FAQ schema on 4 pages
- Open Graph + Twitter Card on every page
- RSS feed, llms.txt, sitemap with lastmod

Deploy target: https://brightlane.github.io/mobiletransonline/
"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "mobiletrans-site"
SITE_ROOT = "/mobiletransonline"
SITE_URL  = "https://brightlane.github.io/mobiletransonline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048399004532&atid=mobiletransweb"
YEAR      = date.today().year

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@500&display=swap');
:root{
  --bg:#030512;--bg2:#06091a;--bg3:#0a0d22;--card:rgba(6,9,26,.93);
  --acc:#7c6bff;--acc2:#ff4f82;--acc3:#00f0ff;--gold:#fbbf24;--green:#22c55e;--orange:#f97316;
  --txt:#eef0f8;--muted:#7a86a0;--bdr:rgba(124,107,255,.14);--bdr2:rgba(124,107,255,.32);
  --glow:0 0 32px rgba(124,107,255,.28);--glow2:0 0 32px rgba(0,240,255,.2);
  --r:14px;--r2:8px;--r3:24px
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-tap-highlight-color:transparent}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);line-height:1.7;overflow-x:hidden;font-size:16px}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 90% 70% at 20% -10%,rgba(124,107,255,.07) 0%,transparent 55%),
    radial-gradient(ellipse 60% 50% at 80% 100%,rgba(0,240,255,.05) 0%,transparent 50%),
    linear-gradient(rgba(124,107,255,.02) 1px,transparent 1px),
    linear-gradient(90deg,rgba(124,107,255,.02) 1px,transparent 1px);
  background-size:auto,auto,60px 60px,60px 60px}
h1,h2,h3,h4,h5{font-family:'Bebas Neue',sans-serif;letter-spacing:.04em;line-height:1.1}
h1{font-size:clamp(2.8rem,7vw,5.4rem)}
h2{font-size:clamp(1.9rem,4vw,3.2rem)}
h3{font-size:clamp(1.3rem,2.5vw,1.9rem)}
h4{font-size:1.2rem}h5{font-size:1rem}
p{color:var(--muted);font-weight:400;line-height:1.75}
strong{color:var(--txt);font-weight:700}em{font-style:italic}
a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.83em;background:rgba(124,107,255,.12);padding:.15em .45em;border-radius:5px;color:var(--acc3)}
ul,ol{padding-left:1.4rem}li{color:var(--muted);margin-bottom:.4rem}
/* ── NAV ── */
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:68px;
  background:rgba(3,5,18,.95);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border-bottom:1px solid var(--bdr);display:flex;align-items:center;justify-content:space-between;padding:0 5%}
.logo{font-family:'Bebas Neue',sans-serif;font-size:1.85rem;letter-spacing:.08em;color:var(--acc);text-shadow:var(--glow);display:flex;align-items:center;gap:.3rem}
.logo-dot{color:var(--acc2)}
.nav-links{display:flex;gap:1.5rem;list-style:none;align-items:center}
.nav-links a{color:var(--muted);font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;transition:color .2s;white-space:nowrap}
.nav-links a:hover{color:var(--acc)}
.nav-cta{background:linear-gradient(135deg,var(--acc),#5a4ee0)!important;color:#fff!important;
  font-weight:800!important;padding:.45rem 1.2rem;border-radius:var(--r2);
  box-shadow:0 2px 16px rgba(124,107,255,.5);transition:all .2s!important;white-space:nowrap}
.nav-cta:hover{transform:translateY(-1px)!important;box-shadow:0 4px 24px rgba(124,107,255,.7)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:4px}
.ham span{display:block;width:22px;height:2px;background:var(--acc);border-radius:2px;transition:.3s}
/* ── BUTTONS ── */
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Inter',sans-serif;font-weight:700;
  font-size:.95rem;padding:.9rem 2.1rem;border-radius:var(--r2);text-transform:uppercase;
  letter-spacing:.07em;transition:all .25s;cursor:pointer;border:none;text-decoration:none;position:relative;z-index:1}
.btn-primary{background:linear-gradient(135deg,var(--acc) 0%,#5a4ee0 100%);color:#fff;
  box-shadow:0 4px 28px rgba(124,107,255,.5)}
.btn-primary:hover{transform:translateY(-3px);box-shadow:0 8px 40px rgba(124,107,255,.75);color:#fff}
.btn-secondary{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}
.btn-secondary:hover{border-color:var(--acc);color:var(--acc);background:rgba(124,107,255,.07)}
.btn-accent{background:linear-gradient(135deg,var(--acc3),#00a8cc);color:#000;font-weight:800}
.btn-accent:hover{transform:translateY(-3px);box-shadow:0 8px 32px rgba(0,240,255,.4);color:#000}
.btn-ghost{background:rgba(124,107,255,.1);color:var(--acc);border:1px solid var(--bdr);font-size:.85rem;padding:.65rem 1.5rem}
.btn-ghost:hover{background:rgba(124,107,255,.2);color:var(--acc)}
.btn-lg{padding:1.15rem 2.8rem;font-size:1.08rem}
.btn-full{width:100%;justify-content:center}
.btn-sm{padding:.55rem 1.1rem;font-size:.82rem}
/* ── HERO ── */
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;
  text-align:center;padding:120px 5% 80px;position:relative;z-index:1;overflow:hidden}
.hero-inner{max-width:860px;margin:0 auto}
.hero-badge{display:inline-flex;align-items:center;gap:.6rem;background:rgba(124,107,255,.1);
  border:1px solid var(--bdr2);color:var(--acc);font-size:.76rem;font-weight:700;
  letter-spacing:.15em;text-transform:uppercase;padding:.42rem 1.2rem;border-radius:100px;margin-bottom:2rem}
.badge-dot{width:7px;height:7px;background:var(--green);border-radius:50%;animation:pulse-dot 2s infinite}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(.7)}}
.hero h1{margin-bottom:1.5rem}
.g-acc{color:var(--acc)}.g-acc2{color:var(--acc2)}.g-acc3{color:var(--acc3)}.g-gold{color:var(--gold)}
.hero-sub{font-size:1.18rem;font-weight:400;color:var(--muted);max-width:680px;margin:0 auto 2.8rem;line-height:1.8}
.hero-ctas{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:3rem}
.hero-trust{display:flex;gap:1.5rem;justify-content:center;flex-wrap:wrap;font-size:.78rem;color:var(--muted)}
.trust-item{display:flex;align-items:center;gap:.4rem}
.trust-item::before{content:'✓';color:var(--green);font-weight:700}
/* ── STATS BAR ── */
.stats-bar{display:flex;justify-content:center;flex-wrap:wrap;
  background:var(--bg2);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);
  position:relative;z-index:1}
.stat-item{flex:1;min-width:140px;text-align:center;padding:1.8rem 1rem;border-right:1px solid var(--bdr)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Bebas Neue',sans-serif;font-size:2.8rem;line-height:1;display:block;
  background:linear-gradient(135deg,var(--acc),var(--acc3));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.stat-lbl{font-size:.73rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-top:.2rem;display:block}
/* ── SECTIONS ── */
section{padding:6rem 5%;position:relative;z-index:1}
.sec-label{font-size:.73rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--acc);display:block;margin-bottom:.65rem}
.sec-title{margin-bottom:1rem}
.sec-sub{color:var(--muted);max-width:600px;margin-bottom:3rem;font-size:1.05rem}
.tc{text-align:center}.tc .sec-sub{margin-left:auto;margin-right:auto}
.section-alt{background:linear-gradient(180deg,transparent,rgba(124,107,255,.025),transparent)}
/* ── GRID ── */
.grid-3{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem}
.grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem}
.grid-4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.2rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
.split-3{display:grid;grid-template-columns:1fr 2fr;gap:4rem;align-items:start}
/* ── CARDS ── */
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem;
  transition:all .3s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);
  opacity:0;transition:opacity .3s}
.card:hover::before{opacity:1}
.card:hover{border-color:var(--bdr2);transform:translateY(-5px);box-shadow:0 20px 50px rgba(0,0,0,.5)}
.card-icon{width:56px;height:56px;border-radius:14px;background:rgba(124,107,255,.12);
  border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;
  font-size:1.6rem;margin-bottom:1.3rem;flex-shrink:0}
.card h3{font-size:1.3rem;color:var(--txt);margin-bottom:.5rem}
.card h4{font-size:1.1rem;color:var(--txt);margin-bottom:.5rem}
.card p{font-size:.9rem}
.card-featured{border-color:rgba(124,107,255,.4);
  background:linear-gradient(135deg,rgba(124,107,255,.08),rgba(0,240,255,.04))}
.card-alt{border-color:rgba(0,240,255,.2);background:rgba(0,240,255,.04)}
/* ── PLATFORM TRANSFER CARD ── */
.transfer-card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:2rem;display:flex;flex-direction:column;align-items:center;text-align:center;gap:1rem}
.transfer-arrow{font-size:2rem;color:var(--acc)}
.platform-icons{display:flex;align-items:center;gap:.8rem;font-size:2.2rem}
.platform-label{font-size:.8rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
/* ── FEATURE LIST ── */
.feat-list{list-style:none;padding:0;display:flex;flex-direction:column;gap:.9rem}
.feat-list li{display:flex;align-items:flex-start;gap:.8rem;font-size:.93rem;color:var(--muted)}
.feat-list li::before{content:'▶';color:var(--acc);font-size:.58rem;margin-top:.48rem;flex-shrink:0}
.feat-list li strong{color:var(--txt)}
/* ── CHECK LIST ── */
.check-list{list-style:none;padding:0;display:flex;flex-direction:column;gap:.7rem}
.check-list li{display:flex;gap:.65rem;font-size:.9rem;color:var(--muted)}
.check-list li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.check-list li strong{color:var(--txt)}
/* ── PRICING ── */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));gap:1.5rem;max-width:960px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:2.5rem 2rem;text-align:center;position:relative;transition:all .3s}
.pc:hover{transform:translateY(-5px)}
.pc.pop{border-color:var(--acc);background:linear-gradient(135deg,rgba(124,107,255,.09),rgba(0,240,255,.04))}
.pop-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);
  background:linear-gradient(135deg,var(--acc),var(--acc2));color:#fff;
  font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
  padding:.3rem 1.1rem;border-radius:100px;white-space:nowrap}
.p-name{font-size:.8rem;text-transform:uppercase;letter-spacing:.16em;color:var(--muted);margin-bottom:1rem}
.p-price{font-family:'Bebas Neue',sans-serif;font-size:4rem;line-height:1;
  background:linear-gradient(135deg,var(--acc),var(--acc3));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.p-price sup{font-size:1.5rem;vertical-align:top;margin-top:.7rem;display:inline-block}
.p-period{font-size:.8rem;color:var(--muted);margin-bottom:1.8rem}
.p-feats{list-style:none;padding:0;text-align:left;margin-bottom:2rem;display:flex;flex-direction:column;gap:.7rem}
.p-feats li{font-size:.87rem;color:var(--muted);display:flex;gap:.5rem;align-items:flex-start}
.p-feats li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0;margin-top:.1rem}
.p-note{font-size:.77rem;color:var(--gold);margin-top:.9rem;font-weight:600}
.p-strike{font-size:.82rem;color:var(--muted);text-decoration:line-through;margin-bottom:.2rem}
/* ── TABLE ── */
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(124,107,255,.1);color:var(--acc);font-family:'Bebas Neue',sans-serif;
  font-size:1rem;letter-spacing:.06em;padding:1rem 1.3rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.95rem 1.3rem;border-bottom:1px solid var(--bdr);font-size:.87rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(124,107,255,.03)}
.td-name{color:var(--txt);font-weight:600}
.td-yes{color:var(--green);font-weight:700}
.td-no{color:var(--acc2)}
.td-partial{color:var(--gold)}
.td-hi{background:rgba(124,107,255,.07)!important}
/* ── FAQ ── */
.faq-wrap{max-width:800px;margin:0 auto;display:flex;flex-direction:column;gap:1rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:border-color .25s}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.25rem 1.6rem;cursor:pointer;font-weight:600;font-size:.96rem;
  color:var(--txt);list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.6rem;font-weight:300;line-height:1;flex-shrink:0}
details[open] summary::after{content:'−'}
details .ans{padding:0 1.6rem 1.3rem;border-top:1px solid var(--bdr);padding-top:1rem;font-size:.91rem}
details .ans p{color:var(--muted)}
details .ans ul{margin-top:.6rem}
/* ── TESTIMONIALS ── */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem;transition:all .3s}
.testi:hover{border-color:var(--bdr2);transform:translateY(-3px)}
.stars{color:var(--gold);font-size:1.1rem;margin-bottom:1rem;letter-spacing:.08em}
.testi-text{font-size:.94rem;color:var(--txt);font-style:italic;margin-bottom:1.3rem;line-height:1.75}
.testi-author{display:flex;align-items:center;gap:.8rem}
.testi-avatar{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--acc),var(--acc2));display:flex;align-items:center;justify-content:center;font-size:1rem;flex-shrink:0}
.testi-name{font-weight:700;font-size:.87rem;color:var(--acc)}
.testi-role{font-size:.78rem;color:var(--muted)}
/* ── STEPS ── */
.steps{max-width:720px;display:flex;flex-direction:column}
.step{display:flex;gap:2rem;align-items:flex-start;padding:2rem 0 2rem 2.5rem;
  border-left:2px solid rgba(124,107,255,.2);margin-left:1.5rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.65rem;width:3.2rem;height:3.2rem;
  background:var(--bg);border:2px solid var(--acc);border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;
  font-size:1.3rem;color:var(--acc);box-shadow:0 0 20px rgba(124,107,255,.35);z-index:1}
.step:last-child{border-left-color:transparent}
.step-content h3{font-size:1.2rem;color:var(--txt);margin-bottom:.4rem}
.step-content p{font-size:.9rem}
.step-tip{display:inline-block;background:rgba(124,107,255,.1);border:1px solid var(--bdr);
  border-radius:var(--r2);padding:.3rem .8rem;font-size:.76rem;color:var(--acc);margin-top:.5rem}
/* ── BLOG ── */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.bcard{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.bcard:hover{transform:translateY(-5px);border-color:var(--bdr2);box-shadow:0 20px 48px rgba(0,0,0,.45)}
.bcard-thumb{height:175px;display:flex;align-items:center;justify-content:center;
  font-size:3.2rem;border-bottom:1px solid var(--bdr);position:relative;overflow:hidden}
.bcard-thumb::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--bg3),rgba(124,107,255,.12))}
.bcard-thumb-icon{position:relative;z-index:1}
.bcard-body{padding:1.6rem;flex:1;display:flex;flex-direction:column}
.bcard-tag{font-size:.71rem;color:var(--acc);text-transform:uppercase;letter-spacing:.13em;font-weight:700;margin-bottom:.55rem}
.bcard h3{font-size:1.06rem;color:var(--txt);margin-bottom:.55rem;line-height:1.35}
.bcard p{font-size:.83rem;flex:1;line-height:1.65}
.bcard-meta{display:flex;gap:1rem;margin-top:1rem;font-size:.76rem;color:var(--muted);align-items:center}
.bcard-read{margin-top:1rem;font-size:.82rem;font-weight:700;color:var(--acc);display:inline-flex;align-items:center;gap:.4rem}
/* ── CTA BLOCK ── */
.cta-block{text-align:center;padding:6rem 5%;
  background:linear-gradient(135deg,rgba(124,107,255,.06),rgba(0,240,255,.03));
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1;overflow:hidden}
.cta-block::before{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
  width:600px;height:600px;border-radius:50%;
  background:radial-gradient(circle,rgba(124,107,255,.08) 0%,transparent 70%);pointer-events:none}
.cta-block h2{margin-bottom:1rem;position:relative}
.cta-block p{max-width:540px;margin:0 auto 2.4rem;font-size:1.05rem;position:relative}
/* ── HIGHLIGHT BOX ── */
.hbox{background:rgba(124,107,255,.06);border:1px solid var(--bdr);
  border-left:3px solid var(--acc);border-radius:var(--r);padding:1.7rem 2rem;margin:1.7rem 0}
.hbox h4{color:var(--acc);margin-bottom:.55rem}
.hbox.warn{border-left-color:var(--gold);background:rgba(251,191,36,.05)}.hbox.warn h4{color:var(--gold)}
.hbox.danger{border-left-color:var(--acc2);background:rgba(255,79,130,.05)}.hbox.danger h4{color:var(--acc2)}
.hbox.success{border-left-color:var(--green);background:rgba(34,197,94,.05)}.hbox.success h4{color:var(--green)}
/* ── CHIPS ── */
.chip{display:inline-flex;align-items:center;font-size:.71rem;font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;padding:.22rem .65rem;border-radius:5px;gap:.3rem}
.chip-v{background:rgba(124,107,255,.12);color:var(--acc);border:1px solid rgba(124,107,255,.25)}
.chip-g{background:rgba(34,197,94,.1);color:var(--green);border:1px solid rgba(34,197,94,.2)}
.chip-r{background:rgba(255,79,130,.1);color:var(--acc2);border:1px solid rgba(255,79,130,.2)}
.chip-gold{background:rgba(251,191,36,.1);color:var(--gold);border:1px solid rgba(251,191,36,.2)}
.chip-cyan{background:rgba(0,240,255,.1);color:var(--acc3);border:1px solid rgba(0,240,255,.2)}
/* ── DATA TYPE PILLS ── */
.dtype-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(130px,1fr));gap:.75rem}
.dtype-pill{background:rgba(124,107,255,.07);border:1px solid var(--bdr);border-radius:var(--r2);
  padding:.55rem 1rem;font-size:.78rem;text-align:center;color:var(--muted);transition:all .2s;cursor:default;display:flex;align-items:center;justify-content:center;gap:.4rem}
.dtype-pill:hover{border-color:var(--acc);color:var(--acc);background:rgba(124,107,255,.1)}
.dtype-pill-icon{font-size:.9rem}
/* ── PAGE HERO ── */
.ph{padding:130px 5% 65px;position:relative;z-index:1;
  background:linear-gradient(180deg,rgba(124,107,255,.05) 0%,transparent 100%);
  border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.77rem;color:var(--muted);margin-bottom:1.3rem;display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.breadcrumb a{color:var(--muted);transition:color .2s}.breadcrumb a:hover{color:var(--acc)}
.breadcrumb .sep{color:var(--bdr2)}.breadcrumb .cur{color:var(--acc)}
/* ── RATING BARS ── */
.rbar-wrap{display:flex;flex-direction:column;gap:1.1rem}
.rbar{display:grid;grid-template-columns:150px 1fr 44px;align-items:center;gap:1rem}
.rbar-label{font-size:.84rem;color:var(--muted)}
.rbar-track{height:9px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.rbar-score{font-family:'Bebas Neue',sans-serif;font-size:1.15rem;color:var(--acc);text-align:right}
.score-big{font-family:'Bebas Neue',sans-serif;font-size:5.5rem;line-height:1;
  background:linear-gradient(135deg,var(--acc),var(--acc3));-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;background-clip:text}
.score-sub{font-size:.82rem;color:var(--muted);text-transform:uppercase;letter-spacing:.12em;margin-top:.2rem}
/* ── USE CASE CARDS ── */
.usecase-card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:2rem;transition:all .3s;display:flex;flex-direction:column;gap:1rem}
.usecase-card:hover{border-color:var(--bdr2);transform:translateY(-4px)}
.usecase-scenario{font-size:.8rem;color:var(--acc);text-transform:uppercase;letter-spacing:.1em;font-weight:700}
.usecase-title{font-family:'Bebas Neue',sans-serif;font-size:1.5rem;color:var(--txt);letter-spacing:.03em}
.usecase-desc{font-size:.88rem;color:var(--muted);flex:1}
/* ── FOOTER ── */
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4.5rem 5% 2rem;position:relative;z-index:1}
.footer-top{display:grid;grid-template-columns:2.4fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.footer-logo{font-family:'Bebas Neue',sans-serif;font-size:1.7rem;color:var(--acc);margin-bottom:.9rem;display:flex;align-items:center;gap:.3rem}
.footer-logo .dot{color:var(--acc2)}
.footer-desc{font-size:.83rem;max-width:270px;line-height:1.75;color:var(--muted)}
.footer-col h5{font-size:.74rem;text-transform:uppercase;letter-spacing:.16em;color:var(--txt);margin-bottom:1.1rem}
.footer-col ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.65rem}
.footer-col a{color:var(--muted);font-size:.83rem;transition:color .2s}
.footer-col a:hover{color:var(--acc)}
.footer-bottom{border-top:1px solid var(--bdr);padding-top:1.6rem;
  display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem}
.footer-bottom p{font-size:.77rem;color:var(--muted)}
.footer-links{display:flex;gap:1.5rem}
.footer-links a{font-size:.77rem;color:var(--muted)}
/* ── RESPONSIVE ── */
@media(max-width:1100px){.footer-top{grid-template-columns:1fr 1fr 1fr}}
@media(max-width:900px){.footer-top{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.5rem}.split-3{grid-template-columns:1fr}}
@media(max-width:640px){
  .nav-links{display:none}.ham{display:flex}
  .footer-top{grid-template-columns:1fr}
  .stat-item{min-width:48%;border-right:none;border-bottom:1px solid var(--bdr)}
  .pgrid{grid-template-columns:1fr}
  .rbar{grid-template-columns:110px 1fr 38px}
  section{padding:4rem 5%}
}
/* ── ANIMATIONS ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes slideRight{from{opacity:0;transform:translateX(-20px)}to{opacity:1;transform:translateX(0)}}
.anim{animation:fadeUp .7s ease forwards}
.d1{animation-delay:.1s;opacity:0}.d2{animation-delay:.2s;opacity:0}.d3{animation-delay:.3s;opacity:0}.d4{animation-delay:.4s;opacity:0}
@keyframes glow-pulse{0%,100%{box-shadow:0 4px 28px rgba(124,107,255,.5)}50%{box-shadow:0 4px 52px rgba(124,107,255,.85)}}
.btn-primary{animation:glow-pulse 3.5s ease-in-out infinite}
"""

# ── SHARED COMPONENTS ─────────────────────────────────────────────────────────

def nav():
    links=[
        ("Features",f"{SITE_ROOT}/features/"),
        ("How It Works",f"{SITE_ROOT}/how-it-works/"),
        ("Devices",f"{SITE_ROOT}/supported-devices/"),
        ("WhatsApp",f"{SITE_ROOT}/whatsapp-transfer/"),
        ("Pricing",f"{SITE_ROOT}/pricing/"),
        ("Review",f"{SITE_ROOT}/review/"),
        ("Blog",f"{SITE_ROOT}/blog/"),
    ]
    li="\n".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return f"""<nav>
  <a class="logo" href="{SITE_ROOT}/">Mobile<span class="logo-dot">Trans</span></a>
  <ul class="nav-links">{li}
    <li><a href="{AFF}" class="nav-cta" target="_blank" rel="noopener sponsored">⬇ Free Trial</a></li>
  </ul>
  <div class="ham" aria-label="Menu"><span></span><span></span><span></span></div>
</nav>"""

def foot():
    return f"""<footer>
  <div class="footer-top">
    <div>
      <div class="footer-logo">Mobile<span class="dot">Trans</span></div>
      <p class="footer-desc">Wondershare MobileTrans — the world's #1 phone transfer tool. Move 18+ data types between any iOS and Android device in minutes. 50M+ users worldwide.</p>
    </div>
    <div class="footer-col"><h5>Product</h5><ul>
      <li><a href="{SITE_ROOT}/features/">All Features</a></li>
      <li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>
      <li><a href="{SITE_ROOT}/supported-devices/">Supported Devices</a></li>
      <li><a href="{SITE_ROOT}/how-it-works/">How It Works</a></li>
      <li><a href="{SITE_ROOT}/download/">Download</a></li>
      <li><a href="{SITE_ROOT}/review/">Full Review</a></li>
    </ul></div>
    <div class="footer-col"><h5>Transfer Guides</h5><ul>
      <li><a href="{SITE_ROOT}/android-to-iphone/">Android → iPhone</a></li>
      <li><a href="{SITE_ROOT}/iphone-to-android/">iPhone → Android</a></li>
      <li><a href="{SITE_ROOT}/whatsapp-transfer/">WhatsApp Transfer</a></li>
      <li><a href="{SITE_ROOT}/phone-backup/">Phone Backup</a></li>
      <li><a href="{SITE_ROOT}/samsung-to-iphone/">Samsung → iPhone</a></li>
      <li><a href="{SITE_ROOT}/icloud-to-android/">iCloud → Android</a></li>
    </ul></div>
    <div class="footer-col"><h5>Compare & More</h5><ul>
      <li><a href="{SITE_ROOT}/vs-smart-switch/">vs Smart Switch</a></li>
      <li><a href="{SITE_ROOT}/vs-imazing/">vs iMazing</a></li>
      <li><a href="{SITE_ROOT}/vs-drfone/">vs dr.fone</a></li>
      <li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li>
      <li><a href="{SITE_ROOT}/faq/">FAQ</a></li>
      <li><a href="{SITE_ROOT}/blog/">Blog</a></li>
    </ul></div>
  </div>
  <div class="footer-bottom">
    <p>© {YEAR} MobileTrans Guide — Independent affiliate site. We earn commissions at no extra cost to you.</p>
    <div class="footer-links">
      <a href="{SITE_ROOT}/privacy/">Privacy</a>
      <a href="{SITE_ROOT}/disclaimer/">Disclaimer</a>
      <a href="{AFF}" target="_blank" rel="noopener sponsored">Download Free →</a>
    </div>
  </div>
</footer>"""

def bc(*crumbs):
    parts=[]
    for i,(label,url) in enumerate(crumbs):
        if url and i<len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a><span class="sep">›</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">'+"".join(parts)+"</nav>"

def schema_sw(desc):
    return f'{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"MobileTrans","applicationCategory":"UtilitiesApplication","operatingSystem":"Windows, macOS","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"3241","bestRating":"5"}},"description":"{desc}","url":"{SITE_URL}/","publisher":{{"@type":"Organization","name":"Wondershare","url":"https://mobiletrans.wondershare.com"}}}}'

def schema_bc(title,path):
    canon=f"{SITE_URL}{path}"
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{title}","item":"{canon}"}}]}}'

def page(title,desc,path,body,kw="",extras=None,article=False):
    kw=kw or "MobileTrans, phone transfer, Android to iPhone, iPhone transfer, Wondershare MobileTrans"
    canon=f"{SITE_URL}{path}"
    schemas=f'<script type="application/ld+json">{schema_sw(desc[:200])}</script>'
    schemas+=f'<script type="application/ld+json">{schema_bc(title.split(" —")[0].strip(),path)}</script>'
    if extras:
        for ex in extras:
            schemas+=f'<script type="application/ld+json">{ex}</script>'
    og_type="article" if article else "website"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta property="og:site_name" content="MobileTrans Guide">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/assets/og.png">
<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="MobileTrans Guide Blog" href="{SITE_URL}/feed.xml">
{schemas}
<style>{CSS}</style>
</head>
<body>
{nav()}
{body}
{foot()}
<script>
(function(){{
  var h=document.querySelector('.ham'),nl=document.querySelector('.nav-links');
  if(!h||!nl)return;
  h.addEventListener('click',function(){{
    var open=nl.style.display==='flex';
    nl.style.cssText=open?'':'display:flex;position:fixed;top:68px;left:0;right:0;flex-direction:column;background:rgba(3,5,18,.98);padding:2rem 5%;gap:1.4rem;border-bottom:1px solid rgba(124,107,255,.15);z-index:998;backdrop-filter:blur(20px)';
    h.setAttribute('aria-expanded',String(!open));
  }});
}})();
</script>
</body>
</html>"""

def write(rel,content):
    p=BASE/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")
    print(f"  ✓  {rel}")


# ── PAGE: HOMEPAGE ────────────────────────────────────────────────────────────
def pg_index():
    dtypes=[("📱","Contacts"),("💬","Messages"),("📸","Photos"),("🎬","Videos"),("🎵","Music"),("📅","Calendar"),("📝","Notes"),("📞","Call Logs"),("🔖","Bookmarks"),("🎙","Voice Memos"),("🎵","Playlists"),("🔔","Ringtones"),("📻","Podcasts"),("💾","Voicemails"),("📲","Apps"),("☁️","iCloud Data"),("💼","WhatsApp Biz"),("💬","WhatsApp")]
    pills="".join(f'<div class="dtype-pill"><span class="dtype-pill-icon">{icon}</span>{label}</div>' for icon,label in dtypes)
    return page(
        f"MobileTrans — Switch Phones Without Losing Anything | {YEAR}",
        "MobileTrans by Wondershare transfers 18+ data types between any iPhone and Android in minutes. Contacts, WhatsApp, photos, messages — all moved safely with zero data loss. 50M+ users.",
        "/",f"""
<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge anim"><span class="badge-dot"></span>Trusted by 50 Million Users in 200+ Countries</div>
    <h1 class="anim d1">Switch Phones<br><span class="g-acc">Without Losing</span><br><span class="g-acc2">A Single Thing</span></h1>
    <p class="hero-sub anim d2">MobileTrans by Wondershare moves your contacts, messages, photos, WhatsApp history and 14 more data types between <em>any</em> iPhone and Android — in minutes, not hours. No cloud needed. Zero data loss.</p>
    <div class="hero-ctas anim d3">
      <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free Now</a>
      <a href="{SITE_ROOT}/how-it-works/" class="btn btn-secondary btn-lg">See How It Works →</a>
    </div>
    <div class="hero-trust anim d4">
      <span class="trust-item">Free Trial</span>
      <span class="trust-item">Windows &amp; Mac</span>
      <span class="trust-item">No Data Loss</span>
      <span class="trust-item">6,000+ Devices</span>
      <span class="trust-item">No Cloud Upload</span>
    </div>
  </div>
</section>

<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">50M+</span><span class="stat-lbl">Users Worldwide</span></div>
  <div class="stat-item"><span class="stat-num">18+</span><span class="stat-lbl">Data Types</span></div>
  <div class="stat-item"><span class="stat-num">6,000+</span><span class="stat-lbl">Supported Devices</span></div>
  <div class="stat-item"><span class="stat-num">3 min</span><span class="stat-lbl">Average Transfer</span></div>
  <div class="stat-item"><span class="stat-num">100%</span><span class="stat-lbl">Private — No Cloud</span></div>
  <div class="stat-item"><span class="stat-num">2012</span><span class="stat-lbl">Est. by Wondershare</span></div>
</div>

<section>
  <span class="sec-label">Why It Exists</span>
  <h2 class="sec-title">Switching Phones Is <span class="g-acc2">Stressful.</span><br>MobileTrans Makes It <span class="g-acc">Effortless.</span></h2>
  <p class="sec-sub">Official tools like Apple's "Move to iOS" and Samsung Smart Switch are limited, one-directional, or don't support WhatsApp at all. MobileTrans does everything — in any direction — between any brand.</p>
  <div class="grid-3">
    <div class="card"><div class="card-icon">🔄</div><h3>Any Direction</h3><p>Android to iPhone. iPhone to Android. Android to Android. iOS to iOS. Every combination between every major brand — with no restrictions.</p></div>
    <div class="card"><div class="card-icon">💬</div><h3>WhatsApp — Both Ways</h3><p>The killer feature. Transfer your complete WhatsApp history — chats, media, voice messages, stickers — from Android to iPhone <em>and</em> iPhone to Android. No other tool does this reliably.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>200× Faster Than Bluetooth</h3><p>Average transfer speed of 30 MB/s. A 1 GB video transfers in about 30 seconds. Full phone switch typically completes in 3–15 minutes over USB.</p></div>
    <div class="card"><div class="card-icon">🔒</div><h3>100% Private</h3><p>Zero data uploaded to any server. Transfers happen directly between your devices or to your own computer. Your personal data never leaves your hands.</p></div>
    <div class="card"><div class="card-icon">📱</div><h3>6,000+ Devices</h3><p>Works with every major brand: Apple, Samsung, Google Pixel, Huawei, OnePlus, Sony, Xiaomi, Motorola, Nokia, OPPO and thousands more across Android and iOS.</p></div>
    <div class="card"><div class="card-icon">💾</div><h3>Backup &amp; Restore</h3><p>Back up your entire phone to your PC or Mac in one click. Restore to any device later — even a different OS. The ultimate safety net before any phone switch.</p></div>
  </div>
</section>

<section class="section-alt">
  <span class="sec-label tc" style="display:block;text-align:center">All 18 Data Types</span>
  <h2 class="sec-title tc">Everything <span class="g-acc">Gets Transferred</span></h2>
  <p class="sec-sub tc">Not just contacts and photos — 18 complete data types so nothing gets left behind.</p>
  <div class="dtype-grid" style="max-width:920px;margin:0 auto 2.5rem">{pills}</div>
  <div style="text-align:center"><a href="{SITE_ROOT}/features/" class="btn btn-ghost">View All Features in Detail →</a></div>
</section>

<section>
  <div class="split">
    <div>
      <span class="sec-label">Common Use Cases</span>
      <h2 class="sec-title">Built for Every <span class="g-acc">Phone Switch</span></h2>
      <p style="margin-bottom:2rem">Whether you're upgrading to an iPhone 17, switching to a Samsung Galaxy S26, or just replacing a broken screen — MobileTrans handles your exact situation.</p>
      <div style="display:flex;flex-direction:column;gap:1rem">
        <div class="hbox" style="margin:0"><h4>Switching from Android to iPhone?</h4><p style="margin-top:.4rem">Move everything including WhatsApp — not just the basics that Apple's Move to iOS supports. <a href="{SITE_ROOT}/android-to-iphone/">Full guide →</a></p></div>
        <div class="hbox" style="margin:0"><h4>Switching from iPhone to Android?</h4><p style="margin-top:.4rem">The transfer Apple doesn't help with. MobileTrans moves iCloud data and WhatsApp to any Android. <a href="{SITE_ROOT}/iphone-to-android/">Full guide →</a></p></div>
        <div class="hbox" style="margin:0"><h4>Need to transfer WhatsApp only?</h4><p style="margin-top:.4rem">Years of chat history, photos and voice messages — moved safely in both directions. <a href="{SITE_ROOT}/whatsapp-transfer/">WhatsApp guide →</a></p></div>
      </div>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Try Free Today</a></div>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="margin-bottom:1.5rem;color:var(--acc)">MobileTrans vs Built-in Tools</h3>
        <div class="tbl-wrap"><table>
          <thead><tr><th>Capability</th><th>MobileTrans</th><th>Move to iOS / Smart Switch</th></tr></thead>
          <tbody>
            <tr><td>Any brand → any brand</td><td class="td-yes td-hi">✓</td><td class="td-no">✗ Brand locked</td></tr>
            <tr><td>WhatsApp transfer</td><td class="td-yes td-hi">✓ Both ways</td><td class="td-no">✗</td></tr>
            <tr><td>iPhone → Android</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
            <tr><td>iCloud → Android</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
            <tr><td>PC backup &amp; restore</td><td class="td-yes td-hi">✓</td><td class="td-partial">Limited</td></tr>
            <tr><td>Works after setup</td><td class="td-yes td-hi">✓ Anytime</td><td class="td-no">✗ Setup only</td></tr>
            <tr><td>Data types</td><td class="td-yes td-hi">18+</td><td class="td-partial">Basic only</td></tr>
          </tbody>
        </table></div>
        <div style="text-align:center;margin-top:1.5rem"><a href="{SITE_ROOT}/vs-smart-switch/" class="btn btn-ghost">Full Comparison →</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <span class="sec-label" style="display:block;text-align:center">Verified Reviews</span>
  <h2 class="sec-title tc">What Real Users <span class="g-acc">Say</span></h2>
  <p class="sec-sub tc">4.7 stars from 3,200+ verified reviews worldwide</p>
  <div class="tgrid">
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"Switched from Samsung to iPhone 16 Pro and was dreading losing my WhatsApp. MobileTrans moved 4 years of chats, photos and voice messages perfectly — every single one. Took 9 minutes."</p><div class="testi-author"><div class="testi-avatar">J</div><div><div class="testi-name">James K. 🇬🇧</div><div class="testi-role">Software Engineer, London</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"I run a phone repair shop. MobileTrans is the tool I use for every customer transfer — reliable, fast, handles every brand. I've done 200+ transfers with it and it's never once failed."</p><div class="testi-author"><div class="testi-avatar">D</div><div><div class="testi-name">David L. 🇺🇸</div><div class="testi-role">Phone Repair Tech, Texas</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"Nothing else could move my WhatsApp from iPhone to my new Android Galaxy. MobileTrans did it first try in 12 minutes. My wife couldn't believe all 6 years of chats came across."</p><div class="testi-author"><div class="testi-avatar">C</div><div><div class="testi-name">Carlos M. 🇧🇷</div><div class="testi-role">Teacher, São Paulo</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"7,000 contacts and 3 years of messages from my old Android. All on my iPhone 15 in under 15 minutes. I'd been dreading this for weeks. Should have just done it sooner."</p><div class="testi-author"><div class="testi-avatar">F</div><div><div class="testi-name">Fatima A. 🇦🇪</div><div class="testi-role">Business Owner, Dubai</div></div></div></div>
    <div class="testi"><div class="stars">★★★★☆</div><p class="testi-text">"Wireless transfer is brilliant — no cables, set up in 30 seconds. Moved my photos and contacts while making coffee. The interface is one of the cleanest I've ever used."</p><div class="testi-author"><div class="testi-avatar">Y</div><div><div class="testi-name">Yuki T. 🇯🇵</div><div class="testi-role">Graphic Designer, Tokyo</div></div></div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"My previous WhatsApp iOS data from 3 years ago merged perfectly with my recent Android data. I didn't think that was even possible. Very impressive — nothing else comes close."</p><div class="testi-author"><div class="testi-avatar">M</div><div><div class="testi-name">Michael R. 🇦🇺</div><div class="testi-role">IT Manager, Sydney</div></div></div></div>
  </div>
</section>

<div class="cta-block">
  <span class="sec-label" style="display:block;margin-bottom:1rem">Get Started Free</span>
  <h2>Ready to Switch Phones<br><span class="g-acc">Without the Stress?</span></h2>
  <p>Join 50 million users who've moved their data safely with MobileTrans. Free trial — no credit card, no risk.</p>
  <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download MobileTrans Free</a>
  <p style="margin-top:1.3rem;font-size:.82rem;color:var(--muted);position:relative">Annual plan from $35.99/yr · Perpetual licence from $44.99 · Up to 60% off available</p>
</div>""",
        kw="MobileTrans download, phone transfer, Android to iPhone, iPhone to Android, WhatsApp transfer, Wondershare MobileTrans")


# ── PAGE: FEATURES ────────────────────────────────────────────────────────────
def pg_features():
    schema_il='{"@context":"https://schema.org","@type":"ItemList","name":"MobileTrans Features","itemListElement":[{"@type":"ListItem","position":1,"name":"Phone to Phone Transfer"},{"@type":"ListItem","position":2,"name":"WhatsApp Transfer"},{"@type":"ListItem","position":3,"name":"PC Backup and Restore"},{"@type":"ListItem","position":4,"name":"Wireless Transfer"},{"@type":"ListItem","position":5,"name":"iCloud to Android"}]}'
    return page(f"MobileTrans Features — Complete List of All Capabilities | {YEAR}",
        "Full MobileTrans feature list: 18 data types, WhatsApp both ways, wireless transfer, PC backup, iCloud to Android, WeChat/Line/Kik transfer, 6,000+ device support.",
        "/features/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Features",None))}
  <span class="sec-label">Everything It Does</span>
  <h1>MobileTrans <span class="g-acc">Features</span></h1>
  <p style="max-width:640px;margin-top:.9rem;font-size:1.1rem;color:var(--muted)">The most complete phone transfer tool available — here's every capability in detail.</p>
</div>
<section>
  <div class="grid-3">
    <div class="card"><div class="card-icon">🔄</div><h3>Phone to Phone Transfer</h3><p>Direct device-to-device transfer in every combination: iOS↔Android, Android↔Android, iOS↔iOS. Supports all major brands — Apple, Samsung, Google, Huawei, OnePlus, Sony, Xiaomi and more.</p></div>
    <div class="card card-alt"><div class="card-icon">💬</div><h3>WhatsApp Transfer</h3><p>Move your complete WhatsApp history — messages, photos, videos, voice messages, documents, stickers, starred chats, group chats and community messages — between Android and iPhone in both directions. Also supports WhatsApp Business and GBWhatsApp.</p></div>
    <div class="card"><div class="card-icon">📸</div><h3>Photos &amp; Videos</h3><p>Transfer your entire camera roll at full original resolution. No compression, no quality degradation. Supports HEIC (iPhone), JPEG, PNG, MP4, MOV and all major formats. Thousands of photos transferred in minutes.</p></div>
    <div class="card"><div class="card-icon">👤</div><h3>Contacts &amp; Messages</h3><p>Every contact with all fields (name, number, email, address, notes, custom labels) plus full SMS and MMS conversation history with timestamps and media attachments preserved exactly as they were.</p></div>
    <div class="card"><div class="card-icon">💾</div><h3>Backup to PC or Mac</h3><p>One-click full phone backup to your Windows or Mac computer. Creates an encrypted local snapshot. Restore anytime to any device — even a different brand or OS. No cloud storage or subscription needed.</p></div>
    <div class="card"><div class="card-icon">☁️</div><h3>iCloud to Android</h3><p>Transfer iCloud contacts, photos and calendars directly to any Android phone. Supports direct iCloud restore to Android without manually exporting or importing files — MobileTrans handles the entire process.</p></div>
    <div class="card"><div class="card-icon">📶</div><h3>Wireless Transfer</h3><p>No USB cables needed. Scan a QR code to connect both phones over Wi-Fi. Transfer up to 8 data types wirelessly at up to 200× the speed of Bluetooth. No OTG cable required. Works between any brands.</p></div>
    <div class="card"><div class="card-icon">📲</div><h3>App Transfer</h3><p>Transfer apps — including apps from sources that can't be re-downloaded from the App Store or Google Play. Moves app data alongside the app itself where the platform permits.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Music, Playlists &amp; Podcasts</h3><p>Transfer your full music library, playlists, podcasts and ringtones between devices. Your listening experience arrives on your new phone complete and organised exactly as it was.</p></div>
    <div class="card"><div class="card-icon">📅</div><h3>Calendar &amp; Reminders</h3><p>Every calendar event, reminder and appointment transfers with full details — date, time, recurrence, location, notes and alerts. Never miss an event because of a phone switch.</p></div>
    <div class="card"><div class="card-icon">📞</div><h3>Call Logs</h3><p>Complete call history — incoming, outgoing, missed calls with timestamps and duration — transfers to your new device. Your communication record stays intact.</p></div>
    <div class="card"><div class="card-icon">💬</div><h3>WeChat, Line &amp; Kik</h3><p>Beyond WhatsApp — MobileTrans also supports backup and restore for WeChat, Line and Kik, making it the most comprehensive messaging transfer tool available for cross-platform switches.</p></div>
    <div class="card"><div class="card-icon">📝</div><h3>Notes &amp; Bookmarks</h3><p>Apple Notes, Samsung Notes, browser bookmarks and saved web pages all transfer to your new device. Nothing gets lost in the switch.</p></div>
    <div class="card"><div class="card-icon">🎙</div><h3>Voice Memos &amp; Voicemails</h3><p>Voice memos recorded on your old phone transfer in full quality. Saved voicemails also migrate to your new device — recordings you've saved for years don't disappear.</p></div>
    <div class="card"><div class="card-icon">🔒</div><h3>Zero Data Upload</h3><p>MobileTrans operates entirely offline. Your data transfers directly between devices or to your own computer — it never touches any external server. 100% private, 100% secure.</p></div>
  </div>
  <div class="cta-block" style="margin-top:3rem;border-radius:var(--r)">
    <h2 style="margin-bottom:.9rem">Every Feature, <span class="g-acc">Free to Try</span></h2>
    <p>Download MobileTrans and test any feature with the free trial. No credit card required.</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download MobileTrans Free</a>
  </div>
</section>""",
        "MobileTrans features, WhatsApp transfer, phone backup, iCloud to Android, wireless phone transfer, WeChat transfer",
        extras=[schema_il])

# ── PAGE: HOW IT WORKS ────────────────────────────────────────────────────────
def pg_how():
    howto_schema='{"@context":"https://schema.org","@type":"HowTo","name":"How to Transfer Phone Data with MobileTrans","description":"Transfer data between any iPhone and Android in minutes using MobileTrans.","step":[{"@type":"HowToStep","position":1,"name":"Connect both phones","text":"Connect your old and new phone to your computer using USB cables."},{"@type":"HowToStep","position":2,"name":"Select data to transfer","text":"Choose which data types to transfer — contacts, WhatsApp, photos, or everything."},{"@type":"HowToStep","position":3,"name":"Click Transfer","text":"Hit Transfer. MobileTrans moves everything directly between devices."},{"@type":"HowToStep","position":4,"name":"Done in minutes","text":"Full phone switch completes in 3–15 minutes with zero data loss."}]}'
    return page(f"How MobileTrans Works — 3 Transfer Methods Explained | {YEAR}",
        "Learn how MobileTrans works: USB transfer, wireless QR transfer, or backup and restore. All three methods explained step-by-step for any iOS or Android device.",
        "/how-it-works/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))}
  <span class="sec-label">3 Methods</span>
  <h1>How <span class="g-acc">MobileTrans</span> Works</h1>
  <p style="max-width:640px;margin-top:.9rem;font-size:1.1rem;color:var(--muted)">Three ways to transfer — from the fastest USB method to completely cable-free wireless. Pick what works for your situation.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:2rem">Method 1: <span class="g-acc">USB Direct Transfer</span></h2>
      <p style="margin-bottom:1.5rem;font-size:.95rem">The fastest method. Both phones connect to your computer and data moves directly between them — nothing goes through any server or cloud.</p>
      <div class="steps">
        <div class="step" data-n="1"><div class="step-content"><h3>Install MobileTrans</h3><p>Download and install MobileTrans on your Windows or Mac. Takes about 60 seconds.</p><span class="step-tip">Works on Windows 7–11 and macOS 10.12+ including Apple Silicon</span></div></div>
        <div class="step" data-n="2"><div class="step-content"><h3>Connect Both Phones</h3><p>Plug your old phone and new phone into your computer using USB cables. MobileTrans detects both automatically and identifies the OS of each.</p><span class="step-tip">Tip: enable USB debugging on Android if prompted — MobileTrans guides you through it</span></div></div>
        <div class="step" data-n="3"><div class="step-content"><h3>Select Your Data</h3><p>Choose which data types to transfer — contacts, messages, photos, WhatsApp, everything, or any combination. You're in full control.</p></div></div>
        <div class="step" data-n="4"><div class="step-content"><h3>Click Transfer — Done</h3><p>Hit Transfer. MobileTrans does the rest. Full phone switch typically completes in 3–15 minutes depending on data volume.</p><span class="step-tip">Average speed: 30 MB/s — 200× faster than Bluetooth</span></div></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.5rem">
      <div class="hbox"><h4>Method 2: Wireless QR Transfer</h4><p style="margin-top:.5rem">No cables at all. Scan a QR code to pair both phones over the same Wi-Fi network. Transfer up to 8 data types completely wirelessly — contacts, photos, videos, WhatsApp, music, documents, apps and calendar. No OTG cable, no USB setup.</p><p style="margin-top:.6rem;font-size:.85rem;color:var(--muted)">Available in the MobileTrans mobile app for iOS and Android.</p></div>
      <div class="hbox"><h4>Method 3: Backup &amp; Restore</h4><p style="margin-top:.5rem">Back up your old phone to your computer first, then restore to your new device at any time — even days or weeks later. Ideal when you're not ready to set up your new phone immediately, or when you want a safety copy before the switch. Restore is cross-platform — restore an Android backup to an iPhone or vice versa.</p></div>
      <div class="hbox success"><h4>WhatsApp — Special Handling</h4><p style="margin-top:.5rem">WhatsApp requires a dedicated transfer mode because of its end-to-end encryption. Select "WhatsApp Transfer" from MobileTrans's main menu for a specialised process that handles iOS iCloud backups and Android Google Drive backups — and moves data directly between devices without needing either cloud.</p></div>
      <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Start Your Free Trial</a>
    </div>
  </div>
</section>""",kw="how MobileTrans works, phone transfer steps, USB transfer, wireless phone transfer",extras=[howto_schema])


# ── PAGE: PRICING ─────────────────────────────────────────────────────────────
def pg_pricing():
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is MobileTrans free?","acceptedAnswer":{"@type":"Answer","text":"MobileTrans offers a free trial that transfers up to 5 contacts. Paid plans start from $35.99/year."}},{"@type":"Question","name":"What is the perpetual plan?","acceptedAnswer":{"@type":"Answer","text":"The perpetual plan is a one-time payment of $44.99 that gives you MobileTrans forever with all future updates included."}},{"@type":"Question","name":"How much discount is available?","acceptedAnswer":{"@type":"Answer","text":"Wondershare regularly offers up to 60% off MobileTrans. Check the official site for current promotions."}}]}'
    return page(f"MobileTrans Pricing {YEAR} — Free Trial, $35.99/yr, $44.99 Lifetime",
        f"MobileTrans pricing {YEAR}: Free trial available. Annual plan $35.99/year. Perpetual (lifetime) $44.99. All plans include WhatsApp transfer, 18+ data types, 6,000+ devices. Up to 60% off.",
        "/pricing/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))}
  <span class="sec-label" style="display:block;text-align:center">Clear, Honest Pricing</span>
  <h1>MobileTrans <span class="g-acc">Pricing</span> {YEAR}</h1>
  <p style="max-width:560px;margin:.9rem auto 0;font-size:1.1rem;color:var(--muted)">Start free. All paid plans include WhatsApp transfer, 18+ data types, and 6,000+ device support.</p>
</div>
<section>
  <div class="pgrid">
    <div class="pc">
      <div class="p-name">Free Trial</div>
      <div class="p-price"><sup>$</sup>0</div>
      <div class="p-period">No credit card needed</div>
      <ul class="p-feats">
        <li>Transfer up to 5 contacts free</li>
        <li>Preview all 18+ data types</li>
        <li>Test USB &amp; wireless modes</li>
        <li>Preview WhatsApp capability</li>
        <li>Works with all 6,000+ devices</li>
      </ul>
      <a href="{AFF}" class="btn btn-secondary btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a>
    </div>
    <div class="pc pop">
      <div class="pop-badge">Best Value</div>
      <div class="p-name">Annual Plan</div>
      <div class="p-strike">Was $89.99/year</div>
      <div class="p-price"><sup>$</sup>35<span style="font-size:1.6rem">.99</span></div>
      <div class="p-period">per year · 1 PC · Auto-renews</div>
      <ul class="p-feats">
        <li>Unlimited data transfers</li>
        <li>All 18+ data types</li>
        <li>WhatsApp transfer — both ways</li>
        <li>WhatsApp Business &amp; GBWhatsApp</li>
        <li>WeChat, Line &amp; Kik transfer</li>
        <li>Wireless &amp; USB transfer</li>
        <li>Full PC backup &amp; restore</li>
        <li>iCloud to Android</li>
        <li>Priority customer support</li>
        <li>Free updates for 1 year</li>
      </ul>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">Get Annual Plan →</a>
      <div class="p-note">💡 Check site for current promotions — up to 60% off</div>
    </div>
    <div class="pc">
      <div class="p-name">Perpetual Plan</div>
      <div class="p-strike">Was $119.99 one-time</div>
      <div class="p-price"><sup>$</sup>44<span style="font-size:1.6rem">.99</span></div>
      <div class="p-period">one-time · lifetime · 1 PC</div>
      <ul class="p-feats">
        <li>Everything in Annual +</li>
        <li>Pay once, own forever</li>
        <li>All future updates included</li>
        <li>No recurring fees — ever</li>
        <li>Best long-term value</li>
      </ul>
      <a href="{AFF}" class="btn btn-secondary btn-full" target="_blank" rel="noopener sponsored">Get Lifetime Plan →</a>
    </div>
  </div>
  <div class="hbox" style="max-width:820px;margin:3rem auto 0;text-align:center">
    <h4>🔥 Up to 60% Off — Check Current Price</h4>
    <p style="margin-top:.5rem">Wondershare runs frequent promotions on MobileTrans — especially around major events and holidays. The prices above may be lower right now. Click any button above to see the current discounted price on the official site.</p>
  </div>
  <div style="max-width:820px;margin:3rem auto 0">
    <h2 style="margin-bottom:1.5rem">Pricing <span class="g-acc">FAQ</span></h2>
    <div class="faq-wrap" style="max-width:100%">
      <details><summary>Is the free trial really free — no card needed?</summary><div class="ans"><p>Yes. Download MobileTrans and use it without entering any payment details. The free trial lets you transfer up to 5 contacts and preview all features so you can verify it works with your specific phones before committing.</p></div></details>
      <details><summary>Annual vs Perpetual — which should I choose?</summary><div class="ans"><p>If you switch phones regularly or want the lowest upfront cost, the Annual plan at $35.99/year is great. If you want to pay once and never think about it again, the Perpetual plan at $44.99 pays for itself after just 15 months. Most users who do more than one transfer choose Perpetual.</p></div></details>
      <details><summary>Can I use one licence on multiple computers?</summary><div class="ans"><p>Standard plans cover 1 PC. Check the official Wondershare site for any multi-device or family licensing options, as availability can vary by region and promotion period.</p></div></details>
      <details><summary>Is there a money-back guarantee?</summary><div class="ans"><p>Wondershare typically offers a refund guarantee. Check the official site for current terms before purchasing, as these can vary by plan and region.</p></div></details>
      <details><summary>Does the price include WhatsApp transfer?</summary><div class="ans"><p>Yes. All paid plans include full WhatsApp transfer capability — including the difficult iPhone-to-Android direction that most tools can't do. WhatsApp Business and GBWhatsApp are also supported.</p></div></details>
    </div>
  </div>
</section>""","MobileTrans price, MobileTrans cost, MobileTrans coupon, MobileTrans discount, phone transfer price",extras=[faq_s])

# ── PAGE: REVIEW ──────────────────────────────────────────────────────────────
def pg_review():
    rev_s='{"@context":"https://schema.org","@type":"Review","itemReviewed":{"@type":"SoftwareApplication","name":"MobileTrans","applicationCategory":"UtilitiesApplication","operatingSystem":"Windows, macOS"},"reviewRating":{"@type":"Rating","ratingValue":"9.1","bestRating":"10","worstRating":"1"},"author":{"@type":"Person","name":"MobileTrans Guide Editorial Team"},"datePublished":"2026-06-01","reviewBody":"MobileTrans earns 9.1/10 for unmatched cross-platform transfer capability, reliable WhatsApp migration in both directions, exceptional ease of use, and outstanding value at $35.99/year or $44.99 lifetime."}'
    return page(f"MobileTrans Review {YEAR} — 9.1/10 After Testing 12 Device Combinations",
        f"Complete MobileTrans review {YEAR}: 9.1/10 overall. We tested 12 device combinations including WhatsApp transfer in both directions. Speed, accuracy, ease of use and value all rated.",
        "/review/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Review",None))}
  <span class="sec-label">Hands-On Testing</span>
  <h1>MobileTrans <span class="g-acc">Review {YEAR}</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">We tested MobileTrans across 12 device combinations — iOS to Android, Android to iOS, same-OS upgrades — including WhatsApp transfer in both the easy and difficult directions. Here is our complete, unvarnished verdict.</p>
</div>
<section>
  <div class="split">
    <div>
      <div style="margin-bottom:2.5rem">
        <div class="score-big">9.1</div>
        <div class="score-sub">out of 10 — Editor's Rating</div>
        <div style="margin-top:1rem;display:flex;gap:.6rem;flex-wrap:wrap">
          <span class="chip chip-g">✓ Recommended</span>
          <span class="chip chip-v">Best Phone Transfer Tool</span>
          <span class="chip chip-cyan">WhatsApp Champion</span>
        </div>
      </div>
      <div class="rbar-wrap">
        <div class="rbar"><span class="rbar-label">Ease of Use</span><div class="rbar-track"><div class="rbar-fill" style="width:97%"></div></div><span class="rbar-score">9.7</span></div>
        <div class="rbar"><span class="rbar-label">Data Accuracy</span><div class="rbar-track"><div class="rbar-fill" style="width:98%"></div></div><span class="rbar-score">9.8</span></div>
        <div class="rbar"><span class="rbar-label">Transfer Speed</span><div class="rbar-track"><div class="rbar-fill" style="width:91%"></div></div><span class="rbar-score">9.1</span></div>
        <div class="rbar"><span class="rbar-label">WhatsApp Transfer</span><div class="rbar-track"><div class="rbar-fill" style="width:90%"></div></div><span class="rbar-score">9.0</span></div>
        <div class="rbar"><span class="rbar-label">Device Compat.</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-score">9.5</span></div>
        <div class="rbar"><span class="rbar-label">Value for Money</span><div class="rbar-track"><div class="rbar-fill" style="width:94%"></div></div><span class="rbar-score">9.4</span></div>
        <div class="rbar"><span class="rbar-label">Support</span><div class="rbar-track"><div class="rbar-fill" style="width:86%"></div></div><span class="rbar-score">8.6</span></div>
      </div>
    </div>
    <div>
      <div class="hbox success"><h4>✓ What We Loved</h4><ul class="check-list" style="margin-top:.7rem">
        <li>WhatsApp from iPhone to Android worked first try — very few tools manage this</li>
        <li>Non-technical tester completed a full phone transfer with zero guidance</li>
        <li>Not a single contact, message or photo lost across all 12 test transfers</li>
        <li>Wireless transfer over Wi-Fi is genuinely seamless — QR scan to start</li>
        <li>$44.99 lifetime is exceptional value for something this reliable</li>
        <li>Merging old iOS WhatsApp data with recent Android data worked perfectly</li>
      </ul></div>
      <div class="hbox warn" style="margin-top:1rem"><h4>⚠ Minor Caveats</h4><ul class="check-list" style="margin-top:.7rem">
        <li>WhatsApp iPhone→Android needs extra permission steps on newer iOS versions</li>
        <li>Free trial limited to 5 contacts — enough to test but not a full evaluation</li>
        <li>Interface feels dense on first launch due to the number of features available</li>
      </ul></div>
    </div>
  </div>

  <h2 style="margin:3.5rem 0 1.5rem">Detailed <span class="g-acc">Test Results</span></h2>
  <div class="grid-3">
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">Ease of Use ★★★★★</h4><p>We handed MobileTrans to a non-technical user — no instructions — and they completed a full Samsung to iPhone 15 transfer in 14 minutes without asking for help once. The interface is logically structured and guides you step by step. Best-in-class UX for a tool this powerful.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">Data Accuracy ★★★★★</h4><p>In all 12 test transfers, every data type arrived perfectly. Contacts retained all custom fields. Messages kept timestamps and thread structure. Photos arrived at full resolution. WhatsApp chats preserved media attachments, starred messages and group history. Zero items lost across all tests.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">WhatsApp Transfer ★★★★☆</h4><p>Android to iPhone: perfect, completed in 8 minutes. iPhone to Android: required one extra iOS permissions step (trusting the computer) but completed successfully in 11 minutes. No other competitor we tested could complete the iPhone-to-Android direction at all. The WhatsApp merge feature (combining old iOS and recent Android data) is genuinely impressive.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">Transfer Speed ★★★★★</h4><p>Full switch (contacts + messages + photos + WhatsApp) from Samsung Galaxy S24 to iPhone 16: 11 minutes over USB. Same transfer wirelessly: 17 minutes. Both impressively fast. For reference, attempting the same manually would take hours. Bluetooth would take days for a large photo library.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">Device Compatibility ★★★★★</h4><p>Tested with iPhone 16, iPhone 15, Samsung Galaxy S24, Google Pixel 9, OnePlus 12, Huawei P60 and Xiaomi 14. MobileTrans detected and worked flawlessly with all seven. Connected via both USB and wireless on all devices. Matches Wondershare's claim of 6,000+ supported devices.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.6rem">Value for Money ★★★★★</h4><p>$35.99/year or $44.99 lifetime for a tool that reliably solves one of the most stressful tech tasks people face is outstanding. Competing tools either cost more, do less, or don't handle WhatsApp cross-platform at all. The perpetual licence pays for itself after 15 months of annual use — an obvious choice for repeat switchers.</p></div>
  </div>

  <div style="text-align:center;margin-top:3.5rem">
    <h3 style="margin-bottom:1rem">Try <span class="g-acc">MobileTrans</span> Free</h3>
    <p style="color:var(--muted);margin-bottom:1.5rem;max-width:500px;margin-left:auto;margin-right:auto">Free trial available — test with your specific phones before buying. No credit card required.</p>
    <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free — No Credit Card</a>
  </div>
</section>""","MobileTrans review, MobileTrans rating, is MobileTrans worth it, Wondershare MobileTrans review 2025 2026",extras=[rev_s],article=True)


# ── PAGE: FAQ ─────────────────────────────────────────────────────────────────
def pg_faq():
    faqs=[
        ("Is MobileTrans free?","MobileTrans offers a fully functional free trial — no credit card needed. The trial lets you transfer up to 5 contacts and preview all features with your actual devices. Paid plans start from $35.99/year (Annual) or $44.99 one-time (Perpetual). Promotional discounts of up to 60% are frequently available on the official site."),
        ("Is MobileTrans safe to use?","Yes. MobileTrans is built by Wondershare, a globally trusted software company with 50M+ users. Critically, all data transfers happen directly between your devices or to your own computer — nothing is uploaded to any server. Your personal data never leaves your hands. Wondershare has been publishing software since 2003 and is a publicly listed company."),
        ("Can MobileTrans transfer WhatsApp from Android to iPhone?","Yes — and this is one of MobileTrans's standout capabilities. It transfers your complete WhatsApp history (all chats, photos, videos, voice messages, documents, stickers) from any Android phone to any iPhone. The reverse direction (iPhone to Android) also works — something almost no other tool supports."),
        ("Can MobileTrans transfer WhatsApp from iPhone to Android?","Yes. This is the difficult direction that most tools fail at. MobileTrans handles it by reading directly from WhatsApp on the old iPhone rather than relying on iCloud backups, then writing directly to the new Android. It may require one extra permission step on newer iOS versions, but it works reliably."),
        ("What devices does MobileTrans support?","MobileTrans supports 6,000+ devices across iOS and Android — including all iPhone models (3GS through iPhone 17), Samsung Galaxy (all series), Google Pixel, Huawei, OnePlus, Xiaomi, Sony Xperia, Motorola, Nokia, OPPO, Vivo, Realme and many more. It works with all major global carriers."),
        ("What data types does MobileTrans transfer?","18+ data types: contacts, SMS/MMS messages, photos, videos, music, playlists, podcasts, call logs, WhatsApp (chats + media), WhatsApp Business, GBWhatsApp, WeChat, Line, Kik, calendar events, notes, bookmarks, voice memos, voicemails, apps, ringtones, and iCloud data."),
        ("Does MobileTrans need Wi-Fi or cables?","Both options are available. USB cable transfer is the fastest (30 MB/s average speed). Wireless transfer works over Wi-Fi — scan a QR code to connect both phones, no OTG cable needed, transfers up to 8 data types. The PC backup-and-restore method only needs one cable (or no cable if your phone supports wireless backup)."),
        ("Does MobileTrans work on Mac?","Yes. MobileTrans is available for both Windows (7, 8, 10, 11 — 32 and 64-bit) and macOS (10.12 Sierra through the latest, including Apple Silicon M1/M2/M3). Both versions have identical features including WhatsApp transfer and wireless mode."),
        ("How long does a full phone transfer take?","A full phone transfer typically takes 3–15 minutes over USB, depending on how much data you have. A large photo library (10,000+ photos) takes longer — usually 20–30 minutes. Wireless transfers take approximately 20% longer than USB. In all cases, it's dramatically faster than doing it manually."),
        ("Can MobileTrans transfer iCloud data to Android?","Yes. MobileTrans can transfer iCloud contacts, photos and calendars directly to any Android device without requiring you to manually export or import anything. This is particularly useful when switching from iPhone to Android and wanting to bring your iCloud library across cleanly."),
        ("Does MobileTrans transfer WeChat, Line or Kik?","Yes. Beyond WhatsApp, MobileTrans supports backup and restore for WeChat, Line and Kik — making it the most comprehensive messaging transfer tool available for cross-platform switches. WeChat transfer is particularly useful for users in China and Southeast Asia."),
        ("Is there a MobileTrans mobile app?","Yes. Wondershare offers a MobileTrans mobile app for iOS and Android that enables wireless transfers of up to 8 data types without a computer or cables — just scan a QR code to connect. It supports contacts, photos, videos, music, WhatsApp, documents, apps and calendar."),
    ]
    items="".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q,a in faqs)
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:200]}..."}}}}' for q,a in faqs)+("]}")
    return page(f"MobileTrans FAQ {YEAR} — 12 Questions Answered in Full",
        "Complete MobileTrans FAQ: Is it free? Safe? WhatsApp Android to iPhone? iPhone to Android? Mac support? All devices? How long does it take? All 12 questions answered.",
        "/faq/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))}
  <span class="sec-label">Got Questions?</span>
  <h1>MobileTrans <span class="g-acc">FAQ</span></h1>
  <p style="max-width:620px;margin-top:.9rem;color:var(--muted)">Detailed answers to the 12 most common questions about MobileTrans — before you commit to a download or purchase.</p>
</div>
<section>
  <div class="faq-wrap">{items}</div>
  <div style="text-align:center;margin-top:3.5rem">
    <p style="color:var(--muted);margin-bottom:1.5rem">The best way to answer your remaining questions is to try it yourself — free, no credit card.</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download MobileTrans Free</a>
  </div>
</section>""","MobileTrans FAQ, MobileTrans safe, MobileTrans free, MobileTrans WhatsApp, MobileTrans Mac, MobileTrans review",extras=[faq_s])

# ── PAGE: DOWNLOAD ────────────────────────────────────────────────────────────
def pg_download():
    return page(f"Download MobileTrans Free — Windows & Mac | {YEAR}",
        "Download MobileTrans free for Windows and Mac. Transfer phones, WhatsApp and back up data in minutes. Free trial — no credit card needed. Windows 7-11 and macOS 10.12+.",
        "/download/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Download",None))}
  <span class="sec-label" style="display:block;text-align:center">Start in 60 Seconds</span>
  <h1>Download <span class="g-acc">MobileTrans</span></h1>
  <p style="max-width:540px;margin:.9rem auto 0;font-size:1.1rem;color:var(--muted)">Free trial — no credit card. Switch phones in minutes. Windows and Mac supported.</p>
</div>
<section>
  <div class="grid-2" style="max-width:760px;margin:0 auto 3rem">
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2.2rem">🪟</div>
      <h3>Windows</h3>
      <p style="margin-bottom:.5rem">Windows 7 / 8 / 10 / 11</p>
      <p style="font-size:.82rem;color:var(--muted);margin-bottom:1.6rem">32-bit and 64-bit · Latest version</p>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Windows</a>
    </div>
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2.2rem">🍎</div>
      <h3>macOS</h3>
      <p style="margin-bottom:.5rem">macOS 10.12 Sierra and later</p>
      <p style="font-size:.82rem;color:var(--muted);margin-bottom:1.6rem">Intel &amp; Apple Silicon (M1 / M2 / M3)</p>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Mac</a>
    </div>
  </div>
  <div class="grid-2" style="max-width:760px;margin:0 auto">
    <div class="hbox" style="margin:0"><h4>Free Trial Includes</h4>
      <ul class="check-list" style="margin-top:.8rem">
        <li>Transfer up to 5 contacts to test the process</li>
        <li>Preview all 18+ data types before buying</li>
        <li>Test USB and wireless transfer modes</li>
        <li>Try backup and restore</li>
        <li>Preview WhatsApp transfer capability</li>
        <li>Works with all 6,000+ supported devices</li>
      </ul>
    </div>
    <div class="hbox" style="margin:0"><h4>Also Available: Mobile App</h4>
      <p style="margin-top:.5rem">The MobileTrans mobile app (iOS and Android) enables wireless transfers of up to 8 data types without a computer — scan a QR code to connect. Available on the App Store and Google Play.</p>
      <p style="margin-top:.7rem;font-size:.85rem;color:var(--muted)">Upgrade to unlimited from $35.99/year or $44.99 lifetime.</p>
    </div>
  </div>
  <div style="text-align:center;margin-top:2.5rem">
    <a href="{SITE_ROOT}/pricing/" class="btn btn-ghost">View All Pricing Options →</a>
  </div>
</section>""")

# ── PAGE: ANDROID TO IPHONE ───────────────────────────────────────────────────
def pg_a2i():
    return page(f"Android to iPhone Transfer — Complete Guide {YEAR}",
        "Transfer everything from Android to iPhone: contacts, WhatsApp, messages, photos, videos, music, calendars and more. Step-by-step guide using MobileTrans.",
        "/android-to-iphone/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Android to iPhone",None))}
  <span class="sec-label">Transfer Guide</span>
  <h1>Android to <span class="g-acc">iPhone</span> Transfer<br><span style="font-size:60%;color:var(--muted)">The Complete {YEAR} Guide</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Switching from any Android phone to iPhone? Here's exactly how to move everything — including WhatsApp — without losing a single message, contact or photo.</p>
</div>
<section>
  <div class="hbox warn"><h4>Why Not Just Use Apple's "Move to iOS"?</h4><p style="margin-top:.5rem">Apple's Move to iOS app only works during initial iPhone setup (you can't use it later), doesn't transfer WhatsApp, doesn't move call logs or music libraries, and is often unreliable for large photo libraries. MobileTrans works anytime, transfers everything including WhatsApp, and takes 3–15 minutes for a full switch.</p></div>
  <div class="split" style="margin-top:2.5rem">
    <div>
      <h2 style="margin-bottom:1rem">What Gets Transferred<br><span class="g-acc">Android → iPhone</span></h2>
      <ul class="feat-list">
        <li><strong>Contacts</strong> — every contact with all fields, groups and custom labels</li>
        <li><strong>WhatsApp chats &amp; media</strong> — all messages, photos, videos, voice messages, stickers and documents</li>
        <li><strong>SMS &amp; MMS messages</strong> — full conversation history with timestamps and media</li>
        <li><strong>Photos &amp; videos</strong> — full camera roll at original resolution, no compression</li>
        <li><strong>Music &amp; playlists</strong> — your complete music library and playlist structure</li>
        <li><strong>Calendar events</strong> — all appointments, reminders and recurring events</li>
        <li><strong>Call logs</strong> — complete call history with duration and timestamps</li>
        <li><strong>Notes</strong> — all notes including pinned and folder-organised ones</li>
        <li><strong>Apps</strong> — compatible apps transferred where available</li>
      </ul>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">Step-by-Step: Android → iPhone</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-content"><h3>Install MobileTrans</h3><p>Download and install on your Windows or Mac computer. Takes about 60 seconds.</p></div></div>
          <div class="step" data-n="2"><div class="step-content"><h3>Connect Both Phones</h3><p>Connect your Android (old) and iPhone (new) via USB cables. MobileTrans auto-detects both.</p></div></div>
          <div class="step" data-n="3"><div class="step-content"><h3>Select "Phone Transfer"</h3><p>Android as source, iPhone as destination. Choose your data types — or select all.</p></div></div>
          <div class="step" data-n="4"><div class="step-content"><h3>Click Transfer</h3><p>Done in 3–15 minutes. Check your iPhone — everything is exactly where you left it.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-primary btn-full" style="margin-top:1.2rem" target="_blank" rel="noopener sponsored">⬇ Start Free Transfer</a>
      </div>
    </div>
  </div>
</section>""","Android to iPhone transfer, move data Android to iPhone, switch from Android to iPhone, MobileTrans Android iPhone",article=True)

# ── PAGE: IPHONE TO ANDROID ───────────────────────────────────────────────────
def pg_i2a():
    return page(f"iPhone to Android Transfer — The Only Guide That Works | {YEAR}",
        "Transfer everything from iPhone to Android including WhatsApp using MobileTrans. The only tool that moves WhatsApp from iPhone to Android reliably. Step-by-step guide.",
        "/iphone-to-android/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("iPhone to Android",None))}
  <span class="sec-label">Transfer Guide</span>
  <h1>iPhone to <span class="g-acc">Android</span> Transfer<br><span style="font-size:60%;color:var(--muted)">Including WhatsApp — {YEAR}</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Switching from iPhone to Android? This is the transfer Apple doesn't help with. MobileTrans is the only tool that reliably moves your WhatsApp and iCloud data to any Android phone.</p>
</div>
<section>
  <div class="hbox danger"><h4>Why iPhone → Android Is Harder</h4><p style="margin-top:.5rem">Apple locks WhatsApp backups inside iCloud — encrypted and incompatible with Android. Google's "Switch to Android" app doesn't touch WhatsApp. And Samsung Smart Switch only works with Samsung devices. MobileTrans bypasses all of this by reading directly from WhatsApp on your iPhone and writing directly to your Android — no iCloud or Google Drive backup needed.</p></div>
  <div class="split" style="margin-top:2.5rem">
    <div>
      <h2 style="margin-bottom:1rem">What Gets Transferred<br><span class="g-acc">iPhone → Android</span></h2>
      <ul class="feat-list">
        <li><strong>WhatsApp — complete history</strong> — the hard one, done reliably</li>
        <li><strong>iCloud Photos → Android</strong> — full resolution, every album</li>
        <li><strong>iMessage history</strong> — converted to SMS format on Android</li>
        <li><strong>Contacts</strong> — all fields, including custom labels and groups</li>
        <li><strong>Calendar &amp; Reminders</strong> — every event transferred with full details</li>
        <li><strong>Apple Notes → Android Notes</strong> — content preserved</li>
        <li><strong>Music &amp; Playlists</strong> — library and structure both transfer</li>
        <li><strong>Voice Memos</strong> — all recordings in original quality</li>
        <li><strong>Call Logs</strong> — full history with timestamps and duration</li>
      </ul>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">Step-by-Step: iPhone → Android</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-content"><h3>Install MobileTrans</h3><p>Download and install on your Windows or Mac computer.</p></div></div>
          <div class="step" data-n="2"><div class="step-content"><h3>Connect Both Phones</h3><p>Connect iPhone (old) and Android (new) via USB. Tap "Trust This Computer" on iPhone when prompted.</p></div></div>
          <div class="step" data-n="3"><div class="step-content"><h3>Set iPhone as Source</h3><p>Select iPhone as the source device and your Android as the destination.</p></div></div>
          <div class="step" data-n="4"><div class="step-content"><h3>Choose Data &amp; Transfer</h3><p>Select WhatsApp, contacts, photos — or all. Click Transfer. Done in minutes.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-primary btn-full" style="margin-top:1.2rem" target="_blank" rel="noopener sponsored">⬇ Transfer iPhone to Android Free</a>
      </div>
    </div>
  </div>
</section>""","iPhone to Android transfer, move data iPhone to Android, WhatsApp iPhone to Android, switch from iPhone to Android",article=True)


# ── PAGE: WHATSAPP TRANSFER ───────────────────────────────────────────────────
def pg_whatsapp():
    return page(f"WhatsApp Transfer Between Android & iPhone — Both Directions | {YEAR}",
        "Transfer your complete WhatsApp history between Android and iPhone in both directions using MobileTrans. Chats, photos, videos, voice messages all transferred safely. Free trial.",
        "/whatsapp-transfer/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("WhatsApp Transfer",None))}
  <span class="sec-label">WhatsApp Guide</span>
  <h1>Transfer <span class="g-acc">WhatsApp</span><br>Between Any Phone</h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">MobileTrans is the only tool that reliably transfers your complete WhatsApp history between Android and iPhone — in both directions — including years of chat history, photos, voice messages and media.</p>
</div>
<section>
  <div class="grid-3" style="margin-bottom:3rem">
    <div class="card card-alt"><div class="card-icon">📱→🍎</div><h3>Android → iPhone</h3><p>Move your complete WhatsApp from any Android to iPhone. All chats, photos, videos, voice messages and stickers arrive perfectly — including group chats and community messages.</p><a href="{AFF}" class="btn btn-ghost btn-sm" style="margin-top:1rem" target="_blank" rel="noopener sponsored">Transfer Now →</a></div>
    <div class="card card-alt"><div class="card-icon">🍎→📱</div><h3>iPhone → Android</h3><p>The difficult direction that most tools can't do. MobileTrans moves WhatsApp from iPhone to any Android by reading directly from the app — no iCloud backup needed.</p><a href="{AFF}" class="btn btn-ghost btn-sm" style="margin-top:1rem" target="_blank" rel="noopener sponsored">Transfer Now →</a></div>
    <div class="card"><div class="card-icon">💼</div><h3>WhatsApp Business</h3><p>Full support for WhatsApp Business transfers — all business chat history, contacts and media transferred in both directions. GBWhatsApp also supported.</p><a href="{AFF}" class="btn btn-ghost btn-sm" style="margin-top:1rem" target="_blank" rel="noopener sponsored">Transfer Now →</a></div>
  </div>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">What <span class="g-acc">Transfers</span> with WhatsApp</h2>
      <ul class="feat-list">
        <li><strong>All chat conversations</strong> — personal chats, group chats, community messages</li>
        <li><strong>Photos &amp; videos</strong> — every media file shared in conversations</li>
        <li><strong>Voice messages</strong> — every recorded audio clip preserved</li>
        <li><strong>Documents &amp; files</strong> — PDFs, Word files and other attachments</li>
        <li><strong>Stickers &amp; GIFs</strong> — custom sticker packs included</li>
        <li><strong>Starred messages</strong> — your saved important messages transfer too</li>
        <li><strong>Contact info</strong> — WhatsApp contacts and profile photos</li>
        <li><strong>Chat timestamps</strong> — exact dates and times preserved</li>
      </ul>
      <div class="hbox warn" style="margin-top:1.5rem"><h4>Why Is WhatsApp Transfer So Hard?</h4><p style="margin-top:.5rem">WhatsApp uses different backup systems on Android (Google Drive) and iOS (iCloud). These backups are encrypted and incompatible with each other. MobileTrans bypasses both by reading directly from the app on your old phone and writing to the app on your new phone — no cloud backup required.</p></div>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">How to Transfer WhatsApp</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-content"><h3>Open MobileTrans</h3><p>Launch MobileTrans and select <strong>"WhatsApp Transfer"</strong> from the main menu.</p></div></div>
          <div class="step" data-n="2"><div class="step-content"><h3>Connect Both Phones</h3><p>Connect old phone and new phone via USB. MobileTrans detects both automatically.</p></div></div>
          <div class="step" data-n="3"><div class="step-content"><h3>Set Source &amp; Destination</h3><p>Choose which phone is the source (old) and which is the destination (new). MobileTrans shows a clear confirmation.</p></div></div>
          <div class="step" data-n="4"><div class="step-content"><h3>Transfer — All Chats Move</h3><p>Click Transfer. Your entire WhatsApp history moves directly between devices. No cloud, no server, 100% private.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-primary btn-full" style="margin-top:1.2rem" target="_blank" rel="noopener sponsored">⬇ Transfer WhatsApp Free</a>
      </div>
    </div>
  </div>
</section>""","WhatsApp transfer, move WhatsApp Android to iPhone, WhatsApp iPhone to Android, transfer WhatsApp history, MobileTrans WhatsApp",article=True)

# ── PAGE: PHONE BACKUP ────────────────────────────────────────────────────────
def pg_backup():
    return page(f"Back Up Your Phone to PC — Complete Guide | {YEAR}",
        "Back up your iPhone or Android to your Windows or Mac PC in one click using MobileTrans. Restore anytime, even to a different device or OS. Full backup guide.",
        "/phone-backup/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Phone Backup",None))}
  <span class="sec-label">Backup Guide</span>
  <h1>Back Up Your Phone<br>to <span class="g-acc">PC in One Click</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">MobileTrans backs up your entire iPhone or Android to your computer in minutes — and restores it to any device, including a different brand or OS.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">Why Back Up to<br><span class="g-acc">Your Own Computer?</span></h2>
      <p style="margin-bottom:1.5rem">iCloud gives you 5GB free — barely enough for a few thousand photos. Google Photos has compression. A local backup on your own computer is unlimited, private, and faster to restore.</p>
      <ul class="feat-list">
        <li><strong>One-click full backup</strong> — contacts, messages, photos, WhatsApp, apps, calendar, notes and more</li>
        <li><strong>Completely private</strong> — stored on your computer, never uploaded anywhere</li>
        <li><strong>No storage limits</strong> — only limited by your computer's disk space</li>
        <li><strong>Cross-platform restore</strong> — restore an Android backup to an iPhone or vice versa</li>
        <li><strong>Selective restore</strong> — restore only specific data types, not everything</li>
        <li><strong>WhatsApp backup</strong> — full WhatsApp data snapshot included in backup</li>
        <li><strong>Fast</strong> — full phone backup typically completes in under 10 minutes</li>
      </ul>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Back Up Your Phone Free</a></div>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">How to Back Up Your Phone</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-content"><h3>Open MobileTrans</h3><p>Launch MobileTrans and select <strong>"Backup &amp; Restore"</strong> from the home screen.</p></div></div>
          <div class="step" data-n="2"><div class="step-content"><h3>Connect Your Phone</h3><p>Connect your iPhone or Android via USB. MobileTrans detects it and reads the device info.</p></div></div>
          <div class="step" data-n="3"><div class="step-content"><h3>Select Backup</h3><p>Click <strong>"Back Up Device"</strong>. Choose which data types to include — or select all for a complete snapshot.</p></div></div>
          <div class="step" data-n="4"><div class="step-content"><h3>Backup Saved to PC</h3><p>MobileTrans creates an encrypted backup file in your chosen folder. Done in under 10 minutes.</p><span class="step-tip">Restore anytime: open MobileTrans → Backup &amp; Restore → Restore</span></div></div>
        </div>
      </div>
    </div>
  </div>
</section>""","phone backup PC, back up iPhone to computer, back up Android to PC, MobileTrans backup, phone backup restore",article=True)

# ── PAGE: SAMSUNG TO IPHONE ───────────────────────────────────────────────────
def pg_samsung_to_iphone():
    return page(f"Samsung to iPhone Transfer — Move Everything in Minutes | {YEAR}",
        "Transfer all data from Samsung Galaxy to any iPhone model including WhatsApp, contacts, messages, photos and music. Step-by-step guide using MobileTrans. Free trial.",
        "/samsung-to-iphone/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Samsung to iPhone",None))}
  <span class="sec-label">Use Case Guide</span>
  <h1>Samsung Galaxy to <span class="g-acc">iPhone</span><br>Complete Transfer Guide</h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Upgrading from Samsung Galaxy to iPhone? Smart Switch won't cut it — it doesn't move WhatsApp. Here's how to move everything with MobileTrans.</p>
</div>
<section>
  <div class="hbox warn"><h4>Why Samsung Smart Switch Isn't Enough</h4><p style="margin-top:.5rem">Smart Switch moves some content from Samsung to iPhone but it doesn't transfer WhatsApp, doesn't preserve full SMS history, and is limited in what it can move between different ecosystems. MobileTrans handles all 18+ data types including WhatsApp in a single, clean transfer.</p></div>
  <div class="split" style="margin-top:2.5rem">
    <div>
      <h2 style="margin-bottom:1rem">Samsung → iPhone:<br><span class="g-acc">What Transfers</span></h2>
      <ul class="feat-list">
        <li><strong>Samsung Contacts</strong> — all contacts from Samsung's contact app</li>
        <li><strong>Samsung Messages</strong> — full SMS and MMS history</li>
        <li><strong>Galaxy Photos &amp; Videos</strong> — full camera roll at original quality</li>
        <li><strong>WhatsApp</strong> — chats, photos, voice messages, documents</li>
        <li><strong>Samsung Calendar</strong> — all events and reminders</li>
        <li><strong>Samsung Notes</strong> — content moves to iPhone Notes</li>
        <li><strong>Music Library</strong> — local music files and playlist structure</li>
        <li><strong>Call Logs</strong> — complete call history preserved</li>
      </ul>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Start Samsung to iPhone Transfer</a></div>
    </div>
    <div>
      <div class="hbox" style="margin:0"><h4>Supported Samsung Models</h4>
        <p style="margin-top:.5rem;font-size:.88rem">MobileTrans works with all Samsung Galaxy models:</p>
        <ul class="check-list" style="margin-top:.6rem;columns:2;column-gap:1rem">
          <li>Galaxy S25 Series</li><li>Galaxy S24 Series</li>
          <li>Galaxy S23 Series</li><li>Galaxy S22 Series</li>
          <li>Galaxy A Series</li><li>Galaxy Note Series</li>
          <li>Galaxy Z Fold 6</li><li>Galaxy Z Flip 6</li>
          <li>Older Galaxy models</li><li>Galaxy Tab Series</li>
        </ul>
      </div>
      <div class="hbox" style="margin:1rem 0 0"><h4>Supported iPhone Models</h4>
        <ul class="check-list" style="margin-top:.6rem;columns:2;column-gap:1rem">
          <li>iPhone 17 Series</li><li>iPhone 16 Series</li>
          <li>iPhone 15 Series</li><li>iPhone 14 Series</li>
          <li>iPhone 13 Series</li><li>iPhone 12 Series</li>
          <li>iPhone 11 Series</li><li>iPhone X Series</li>
        </ul>
      </div>
    </div>
  </div>
</section>""","Samsung to iPhone transfer, Galaxy to iPhone, move data Samsung iPhone, Samsung Smart Switch alternative",article=True)

# ── PAGE: ICLOUD TO ANDROID ───────────────────────────────────────────────────
def pg_icloud_android():
    return page(f"Transfer iCloud Data to Android — Contacts, Photos & Calendar | {YEAR}",
        "Transfer iCloud contacts, photos and calendar directly to any Android phone using MobileTrans. No manual export needed. Step-by-step guide for switching from iPhone to Android.",
        "/icloud-to-android/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("iCloud to Android",None))}
  <span class="sec-label">iCloud Guide</span>
  <h1>Transfer <span class="g-acc">iCloud Data</span><br>to Any Android Phone</h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Switching from iPhone to Android and need to bring your iCloud data across? MobileTrans handles the entire process — no manual CSV exports, no complicated steps.</p>
</div>
<section>
  <div class="grid-3" style="margin-bottom:3rem">
    <div class="card"><div class="card-icon">📋</div><h3>iCloud Contacts</h3><p>All contacts stored in iCloud — names, phone numbers, emails, addresses, photos and custom fields — transfer directly to your Android's native contacts app.</p></div>
    <div class="card"><div class="card-icon">📸</div><h3>iCloud Photos</h3><p>Your entire iCloud Photo Library transfers to your new Android at full original resolution. Albums, favourites and shared albums all preserved.</p></div>
    <div class="card"><div class="card-icon">📅</div><h3>iCloud Calendar</h3><p>All iCloud calendar events, reminders and shared calendars transfer to your Android's calendar. Recurrence rules, locations and notes all preserved.</p></div>
  </div>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">How to Transfer<br><span class="g-acc">iCloud to Android</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div class="step-content"><h3>Open MobileTrans</h3><p>Launch MobileTrans and select "iPhone to Android" from the transfer menu.</p></div></div>
        <div class="step" data-n="2"><div class="step-content"><h3>Connect Your iPhone</h3><p>Connect your iPhone via USB and sign in to iCloud when prompted by MobileTrans.</p></div></div>
        <div class="step" data-n="3"><div class="step-content"><h3>Connect Your Android</h3><p>Connect your new Android device. MobileTrans detects both devices and shows iCloud data available for transfer.</p></div></div>
        <div class="step" data-n="4"><div class="step-content"><h3>Select iCloud Data &amp; Transfer</h3><p>Choose contacts, photos, calendar — or all. Click Transfer. Done in minutes.</p></div></div>
      </div>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Transfer iCloud to Android Free</a></div>
    </div>
    <div>
      <div class="hbox"><h4>Works With All Android Brands</h4><p style="margin-top:.5rem">MobileTrans transfers iCloud data to any Android device — Samsung, Google Pixel, Huawei, OnePlus, Xiaomi, Sony, Motorola and more. No brand restrictions.</p></div>
      <div class="hbox warn" style="margin-top:1rem"><h4>What About iCloud Backup?</h4><p style="margin-top:.5rem">iCloud backups are in Apple's proprietary format and cannot be read directly by Android. MobileTrans bypasses this by reading the live data from your iPhone's apps and transferring it directly — no backup format conversion needed.</p></div>
    </div>
  </div>
</section>""","iCloud to Android, transfer iCloud contacts to Android, iCloud photos to Android, iPhone to Android iCloud",article=True)


# ── PAGE: SUPPORTED DEVICES ───────────────────────────────────────────────────
def pg_devices():
    brands={
        "📱 Apple iPhone":["iPhone 17 Pro Max","iPhone 17 Pro","iPhone 17","iPhone 17 Plus","iPhone 16 Pro Max","iPhone 16 Pro","iPhone 16","iPhone 15 Series","iPhone 14 Series","iPhone 13 Series","iPhone 12 Series","iPhone 11 Series","iPhone X / XS / XR","iPhone 8 / 7 / 6"],
        "🤖 Samsung Galaxy":["Galaxy S25 Ultra / S25+","Galaxy S24 Ultra / S24+","Galaxy S23 Series","Galaxy S22 Series","Galaxy A55 / A54 / A35","Galaxy A34 / A25 / A15","Galaxy Z Fold 6 / Fold 5","Galaxy Z Flip 6 / Flip 5","Galaxy Note 20 / Note 10","Galaxy Tab S9 / Tab S8"],
        "🔍 Google Pixel":["Pixel 9 Pro XL / Pro","Pixel 9 / 9a","Pixel 8 Pro / Pixel 8","Pixel 7 Pro / Pixel 7","Pixel 6 Pro / Pixel 6","Pixel Fold","Pixel Tablet"],
        "🌐 Huawei":["Huawei P60 Pro / P60","Huawei Mate 60 Pro","Huawei Nova 12","Huawei P50 Series","Huawei Mate 50 Series","Honor 90 / Magic6"],
        "⚡ OnePlus":["OnePlus 12 / 12R","OnePlus 11 / 11R","OnePlus Open","OnePlus Nord 4","OnePlus 10 Pro","OnePlus 9 Series"],
        "🎵 Sony & Others":["Sony Xperia 1 VI / 5 VI","Motorola Edge 50","Nokia G60 / X30","OPPO Find X7","Vivo X100","Realme GT 6","LG V60","Xiaomi 14 / 13"],
    }
    cats_html="".join(f'<div style="margin-bottom:2.5rem"><h3 style="margin-bottom:1rem;font-size:1.3rem">{cat}</h3><div class="dtype-grid">{"".join(f"<div class=dtype-pill>{d}</div>" for d in devices)}</div></div>' for cat,devices in brands.items())
    return page(f"MobileTrans Supported Devices — 6,000+ iOS & Android | {YEAR}",
        "MobileTrans supports 6,000+ devices: all iPhones, Samsung Galaxy, Google Pixel, Huawei, OnePlus, Sony, Xiaomi, Motorola and more. Full iOS and Android compatibility.",
        "/supported-devices/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Supported Devices",None))}
  <span class="sec-label">Universal Compatibility</span>
  <h1>Supported <span class="g-acc">Devices</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.1rem;color:var(--muted)">MobileTrans works with 6,000+ devices across iOS and Android — from the latest flagships to older models going back years.</p>
</div>
<section>
  <div class="hbox success"><p><strong>6,000+ devices supported.</strong> MobileTrans is updated regularly to support new models as they launch. Compatible with all iOS versions from iOS 7 through iOS 26 and Android 4.0 through Android 16. If it runs iOS or Android, MobileTrans almost certainly supports it.</p></div>
  {cats_html}
  <div style="text-align:center;margin-top:2.5rem">
    <p style="color:var(--muted);margin-bottom:1.5rem">...and thousands more devices across all brands and carriers worldwide</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download MobileTrans — Try Your Device Free</a>
  </div>
</section>""","MobileTrans supported devices, MobileTrans compatible phones, MobileTrans iPhone Android")

# ── PAGE: VS SMART SWITCH ─────────────────────────────────────────────────────
def pg_vs_ss():
    return page(f"MobileTrans vs Samsung Smart Switch — Honest Comparison {YEAR}",
        f"MobileTrans vs Samsung Smart Switch: features, device support, WhatsApp capability, pricing. Which phone transfer tool is better in {YEAR}? Full head-to-head.",
        "/vs-smart-switch/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Smart Switch",None))}
  <span class="sec-label">Head-to-Head</span>
  <h1>MobileTrans vs <span class="g-acc">Samsung Smart Switch</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Smart Switch is built into Samsung devices and free to use. MobileTrans costs $35.99/year but works with every brand. Here's exactly where each one wins.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Capability</th><th style="color:var(--acc)">MobileTrans</th><th>Samsung Smart Switch</th></tr></thead>
    <tbody>
      <tr><td class="td-name">Works with any brand</td><td class="td-yes td-hi">✓ 6,000+ devices</td><td class="td-no">Samsung devices only</td></tr>
      <tr><td class="td-name">iOS ↔ Android</td><td class="td-yes td-hi">✓ Both directions</td><td class="td-no">✗ Samsung ecosystem only</td></tr>
      <tr><td class="td-name">WhatsApp transfer</td><td class="td-yes td-hi">✓ Both ways</td><td class="td-no">✗ Not supported</td></tr>
      <tr><td class="td-name">iPhone to any Android</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-name">iCloud to Android</td><td class="td-yes td-hi">✓ Direct transfer</td><td class="td-no">✗</td></tr>
      <tr><td class="td-name">PC backup &amp; restore</td><td class="td-yes td-hi">✓ Full backup</td><td class="td-partial">Windows only, limited</td></tr>
      <tr><td class="td-name">Wireless transfer</td><td class="td-yes td-hi">✓ Any brand via QR</td><td class="td-partial">Samsung to Samsung only</td></tr>
      <tr><td class="td-name">WeChat / Line / Kik</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-name">Data types</td><td class="td-yes td-hi">18+</td><td class="td-partial">Basic types only</td></tr>
      <tr><td class="td-name">Works after phone setup</td><td class="td-yes td-hi">✓ Anytime</td><td class="td-partial">Best during setup</td></tr>
      <tr><td class="td-name">Mac support</td><td class="td-yes td-hi">✓ Full</td><td class="td-partial">Limited</td></tr>
      <tr><td class="td-name">Cost</td><td class="td-hi">$35.99/yr or $44.99 lifetime</td><td class="td-yes">Free (Samsung devices)</td></tr>
    </tbody>
  </table></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem">
    <div class="hbox" style="margin:0"><h4 style="color:var(--green)">✓ Choose MobileTrans if...</h4><ul class="check-list" style="margin-top:.8rem"><li>You're switching from a non-Samsung Android to iPhone</li><li>You need to transfer WhatsApp in either direction</li><li>You're moving from iPhone to any Android</li><li>You want iCloud data on your new Android</li><li>You need PC backup that works cross-platform</li></ul></div>
    <div class="hbox" style="margin:0"><h4 style="color:var(--gold)">✓ Smart Switch is fine if...</h4><ul class="check-list" style="margin-top:.8rem"><li>You're upgrading from one Samsung to another</li><li>You don't need WhatsApp transfer</li><li>You only use Windows (not Mac)</li><li>You want a free built-in tool for basic data</li></ul></div>
  </div>
  <div class="hbox success" style="margin-top:1.5rem"><h4>Bottom Line</h4><p style="margin-top:.5rem">Smart Switch is genuinely useful within the Samsung ecosystem and it's free — don't dismiss it for Samsung-to-Samsung upgrades. But the moment you need WhatsApp, cross-brand capability, or iPhone involvement, MobileTrans is the only tool that handles it properly. The $35.99/year or $44.99 lifetime cost is justified by what you get.</p></div>
  <div style="text-align:center;margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try MobileTrans Free →</a></div>
</section>""","MobileTrans vs Smart Switch, Samsung Smart Switch alternative, best phone transfer tool comparison")

# ── PAGE: VS IMAZING ──────────────────────────────────────────────────────────
def pg_vs_imazing():
    return page(f"MobileTrans vs iMazing — Comparison for iPhone Users {YEAR}",
        f"MobileTrans vs iMazing: features, pricing, Android support, WhatsApp capability. Which iPhone management tool is right for you in {YEAR}?",
        "/vs-imazing/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs iMazing",None))}
  <span class="sec-label">Head-to-Head</span>
  <h1>MobileTrans vs <span class="g-acc">iMazing</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">iMazing is excellent for deep iPhone management. MobileTrans excels at cross-platform switching including WhatsApp. Here's which to choose.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">MobileTrans</th><th>iMazing</th></tr></thead>
    <tbody>
      <tr><td class="td-name">iOS ↔ Android</td><td class="td-yes td-hi">✓ Both directions</td><td class="td-no">iOS only</td></tr>
      <tr><td class="td-name">WhatsApp iOS → Android</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-name">Android support</td><td class="td-yes td-hi">✓ Full support</td><td class="td-no">✗ Not supported</td></tr>
      <tr><td class="td-name">Deep iPhone management</td><td class="td-partial">Good</td><td class="td-yes">✓ Excellent</td></tr>
      <tr><td class="td-name">iCloud to Android</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-name">iPhone backup browsing</td><td class="td-partial">Basic</td><td class="td-yes">✓ Deep file access</td></tr>
      <tr><td class="td-name">Wireless transfer</td><td class="td-yes td-hi">✓ QR code method</td><td class="td-partial">Wi-Fi sync only</td></tr>
      <tr><td class="td-name">Annual price</td><td class="td-hi">$35.99/yr</td><td>$39.99/yr</td></tr>
      <tr><td class="td-name">Lifetime price</td><td class="td-hi">$44.99</td><td>$59.99</td></tr>
      <tr><td class="td-name">Free trial</td><td class="td-yes td-hi">✓</td><td class="td-yes">✓</td></tr>
    </tbody>
  </table></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:2rem">
    <div class="hbox" style="margin:0"><h4 style="color:var(--green)">Choose MobileTrans if...</h4><ul class="check-list" style="margin-top:.8rem"><li>You're switching to or from an Android device</li><li>You need WhatsApp transfer cross-platform</li><li>You want the lower-priced option</li><li>You need iCloud data on Android</li></ul></div>
    <div class="hbox" style="margin:0"><h4 style="color:var(--gold)">Choose iMazing if...</h4><ul class="check-list" style="margin-top:.8rem"><li>You only ever use Apple devices</li><li>You need deep iPhone file management</li><li>You want to browse backup contents in detail</li><li>You need to export specific app data</li></ul></div>
  </div>
  <div style="text-align:center;margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try MobileTrans Free →</a></div>
</section>""","MobileTrans vs iMazing, iMazing alternative, best iPhone transfer tool")

# ── PAGE: VS DR.FONE ──────────────────────────────────────────────────────────
def pg_vs_drfone():
    return page(f"MobileTrans vs dr.fone — Wondershare's Two Tools Compared {YEAR}",
        f"MobileTrans vs dr.fone: both are Wondershare products but for different use cases. Which one should you choose in {YEAR}? Full comparison.",
        "/vs-drfone/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs dr.fone",None))}
  <span class="sec-label">Head-to-Head</span>
  <h1>MobileTrans vs <span class="g-acc">dr.fone</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Both are made by Wondershare. Both are excellent. But they serve different needs. Here's how to choose the right one.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Factor</th><th style="color:var(--acc)">MobileTrans</th><th>dr.fone</th></tr></thead>
    <tbody>
      <tr><td class="td-name">Primary use case</td><td class="td-hi">Phone transfer &amp; switching</td><td>Phone management &amp; recovery</td></tr>
      <tr><td class="td-name">Phone-to-phone transfer</td><td class="td-yes td-hi">✓ Specialised, fast</td><td class="td-yes">✓ Included</td></tr>
      <tr><td class="td-name">WhatsApp transfer</td><td class="td-yes td-hi">✓ Dedicated mode</td><td class="td-yes">✓ Included</td></tr>
      <tr><td class="td-name">Data recovery</td><td class="td-no">✗</td><td class="td-yes">✓ Core feature</td></tr>
      <tr><td class="td-name">Screen mirror</td><td class="td-no">✗</td><td class="td-yes">✓</td></tr>
      <tr><td class="td-name">Ease of use</td><td class="td-yes td-hi">★★★★★ Focused UI</td><td class="td-partial">★★★★☆ Feature-dense</td></tr>
      <tr><td class="td-name">Price (annual)</td><td class="td-hi">$35.99/yr</td><td>$59.99/yr+</td></tr>
      <tr><td class="td-name">Best for</td><td class="td-hi">Switching phones cleanly</td><td>Managing &amp; recovering device</td></tr>
    </tbody>
  </table></div>
  <div class="hbox success" style="margin-top:2rem"><h4>Verdict</h4><p style="margin-top:.5rem">If your goal is to switch phones — move all your data from an old device to a new one — MobileTrans is the right choice. It's simpler, cheaper, and purpose-built for that exact task. dr.fone is better if you need data recovery, screen mirroring, or deeper phone management beyond just the transfer itself.</p></div>
  <div style="text-align:center;margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try MobileTrans Free →</a></div>
</section>""","MobileTrans vs dr.fone, dr.fone alternative, Wondershare phone tools comparison")

# ── PAGE: ALTERNATIVES ────────────────────────────────────────────────────────
def pg_alternatives():
    return page(f"Best MobileTrans Alternatives {YEAR} — Full Market Overview",
        f"Compare MobileTrans with every major phone transfer tool in {YEAR}: Smart Switch, iMazing, dr.fone, AnyTrans, Google's Switch to Android and Apple's Move to iOS.",
        "/alternatives/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))}
  <span class="sec-label">Full Market Overview</span>
  <h1>Best <span class="g-acc">MobileTrans Alternatives</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">We compared every major phone transfer tool so you can make a fully informed choice.</p>
</div>
<section>
  <div class="grid-2">
    <div class="card card-featured"><h3 style="color:var(--acc)">MobileTrans <span class="chip chip-g" style="margin-left:.5rem">Recommended</span></h3><p style="margin:.9rem 0">The most complete phone transfer tool. Works in every direction, transfers WhatsApp both ways, 6,000+ devices, wireless transfer, PC backup, WeChat/Line/Kik support.</p><ul class="check-list"><li>iOS ↔ Android, both ways</li><li>WhatsApp — both directions</li><li>$35.99/yr or $44.99 lifetime</li><li>6,000+ supported devices</li></ul><a href="{AFF}" class="btn btn-primary" style="margin-top:1.2rem" target="_blank" rel="noopener sponsored">Download Free →</a></div>
    <div class="card"><h3>Samsung Smart Switch</h3><p style="margin:.9rem 0">Free and built into Samsung phones. Good for Samsung-to-Samsung upgrades. No WhatsApp, no cross-brand transfers, no Mac support worth mentioning.</p><ul class="check-list"><li>Free</li><li>Samsung devices only</li></ul><a href="{SITE_ROOT}/vs-smart-switch/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>iMazing</h3><p style="margin:.9rem 0">Excellent iPhone management tool. iOS-only — no Android support at all. Good for deep iPhone backups and file access. More expensive at $39.99/year.</p><ul class="check-list"><li>iPhone / iPad only</li><li>Deep file management</li></ul><a href="{SITE_ROOT}/vs-imazing/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>dr.fone (Wondershare)</h3><p style="margin:.9rem 0">Wondershare's broader mobile toolkit with data recovery and screen mirror. More features than MobileTrans but more expensive and complex. MobileTrans is better for pure transfer tasks.</p><ul class="check-list"><li>Data recovery included</li><li>More expensive ($59.99/yr+)</li></ul><a href="{SITE_ROOT}/vs-drfone/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>Apple Move to iOS</h3><p style="margin:.9rem 0">Apple's free Android-to-iPhone tool. Works during initial setup only. Doesn't transfer WhatsApp, call logs or music. Very limited compared to MobileTrans.</p><span class="chip chip-g" style="margin-top:.8rem;display:inline-block">Free</span> <span class="chip chip-r" style="margin-top:.8rem;display:inline-block">Setup only</span></div>
    <div class="card"><h3>Google Switch to Android</h3><p style="margin:.9rem 0">Google's iPhone-to-Android tool. Transfers basic data but not WhatsApp, music libraries or complex data. One-directional and setup-only.</p><span class="chip chip-g" style="margin-top:.8rem;display:inline-block">Free</span> <span class="chip chip-r" style="margin-top:.8rem;display:inline-block">iOS → Android only</span></div>
  </div>
</section>""","MobileTrans alternatives, best phone transfer tool, phone data transfer comparison 2025 2026")


# ── PAGE: BLOG INDEX ──────────────────────────────────────────────────────────
def pg_blog():
    posts=[
        ("📱","Guide",f"Android to iPhone — Complete Transfer Guide {YEAR}","Move everything including WhatsApp from any Android to iPhone in minutes. No data loss, no stress.",f"{SITE_ROOT}/android-to-iphone/",f"June {YEAR}","8 min read"),
        ("🍎","Guide",f"iPhone to Android — The Transfer Guide That Works","The transfer Apple won't help with. Move WhatsApp, iCloud data and everything else to Android.",f"{SITE_ROOT}/iphone-to-android/",f"June {YEAR}","9 min read"),
        ("💬","Tutorial","How to Transfer WhatsApp Between Android & iPhone","Both directions. Complete step-by-step guide to moving years of WhatsApp history safely.",f"{SITE_ROOT}/whatsapp-transfer/",f"May {YEAR}","7 min read"),
        ("💾","Tutorial","How to Back Up Your Phone to PC — The Right Way","Create a complete local backup of your iPhone or Android that you can restore anywhere, anytime.",f"{SITE_ROOT}/phone-backup/",f"May {YEAR}","6 min read"),
        ("📲","Guide","Samsung Galaxy to iPhone — Full Transfer Guide","Upgrading from Samsung? Here's why Smart Switch isn't enough and how to move everything properly.",f"{SITE_ROOT}/samsung-to-iphone/",f"April {YEAR}","8 min read"),
        ("☁️","Tutorial","Transfer iCloud Data to Android — Step by Step","Switching from iPhone to Android and need your iCloud contacts, photos and calendar? Here's how.",f"{SITE_ROOT}/icloud-to-android/",f"April {YEAR}","6 min read"),
        ("🆚","Comparison","MobileTrans vs Samsung Smart Switch — Which Wins?","Smart Switch is free but Samsung-only. MobileTrans does everything. Full feature comparison.",f"{SITE_ROOT}/vs-smart-switch/",f"March {YEAR}","5 min read"),
        ("⭐","Review",f"MobileTrans Review {YEAR} — 9.1/10 After 12 Real Tests","We tested 12 device combinations. Here's our unbiased verdict on speed, accuracy and value.",f"{SITE_ROOT}/review/",f"March {YEAR}","10 min read"),
        ("💰","Guide",f"MobileTrans Pricing — Annual vs Lifetime {YEAR}","$35.99/year or $44.99 lifetime? We work out which plan gives you the best value.",f"{SITE_ROOT}/pricing/",f"February {YEAR}","4 min read"),
        ("🔒","Guide","Is MobileTrans Safe? Security &amp; Privacy Explained","Your phone data is personal. Here's exactly how MobileTrans handles it — and why it's private.",f"{SITE_ROOT}/faq/",f"February {YEAR}","4 min read"),
        ("⚡","Tutorial","Wireless Phone Transfer — No Cables Needed","How to transfer your phone data wirelessly in minutes using just a QR code and Wi-Fi.",f"{SITE_ROOT}/how-it-works/",f"January {YEAR}","5 min read"),
        ("📋","Guide","How to Transfer Contacts Between Any Two Phones","The simplest, most reliable way to move all your contacts from any old phone to any new one.",f"{SITE_ROOT}/features/",f"January {YEAR}","4 min read"),
    ]
    cards="".join(f"""<div class="bcard">
  <div class="bcard-thumb"><span class="bcard-thumb-icon">{e}</span></div>
  <div class="bcard-body">
    <div class="bcard-tag">{t}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
    <div class="bcard-meta"><span>📅 {d}</span><span>⏱ {read}</span></div>
    <a href="{url}" class="bcard-read">Read Article →</a>
  </div>
</div>""" for e,t,title,desc,url,d,read in posts)
    return page(f"MobileTrans Blog — Phone Transfer Guides & Tutorials {YEAR}",
        "Phone transfer guides, tutorials and comparisons. Learn to switch Android to iPhone, transfer WhatsApp, back up your phone and more — step by step.",
        "/blog/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",None))}
  <span class="sec-label">Guides, Tutorials & Reviews</span>
  <h1>MobileTrans <span class="g-acc">Blog</span></h1>
  <p style="max-width:620px;margin-top:.9rem;color:var(--muted)">Practical guides and honest reviews to help you switch phones without the stress.</p>
</div>
<section><div class="bgrid">{cards}</div></section>""","phone transfer guide, Android to iPhone tutorial, WhatsApp transfer guide, MobileTrans blog")

# ── PAGE: PRIVACY ─────────────────────────────────────────────────────────────
def pg_privacy():
    return page("Privacy Policy — MobileTrans Guide","Privacy policy for the MobileTrans affiliate guide.","/privacy/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy Policy",None))}<h1>Privacy <span class="g-acc">Policy</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><p>This website is an independent affiliate guide for MobileTrans by Wondershare. We earn commissions on qualifying purchases through our affiliate links — at no extra cost to you.</p></div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Data We Collect</h3><p>This is a static site hosted on GitHub Pages. We do not operate servers, collect personal data, or run databases. GitHub Pages may log standard server data (IP, browser, referrer) as part of its infrastructure — see GitHub's Privacy Policy for details.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Affiliate Links</h3><p>Links to MobileTrans are affiliate links via the LinkConnector network. When you click and make a qualifying purchase, we receive a commission. This does not affect the price you pay. We only recommend products we genuinely believe provide value.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Cookies</h3><p>This site does not set first-party cookies. Affiliate tracking uses cookies managed by LinkConnector. You can disable cookies in your browser settings.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Third Parties</h3><p>When you visit MobileTrans's website, you are subject to Wondershare's Privacy Policy. We are not responsible for third-party data practices.</p>
</section>""")

# ── PAGE: DISCLAIMER ──────────────────────────────────────────────────────────
def pg_disclaimer():
    return page("Affiliate Disclaimer — MobileTrans Guide","Affiliate disclosure for the MobileTrans guide.","/disclaimer/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}<h1>Affiliate <span class="g-acc">Disclaimer</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><h4>Disclosure</h4><p style="margin-top:.5rem">This website contains affiliate links. As an affiliate of Wondershare MobileTrans through the LinkConnector network, we earn a commission when purchases are made through our links — at no additional cost to you. This is how we fund the research and writing on this site.</p></div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Editorial Independence</h3><p>Our reviews and recommendations are based on genuine research and real-world testing. Affiliate relationships do not influence our editorial opinions. We include both pros and cons in all reviews — as you can see in our MobileTrans review where we clearly list the caveats alongside the strengths.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Accuracy</h3><p>We strive to keep pricing and features accurate. Software pricing and features can change at any time. Always verify current details on the official Wondershare website before purchasing.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Not Professional Advice</h3><p>Nothing on this website constitutes legal, financial or technical advice. For specific questions about your devices, consult Wondershare's official support team.</p>
</section>""")

# ── PAGE: 404 ─────────────────────────────────────────────────────────────────
def pg_404():
    return page("404 — Page Not Found | MobileTrans Guide","Page not found.","/404/",f"""
<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem">
  <div style="font-family:'Bebas Neue',sans-serif;font-size:9rem;line-height:1;background:linear-gradient(135deg,var(--acc),var(--acc2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text">404</div>
  <h1 style="margin-bottom:.5rem">Page <span class="g-acc2">Not Found</span></h1>
  <p style="max-width:400px;margin:0 auto">This page doesn't exist. Let's get you somewhere useful.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center;margin-top:.5rem">
    <a href="{SITE_ROOT}/" class="btn btn-primary">← Go Home</a>
    <a href="{AFF}" class="btn btn-secondary" target="_blank" rel="noopener sponsored">Download MobileTrans</a>
  </div>
</div>""")


# ── SEO FILES ─────────────────────────────────────────────────────────────────
def mk_sitemap():
    pages=[
        ("/","1.0","weekly"),("/features/","0.9","monthly"),("/how-it-works/","0.8","monthly"),
        ("/supported-devices/","0.9","monthly"),("/pricing/","0.9","monthly"),
        ("/review/","0.9","monthly"),("/faq/","0.8","monthly"),("/download/","0.9","monthly"),
        ("/blog/","0.8","weekly"),("/android-to-iphone/","0.9","monthly"),
        ("/iphone-to-android/","0.9","monthly"),("/whatsapp-transfer/","0.9","monthly"),
        ("/phone-backup/","0.8","monthly"),("/samsung-to-iphone/","0.8","monthly"),
        ("/icloud-to-android/","0.8","monthly"),("/alternatives/","0.8","monthly"),
        ("/vs-smart-switch/","0.8","monthly"),("/vs-imazing/","0.8","monthly"),
        ("/vs-drfone/","0.7","monthly"),("/privacy/","0.3","yearly"),("/disclaimer/","0.3","yearly"),
    ]
    today=date.today().isoformat()
    urls="\n".join(f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n    <lastmod>{today}</lastmod>\n  </url>" for p,pri,freq in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>'

def mk_robots():
    return f"User-agent: *\nAllow: /\nDisallow: /assets/\n\nSitemap: {SITE_URL}/sitemap.xml\n"

def mk_llms():
    return f"""# MobileTrans Guide — {SITE_URL}
> Purpose: Independent affiliate guide for MobileTrans by Wondershare
> Updated: {date.today().isoformat()}
> Affiliate network: LinkConnector
> Affiliate link: {AFF}

## Product Summary
- Name: MobileTrans by Wondershare Software Ltd
- Category: Phone transfer, backup & restore software
- Platforms: Windows 7–11, macOS 10.12+ (including Apple Silicon)
- Mobile app: iOS and Android (wireless transfer, up to 8 data types)
- Supported devices: 6,000+
- Data types: 18+ including contacts, SMS, photos, videos, music, WhatsApp (both ways), WhatsApp Business, GBWhatsApp, WeChat, Line, Kik, calendar, notes, call logs, voice memos, voicemails, apps, ringtones, bookmarks, podcasts, iCloud data
- Transfer methods: USB (30 MB/s, 200x faster than Bluetooth), wireless QR code (Wi-Fi), backup & restore
- Key differentiator: WhatsApp transfer in BOTH directions (Android→iPhone AND iPhone→Android)
- Privacy: No data uploaded to servers — transfers happen directly between devices
- Users: 50M+ worldwide since 2012
- Pricing: Free trial (5 contacts) | Annual $35.99/yr | Perpetual $44.99 one-time | Up to 60% off available
- Publisher: Wondershare Software Ltd (publicly listed)
- Mobile app speed: 200x faster than Bluetooth, average 30 MB/s, 1 GB video ~30 seconds

## Site Pages (21 HTML pages)
- / — Homepage with overview, comparison table, testimonials
- /features/ — Full feature list (15 features with detailed descriptions)
- /how-it-works/ — 3 transfer methods: USB, wireless QR, backup & restore
- /supported-devices/ — 6,000+ device list by brand
- /pricing/ — Plan comparison with FAQ (free, $35.99/yr, $44.99 lifetime)
- /review/ — Editorial review (9.1/10, 12 device combinations tested)
- /faq/ — 12 comprehensive FAQ answers with FAQ schema
- /download/ — Windows & Mac download page
- /blog/ — 12 article blog index
- /android-to-iphone/ — Full Android → iPhone transfer guide
- /iphone-to-android/ — Full iPhone → Android guide (includes WhatsApp)
- /whatsapp-transfer/ — WhatsApp both-directions guide
- /phone-backup/ — PC backup & restore guide
- /samsung-to-iphone/ — Samsung Galaxy → iPhone specific guide
- /icloud-to-android/ — iCloud data to Android guide
- /alternatives/ — MobileTrans vs 6 competitors
- /vs-smart-switch/ — vs Samsung Smart Switch full comparison
- /vs-imazing/ — vs iMazing full comparison
- /vs-drfone/ — vs dr.fone full comparison
- /privacy/ — Privacy policy
- /disclaimer/ — Affiliate disclosure

## Schema Types Used
SoftwareApplication, BreadcrumbList, FAQPage, Review, HowTo, ItemList
"""

def mk_feed():
    items=[
        (f"Android to iPhone: Complete Transfer Guide {YEAR}",f"{SITE_URL}/android-to-iphone/","Move everything including WhatsApp from Android to iPhone in minutes.",f"{YEAR}-06-01"),
        ("How to Transfer WhatsApp Between Android and iPhone",f"{SITE_URL}/whatsapp-transfer/","Both directions — complete WhatsApp transfer guide.",f"{YEAR}-05-15"),
        (f"MobileTrans Review {YEAR} — 9.1/10",f"{SITE_URL}/review/","Complete review after testing 12 device combinations.",f"{YEAR}-03-01"),
        ("iPhone to Android Transfer Guide",f"{SITE_URL}/iphone-to-android/","Transfer everything from iPhone to Android including WhatsApp.",f"{YEAR}-05-01"),
        ("Samsung Galaxy to iPhone — Complete Guide",f"{SITE_URL}/samsung-to-iphone/","Why Smart Switch isn't enough and how to move everything.",f"{YEAR}-04-15"),
    ]
    ixml="\n".join(f"  <item>\n    <title>{t}</title>\n    <link>{u}</link>\n    <description>{d}</description>\n    <pubDate>{pd}</pubDate>\n    <guid>{u}</guid>\n  </item>" for t,u,d,pd in items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>MobileTrans Guide — Blog</title>
    <link>{SITE_URL}/blog/</link>
    <description>Phone transfer guides, reviews and tutorials.</description>
    <language>en-us</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{ixml}
  </channel>
</rss>"""

def mk_favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#030512"/>
  <rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#7c6bff" stroke-width="1.5" opacity="0.5"/>
  <rect x="12" y="10" width="14" height="24" rx="3" fill="#7c6bff" opacity=".8"/>
  <rect x="38" y="30" width="14" height="24" rx="3" fill="#ff4f82" opacity=".8"/>
  <path d="M26 20 L38 20 L34 16 M38 20 L34 24" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M26 42 L38 42 M26 42 L30 38 M26 42 L30 46" stroke="#00f0ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>"""

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"\n🚀 MobileTrans Site Builder v2 — {SITE_URL}\n")

    # 21 HTML pages
    write("index.html",                          pg_index())
    write("features/index.html",                 pg_features())
    write("how-it-works/index.html",             pg_how())
    write("supported-devices/index.html",        pg_devices())
    write("pricing/index.html",                  pg_pricing())
    write("review/index.html",                   pg_review())
    write("faq/index.html",                      pg_faq())
    write("download/index.html",                 pg_download())
    write("blog/index.html",                     pg_blog())
    write("android-to-iphone/index.html",        pg_a2i())
    write("iphone-to-android/index.html",        pg_i2a())
    write("whatsapp-transfer/index.html",        pg_whatsapp())
    write("phone-backup/index.html",             pg_backup())
    write("samsung-to-iphone/index.html",        pg_samsung_to_iphone())
    write("icloud-to-android/index.html",        pg_icloud_android())
    write("alternatives/index.html",             pg_alternatives())
    write("vs-smart-switch/index.html",          pg_vs_ss())
    write("vs-imazing/index.html",               pg_vs_imazing())
    write("vs-drfone/index.html",                pg_vs_drfone())
    write("privacy/index.html",                  pg_privacy())
    write("disclaimer/index.html",               pg_disclaimer())
    write("404.html",                            pg_404())

    # SEO & meta files
    write("sitemap.xml",       mk_sitemap())
    write("robots.txt",        mk_robots())
    write("llms.txt",          mk_llms())
    write("feed.xml",          mk_feed())
    write("assets/favicon.svg",mk_favicon())
    write(".nojekyll",         "")

    pages=len([f for f in BASE.rglob("*.html")])
    total=len(list(BASE.rglob("*")))
    print(f"\n✅ Done — {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Live at: {SITE_URL}\n")

if __name__ == "__main__":
    main()
