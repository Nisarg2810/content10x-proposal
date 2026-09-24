#!/usr/bin/env python3
"""Build the Content 10x proposal site."""
import pathlib
import html as H
OUT = pathlib.Path(__file__).parent

SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SQ = '<svg viewBox="0 0 200 14" preserveAspectRatio="none"><path d="M2 8 Q 12 2 22 8 T 42 8 T 62 8 T 82 8 T 102 8 T 122 8 T 142 8 T 162 8 T 182 8 T 198 8"/></svg>'

def sq(w):
    return f'<span class="nw"><span class="squig">{w}{SQ}</span></span>'

NAV = [('index.html', 'Overview'), ('option-1.html', 'Option 1'), ('answers.html', 'Your questions'), ('investment.html', 'Investment'), ('option-2.html', 'Option 2'), ('option-3.html', 'Option 3')]

HEY = '''<div class="hey" id="hey" aria-hidden="true">
  <div class="hey-in">
    <img class="hey-sticker" src="assets/img/amy.webp" alt="" width="760" height="950" fetchpriority="high">
    <p class="hey-kick">A proposal, made for you</p>
    <div class="hey-h">Hey <span class="squig">Amy%s</span></div>
    <p class="hey-sub">Your website and blog, three ways. Two minutes to read.</p>
    <div class="hey-bar"><i></i></div>
    <button class="hey-skip" id="heySkip" type="button">Skip</button>
  </div>
</div>''' % SQ


def shell(page, title, desc, body):
    ON = ' class="on"'
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ON if h == page else '', t) for h, t in NAV)
    nav += '<a class="nav-cmp" href="index.html#compare">Compare</a>'
    sheet = ''.join(f'<a href="{h}"><b>{i+1:02d}</b>{t}</a>' for i, (h, t) in enumerate(NAV))
    sheet += '<a href="index.html#compare"><b>05</b>Compare the three</a>'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#060910">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%235B8CFF'/%3E%3Ctext x='32' y='43' font-size='34' text-anchor='middle' fill='white' font-family='sans-serif' font-weight='bold'%3E10%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&display=swap">
<link rel="stylesheet" href="assets/site.css?v=1">
<link rel="stylesheet" href="assets/mock.css?v=1">\n<link rel="stylesheet" href="assets/film.css?v=7">
<script>try{{var t=localStorage.getItem('c10-theme')||'dark';document.documentElement.setAttribute('data-theme',t);}}catch(e){{document.documentElement.setAttribute('data-theme','dark');}}</script>
</head>
<body>
<div class="mesh" aria-hidden="true"></div>
{HEY if page == "index.html" else ""}
<header class="hdr"><div class="hdr-row">
  <a class="logo" href="index.html"><i>10</i><span>Content 10x <span style="color:var(--t3);font-weight:500">proposal</span></span></a>
  <nav class="nav">{nav}</nav>
  <div class="hdr-r">
    <button class="tbtn" id="themeBtn" aria-label="Switch theme"><svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M19.1 4.9l-1.8 1.8M6.7 17.3l-1.8 1.8" stroke-linecap="round"/></svg><svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 14.2A8.2 8.2 0 1 1 9.8 4a6.6 6.6 0 0 0 10.2 10.2z"/></svg></button>
    <button class="burger" id="burger" aria-label="Menu"><i></i><i></i></button>
  </div>
</div></header>
<div class="sheet"><div class="wrap" style="width:100%">{sheet}</div></div>
<main>
{body}
</main>
<footer class="ftr"><div class="wrap">
  <div class="ftr-top">
    <div><a class="logo" href="index.html"><i>10</i><span>Content 10x proposal</span></a>
      <p style="color:var(--t2);font-size:15px;margin-top:14px;max-width:38ch">Website and blog proposal for Content 10x. Three options, one shared content structure, prepared by Nisarg Mehta.</p></div>
    <div><h4>The options</h4>{''.join(f'<a href="{h}">{t}</a><br>' for h, t in NAV)}</div>
    <div><h4>On this proposal</h4><a href="index.html#compare">Compare the three</a><br><a href="index.html#safety">Search rankings</a><br><a href="index.html#need">What I need from you</a><br><a href="index.html#scope">What is included</a></div>
  </div>
  <div class="ftr-b"><p>Prepared for Content 10x &middot; September <span id="yr">2026</span></p><p>Happy to adjust the scope to suit your priorities</p></div>
