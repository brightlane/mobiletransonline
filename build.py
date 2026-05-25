import os
import re
import random
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Configuration Overrides for Subbly Target
AFFILIATE_URL = "https://join.subbly.co/507vschv6rlq"
BASE_URL = "https://brightlane.github.io/subbly"

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def load_keywords(filename="keywords.txt", default_list=None):
    if not os.path.exists(filename):
        return default_list or ["Subscription Box Setup", "Recurring Billing Tool"]
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_dynamic_variations(keyword):
    hooks = [
        f"Launch and scale your recurring revenue engine using professional {keyword} tools.",
        f"Eliminate messy plug-ins. Build a turnkey subscription business with custom {keyword} matrices.",
        f"Maximize customer lifetime value. Deploy optimized checkouts built for modern {keyword} channels."
    ]
    return {"hook": random.choice(hooks)}

def generate_page_html(keyword, slug):
    v = get_dynamic_variations(keyword)
    title = f"Free {keyword} Blueprint & Platform Setup | Subbly Builder"
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="Build your subscription business instantly. Access premium {keyword} layouts, turnkey website structures, and automated billing matrices.">
    <link rel="canonical" href="{BASE_URL}/pages/{slug}.html">
    <style>
        :root {{ --primary: #FF2E93; --dark: #0F172A; --muted: #64748B; --bg-light: #FAFAFA; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: var(--dark); line-height: 1.6; margin: 0; padding: 0; }}
        header {{ padding: 1.25rem 2rem; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; background: #fff; }}
        .logo {{ font-size: 1.4rem; font-weight: 700; text-decoration: none; color: var(--dark); }}
        .logo span {{ color: var(--primary); }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 0 1.5rem; }}
        .hero {{ padding: 5rem 0 4rem; text-align: center; background: linear-gradient(180deg, #FFF0F6 0%, #FFF 100%); }}
        h1 {{ font-size: 3rem; font-weight: 800; letter-spacing: -0.02em; margin-bottom: 1.5rem; }}
        .hero p {{ font-size: 1.25rem; color: var(--muted); max-width: 700px; margin: 0 auto 2.5rem; }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 1rem 2.25rem; font-weight: 600; text-decoration: none; border-radius: 6px; box-shadow: 0 4px 14px rgba(255, 46, 147, 0.25); transition: opacity 0.2s; }}
        .btn:hover {{ opacity: 0.9; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin: 4rem 0; text-align: left; }}
        .card {{ padding: 2rem; border: 1px solid #E2E8F0; border-radius: 8px; background: #fff; }}
        .card h3 {{ margin-top: 0; color: var(--dark); }}
        .faq-section {{ background: var(--bg-light); padding: 4rem 0; border-top: 1px solid #E2E8F0; }}
        .faq-box {{ max-width: 750px; margin: 0 auto; }}
        .faq-item {{ background: #fff; padding: 1.5rem; border-radius: 6px; margin-bottom: 1rem; border: 1px solid #E2E8F0; }}
        footer {{ background: var(--dark); color: #94A3B8; padding: 2.5rem 0; text-align: center; font-size: 0.85rem; }}
    </style>

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "What is the fastest way to implement a professional {keyword} system?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "Subbly provides native, all-in-one structures including visual builder tools, automated subscription checkout links, and retention settings to handle your custom {keyword} deployment directly out of the box."
          }}
        }},
        {{
          "@type": "Question",
          "name": "Does this require complex coding or external plug-in stacks?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "No. Unlike generic e-commerce applications, Subbly features deeply integrated billing systems, eliminating plug-in conflicts and security issues completely."
          }}
        }}
      ]
    }}
    </script>
</head>
<body>
    <header>
        <a href="../" class="logo">bright<span>lane</span></a>
        <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn" style="padding: 0.5rem 1rem; font-size: 0.9rem;">Start Trial</a>
    </header>
    <main>
        <section class="hero">
            <div class="container">
                <h1>The Premium Platform Built For <br><span style="color:var(--primary);">{keyword}</span></h1>
                <p>{v["hook"]}</p>
                <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn">Launch Your Subscription Free</a>
            </div>
        </section>

        <div class="container">
            <section class="grid">
                <div class="card">
                    <h3>All-In-One Tech Stack</h3>
                    <p>Stop duct-taping standard CMS platforms together. Access completely integrated billing cycles, shipping schedules, customer accounts, and churn recovery rules natively.</p>
                </div>
                <div class="card">
                    <h3>Conversion Optimized Checkouts</h3>
                    <p>Kill order friction instantly. Our frameworks are custom engineered to handle multi-tier pricing plans, automatic tax logic, upsells, and digital or physical items seamlessly.</p>
                </div>
            </section>
        </div>

        <section class="faq-section">
            <div class="container">
                <div class="faq-box">
                    <h2 style="margin-bottom: 2rem; text-align: center;">Frequently Asked Questions</h2>
                    <div class="faq-item">
                        <h4>Can I test this setup prior to launching live?</h4>
                        <p>Yes. You can build your store configurations, try out subscription payment cycles, and optimize layout pipelines during your free sandbox evaluation run.</p>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2026 brightlane. Independent promotional resource channel supporting modern e-commerce entrepreneurs.</p>
    </footer>
</body>
</html>"""

def generate_blog_html(title, slug, random_internal_landing=None):
    today_str = datetime.now().strftime("%B %d, %Y")
    
    # Advanced Multi-Variant Content Pools to guarantee uniqueness on daily runs
    intros = [
        f"Scaling reliable recurring pipelines requires strategic backend engineering. Analyzing {title} gives digital merchants the tools needed to build long-term subscriber equity.",
        f"When orchestrating a major subscription rollout, analyzing patterns within {title} allows optimization teams to protect thin margins and prevent early member attrition.",
        f"Modern subscription commerce is moving rapidly. Staying ahead with strategic tools like {title} ensures consistent month-over-month recurring growth configurations."
    ]
    
    body_p1 = [
        "Traditional digital storefront architectures fail when tracking recurring shipment parameters out of the box. Patching disjointed, third-party plug-ins together often results in fatal database sync errors and broken user account areas. Running true recurring storefronts demands a natively continuous solution built to accurately process billing tokens securely.",
        "Maximizing subscriber lifetime valuation metrics begins at the initial validation steps. When checkout sequences load with minimal layout friction, conversion success ticks upwards across desktop and mobile pathways. Minimizing multi-page customer onboarding steps ensures transactional acquisition costs stay low."
    ]
    
    body_p2 = [
        "Beyond initial customer checkout optimizations, your ongoing retention rules must execute predictably behind the scenes. Utilizing intelligent dunning sequences and flexible customer portal systems lets subscribers modify, pause, or adjust shipment cycles easily without calling help desks. This structural autonomy directly prevents accidental subscriber drop-offs.",
        "Similarly, modern supply chains require instant webhooks to accurately manage inventory layers. Integrating subscription pipelines cleanly into backend fulfillment workflows automates packing workflows and tracking routes. Eliminating manual fulfillment tasks frees up operating margins to reinvest into paid growth channels."
    ]

    internal_link_html = ""
    if random_internal_landing:
        landing_slug = slugify(random_internal_landing)
        internal_link_html = f'<p style="margin-top: 2rem; background: #FFF0F6; border-left: 4px solid var(--primary); padding: 1rem; border-radius: 4px;">Looking for direct implementation tracks? Read our step-by-step master reference on <a href="../pages/{landing_slug}.html" style="color:var(--primary); font-weight:700; text-decoration: underline;">{random_internal_landing} Solutions</a>.</p>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | brightlane Insights</title>
    <meta name="description" content="Expert look at {title}. Master custom subscription layouts, recurring checkouts, and customer churn metrics.">
    <link rel="canonical" href="{BASE_URL}/blog/{slug}.html">
    <style>
        :root {{ --primary: #FF2E93; --dark: #0F172A; --muted: #64748B; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; color: var(--dark); line-height: 1.7; margin: 0; padding: 0; }}
        header {{ padding: 1.25rem 2rem; border-bottom: 1px solid #E2E8F0; display: flex; justify-content: space-between; align-items: center; }}
        .container {{ max-width: 700px; margin: 0 auto; padding: 3rem 1.5rem; }}
        .meta {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 1rem; }}
        .cta-box {{ background: #FAFAFA; border: 1px solid #E2E8F0; padding: 2.5rem; border-radius: 8px; margin-top: 3.5rem; text-align: center; }}
        .btn {{ display: inline-block; background: var(--primary); color: white; padding: 0.85rem 1.75rem; text-decoration: none; border-radius: 6px; font-weight: 600; margin-top: 1.25rem; }}
    </style>
</head>
<body>
    <header>
        <a href="../" style="font-size:1.4rem; font-weight:700; text-decoration:none; color:var(--dark);">bright<span style="color:var(--primary);">lane</span></a>
    </header>
    <main class="container">
        <div class="meta">Published on {today_str} • Subscription Analytics Lab</div>
        <h1>{title}</h1>
        <p style="font-size:1.15rem; color:#475569; margin: 1.5rem 0 2rem;">{random.choice(intros)}</p>
        
        <h2>Architecting Clean Recurring Funnels</h2>
        <p>{random.choice(body_p1)}</p>
        
        <h2>Maximizing Long-Term Retention Rules</h2>
        <p>{random.choice(body_p2)}</p>

        {internal_link_html}

        <div class="cta-box">
            <h3>Scale Your Subscriptions to Consistent Profitability</h3>
            <p>Access the robust all-in-one native architecture optimized specifically for complex recurring business checkouts.</p>
            <a href="{AFFILIATE_URL}" target="_blank" rel="noopener sponsored" class="btn">Claim Your Free Subbly Trial Now</a>
        </div>
    </main>
</body>
</html>"""

def generate_index_html(pages_list, posts_list):
    """Builds an SEO-optimized hub index page so search engines can easily crawl and pass authority to all child links."""
    links_html = "".join([f'<li><a href="pages/{p[1]}">{p[0]} Blueprint</a></li>' for p in pages_list])
    blogs_html = "".join([f'<li><a href="blog/{b[1]}">{b[0]}</a></li>' for b in posts_list])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Subscription E-Commerce Blueprint Hub | brightlane</title>
    <meta name="description" content="Access specialized programmatic blueprints and insights designed to help build high-growth recurring revenue storefronts effortlessly.">
    <style>
        :root {{ --primary: #FF2E93; --dark: #0F172A; --muted: #64748B; }}
        body {{ font-family: -apple-system, sans-serif; color: var(--dark); line-height: 1.6; margin: 0; padding: 0; }}
        .container {{ max-width: 900px; margin: 0 auto; padding: 4rem 1.5rem; }}
        h1 {{ font-size: 2.5rem; margin-bottom: 0.5rem; }}
        .subtitle {{ font-size: 1.2rem; color: var(--muted); margin-bottom: 3rem; }}
        .hub-section {{ display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 2rem; }}
        @media(max-width: 768px) {{ .hub-section {{ grid-template-columns: 1fr; }} }}
        ul {{ list-style: none; padding: 0; }}
        li {{ margin-bottom: 0.75rem; }}
        a {{ color: var(--primary); text-decoration: none; font-weight: 500; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <main class="container">
        <h1>brightlane Subscription Optimization Directory</h1>
        <p class="subtitle">Programmatic blueprints and daily tactical guides engineered to skyrocket subscriber retention.</p>
        
        <div class="hub-section">
            <div>
                <h2>Target Deployment Blueprints</h2>
                <ul>{links_html}</ul>
            </div>
            <div>
                <h2>Daily Optimization Insights</h2>
                <ul>{blogs_html}</ul>
            </div>
        </div>
    </main>
</body>
</html>"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Master Hub Index compiled live.")

def build_unified_sitemap(pages, posts):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Hub Root Entry
    root_url = ET.SubElement(urlset, "url")
    ET.SubElement(root_url, "loc").text = f"{BASE_URL}/"
    ET.SubElement(root_url, "changefreq").text = "daily"
    ET.SubElement(root_url, "priority").text = "1.0"

    for p in pages:
        u = ET.SubElement(urlset, "url")
        ET.SubElement(u, "loc").text = f"{BASE_URL}/pages/{p}"
        ET.SubElement(u, "changefreq").text = "weekly"
        ET.SubElement(u, "priority").text = "0.8"

    for b in posts:
        u = ET.SubElement(urlset, "url")
        ET.SubElement(u, "loc").text = f"{BASE_URL}/blog/{b}"
        ET.SubElement(u, "changefreq").text = "daily"
        ET.SubElement(u, "priority").text = "0.9"

    xml_str = ET.tostring(urlset, encoding="utf-8")
    parsed_xml = minidom.parseString(xml_str)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(parsed_xml.toprettyxml(indent="  "))
    print("✓ Sitemap synchronized cleanly.")

def main():
    os.makedirs("pages", exist_ok=True)
    os.makedirs("blog", exist_ok=True)
    
    # 1. Compile Landing Pages Matrix
    keywords = load_keywords("keywords.txt", ["Subscription Box Platform", "Recurring Subscription Billing"])
    pages_tracking = []
    for kw in keywords:
        slug = slugify(kw)
        file_name = f"{slug}.html"
        with open(os.path.join("pages", file_name), "w", encoding="utf-8") as f:
            f.write(generate_page_html(kw, slug))
        pages_tracking.append((kw, file_name))

    # 2. Compile Daily Dynamic Blog Entry
    blog_topics = load_keywords("blog_topics.txt", ["How to Launch a Profitable Subscription Box Business"])
    if blog_topics:
        current_topic = blog_topics[0]
        blog_slug = slugify(current_topic)
        random_link_target = random.choice(keywords) if keywords else None
        
        with open(os.path.join("blog", f"{blog_slug}.html"), "w", encoding="utf-8") as f:
            f.write(generate_blog_html(current_topic, blog_slug, random_link_target))
        print(f"✓ Blog post generated: '{current_topic}'")

    # 3. Pull historical blogs to display on home page & sitemap
    raw_blog_files = [f for f in os.listdir("blog") if f.endswith(".html")]
    
    # Map out display titles for home page linking
    blog_tracking = []
    for f in raw_blog_files:
        clean_title = f.replace("-", " ").replace(".html", "").title()
        blog_tracking.append((clean_title, f))

    # 4. Generate Master Navigation Hub Index and Unified Sitemap
    generate_index_html(pages_tracking, blog_tracking)
    build_unified_sitemap([p[1] for p in pages_tracking], raw_blog_files)

if __name__ == "__main__":
    main()