</div></footer>
<script src="assets/site.js?v=1"></script>
</body>
</html>
"""

# ---------------------------------------------------------------- mockups
def frame(url, body, phone='', cursor=True, caption='', nav=True, tall=False):
    n = ('<div class="mk-nav"><span class="mk-logo">Content <em>10x</em></span><span>What we do</span><span>Industries</span>'
         '<span>Our work</span><span>Resources</span><span class="mk-cta">Book a call</span></div>') if nav else ''
    cur = '<span class="mk-cursor"></span>' if cursor else ''
    cap = '<figcaption class="mk-cap">%s</figcaption>' % caption if caption else ''
    return (f'<figure class="mk"><div class="mk-win">'
            f'<div class="mk-bar"><i></i><i></i><i></i><div class="mk-url"><b>&#128274;</b>{url}</div></div>'
            f'<div class="mk-body">{n}{body}</div></div>{phone}{cur}'
            f'<span class="mk-live"><i></i>Live preview</span>{cap}</figure>')

def card(tag, tone, title, meta):
    return f'<div class="mk-card"><span class="th"></span><span class="mk-tag {tone}">{tag}</span><b>{title}</b><small>{meta}</small></div>'

OLD_POSTS = [('', '', 'How to Turn One Event Sponsorship Into Six Months of Content', 'March 2019'),
             ('', '', 'The B2B Podcast Playbook: Planning Your First Season', 'August 2021'),
             ('', '', '12 Ways to Repurpose a Webinar Recording', 'January 2020'),
             ('', '', 'Why Your LinkedIn Strategy Needs Employee Advocacy', 'June 2023'),
             ('', '', 'Content Marketing Benchmarks You Should Actually Track', 'May 2018'),
             ('', '', 'Our Favourite Tools for Repurposing Video in 2022', 'October 2022')]

def mk_blog_today():
    cards = ''.join(f'<div class="mk-card"><span class="th"></span><b>{t}</b><small>{d}</small></div>' for _, _, t, d in OLD_POSTS)
    return frame('content10x.com/blog',
        '<div class="mk-page"><div class="mk-h1">The Content 10x Blog</div>'
        '<div class="mk-sub">Over 350 blog posts on B2B content marketing, repurposing and distribution.</div>'
        f'<div class="mk-search">{SEARCH}Search the blog...</div>'
        f'<div class="mk-grid">{cards}</div>'
        '<div class="mk-more">...continues for 350+ posts, newest first, no grouping</div></div>'
        '<span class="mk-note n1">Search is the only way in</span>'
        '<span class="mk-note n2">A podcast write up looks like a news post</span>'
        '<span class="mk-note n3">No next step for the reader</span>', cursor=False,
        caption='The blog as a visitor meets it today: one long list, no grouping, no way to browse a topic.')

def mk_blog_new():
    set_a = ''.join([card('PODCAST', '', 'How to Turn One Event Sponsorship Into Six Months of Content', '38 min listen &middot; Repurposing'),
                     card('GUIDE', 'g', 'The Complete Guide to B2B Content Repurposing', '12 min read &middot; Repurposing'),
                     card('HOW-TO', 'a', 'Build a Weekly LinkedIn Rhythm With Your Team', '7 min read &middot; Employee led')])
    set_b = ''.join([card('PODCAST', '', 'Season Planning for a B2B Show That Actually Converts', '38 min listen &middot; Podcasting'),
                     card('GUIDE', 'g', 'Booking Guests Your Buyers Want to Hear From', '12 min read &middot; Podcasting'),
                     card('INTERVIEW', 'v', 'Inside a Podcast Led Content Programme', '24 min listen &middot; Podcasting')])
    return frame('content10x.com/blog/podcasting',
        '<div class="mk-page"><div class="mk-h1">The Content 10x Blog</div>'
        '<div class="mk-sub">Browse by topic, format or time. Or search inside a topic.</div>'
        '<div class="mk-fil"><span class="on first">All</span><span>Strategy</span><span>Repurposing</span>'
        '<span class="pick">Podcasting</span><span>Employee led</span><span>AI &amp; Search</span><span>+2</span></div>'
        f'<div class="mk-search">{SEARCH}Search within Podcasting</div>'
        f'<div class="mk-swap"><div class="set a"><div class="mk-grid">{set_a}</div></div>'
        f'<div class="set b"><div class="mk-grid">{set_b}</div>'
        '<div class="mk-start"><b>Start here: B2B Podcasting</b><p>New to this topic? These five posts are the place to begin.</p>'
        '<div class="rows"><span>Should your B2B brand start a podcast?</span><span>Planning your first season</span><span>Turning one episode into ten assets</span></div></div>'
        '<div class="mk-news"><b>Get the next podcasting post by email</b><span>Subscribe</span></div></div></div></div>',
        caption='One click per topic, search inside a topic, format and time on every card, and a Start here list on each hub.')

def mk_hub():
    return frame('content10x.com/blog/repurposing',
        '<div class="mk-page"><span class="mk-tag">NICHE HUB</span><div class="mk-h1" style="margin-top:.3em">Repurposing and Distribution</div>'
        '<div class="mk-sub" style="max-width:34em">Turning one asset into many, distribution systems and multi platform publishing. Everything Content 10x has published on repurposing, in one place.</div>'
        '<div class="mk-start" style="margin-top:1em"><b>Start here</b><p>Five posts that cover the basics in order.</p>'
        '<div class="rows"><span>What repurposing actually means</span><span>The one to many framework</span><span>Repurposing a webinar, step by step</span><span>Building a distribution system</span><span>Measuring what repurposing returns</span></div></div>'
        f'<div class="mk-grid" style="margin-top:.8em">{card("GUIDE","g","The Complete Guide to B2B Content Repurposing","12 min read")}{card("PODCAST","","One Event, Six Months of Content","38 min listen")}{card("TEMPLATE","v","The Repurposing Planner","Download")}</div>'
        '<div class="mk-news"><b>Get the next repurposing post by email</b><span>Subscribe</span></div></div>',
        cursor=False, caption='Each niche gets a real landing page: an introduction, the best posts, a Start here list and its own call to action.')

def mk_home():
    return frame('content10x.com',
        '<div class="mk-hero"><h2>Turn one piece of content into ten.</h2>'
        '<p>B2B content repurposing, podcasting and distribution, done for you by a specialist team.</p>'
        '<div class="btns"><span>Book a call</span><span class="ghost">See our work</span></div></div>'
        '<div class="mk-logos"><small>TRUSTED BY</small><i></i><i></i><i></i><i></i><i></i></div>'
        '<div class="mk-srv"><div><b>Repurposing</b><p>One asset becomes a month of content across every channel.</p></div>'
        '<div><b>Podcasting</b><p>Strategy, production and the content programme around the show.</p></div>'
        '<div><b>Content strategy</b><p>Positioning, planning and the system that keeps it running.</p></div></div>',
        cursor=False, caption='A new homepage built from the agreed design direction. Layout shown is indicative, the real direction is agreed with you first.')

def mk_ds():
    sw = ''.join(f'<div style="background:{c}">{n}</div>' for c, n in [('#101A33', 'Navy'), ('#2F62FF', 'Blue'), ('#34C7A1', 'Accent'), ('#E8EDF7', '<span style="color:#475467">Surface</span>'), ('#F7F9FC', '<span style="color:#475467">Ground</span>')])
    return frame('content10x.com/design-system',
        f'<div class="mk-ds"><div><div class="mk-sw">{sw}</div>'
        '<div class="mk-ty"><b>Aa Headings</b><small>Display sans, used for every page title and section heading</small>'
        '<b style="font-family:var(--f-b);font-size:1.2em">Aa Body</b><small>Reading face, used for all long form text</small></div></div>'
        '<div class="mk-comp"><div class="row"><span style="background:#101827;color:#fff">Primary button</span><span style="background:#fff;color:#101827;border:1px solid #e1e5ec">Secondary</span></div>'
        '<div class="mk-block">Card block: image, tag, title, meta</div><div class="mk-block">Feature block: heading, text, two buttons</div>'
        '<div class="mk-block">Call to action block: headline and form</div><div class="mk-block">Post list block: filters and cards</div></div></div>',
        nav=False, cursor=False, caption='Colours, type, buttons and page blocks are defined once, then every page is built from them.')

def mk_cms():
    return frame('cms.content10x.com/podcast-episodes/354',
        '<div class="cms"><aside class="cms-side"><h6>CONTENT</h6>'
        '<span class="on">Podcast episodes</span><span>Blog posts</span><span>Guests</span><span>Case studies</span><span>Industries</span><span>Resources</span><span>Pages</span>'
        '<h6>SETTINGS</h6><span>Niches &amp; tags</span><span>Media library</span><span>Users &amp; roles</span><span>Redirects</span></aside>'
        '<div class="cms-main"><div class="cms-top"><b>Podcast episode &middot; Draft</b><span>Preview</span><span>Save</span><span class="pub">Publish</span></div>'
        '<div class="cms-cols"><div>'
        '<div class="cms-f"><small>TITLE</small><div>How to Turn One Event Sponsorship Into Six Months of Content</div></div>'
        '<div class="cms-f sel"><small>NICHE</small><div>Repurposing <em style="font-style:normal;color:#98a2b3">&#9662;</em></div></div>'
        '<div class="cms-f sel"><small>FORMAT</small><div>Podcast episode <em style="font-style:normal;color:#98a2b3">&#9662;</em></div></div>'
        '<div class="cms-f sel"><small>GUEST</small><div>Jillian Hoefer <em style="font-style:normal;color:#98a2b3">&#9662;</em></div></div>'
        '<div class="cms-blocks"><h6>PAGE BLOCKS &middot; DRAG TO REORDER</h6><p>Audio player &middot; Episode 354</p><p class="drag">Pull quote</p><p>Rich text</p><p>Newsletter call to action</p><span class="cms-add">+ Add block</span></div>'
        '<div class="cms-note">&#10003; Filters and hub pages update automatically</div></div>'
        '<div><div class="cms-seo"><h6>SEARCH APPEARANCE</h6>'
        '<div class="cms-f"><small>SEO TITLE</small><div>One Event Sponsorship, Six Months of Content</div></div>'
        '<div class="cms-f"><small>META DESCRIPTION</small><div style="font-size:.7em">Badge scans and a tote bag are the standard souvenir from sponsoring an event. Here is how to get six months of content instead.</div></div>'
        '<div class="cms-count">142 / 155</div>'
        '<div class="cms-prev"><b>How to Turn One Event Spons...</b><small>content10x.com &rsaquo; blog &rsaquo; repurposing</small>'
        '<p>Badge scans and a tote bag are the standard souvenir from sponsoring an event...</p></div></div>'
        '<div class="cms-pub"><span>Schedule for 4 Oct, 09:00</span><span>Author &middot; Amy Woods</span><span>Status &middot; Needs review</span></div></div></div></div></div>',
        nav=False, caption='The editor your team opens every week. Niche and format are fields, not free text, which is why the filters can never fall out of date.')

def mk_redirects():
    rows = [('/blog/old-podcast-post-2019', 'Podcasting hub', 'niche hub'),
            ('/blog/repurposing-tips-part-1', 'The complete repurposing guide', 'merged'),
            ('/blog/how-we-use-tool-x', 'Content operations hub', 'closest match'),
            ('/blog/2018-benchmarks-report', 'Measurement and ROI hub', 'niche hub')]
    rs = ''.join(f'<div class="rd-r"><code>{a}</code><span class="p">301</span><span><b>{b}</b><small>{c}</small></span></div>' for a, b, c in rows)
    return frame('content10x.com/redirect-map',
        '<div class="rd"><div class="rd-h"><span>OLD URL</span><span style="text-align:center">REDIRECT</span><span>NEW DESTINATION</span></div>' + rs +
        '<div class="rd-safe"><span>Removed posts go to draft, never deleted</span><span>Full crawl for broken links</span><span>Sitemap resubmitted</span><span>Search Console watched for two weeks</span></div></div>',
        nav=False, cursor=False, caption='Every URL keeps a destination. Nothing is deleted outright, so any decision can be reversed.')

NICHES = [('B2B Content Strategy', 'Goals, messaging, positioning, channels, competitors', '#2F62FF'),
          ('Repurposing &amp; Distribution', 'One asset into many, distribution systems', '#34C7A1'),
          ('B2B Podcasting', 'Show strategy, guests, production, programmes', '#FF8A4C'),
          ('Employee Led &amp; Social', 'LinkedIn, advocacy, founder led content', '#B48CFF'),
          ('AI &amp; Search', 'AI search, zero click, SEO shifts, AI workflows', '#0EA5E9'),
          ('Content Operations &amp; Team', 'Team structure, workflows, tooling, benchmarks', '#F4B740'),
          ('Measurement &amp; ROI', 'Metrics, attribution, reporting, contribution', '#FF6B8A'),
          ('Your eighth, if needed', 'The final list is agreed in the audit', '#94A3B8')]

def mk_niches():
    g = ''.join(f'<div style="--c:{c}">{n}<small>{d}</small></div>' for n, d, c in NICHES)
    tags = [('Format tags', ['Podcast episode', 'Guide', 'How to', 'Interview', 'Framework', 'Industry news', 'Template']),
            ('Industry tags', ['SaaS', 'Professional services', 'Agencies', 'Technology', 'Finance']),
            ('Stage tags', ['Getting started', 'Scaling', 'Advanced'])]
    t = ''.join('<p><b>' + n + '</b>' + ''.join(f'<span>{x}</span>' for x in xs) + '</p>' for n, xs in tags)
    return frame('content10x.com/content-structure',
        f'<div class="nch"><div class="nch-g">{g}</div><div class="nch-t">{t}</div>'
        '<p style="font-size:.72em;color:#667085;margin-top:.8em">Every post gets one primary niche, and any number of format, industry and stage tags. '
        'The niche drives the filters and the hub pages. The tags drive everything finer grained.</p></div>',
        nav=False, cursor=False, caption='The starting proposal for the structure, based on what is published today. The final list is decided together in the audit.')

def mk_audit():
    rows = [('/blog/repurposing-guide', 'The Complete Guide to Repurposing', '4,120', 'Keep', 'st-keep'),
            ('/blog/webinar-repurposing', '12 Ways to Repurpose a Webinar', '2,880', 'Keep', 'st-keep'),
            ('/blog/tools-2022', 'Our Favourite Tools in 2022', '310', 'Update', 'st-upd'),
            ('/blog/repurposing-tips-part-1', 'Repurposing Tips, Part 1', '95', 'Merge', 'st-mrg'),
            ('/blog/old-event-post-2018', 'Event Recap, 2018', '12', 'Remove', 'st-rem')]
    rs = ''.join(f'<tr class="late"><td>{u}</td><td>{t}</td><td>{v}</td><td><span class="st {c}">{s}</span></td></tr>' for u, t, v, s, c in rows)
    return frame('content10x.com/audit-spreadsheet',
        '<div class="sht"><div class="sht-top"><b>Blog audit &middot; 350+ posts</b>'
        '<span class="st st-keep">Keep 168</span><span class="st st-upd">Update 54</span><span class="st st-mrg">Merge 38</span><span class="st st-rem">Remove 94</span></div>'
        f'<table><thead><tr><th>URL</th><th>Title</th><th>12 month views</th><th>Decision</th></tr></thead><tbody>{rs}</tbody></table>'
        '<p style="font-size:.72em;color:#667085;margin-top:.6em">Every decision carries a one line reason, so the list is reviewable before anything changes.</p></div>',
        nav=False, cursor=False, caption='The audit spreadsheet is yours to keep, with performance data and a decision on every post.')

def mk_phone():
    return ('<div class="mk-phone"><div class="scr"><b>The Blog</b>'
            '<div class="fil"><span>All</span><span class="on">Podcasting</span><span>Strategy</span><span>AI</span></div>'
            '<div class="c"><em>PODCAST</em><i>Season planning for a B2B show</i></div>'
            '<div class="c"><em>GUIDE</em><i>Booking guests buyers want</i></div>'
            '<div class="c"><em>HOW-TO</em><i>One episode into ten assets</i></div></div></div>')

# ---------------------------------------------------------------- shared page parts
# ------------------------------------------------- answers to Amy's questions

MONTHS = ['Jun 25', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan 26', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
HEIGHTS = [38, 44, 41, 52, 61, 58, 44, 66, 71, 64, 58, 69, 74, 70, 63, 72]


def mk_window():
    bars = ''.join(
        '<div class="w16-b" style="--h:%d%%;--d:%dms"><i></i><span>%s</span></div>' % (h, i * 55, m)
        for i, (m, h) in enumerate(zip(MONTHS, HEIGHTS)))
    rows = ''.join(
        '<div class="w16-r"><b>%s</b><span>%s</span></div>' % (a, b) for a, b in [
            ('Clicks', 'How many people arrived from search'),
            ('Impressions', 'How often it appeared in results'),
            ('Average position', 'Where it ranks for its main queries'),
            ('Top queries', 'What people were actually looking for')])
    return frame('search.google.com/search-console',
        '<div class="mk-page"><div class="mk-h1" style="font-size:1.5em">Performance, last 16 months</div>'
        '<div class="mk-sub">Every post exported with its own numbers, the full window Search Console keeps.</div>'
        '<div class="w16">' + bars + '</div>'
        '<div class="w16-lb"><span>16 months is everything Google holds</span><span>Sep 2026</span></div>'
        '<div class="w16-grid">' + rows + '</div></div>', cursor=False, nav=False,
        caption='Sixteen months of real search data per post. Anything older is judged on what it says, not on numbers that no longer exist.')


def sc_row(name, score, tone, note):
    return ('<div class="sc-r"><div class="sc-t"><b>%s</b><span class="sc-p %s">%s</span></div>'
            '<div class="sc-bar"><i class="%s" style="--w:%s"></i></div><small>%s</small></div>'
            % (name, tone, score, tone, score.split('/')[0].strip() + '0%', note))


def mk_test():
    return frame('content10x.com/audit/post-1042',
        '<div class="mk-page"><span class="mk-tag">POST UNDER REVIEW</span>'
        '<div class="mk-h1" style="font-size:1.35em;margin-top:.35em">12 Ways to Repurpose a Webinar Recording</div>'
        '<div class="mk-sub">Published January 2020 &middot; 1,410 words &middot; 340 clicks in 16 months</div>'
        '<div class="sc">'
        + sc_row('Still relevant', '8/10', 'g', 'People still search this. 61 clicks last month, rising.')
        + sc_row('Quality today', '5/10', 'a', 'Thin in the middle, no examples, no images, reads like 2020.')
        + sc_row('How well it has aged', '3/10', 'r', 'Names three tools that no longer exist. Screenshots are old.')
        + '</div>'
        '<div class="sc-out"><span class="sc-dec">Decision: Update</span>'
        '<p>Traffic says keep it. Quality says rewrite the middle. Nothing about the URL changes, so nothing at risk.</p></div>'
        '</div>', cursor=False, nav=False,
        caption='Every post scored on the same three tests, with the evidence written next to the score. You sign off the list, not each post.')


def mk_flow():
    def lane(tag, tone, title, steps, note):
        li = ''.join('<li>%s</li>' % s for s in steps)
        return ('<div class="fl-l"><span class="mk-tag %s">%s</span><b>%s</b><ol>%s</ol>'
                '<small>%s</small></div>' % (tone, tag, title, li, note))
    return frame('content10x.com/audit/workflow',
        '<div class="mk-page"><div class="mk-h1" style="font-size:1.4em">What happens after the decision</div>'
        '<div class="mk-sub">Four outcomes, four routes. Two of them need you, two of them do not.</div>'
        '<div class="fl">'
        + lane('KEEP', 'g', 'Keep as it is', ['Tagged with its niche and formats.', 'Appears in the right filters and hub.', 'No writing needed.'], 'About half the posts land here.')
        + lane('UPDATE', 'a', 'Update in place', ['I list exactly what is wrong: old tools, missing examples, weak intro.', 'Your writer fixes those parts, or I do the structural edits and you approve.', 'Same URL, refreshed date, internal links added.'], 'You choose who writes. The list is specific, never "make it better".')
        + lane('MERGE', 'v', 'Merge into one', ['Two or three posts on the same question become one strong post.', 'The strongest URL survives and grows.', 'The others redirect into it with a 301, so their traffic follows.'], 'Nothing is thrown away. Sections are moved, not deleted.')
        + lane('REMOVE', '', 'Retire quietly', ['Checked for backlinks and traffic first.', 'Redirected to the closest hub, never left to 404.', 'Kept in the sheet in case you want it back.'], 'A post is only removed when nothing points at it.')
        + '</div></div>', cursor=False, nav=False,
        caption='Update and merge are the only two that need writing. You see the exact list of changes before anyone starts.')


def mk_tagging():
    chips = lambda items, cls='': ''.join('<span class="%s">%s</span>' % (cls if i == 0 else '', t) for i, t in enumerate(items))
    return frame('content10x.com/admin/post/1042',
        '<div class="mk-page"><div class="mk-h1" style="font-size:1.35em">How one post gets filed</div>'
        '<div class="mk-sub">One niche, then as many tags as it earns. Ten seconds per post, once.</div>'
        '<div class="tg">'
        '<div class="tg-r"><b>Niche</b><small>Pick one. This drives the filters and the hub page.</small>'
        '<div class="tg-c">' + chips(['Repurposing &amp; Distribution', 'B2B Podcasting', 'Content Strategy', 'AI &amp; Search'], 'on') + '</div></div>'
        '<div class="tg-r"><b>Format</b><small>What kind of thing is it, so the card can say so.</small>'
        '<div class="tg-c">' + chips(['How-to', 'Podcast episode', 'Guide', 'Interview', 'Framework'], 'on') + '</div></div>'
        '<div class="tg-r"><b>Industry</b><small>Only when the post is genuinely about one.</small>'
        '<div class="tg-c">' + chips(['SaaS', 'Agencies', 'Professional services', 'Not specific'], '') + '</div></div>'
        '<div class="tg-r"><b>Stage</b><small>Who it is for. Powers Start here lists.</small>'
        '<div class="tg-c">' + chips(['Getting started', 'Scaling', 'Advanced'], 'on') + '</div></div>'
        '</div>'
        '<div class="tg-out">This post now appears under Repurposing, in the How-to filter, and first in the Start here list for beginners.</div>'
        '</div>', cursor=False, nav=False,
        caption='The niche is a single choice, which is what keeps the navigation clean. Tags are generous, which is what makes search useful.')


def mk_design():
    sw = ''.join('<i style="background:%s"></i>' % c for c in ['#1B1F3B', '#3B5BDB', '#F5A524', '#F1F3F7', '#0B0D18'])
    return frame('figma.com/content10x-blog',
        '<div class="mk-page"><div class="mk-h1" style="font-size:1.35em">How the look gets decided</div>'
        '<div class="mk-sub">Three short rounds. You only ever choose between things you can see.</div>'
        '<div class="dz">'
        '<div class="dz-s"><span>ROUND 1</span><b>Direction</b><p>Two versions of the blog page, same content, different feel. You pick one and say what to change.</p></div>'
        '<div class="dz-s"><span>ROUND 2</span><b>The pieces</b><p>Card, filter bar, hub header, article page. Agreed one by one, so nothing is a surprise later.</p></div>'
        '<div class="dz-s"><span>ROUND 3</span><b>Sign off</b><p>Desktop and mobile, real posts in it, ready to build. After this the design does not move.</p></div>'
        '</div>'
        '<div class="dz-sys"><div class="dz-col"><small>YOUR COLOURS, KEPT</small><div class="dz-sw">' + sw + '</div></div>'
        '<div class="dz-col"><small>TYPE SCALE</small><div class="dz-ty"><b>Aa</b><span>Aa</span><em>Aa</em></div></div>'
        '<div class="dz-col"><small>CARD</small><div class="dz-card"><i></i><u></u><u class="s"></u></div></div></div>'
        '</div>', cursor=False, nav=False,
        caption='It stays inside the Content 10x brand. This is a tidy up of the blog, not a rebrand.')


def mk_after_post():
    rel = ''.join('<div class="pst-r"><span class="mk-tag %s">%s</span><b>%s</b></div>' % (t, g, n) for g, t, n in [
        ('GUIDE', 'g', 'The complete guide to B2B content repurposing'),
        ('HOW-TO', 'a', 'Turn one webinar into ten assets'),
        ('PODCAST', '', 'Season planning for a B2B show')])
    return frame('content10x.com/blog/repurposing/webinar-to-ten-assets',
        '<div class="mk-page"><div class="pst-crumb">Blog <span>/</span> Repurposing &amp; Distribution <span>/</span> How-to</div>'
        '<div class="mk-h1" style="font-size:1.4em">12 Ways to Repurpose a Webinar Recording</div>'
        '<div class="pst-meta"><span class="mk-tag a">HOW-TO</span><span>7 min read</span><span>Updated September 2026</span></div>'
        '<div class="pst-body"><u></u><u></u><u class="s"></u><u></u><u class="s"></u></div>'
        '<div class="pst-cta"><b>Get the next repurposing post by email</b><span>Subscribe</span></div>'
        '<div class="pst-h">Read next in Repurposing</div>' + rel +
        '</div>', cursor=False,
        caption='Every article now says which niche it belongs to, how long it takes, when it was last updated, and what to read next.')


def phase(num, label, title, intro, do, get):
    dl = ''.join(f'<li>{x}</li>' for x in do)
    gl = ''.join(f'<li>{x}</li>' for x in get)
    return f'''
  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>{num}</b> {label}</span><h2 class="split">{title}</h2><p>{intro}</p></div>
      <div class="g2">
        <div class="panel pad rev"><span class="kick"><b></b> What I will do</span><ul class="ticks" style="margin-top:20px">{dl}</ul></div>
        <div class="panel pad rev" style="background:linear-gradient(180deg,rgba(61,220,151,.07),var(--ink-900))"><span class="kick"><b></b> What you receive</span><ul class="ticks get" style="margin-top:20px">{gl}</ul></div>
      </div>
    </div>
  </section>'''

def cta(title, sub, primary='Book a call to talk it through', secondary=None):
    sec = f'<a class="btn btn-g btn-lg" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ''
    return f'''
  <section class="sec">
    <div class="wrap"><div class="panel pad rev" style="text-align:center;padding:64px 34px">
      <h2 class="split" style="font-size:clamp(26px,3vw,38px)">{title}</h2>
      <p style="color:var(--t2);margin:18px auto 0;max-width:56ch">{sub}</p>
      <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:28px"><a class="btn btn-p btn-lg" href="mailto:hello@example.com">{primary}</a>{sec}</div>
    </div></div>
  </section>'''

DOODLE = '<span class="doodle {cls}">{text} <svg class="dd-arrow" viewBox="0 0 90 60"><path d="M4 8 C 30 4, 60 14, 70 44"/><path d="M58 38 L 71 46 L 76 32"/></svg></span>'


def dd(text, cls=''):
    return DOODLE.format(cls=cls, text=text)


def opt_hero(num, dur, kind, title, word, lede, points):
    pl = ''.join(f'<span class="badge">{p}</span>' for p in points)
    return f'''
  <section class="sec" style="padding-top:140px">
    <div class="wrap">
      <nav class="kick rev" style="margin-bottom:22px"><a href="index.html" style="color:var(--t2)">Overview</a> <span style="color:var(--t3)">/</span> <span style="color:var(--t1)">Option {num}</span></nav>
      <div class="g2" style="align-items:center;gap:48px;position:relative">
        <div class="rev" style="position:relative">
          {dd('live in ' + dur, 'd-opt')}
          <span class="kick"><b>OPTION {num}</b> {dur} &middot; {kind}</span>
          <h1 class="split" style="font-size:clamp(32px,4vw,54px);margin:18px 0 0">{title}</h1>
          <p class="lede">{lede}</p>
          <div class="chips" style="margin-top:22px">{pl}</div>
        </div>
        <div class="rev">{word}</div>
      </div>
    </div>
  </section>'''

# ---------------------------------------------------------------- index
def index():
    probs = [('Search is the only way in', 'You have to already know what you are looking for before the blog can help you.'),
             ('A fixed popular strip', 'Hand picked, rarely updated, and the same for everyone who lands on the page.'),
             ('No categories or formats', 'A 40 minute podcast write up looks exactly like a 3 minute news post.'),
             ('Nothing to build on', 'No hub pages, no related posts, and no next step for the reader.')]
    pc = ''.join(f'<div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(probs))
    opts = [('1', 'Blog restructure', '2 to 3 weeks', 'Lowest risk &middot; Blog only',
             'Reorganise and improve the blog inside the current WordPress site. Nothing else changes.', 'option-1.html'),
            ('2', 'AI assisted new site', '3 to 4 weeks', 'Full rebuild &middot; New design',
             'A complete new website, built fast with AI assisted development, then reviewed and hardened by hand.', 'option-2.html'),
            ('3', 'Custom site and CMS', '30 days', 'Full rebuild &middot; Custom CMS',
             'Designed and built from scratch in 30 days, with a CMS shaped around how your team actually publishes.', 'option-3.html')]
    oc = ''.join(f'''<a class="opt" href="{h}"><span class="on">Option {n}</span><h3>{t}</h3><p>{d}</p>
      <div class="meta"><span class="badge acc">{dur}</span><span class="badge">{k}</span></div>
      <span class="go">See what is included {ARROW}</span></a>''' for n, t, dur, k, d, h in opts)
    rows = [('Scope', 'Blog section only', 'Entire website rebuilt', 'Entire website rebuilt'),
            ('Design', 'Current design stays, the blog page is improved', 'New modern design, created with AI assisted tools and refined by hand', 'Fully custom design created for the Content 10x brand'),
            ('How it is built', 'Current WordPress site, using trusted plugins and light custom code in a child theme', 'AI assisted development, then reviewed, tested and hardened by me', 'Hand built custom code with a planned, documented structure'),
            ('Editing content', 'The same WordPress editor your team already uses', 'Simple content editing set up so your team does not need code', 'Custom CMS with editable templates and blocks built around your workflow'),
            ('Blog organisation', 'Audit, niches, tags and filters', 'Included, so content arrives already organised', 'Included, so content arrives already organised'),
            ('Search rankings', 'Lowest risk, as only the blog changes', 'Protected with full URL mapping and 301 redirects', 'Protected with full URL mapping and 301 redirects'),
            ('Existing tools', 'Keep working as they are', 'Rebuilt and retested', 'Rebuilt and retested'),
            ('Team training', 'Written tagging guide', 'Written guide and walkthrough', 'Live training session and full documentation'),
            ('Indicative timeline', '2 to 3 weeks', '3 to 4 weeks', '30 days'),
            ('Post launch support', '2 weeks', '2 weeks', '2 weeks'),
            ('Best for', 'Fixing the blog quickly, with minimal change and minimal risk', 'A full refresh with a lighter scope and a faster turnaround', 'A complete, long term website built exactly for your team')]
    tr = ''.join('<tr><th>' + r[0] + '</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rows)
    onames = [('Blog restructure', 'OPTION 1'), ('AI assisted new site', 'OPTION 2'), ('Custom site and CMS', 'OPTION 3')]
    cmpm = ''
    for i, (nm, lb) in enumerate(onames):
        dl = ''.join(f'<div class="cm-r"><dt>{r[0]}</dt><dd>{r[i+1]}</dd></div>' for r in rows)
        cmpm += f'<div class="cm-card"><span class="kick"><b>0{i+1}</b> Option {i+1}</span><h3>{nm}</h3><dl>{dl}</dl><a class="go" href="option-{i+1}.html">See what is included {ARROW}</a></div>'
    need = [('Access', ['Admin or editor access to WordPress.', 'Read access to Google Analytics and Google Search Console.', 'A staging site if one exists, or approval to work on the live site after a full backup, for Option 1.']),
            ('Materials for Options 2 and 3', ['Brand assets: logo files, fonts, colours, imagery and any brand guidelines.', 'A list of must have pages and integrations.']),
            ('Decisions', ['Sign off on the niche and tag structure at the end of the audit.', 'Sign off on the keep list: the 150 to 200 posts that stay.', 'Sign off on the design direction before build begins, for Options 2 and 3.']),
            ('People', ['One point of contact for quick answers and feedback, ideally within two working days.', 'For Option 3, whoever publishes each week available for the Week 2 content model conversation and the Week 4 training.'])]
    nc = ''.join(f'<div class="panel pad"><span class="kick"><b></b> {t}</span><ul class="ticks" style="margin-top:18px">' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul></div>' for t, xs in need)
    return f'''
  <section class="sec" style="padding-top:150px">
    <div class="wrap">
      <div class="g2" style="align-items:center;gap:52px">
        <div class="rev">
          <span class="kick"><b>PROPOSAL</b> Prepared for Content 10x &middot; September 2026</span>
          <h1 class="split" style="font-size:clamp(34px,4.4vw,60px);margin:20px 0 0">Website and blog proposal: {sq('three options')}.</h1>
          <p class="lede">The Content 10x blog holds over 350 posts in one continuous list, with a search box as the only way in. This proposal sets out three ways to fix that, from a focused blog restructure to a fully custom website, with <mark>the same underlying content structure in all three</mark>, so nothing is ever done twice.</p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:26px"><a class="btn btn-p btn-lg" href="#options">See the three options</a><a class="btn btn-g btn-lg" href="#compare">Compare side by side</a></div>
          <p style="margin-top:18px;color:var(--t3);font-size:14.5px">Prepared by Nisarg Mehta</p>
        </div>
        <div class="rev">{mk_blog_today()}</div>
      </div>
    </div>
  </section>

  <section class="sec" id="problem">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>01</b> The problem</span><h2 class="split">What a visitor meets today.</h2>
        <p>Podcast episode write ups, long form guides and industry commentary all sit in the same undifferentiated list. A reader who came for B2B podcasting has no way to see only podcasting. A reader who came from a Google result has no obvious second thing to read.</p></div>
      <div class="g4 stag">{pc}</div>
      <p class="rev" style="color:var(--t2);margin-top:26px;max-width:70ch">The same problem shows up in search. When 350 posts share no structure, search engines have nothing to tell them which topics this site is genuinely an authority on. <mark>The signal is spread thin</mark> across everything instead of concentrated where it should be.</p>
    </div>
  </section>

  <section class="sec" id="foundation">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>02</b> Shared foundation</span><h2 class="split">The content structure, agreed once.</h2>
        <p>Every option starts from the same piece of work: an audit of all 350+ posts, and a niche structure agreed with you. This is the part that actually fixes the problem. The rest is how far the site around it changes.</p></div>
      <div class="rev">{mk_niches()}</div>
      <div class="g2" style="margin-top:56px;align-items:center;gap:40px">
        <div class="rev">{mk_audit()}</div>
        <div class="rev"><span class="kick"><b></b> How the audit works</span>
          <h3 style="font-size:clamp(22px,2.4vw,30px);margin:16px 0 14px">Every post gets a decision, with a reason.</h3>
          <p style="color:var(--t2)">All 350+ posts are exported with 12 months of performance data, then reviewed against three tests: is it still relevant, is the quality up to today's standard, and how badly has it dated. Each post is marked Keep, Update, Merge or Remove, and posts carrying meaningful backlinks or traffic are flagged so no URL is ever removed without a deliberate redirect.</p>
          <div class="chips" style="margin-top:20px"><span>One primary niche per post</span><span>Format, industry and stage tags</span><span>Signed off before anything changes</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="sec" id="options">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>03</b> The three options</span><h2 class="split">Three ways to fix it.</h2>
        <p>They can be chosen on their own, or staged one after another. Each one includes the shared foundation above.</p></div>
      <div class="opts stag" style="position:relative">{dd('most start here', 'd-first')}{oc}</div>
    </div>
  </section>

  <section class="sec" id="compare">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>04</b> At a glance</span><h2 class="split">The three options, side by side.</h2></div>
      <div class="cmp rev"><table><thead><tr><th>&nbsp;</th>
        <th>Blog restructure<small>OPTION 1</small></th><th>AI assisted new site<small>OPTION 2</small></th><th>Custom site and CMS<small>OPTION 3</small></th></tr></thead>
        <tbody>{tr}</tbody></table></div>
      <div class="cmp-m stag">{cmpm}</div>
      <p class="hint">Scroll the table sideways to compare all three.</p>
    </div>
  </section>

  <section class="sec" id="safety">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>05</b> In all three options</span><h2 class="split">Nothing loses its rankings.</h2>
        <p>The main risk in any restructure is losing the search traffic and backlinks that 350 posts have built up. That risk is handled the same way in all three options: <mark>no URL ever simply disappears</mark>.</p></div>
      <div class="rev">{mk_redirects()}</div>
    </div>
  </section>

  <section class="sec" id="need">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>06</b> From your side</span><h2 class="split">What I need from you.</h2></div>
      <div class="g2 stag">{nc}</div>
    </div>
  </section>

  <section class="sec" id="scope">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>07</b> Scope</span><h2 class="split">What is and is not included.</h2></div>
      <div class="ba rev">
        <div class="panel after"><h4>Included in all options</h4><ul>
          <li>Everything listed in the option chosen.</li>
          <li>Up to two rounds of revisions per phase, or per design stage for Options 2 and 3.</li>
          <li>Two weeks of post launch support.</li>
          <li>A written handover so nothing depends on me afterwards.</li></ul></div>
        <div class="panel before"><h4>Not included in any option</h4><ul>
          <li>Writing new content, or fully rewriting existing posts.</li>
          <li>Photography, video and custom illustration.</li>
          <li>Hosting, domains and paid plugin or software licences, agreed with you first.</li>
          <li>Ongoing maintenance or SEO work after the post launch support period.</li></ul></div>
      </div>
      <div class="panel pad rev" style="margin-top:22px">
        <span class="kick"><b></b> How the options fit together</span>
        <p style="color:var(--t2);margin-top:16px;max-width:76ch">Starting with Option 1 fixes the biggest problem quickly and at the lowest risk. The audit, the niche structure and the tagging it produces carry straight into a full website later. Options 2 and 3 include that same work, so <mark>nothing is ever paid for twice</mark>. Each option also stands entirely on its own.</p>
      </div>
    </div>
  </section>
''' + cta('Thank you for considering this.',
          'I am happy to adjust the scope or the phases to suit your priorities, including mixing parts of one option into another. If it would help, I can walk through any of the three on a call and show the blog structure applied to your real posts.',
          'Talk it through on a call', ('Start with Option 1', 'option-1.html'))

# ---------------------------------------------------------------- option 1
def option1():
    wins = [('One click per niche', 'Seven filter buttons, plus All. Each one is also its own page with its own URL.'),
            ('Search and filters combined', 'Search inside a niche, and filter by format. Popular or Latest.'),
            ('Format and time on every card', 'A reader with seven minutes can see what fits before clicking.'),
            ('A hub page per niche', 'Introduction, best posts, Start here and a call to action. A real landing page for each topic you own.'),
            ('A next step on every topic', 'Topic specific sign up instead of one generic footer form.')]
    wc = ''.join(f'<div class="card"><span class="num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(wins))
    body = opt_hero('1', '2 to 3 weeks', 'Blog only', f'Blog restructuring, inside the {sq("site you have")}.',
        mk_blog_new(),
        'All work stays inside the current WordPress site. Nothing else on the website changes. The blog is sorted into the agreed niches and reduced to <mark>the strongest 150 to 200 posts</mark>, so what remains is easy to browse and clearly about something.',
        ['Lowest risk', 'Blog section only', 'Current design stays', '2 weeks support after launch'])
    body += f'''
  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>01</b> What changes for a reader</span><h2 class="split">The same site, a blog that finally browses.</h2></div>
      <div class="g3 stag">{wc}</div>
      <div class="g2" style="margin-top:46px;align-items:center;gap:40px">
        <div class="rev">{mk_hub()}</div>
        <div class="rev"><span class="kick"><b></b> Hub pages</span><h3 style="font-size:clamp(22px,2.4vw,30px);margin:16px 0 14px">Each niche becomes a page worth landing on.</h3>
          <p style="color:var(--t2)">Seven filter buttons on the blog, and seven pages behind them. Each hub introduces the topic, lists the strongest posts, gives a Start here path for newcomers, and ends with a sign up that matches what the reader just read.</p>
          <div class="chips" style="margin-top:20px"><span>Own shareable URL</span><span>Start here list</span><span>Related posts</span><span>Topic matched sign up</span></div></div>
      </div>
    </div>
  </section>
  <section class="sec tight"><div class="wrap"><div class="panel pad rev" style="display:flex;gap:18px;flex-wrap:wrap;align-items:center;justify-content:space-between">
    <div><span class="kick"><b></b> How it is built</span><p style="color:var(--t2);max-width:64ch;margin-top:12px">Built with trusted WordPress plugins plus small pieces of custom code in a child theme, so it stays stable, fast and easy for your team to maintain, and survives future theme updates.</p></div>
    <div class="chips"><span>WordPress</span><span>Child theme</span><span>No page builder lock in</span></div>
  </div></div></section>
'''
    body += phase('02', 'Phase 01 &middot; Audit and structure', 'Understand what exists, then agree the structure.',
        'Decide what stays and lock the final structure before anything changes on the live site.',
        ['Get read access to WordPress, Google Analytics and Google Search Console.',
         'Export all 350+ posts into one spreadsheet: URL, title, publish date, author, current category, word count and content type.',
         'Add 12 months of performance data per post: page views, average time on page, search impressions, clicks, average position and referring domains.',
         'Review each post against three tests: is it still relevant, is the quality up to today\'s standard, and how badly has it dated.',
         'Assign each post a status of Keep, Update, Merge or Remove, with a one line reason so every decision is reviewable.',
         'Flag the posts carrying meaningful backlinks or search traffic, so those URLs are never removed without a deliberate redirect.',
         'Work through the niche and tag structure with you and lock it down.'],
        ['The full audit spreadsheet, yours to keep.',
         'A one page niche and tag structure for approval.',
         'The recommended list of 150 to 200 posts to keep, for your sign off.',
         'A short list of merge candidates: overlapping posts worth combining into one stronger piece.'])
    body += phase('03', 'Phase 02 &middot; Categorise, tag, clean up', 'Apply the structure, safely and reversibly.',
        'The approved structure goes onto the live site, and the blog is reduced to the chosen posts without losing a single link.',
        ['Take a full site backup, and work on a staging copy first if one is available.',
         'Create the final categories and tags in WordPress, including the format and industry tag sets.',
         'Assign one primary category and the right tags to every kept post.',
         'Merge overlapping posts, keeping the stronger URL and redirecting the other.',
         'Make light updates to outdated posts: titles, dates, dead links, old product names. Full rewrites are not included.',
         'Set up 301 redirects from every removed post to the most relevant remaining post or niche hub.',
         'Move removed posts to draft rather than deleting them, so anything can be brought back.',
         'Run a full broken link and error crawl after the changes, and resubmit the XML sitemap.'],
        ['Every remaining post categorised and tagged.',
         '150 to 200 posts live, and the rest redirected, not deleted.',
         'A redirect map showing exactly where each removed post now points.',
         'A clean crawl report: no broken links, no redirect chains.'])
    body += phase('04', 'Phase 03 &middot; Blog page experience', 'Make the blog easy and pleasant to browse.',
        'This is the part your readers actually see: filters, formats, hubs and a next step on every page.',
        ['Add niche filter buttons at the top of the blog page, one per niche plus All, each with its own shareable URL.',
         'Improve search so it can be combined with the niche and format filters.',
         'Show a format label on every card, with reading or listening time.',
         'Replace the fixed popular strip with a Popular and Latest toggle.',
         'Build a hub page for each niche: a short introduction, the best posts, and a call to action.',
         'Add a Start here section of 3 to 5 must read posts to each hub.',
         'Add related posts at the foot of every article, matched by niche and tags.',
         'Add a newsletter or download prompt to each niche page, so the offer matches the topic.',
         'Test on desktop, tablet and mobile, and check the page still loads fast with the new filtering.'],
        ['The updated blog page, live.',
         'A hub page for each of the niches.',
         'Related posts and topic matched sign up prompts.',
         'A short written guide for your team on categorising and tagging new posts.'])
    body += f'''
  <section class="sec tight"><div class="wrap"><div class="panel pad rev">
    <span class="kick"><b>+ 2 WEEKS</b> After launch</span>
    <p style="color:var(--t2);margin-top:14px;max-width:72ch">For two weeks I monitor Google Search Console for crawl errors and coverage drops, fix any broken redirects, and make small adjustments to the filters or tags as real usage shows what people click.</p>
  </div></div></section>
'''
    return body + cta('Option 1 fixes the biggest problem first.',
        'The audit, the niche structure and the tagging carry straight into a full website later, so nothing is ever done twice.',
        'Talk through Option 1', ('Compare all three', 'index.html#compare'))

# ------------------------------------------------ the transformation film

FILM_POSTS = [('How to Turn One Event Sponsorship Into Six Months of Content with Jillian Hoefer',
               'Badge scans and a tote bag are the standard souvenir from sponsoring an event. Jillian Hoefer walked away with six months of content instead.',
               'EPISODE 387', 'How to Turn One Event Sponsorship Into Six Months of Content', 'PODCAST', '', '38 min listen'),
              ('Zero-Click, AI Search, and the Last-Click Attribution Trap with Amanda Natividad',
               'A lot of marketers have made peace with zero click search by now. Then AI search showed up and raised the stakes again.',
               'EPISODE 382', 'Zero-Click, AI Search and the Attribution Trap', 'PODCAST', '', '41 min listen'),
              ('The Sales and Marketing Relationship: Why Most Teams Get It Wrong and How to Fix It',
               'Sales and marketing spend a lot of time talking about alignment. It is easy to agree that it matters. It is much harder to make it happen.',
               'EPISODE 381', 'The Sales and Marketing Relationship', 'PODCAST', '', '36 min listen'),
              ('How to Measure Your B2B Content Strategy (Without Drowning in Data)',
               'You can be four months into implementing a well built content strategy, with clear goals and a schedule you never miss, and still have no idea whether it is working.',
               'EPISODE 380', 'How to Measure Your B2B Content Strategy', 'FRAMEWORK', 'a', '9 min read'),
              ('Why Content Repurposing and Distribution Should Be Built Into Your B2B Content Strategy',
               'Repurposing has a reputation problem. Most people hear it and immediately think copy paste, checkbox marketing, the same LinkedIn post going out on six platforms.',
               'EPISODE 379', 'Why Repurposing Belongs In Your Strategy', 'HOW-TO', 'a', '7 min read'),
              ('How to Choose Your B2B Content Channels and Formats',
               'You do not have to be on every platform. Trying to be everywhere is the fastest way to dilute your content. And yet, that is often what happens.',
               'EPISODE 378', 'How to Choose Your Channels and Formats', 'GUIDE', 'g', '11 min read')]

FILM_POD = [('Should Your B2B Brand Start a Podcast?',
             'Before you book a studio or buy a microphone, there are four questions worth answering honestly about your audience and your team.',
             'EPISODE 340', 'Should Your B2B Brand Start a Podcast?', 'GUIDE', 'g', '9 min read'),
            ('Planning Your First Season, End to End',
             'A season needs a spine. Here is how we plan twelve episodes that build on each other instead of twelve one off conversations.',
             'EPISODE 344', 'Planning Your First Season', 'PODCAST', '', '38 min listen'),
            ('Turning One Episode Into Ten Assets',
             'The episode is the raw material, not the finished product. This is the exact list of what we make from every recording.',
             'EPISODE 351', 'One Episode Into Ten Assets', 'HOW-TO', 'a', '7 min read'),
            ('Booking Guests Your Buyers Want to Hear From',
             'Big names are easy to want and hard to convert. Here is how to pick guests your actual buyers would clear an hour for.',
             'EPISODE 356', 'Booking Guests Your Buyers Want', 'GUIDE', 'g', '11 min read'),
            ('Inside a Podcast Led Content Programme',
             'What it looks like when the show is the centre of the content engine rather than a side project nobody owns.',
             'EPISODE 361', 'Inside a Podcast Led Programme', 'INTERVIEW', '', '24 min listen'),
            ('Measuring a B2B Show Without Vanity Metrics',
             'Downloads are the easiest number to report and the least useful. These are the five we would track instead.',
             'EPISODE 366', 'Measuring a Show Without Vanity Metrics', 'FRAMEWORK', 'a', '8 min read')]

POPULAR = [('EPISODE 384', 'What is a B2B Content Strategy (And Why Does it Matter)?', ''),
           ('THE ULTIMATE GUIDE', 'Planning, Recording and Repurposing Expert Interviews', 'light'),
           ('EPISODE 376', 'Why Employee Led Content Is the Biggest B2B Advantage in 2026', 'red'),
           ('THE ULTIMATE GUIDE', 'Planning, Promoting and Repurposing B2B Webinars', 'light'),
           ('EPISODE 374', 'The Only Type of B2B How-To Guide Worth Creating', ''),
           ('EPISODE 372', 'Why Content Repurposing and Distribution Should Be Built In', '')]


def fm_cards(posts, ident):
    out = ''
    for i, (title, excerpt, ep, thumb, tag, tone, rt) in enumerate(posts):
        out += (f'<div class="fm-c" id="{ident}{i}"><span class="th"><em>{ep}</em><u>{thumb}</u></span>'
                f'<span class="tag {tone}">{tag}</span><b>{title}</b>'
                f'<span class="rt">{rt}</span><small>{excerpt}</small>'
                f'<span class="more">Read More</span></div>')
    return out


def fm_tiles():
    return ''.join(f'<div class="fm-t {cls}"><b>{title}</b><em>{ep}</em><i></i></div>' for ep, title, cls in POPULAR)


def film_stage():
    nav = ('<div class="fm-nav"><b>Content <em>10x</em></b><span>What we do</span><span>Industries</span>'
           '<span>Our work</span><span>Resources</span><span class="cta">Book a call</span></div>')
    fil = ('<div class="fm-fil" id="fil"><span class="on" id="fAll">All</span><span>Content Strategy</span>'
           '<span>Repurposing</span><span id="fPod">B2B Podcasting</span><span>Employee led</span>'
           '<span>AI &amp; Search</span><span>Measurement</span><span>Ops</span></div>')
    band = (f'<div class="fm-band"><i id="bSearch">Search the Content 10x Blog</i><span>{SEARCH}</span></div>')

    blog = (f'<div class="fm-v on" id="vBlog"><div class="fm-scroll" id="scroll">{nav}'
            '<div class="fm-top"><h1>The Content 10x Blog</h1>'
            '<p id="bSub">Over 350 blog posts on B2B content marketing, repurposing and distribution.<br>'
            'Discover a new post every 2 weeks.</p></div>'
            f'<div class="fm-pop" id="pop"><h3>Take a look at some of our most popular posts</h3>'
            f'<div class="fm-tiles">{fm_tiles()}</div></div>'
            '<div class="fm-all" id="bAll">All posts</div>'
            f'{band}{fil}'
            f'<div class="fm-grid" id="gA">{fm_cards(FILM_POSTS, "c")}</div>'
            '<div class="fm-start" id="bStart"><b>Start here: B2B Podcasting</b>'
            '<p>New to this topic? These five are the place to begin.</p>'
            '<span>Should your B2B brand start a podcast?</span><span>Planning your first season</span>'
            '<span>Turning one episode into ten assets</span></div></div></div>')

    hub = (f'<div class="fm-v" id="vHub"><div class="fm-scroll">{nav}'
           '<div class="fm-crumb">Blog <span>/</span> B2B Podcasting</div>'
           '<div class="fm-h1" style="margin-top:6px;color:#1F3C88">B2B Podcasting</div>'
           '<p class="lead">Everything we have published on planning, recording, repurposing and measuring a B2B show. '
           'Forty one posts, grouped so you can start anywhere.</p>'
           '<div class="fm-start in" style="margin-top:12px"><b>Start here</b>'
           '<p>Five posts, in order, if this is new to you.</p>'
           '<span>Should your B2B brand start a podcast?</span><span>Planning your first season</span>'
           '<span>Turning one episode into ten assets</span></div>'
           f'<div class="fm-grid" style="margin-top:14px">{fm_cards(FILM_POD[:3], "h")}</div>'
           '<div class="fm-sign"><b>Get the next podcasting post by email</b><span>Subscribe</span></div></div></div>')

    post = (f'<div class="fm-v" id="vPost"><div class="fm-scroll">{nav}'
            '<div class="fm-crumb">Blog <span>/</span> B2B Podcasting <span>/</span> How-to</div>'
            '<div class="fm-h1" style="margin-top:6px;font-size:20px;color:#1F3C88">Turning One Episode Into Ten Assets</div>'
            '<div class="fm-meta"><span class="tag a" style="font:600 9px var(--f-m);padding:3px 7px;border-radius:99px;'
            'background:#fdf3e0;color:#9a6712">HOW-TO</span><span>7 min read</span><span>Updated September 2026</span></div>'
            '<div class="fm-lines"><u></u><u></u><u class="s"></u><u></u><u></u><u class="s"></u></div>'
            '<div class="fm-sign"><b>Get the next podcasting post by email</b><span>Subscribe</span></div>'
            '<div class="fm-next"><h6>Read next in B2B Podcasting</h6><div class="fm-ngrid">'
            + ''.join(f'<div class="fm-c"><span class="th"><em>{ep}</em><u>{th}</u></span>'
                      f'<span class="tag {tone}" style="opacity:1;transform:none">{tag}</span>'
                      f'<b>{t}</b><span class="rt" style="display:block">{rt}</span></div>'
                      for t, ex, ep, th, tag, tone, rt in FILM_POD[3:6])
            + '</div></div></div></div>')

    return f'''
<div class="fm-cap" id="cap"></div>
<div class="fm-badge" id="badge"><span id="b1">Seven topics</span><span id="b2">Format and length on every card</span>
  <span id="b3">A hub per topic</span><span id="b4">Read next on every article</span></div>
<div class="fm-win"><div class="fm-bar"><i></i><i></i><i></i><div class="fm-url" id="url">content10x.com/blog</div></div>
  <div class="fm-body">{blog}{hub}{post}
    <span class="fm-note n1" id="n1">Six popular posts, then 350 in one list</span>
    <span class="fm-note n2" id="n2">Search is the only way in</span>
    <span class="fm-note n3" id="n3">A podcast looks the same as a guide</span>
  </div></div>
<div class="fm-cursor" id="tap"><span class="rp"></span></div>
'''


def film_script():
    parts = []
    for i, (t, ex, ep, th, tag, tone, rt) in enumerate(FILM_POD):
        at = round(3.9 + i * .16, 2)
        safe = t.replace("'", "")
        parts.append("[%s,0,html('#c%d b','%s')]" % (at, i, safe))
        parts.append("[%s,0,html('#c%d small','%s')]" % (at, i, ex.replace("'", "")))
        parts.append("[%s,0,html('#c%d .rt','%s')]" % (at, i, rt))
        parts.append("[%s,0,html('#c%d .th u','%s')]" % (at, i, th.replace("'", "")))
        parts.append("[%s,0,html('#c%d .th em','%s')]" % (at, i, ep))
        parts.append("[%s,0,cls('#c%d .tag','tag %s')]" % (at, i, tone))
        parts.append("[%s,0,html('#c%d .tag','%s')]" % (at, i, tag))
    swap = ','.join(parts)
    return """
<script src="assets/film.js?v=6"></script>
<script>
var view=D.view,add=D.add,rem=D.rem,move=D.move,press=D.press,type=D.type,html=D.html,cls=D.cls,style=D.style;
var SC=function(sel,pad){var el=document.querySelector(sel);return el?Math.max(0,el.offsetTop-(pad||70)):0;};
var GOTO=function(sel,pad){return function(){var s=document.getElementById('scroll');if(s)s.scrollTop=SC(sel,pad);};};
var STAGE = document.getElementById('filmStage').innerHTML;
document.getElementById('filmStage').remove();
var GLIDE=function(sel,pad){var from=null,to=null;return function(p){var s=document.getElementById('scroll');if(!s)return;
  if(from===null){from=s.scrollTop;to=SC(sel,pad);}s.scrollTop=from+(to-from)*(p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2);};};

D.scene('Your blog today','Six popular posts, a search box, then every post ever published in one long list.',9,[
 [0,0,view('vBlog')],[0,0,html('#url','content10x.com/blog')],[0,0,function(){var s=document.getElementById('scroll');if(s)s.scrollTop=0;}],
 [1,0,add('#n1')],[2.2,0,add('#n2')],
 [4,1.6,GLIDE('#gA',210)],
 [5.4,0,add('#n3')]]);

D.scene('Seven topics appear','The same posts, the same brand, grouped the way your readers think. Each topic gets its own address.',7,[
 [0,0,rem('#n1')],[0,0,rem('#n2')],[0,0,rem('#n3')],
 [0,0,GOTO('#pop',150)],
 [.5,0,add('#fil')],[.8,0,html('#bSub','Browse by topic, format or time. Or search inside a topic.')],
 [1.6,0,add('#b1','in')]]);

D.scene('Every card says what it is','Format and length on the card, so nobody opens a podcast expecting a five minute read.',7,[
 [0,1.2,GLIDE('#gA',86)],
 [.3,0,add('#c0','tagged')],[.5,0,add('#c1','tagged')],[.7,0,add('#c2','tagged')],
 [.9,0,add('#c3','tagged')],[1.1,0,add('#c4','tagged')],[1.3,0,add('#c5','tagged')],
 [2.2,0,add('#b2','in')]]);

D.scene('One click, one topic','The filter changes the page and the address, so a topic can be shared, linked and found in search.',9,[
 [0,1,GLIDE('#fil',120)],
 [1.2,1,move('#fPod')],[2.3,0,press('#fPod')],[2.5,0,cls('#fPod','pick')],[2.5,0,cls('#fAll','')],
 [2.6,0,html('#url','content10x.com/blog/podcasting')],[2.6,0,html('#bAll','41 posts in B2B Podcasting')],[3.4,1.2,GLIDE('#gA',86)],
 SWAP,
 [6.2,0,add('#bStart','in')]]);

D.scene('Each topic gets a home','A hub page that introduces the topic, points at the best five posts, and offers the sign up that matches.',7,[
 [.2,0,view('vHub')],[.2,0,html('#url','content10x.com/blog/podcasting')],[1.4,0,add('#b3','in')]]);

D.scene('And the article knows where it sits','Breadcrumb, format, reading time, the date it was updated, and what to read next inside the same topic.',7,[
 [.2,0,view('vPost')],[.2,0,html('#url','content10x.com/blog/podcasting/one-episode-ten-assets')],
 [1.6,0,add('#b4','in')]]);

D.init({ stage: STAGE, chapters: ['Today','Topics','Cards','Filter','Hub','Article'],
  note: 'A mock up of content10x.com/blog after Option 1, in your own brand, drawn in code.' });
</script>
""".replace('SWAP', swap)


def film_block():
    return f'''<div id="filmMount"></div>
    <div id="filmStage" hidden>{film_stage()}</div>'''



NOW_NEXT = [
    ('Finding a topic', 'A search box, and only if you already know the words to type.',
     'Seven topic filters at the top of the blog, each with its own page and address.'),
    ('Browsing', 'One list, newest first, 350 posts deep.',
     'Browse by topic, then narrow by format or reader stage.'),
    ('Knowing what a post is', 'A title and a thumbnail. A podcast looks like an article.',
     'Format and length on every card, so the choice is made before the click.'),
    ('Where a beginner starts', 'Nowhere in particular.',
     'A Start here list of three to five posts on every topic hub.'),
    ('After reading a post', 'Nothing follows. The reader leaves.',
     'Read next, matched to the same topic, at the foot of every article.'),
    ('The back catalogue', '350 posts, some excellent, some from 2018, all treated the same.',
     'Every post kept, updated, merged or retired, with a reason written next to it.'),
    ('Sign up prompts', 'One prompt, the same for everyone.',
     'The prompt matches the topic being read.'),
    ('Publishing a new post', 'Publish and hope it gets found.',
     'Publish, pick one niche, add tags. Ten seconds, and it files itself.'),
    ('Search rankings', 'Nothing at risk, and nothing improving either.',
     'Every URL kept or redirected, so rankings follow the content.'),
    ('The design', 'The blog page as it is today.',
     'Same brand, same colours. A tidier blog page, hub pages and article layout.'),
]


def now_next():
    rows = ''.join(
        f'<div class="nn-r"><div class="nn-l">{H.escape(label)}</div>'
        f'<div class="nn-a"><span class="nn-t">Right now</span><p>{H.escape(now)}</p></div>'
        f'<div class="nn-b"><span class="nn-t">After Option 1</span><p>{H.escape(nxt)}</p></div></div>'
        for label, now, nxt in NOW_NEXT)
    return f"""
  <section class="sec" id="nownext">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>06</b> Side by side</span>
        <h2 class="split">What changes, line by line.</h2>
        <p class="lede">Ten things a reader or your team runs into. On the left is today, on the right is the same thing after Option 1.</p></div>
      <div class="nn rev"><div class="nn-h"><span></span><span>Right now</span><span>After Option 1</span></div>{rows}</div>
    </div>
  </section>"""


def qblock(num, question, lede, paras, mock, points=None, pts_title='In practice'):
    body = ''.join('<p>%s</p>' % p for p in paras)
    pl = ''
    if points:
        pl = ('<div class="qa-pts"><h4>%s</h4><ul class="ticks">%s</ul></div>'
              % (pts_title, ''.join('<li>%s</li>' % p for p in points)))
    return f"""
  <section class="sec qa" id="q{num}">
    <div class="wrap">
      <div class="qa-h rev"><span class="kick"><b>{num}</b> Your question</span>
        <h2 class="split">{question}</h2>
        <p class="lede">{lede}</p></div>
      <div class="qa-b rev"><div class="qa-copy">{body}{pl}</div></div>
      <div class="rev">{mock}</div>
    </div>
  </section>"""


def answers():
    body = f'''
  <section class="hero">
    <div class="wrap">
      <span class="kick"><b>01</b> Option 1, in detail</span>
      <h1 class="split">Your questions, {sq('answered')} one at a time.</h1>
      <p class="lede">You asked exactly the right things. Below is how each part actually works, with a picture of it
      rather than a promise. Nothing here changes the shape of Option 1, it is the same work described properly.</p>
      <div class="chips" style="margin-top:26px">
        <span><a href="#q01">Data window</a></span><span><a href="#q02">The three tests</a></span>
        <span><a href="#q03">Filters and categories</a></span>
        <span><a href="#q04">Design process</a></span><span><a href="#q05">What it will look like</a></span>
      </div>
    </div>
  </section>
'''

    body += qblock('01', 'How far back does the data go?',
        'Sixteen months, because that is everything Google keeps. Older posts are judged on what they say, not on numbers nobody has.',
        ['Search Console holds sixteen months of performance history and no more. Every post in the audit gets its own row of that '
         'data: clicks, impressions, average position and the queries people actually used to find it.',
         'That window is enough to see the thing that matters, which is direction. A post from 2018 that still picks up steady '
         'clicks today is earning its place. A post from last year that has never been found is not.',
         'If Google Analytics goes back further on your side, I will use it, and it makes the picture richer. If it does not, '
         'nothing is lost. Posts with no numbers are still read and judged on relevance and quality, and I will tell you plainly '
         'when a decision is based on judgement rather than data.'],
        mk_window(),
        ['Every post gets its own performance row, exported once at the start.',
         'Posts with meaningful backlinks are flagged separately, whatever their traffic.',
         'Anything older than the window is marked so you can see which calls were made on judgement.'])

    body += qblock('02', 'What are the relevance, quality and dated tests?',
        'Three questions asked of every post, in the same order, with the evidence written down next to the answer.',
        ['<b>Still relevant.</b> Does anyone still want this? Search demand for the topic, the clicks the post gets now, '
         'and whether the question it answers is still a question your buyers ask.',
         '<b>Quality today.</b> Held against what you would publish this week, not against 2019. Depth, examples, structure, '
         'whether it reaches a point, and whether it sounds like Content 10x.',
         '<b>How well it has aged.</b> Your dated test, scored the other way up so a low number always means trouble. Named tools '
         'that have changed or closed, screenshots of old interfaces, statistics with a year in them, advice that is simply no longer '
         'true. This is the test that decides how much work an update really is.',
         'The three answers together give the decision. High relevance with low quality means update. Low relevance with high '
         'quality usually means merge into something stronger. Low on all three means retire.'],
        mk_test(),
        ['You see the scores and the reason, not just the verdict.',
         'Anything I am unsure about is marked for your call rather than decided quietly.',
         'You sign off the whole list once, before a single post is touched.'])

    body += qblock('03', 'How do the filters and categories get decided?',
        'You pick the seven niches, I file every post against them. One niche per post, then as many tags as it earns.',
        ['The niches come out of the audit, not out of my head. Once 350 posts are in a sheet with their topics visible, the natural '
         'groupings are obvious, and I bring you a proposed list with the post count in each. You cut, rename and merge until it '
         'sounds like Content 10x. That list is then fixed, because the navigation depends on it.',
         'Each post gets exactly one niche. That single choice is what keeps the blog easy to browse, because a post can only ever '
         'live in one place. It is also what makes the hub pages possible.',
         'Tags are different. A post can carry as many as it deserves: the format, the industry if it is genuinely about one, and the '
         'stage the reader is at. Tags power the finer filtering and the Start here lists, and they never affect the main navigation, '
         'so you can add new ones later without anything breaking.',
         'Your team gets a one page guide so new posts are filed the same way, which is the part that keeps this from drifting in six months.'],
        mk_tagging(),
        ['You approve the niche list before any post is filed.',
         'One niche per post, unlimited tags.',
         'A written guide for your team, so new posts land in the right place.'])

    body += qblock('04', 'What is the design process for the theme?',
        'Three short rounds, and you only ever choose between things you can see on screen.',
        ['This is a tidy up of the blog inside your current site, so your brand does not change. Same colours, same logo, same voice. '
         'What changes is the blog page, the hub pages and the article layout.',
         'Round one is direction: two versions of the blog page with your real posts in them, different in feel but both recognisably '
         'Content 10x. You pick one and tell me what to change.',
         'Round two is the pieces: the post card, the filter bar, the hub header and the article page, agreed one at a time so nothing '
         'is a surprise at the end.',
         'Round three is sign off: desktop and mobile, real content, ready to build. After that the design stops moving, which is what '
         'keeps the two to three weeks honest.'],
        mk_design(),
        ['Nothing is designed in isolation, every screen uses your real posts.',
         'Mobile is designed at the same time, not adapted afterwards.',
         'Once signed off, the design is frozen so the build can be predictable.'])

    body += qblock('05', 'Can I see an example of the finished result?',
        'Rather than show you somebody else, here is your own blog after the work, drawn out screen by screen.',
        ['Past work for other clients would tell you how their site looks. This tells you how yours will. Every screen below uses '
         'your real post titles, your topics and your structure, laid out the way it would be on the day this goes live.',
         'Better than watching it, <a href="blog/" style="color:var(--acc);font-weight:600">open the working prototype</a> and use it. '
         'Filter by topic, search inside a topic, open a post, follow Read next. It runs in your browser with dummy posts in place of '
         'your real ones, and every filter changes the address bar exactly as it would on the live blog.',
         'Three things change for a reader. They can browse by topic instead of scrolling. They land on a hub that tells them where '
         'to start. And at the end of any article they are told what to read next, inside the same topic.'],
        film_block(),
        ['The blog page, with one filter per niche and search inside a topic.',
         'A hub page per niche, with a Start here list.',
         'An article page that says what it is, how long it takes, and what comes next.'])

    body += f'''
  <section class="sec" style="padding-top:0"><div class="wrap">
    <div class="rev">{mk_hub()}</div>
    <div class="rev" style="margin-top:40px">{mk_after_post()}</div>
  </div></section>
'''

    body += '''
  <section class="sec" style="padding-top:0"><div class="wrap"><div class="panel pad rev" style="text-align:center;padding:46px 30px">
    ''' + dd('open it, it works', 'd-try') + '''
    <span class="kick" style="justify-content:center"><b></b> Better than a video</span>
    <h2 class="chrome-text" style="font-size:clamp(23px,2.6vw,32px);margin-top:14px">Open the prototype and use it yourself.</h2>
    <p style="color:var(--t2);margin:14px auto 0;max-width:60ch">Topic filters, search inside a topic, hub pages, an article page with
    Read next. Real behaviour, dummy posts, running in your browser.</p>
    <div class="hero-cta" style="justify-content:center;margin-top:24px">
      <a class="btn btn-p btn-lg" href="blog/">Open the working prototype</a>
      <a class="btn btn-g btn-lg" href="option-1.html">Back to Option 1</a></div>
  </div></div></section>
'''
    body += now_next()
    body += film_script()
    return body + cta('Happy to walk through any of this live.',
        'If something here does not match how your team works, that is useful to know before we start rather than after.',
        'Talk it through', ('Back to Option 1', 'option-1.html'))


# ---------------------------------------------------------------- investment

SOW = [
    ('The audit', [
        'Every post exported with 16 months of Search Console data.',
        'A decision on each one: keep, update, merge or retire, with the reason written next to it.',
        'Posts carrying backlinks or steady traffic flagged before any decision is made.',
        'The sheet is yours to keep, whatever you do next.']),
    ('The structure', [
        'Seven niches agreed with you, plus format, industry and stage tags.',
        'Every post filed in WordPress against that structure.',
        'Old and duplicate categories cleaned up, nothing left uncategorised.']),
    ('The blog, rebuilt', [
        'A new blog front page: featured posts, browse by category, series and latest articles.',
        'Topic filters, format and stage filters, and search that works inside a topic.',
        'Format and reading time on every card.',
        'Built inside your existing theme as a child theme, so the rest of the site is untouched.']),
    ('Category pages', [
        'A hub page for each niche with an introduction, the posts in it and a Start here list.',
        'A sign up prompt on each hub that matches the topic.']),
    ('Article pages', [
        'Breadcrumb, format label, reading time and the date it was last updated.',
        'Read next: three posts from the same topic, with images, at the foot of every article.']),
    ('Search safety', [
        'A full URL map before anything moves.',
        '301 redirects for every merged or retired post, so nothing 404s.',
        'Sitemap resubmitted and Search Console watched for two weeks after launch.']),
    ('Handover', [
        'A one page guide so your team files new posts the same way.',
        'A walkthrough call with whoever publishes each week.',
        'Two weeks of support after launch, included.']),
]

NOT_IN = [
    'Writing or rewriting posts. You get the exact list of what to change on each one, your team writes.',
    'A rebrand. Same logo, same colours, same voice.',
    'Changes to pages outside the blog, such as home, services or contact.',
    'A new CMS, new hosting or a migration. Everything stays on your WordPress.',
    'An ongoing SEO or content retainer after the two weeks of support.',
]

HOW = [
    ('A live link from day one',
     'You get a staging link the day we start. Every change appears there, so you are never waiting for a reveal or wondering where things are.'),
    ('A short call each week, and notes in between',
     'One scheduled catch up a week while the work runs, plus a written update whenever something lands. If you would rather have more, say so.'),
    ('Revisions are part of the price',
     'Within the scope on this page, changes cost nothing extra. No change requests, no hourly top ups, no invoices you did not expect.'),
    ('One point of contact',
     'You deal with me, start to finish. The person who scopes it is the person who builds it.'),
]

NEED = [
    'Admin access to WordPress, and read access to Search Console and Analytics.',
    'A staging site if you have one, or permission to work on live after a full backup.',
    'Sign off on the niche list and on the keep list, once each.',
    'One person who can answer a question within a couple of working days.',
]


def investment():
    sow = ''.join(
        f'''<div class="sow-b rev"><h3>{H.escape(title)}</h3><ul class="ticks">'''
        + ''.join(f'<li>{H.escape(x)}</li>' for x in items) + '</ul></div>'
        for title, items in SOW)
    notin = ''.join(f'<li>{H.escape(x)}</li>' for x in NOT_IN)
    how = ''.join(f'<div class="card"><h3>{H.escape(t)}</h3><p>{H.escape(b)}</p></div>' for t, b in HOW)
    need = ''.join(f'<li>{H.escape(x)}</li>' for x in NEED)

    return f'''
  <section class="hero">
    <div class="wrap">
      <span class="kick"><b>OPTION 1</b> Blog restructure</span>
      <h1 class="split">The {sq('investment')}, and what it covers.</h1>
      <p class="lede">Everything below is what you get for one number, on one timeline, with one person doing it.
      No hourly billing, no change requests, nothing added later.</p>
    </div>
  </section>

  <section class="sec tight">
    <div class="wrap">
      <div class="price rev">
        <div class="price-l">
          <span class="kick"><b></b> Total</span>
          <div class="price-n">&pound;3,600</div>
          <p>For the whole of Option 1: the audit, the structure, the rebuilt blog, the category pages, the article
          pages, the redirects and the handover. Two to three weeks, plus two weeks of support.</p>
        </div>
        <div class="price-r">
          <div class="pay">
            <span class="badge">Standard</span>
            <h3>50 now, 50 on launch</h3>
            <p>Half to start, half when the new blog goes live and you have signed it off.</p>
            <div class="pay-n">&pound;1,800 &middot; &pound;1,800</div>
          </div>
          <div class="pay best">
            <span class="badge acc">Paid up front</span>
            <h3>One payment, 5 percent off</h3>
            <p>If you would rather settle it in one go at the start.</p>
            <div class="pay-n">&pound;3,420</div>
          </div>
        </div>
      </div>
      <p class="tiny rev">Invoiced in pounds. Payment by bank transfer or Wise, whichever is easier for you.</p>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>01</b> What you get</span>
        <h2 class="split">Everything in the price, written out.</h2>
        <p class="lede">If it is on this list it is included. If it is not, it is on the short list below it.</p></div>
      <div class="sow stag">{sow}</div>
    </div>
  </section>

  <section class="sec tight">
    <div class="wrap">
      <div class="g2" style="gap:28px;align-items:start">
        <div class="panel pad rev">
          <span class="kick"><b></b> Not included</span>
          <ul class="nolist" style="margin-top:16px">{notin}</ul>
        </div>
        <div class="panel pad rev">
          <span class="kick"><b></b> What I need from you</span>
          <ul class="ticks" style="margin-top:16px">{need}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>02</b> How it runs</span>
        <h2 class="split">You will always know where it is.</h2></div>
      <div class="g2 stag" style="gap:18px">{how}</div>
    </div>
  </section>

  <section class="sec tight">
    <div class="wrap">
      <div class="panel pad rev">
        <span class="kick"><b>03</b> Timeline</span>
        <div class="tl" style="margin-top:20px">
          <div class="tl-i"><b>Week 1</b><p>Audit of all 350 plus posts, and the niche structure proposed for your sign off.</p></div>
          <div class="tl-i"><b>Week 2</b><p>The structure applied: categories, tags, merges and redirects, on staging.</p></div>
          <div class="tl-i"><b>Week 3</b><p>The new blog front page, category pages and article pages. Sign off, then live.</p></div>
          <div class="tl-i"><b>+ 2 weeks</b><p>Support: crawl errors, redirects, small adjustments once real traffic arrives.</p></div>
        </div>
        <p class="tiny" style="margin-top:18px">The clock starts when access and the go ahead land, not when the invoice does.</p>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="wrap">
      <div class="panel pad rev note-me">
        <span class="kick"><b></b> A personal note</span>
        <p>I would rather you see this being built than read about it afterwards. The staging link is live from day one,
        you will hear from me every week without chasing, and anything inside the scope above gets changed as many times
        as it needs, at no extra cost. If something turns out to be a bad idea halfway through, I will tell you rather
        than build it quietly.</p>
        <p style="margin-top:14px">If this sounds right, just reply by email or message me on LinkedIn and we can get started.</p>
        <div class="hero-cta" style="margin-top:26px">
          <a class="btn btn-p btn-lg" href="mailto:solviqodigital@gmail.com?subject=Content%2010x%20blog%20restructure">Email me</a>
          <a class="btn btn-g btn-lg" href="answers.html">Back to your questions</a>
        </div>
      </div>
    </div>
  </section>
'''


# ---------------------------------------------------------------- option 2
def option2():
    body = opt_hero('2', '3 to 4 weeks', 'Full rebuild', f'A new website, built fast and then {sq("hardened by hand")}.',
        mk_home(),
        'A complete new website for Content 10x, built faster by using AI assisted development tools for the heavy lifting. Every page and every line of code is then reviewed, tested and hardened by hand, so the result is <mark>a reliable business website and not a quick prototype</mark>. The blog audit and niche structure from Option 1 are included here, so content moves across already organised.',
        ['New design', 'Whole site rebuilt', 'Blog organised from day one', '2 weeks support after launch'])
    body += f'''
  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>01</b> What you get to see</span><h2 class="split">A new site, and a blog organised from day one.</h2>
        <p>Indicative layouts. The real design direction, meaning look, feel, colours and typography, is agreed with you in Phase 1 before anything is built.</p></div>
      <div class="g2" style="gap:30px;align-items:start">
        <div class="rev">{mk_blog_new()}</div>
        <div class="rev">{mk_ds()}</div>
      </div>
    </div>
  </section>
'''
    body += phase('02', 'Phase 01 &middot; Discovery and content mapping', 'Agree exactly what the new site contains.',
        'Nothing is built until the sitemap, the integrations list and the design direction are signed off.',
        ['Crawl the current site and list every page, form, tracking tag and integration that must carry over: Google Analytics, Tag Manager, the LinkedIn pixel, contact and lead forms, podcast players and email sign ups.',
         'Agree the sitemap and page structure with you, including what to drop.',
         'Agree a design direction: look and feel, colours, typography, and reference sites you like.',
         'Decide how your team will edit content, and confirm the CMS approach.',
         'Run the full blog audit and niche structure from Option 1, so all content moves across already organised.'],
        ['The agreed sitemap.', 'An integrations checklist: everything that must still work on launch day.',
         'The audit spreadsheet and approved niche structure.', 'A written design direction to sign off.'])
    body += phase('03', 'Phase 02 &middot; Design and build', 'Produce the new website quickly.',
        'The design system comes first, so every page is consistent by construction rather than by luck.',
        ['Create the design system first: colours, fonts, buttons, cards and page layouts.',
         'Build the pages with AI assisted tools: homepage, service pages, industry pages, case studies, podcast, resources and blog.',
         'Build the new blog with niche filters, combined search, format labels and hub pages.',
         'Make every page responsive across desktop, tablet and mobile.',
         'Share progress for feedback as it goes, with up to two rounds of revisions.'],
        ['A live staging link, updated as pages are finished.',
         'Every page from the agreed sitemap, built and responsive.',
         'Two rounds of revisions on the design.'])
    body += phase('04', 'Phase 03 &middot; Review and hardening', 'The phase that separates a website from a prototype.',
        'Every generated file is read by hand, then the site is tested for security, speed, search and accessibility.',
        ['Read every generated file by hand and remove anything unnecessary, duplicated or unsafe.',
         'Run security checks on forms and any user input: validation, spam protection, and safe handling of submitted data.',
         'Tune performance against Core Web Vitals: compressed and correctly sized images, lazy loading below the fold, minimal blocking scripts.',
         'Set up the SEO fundamentals: page titles, meta descriptions, one H1 per page, heading order, image alt text, structured data for articles and podcast episodes, canonical tags and an XML sitemap.',
         'Check accessibility basics: colour contrast, readable text sizes, keyboard navigation, visible focus, and labels on every form field.',
         'Test across Chrome, Safari, Firefox and Edge, on desktop, tablet and phone, and test every form and tracking tag end to end.'],
        ['A written pre launch checklist, ticked off item by item.',
         'Performance and accessibility results, before and after.',
         'Confirmation that every form and tracking tag fires correctly.'])
    body += phase('05', 'Phase 04 &middot; Migration, launch and handover', 'Move everything across without losing rankings or leads.',
        'Launch happens at a time that suits your team, and the first days are watched closely.',
        ['Migrate the remaining content and match every old URL to a new one with 301 redirects, so no page is left without a destination.',
         'Reconnect analytics, Tag Manager, pixels, forms, email sign ups and podcast players, and verify each one.',
         'Go live at a time that suits your team, and watch closely over the first days.',
         'Resubmit the sitemap and monitor Search Console for crawl and coverage issues.',
         'Provide a written guide and a recorded walkthrough so your team can manage the site.'],
        ['A complete, live, responsive website.',
         'The blog organised into niches, with filters and hub pages.',
         'A redirect map from old URLs to new ones.',
         'A written guide and walkthrough for your team.',
         'Two weeks of post launch support.'])
    body += '''
  <section class="sec tight"><div class="wrap"><div class="panel pad rev">
    <span class="kick"><b></b> On content management</span>
    <p style="color:var(--t2);margin-top:14px;max-width:76ch">Your team will be able to add and edit blog posts, pages and key sections without touching code. The exact approach, a WordPress back end or a dedicated CMS, is agreed in Phase 1 based on what is easiest for the people who publish every week, not on what is fastest to build.</p>
  </div></div></section>
'''
    return body + cta('A full refresh, with a lighter scope.',
        'Most of the visible benefit of a custom build, sooner. If exact fit matters more than speed, Option 3 is the one to read next.',
        'Talk through Option 2', ('See Option 3', 'option-3.html'))

# ---------------------------------------------------------------- option 3
def option3():
    cust = [('Reusable page blocks', 'New pages are built by choosing and arranging blocks, with no developer needed.'),
            ('Dedicated content types', 'Posts, podcast episodes, guests, case studies and resources, each with its own simple form.'),
            ('Niche, format and industry fields', 'They power the blog filters automatically, so the structure can never drift out of date.'),
            ('Built in SEO fields', 'Character counts and a search preview, so titles and descriptions are never forgotten.'),
            ('Preview and scheduling', 'See a post exactly as it will appear, and schedule it to publish itself.'),
            ('Roles and permissions', 'Writers, editors and admins each see only what they need.'),
            ('Clear labels and help text', 'A new team member can learn it in an afternoon.')]
    cc = ''.join(f'<div class="card"><span class="num">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(cust))
    body = opt_hero('3', '30 days', 'Full rebuild and custom CMS', f'Designed from scratch, with a CMS {sq("shaped around you")}.',
        mk_cms(),
        'A website designed and developed from scratch specifically for Content 10x, delivered in 30 days, with a content management system customised around how your team actually works. The difference from Option 2 is not speed. It is fit: <mark>podcast episodes know they have guests</mark>, case studies know they have results, and the blog filters are powered by fields your team fills in without thinking about it.',
        ['Fully custom design', 'Custom CMS', 'Team training included', '2 weeks support after launch'])
    body += f'''
  <section class="sec">
    <div class="wrap">
      <div class="sec-h rev"><span class="kick"><b>01</b> The CMS</span><h2 class="split">Customisations that make it easy for your team.</h2>
        <p>Every field exists because it drives something on the front end: the filters, the hub pages, or the search listing.</p></div>
      <div class="g3 stag">{cc}</div>
    </div>
  </section>
  <section class="sec tight">
    <div class="wrap">
      <div class="g2" style="align-items:center;gap:40px">
        <div class="rev"><span class="kick"><b></b> Why this one, over Option 2</span>
          <h3 style="font-size:clamp(22px,2.4vw,30px);margin:16px 0 14px">Fit, not speed.</h3>
          <ul class="ticks" style="margin-top:8px">
            <li>The design is made for Content 10x, not adapted toward it.</li>
            <li>The CMS is modelled on your content, so publishing a podcast episode takes one form instead of a page built by hand.</li>
            <li>Guests, industries and case studies become real linked entities, so a guest page can list everything related to it automatically.</li>
            <li>The structure is documented, so any developer can pick it up later.</li>
          </ul>
          <p style="color:var(--t3);margin-top:16px;font-size:15.5px">If speed matters more than exact fit, Option 2 delivers most of the visible benefit sooner.</p>
        </div>
        <div class="rev">{mk_blog_new()}</div>
      </div>
    </div>
  </section>
'''
    body += phase('02', 'Week 01 &middot; Discovery and design foundations', 'Understand the business, the audience and the content.',
        'The week that sets the direction: what the site must do, and how it should look and feel.',
        ['Kick off call covering goals, audience, brand, and what is and is not working on the current site.',
         'Review every existing page and integration, and agree the sitemap.',
         'Run the blog audit and decide the niche structure with you.',
         'Create wireframes for the key page types: homepage, service, industry, case study, podcast and blog.',
         'Define the design system: colours, typography, spacing scale, buttons and components.'],
        ['Agreed sitemap and wireframes.', 'The audit spreadsheet and niche structure.', 'The design system, documented.'])
    body += phase('03', 'Week 02 &middot; Custom design and CMS planning', 'Finalise how it looks, and how content is structured behind it.',
        'This is where the CMS is modelled on your real content, with the people who publish every week in the room.',
        ['Design the key pages in full, for desktop and mobile.',
         'Run a feedback round and refine the designs.',
         'Model the content in the CMS: dedicated types for blog posts, podcast episodes, guests, case studies, industries and resources, each with only the fields it actually needs.',
         'Plan the reusable page blocks your team will use to build and edit pages without a developer.'],
        ['Full page designs for desktop and mobile.', 'A content model document: every type, every field.', 'The block library, listed and described.'])
    body += phase('04', 'Week 03 &middot; Development', 'Build the site and the CMS.',
        'The front end comes from the approved designs, and the CMS from the content model agreed in Week 2.',
        ['Develop the front end from the approved designs: fast, fully responsive, accessible.',
         'Build the CMS with the content types and page blocks planned in Week 2.',
         'Build the blog with niche filters, combined search, format labels, hub pages, Start here sections and related posts.',
         'Build forms, newsletter sign ups and lead capture, and connect the integrations.',
         'Add SEO fields to every page and post, with live character counts and a search preview.'],
        ['A staging site you can click through and comment on.', 'The CMS, populated with real sample content.'])
    body += phase('05', 'Week 04 &middot; Migration, testing and launch', 'Launch fast, tested and with rankings intact.',
        'Your team is trained before launch, and the first days are watched closely.',
        ['Migrate the remaining content and match every old URL to a new one with 301 redirects.',
         'Test across browsers and devices, check speed, security and accessibility, and test every form and tracking tag.',
         'Train your team with a live walkthrough and a written guide.',
         'Go live and monitor closely over the first days.',
         'Two weeks of post launch support for fixes and small adjustments.'],
        ['A fully custom designed, live website.',
         'A customised CMS set up around your content and workflow.',
         'The blog organised into niches, with filters and hub pages.',
         'A redirect map from old URLs to new ones.',
         'A team training session and written documentation.'])
    return body + cta('The long term option, built exactly for your team.',
        'Thirty days from kick off to a live site, with a CMS your team can run without a developer.',
        'Talk through Option 3', ('Compare all three', 'index.html#compare'))

PAGES = [('investment.html', 'Investment, Content 10x proposal', 'What Option 1 costs, what is included, how it is paid and how the work runs.', investment),
         ('answers.html', 'Your questions, answered, Content 10x proposal', 'How the audit, the tests, the update and merge process, the filters and the design rounds actually work, with a picture of each.', answers),
         ('index.html', 'Website and blog proposal for Content 10x', 'Three options to restructure the Content 10x blog and website, with one shared content structure.', index),
         ('option-1.html', 'Option 1: Blog restructuring, 2 to 3 weeks', 'Reorganise the blog inside the current WordPress site: audit, niches, filters and hub pages.', option1),
         ('option-2.html', 'Option 2: AI assisted new site, 3 to 4 weeks', 'A complete new website built fast with AI assisted development, then reviewed and hardened by hand.', option2),
         ('option-3.html', 'Option 3: Custom site and CMS, 30 days', 'A custom designed website with a CMS modelled on how your team publishes.', option3)]

for page, title, desc, fn in PAGES:
    (OUT / page).write_text(shell(page, title, desc, fn()), encoding='utf-8')
    print('wrote', page)
