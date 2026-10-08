"""Render a settlement JSON file to HTML per style/settlement.md.

Usage: python tools/render_settlement.py <settlement-id> [out.html]
NPC cards are pulled from airth/npcs/ and placed by `location`, then `found`, then `home`.
"""
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from npcref import build_index, md as npc_md

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "airth"

def md(s):
    s = html.escape(s or "")
    return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

def esc(s): return html.escape(s or "")

def load_settlements():
    return {p.stem: json.loads(p.read_text()) for p in (A / "settlements").glob("*.json")}

def npcs_for(sid):
    out = []
    for p in sorted((A / "npcs").glob("*.json")):
        d = json.loads(p.read_text())
        if d.get("home_settlement") == sid:
            out.append(d)
    return out

def place(npc, locations):
    if npc.get("location") in {l["id"] for l in locations}:
        return npc["location"]
    for key in ("found", "home"):
        norm = lambda t: (t or "").lower().replace("\u2019", "'")
        text = norm(npc.get(key))
        for loc in locations:
            name = norm(loc["name"])
            if name in text or name.removeprefix("the ") in text:
                return loc["id"]
    return None

def npc_card(n):
    name = esc(n["name"]) + (f", {esc(n['moniker'])}" if n.get("moniker") and n["moniker"] not in n["name"] else "")
    meta = " · ".join(x for x in [esc(n.get("role")), esc((n.get("faction") or "").replace("-", " "))] if x and x != "none")
    h = [f'<div class="npc"><p class="head"><span class="nm">{name}</span> <span class="meta">· {meta}</span></p>']
    look = esc(n.get("appearance"))
    if n.get("and_yet"): look += f" <em>And yet:</em> {esc(n['and_yet'])}"
    h.append(f"<p>{look}</p>")
    for s in n.get("sayings") or []: h.append(f'<p class="say">“{esc(s)}”</p>')
    run = [(k, n.get(f)) for k, f in [("Wants", "wants"), ("Doesn’t want", "does_not_want"), ("Knows", "knows"), ("Offers", "offers"), ("Found", "found")] if n.get(f)]
    h.append("<p>" + "<br>".join(f"<strong>{k}:</strong> {esc(v)}" for k, v in run) + "</p>")
    depth = [(k, n.get(f)) for k, f in [("Oddly also", "oddly_also"), ("Dreams", "dreams"), ("Thinks with", "thinks_with"), ("Family", "family")] if n.get(f)]
    stories = [("Anecdote", a) for a in n.get("anecdotes") or []] + [("Tragedy", t) for t in n.get("tragedies") or []]
    if n.get("dm_notes"): stories.append(("DM", n["dm_notes"]))
    if depth or stories:
        h.append('<div class="more">')
        if depth: h.append("<p>" + "<br>".join(f"<strong>{k}:</strong> {esc(v)}" for k, v in depth) + "</p>")
        for k, v in stories: h.append(f"<p><strong>{k}:</strong> {esc(v)}</p>")
        h.append("</div>")
    h.append("</div>")
    return "\n".join(h)

LABEL = lambda k: k.replace("_", " ").capitalize().replace("Passing through", "Who’s passing through")

def render(sid):
    S = load_settlements(); s = S[sid]
    out = []
    w = out.append
    w(f'<p class="sample-note">Rendered from <code>airth/settlements/{sid}.json</code> to <code>style/settlement.md</code>. Gaps in the data are shown in grey.</p>')
    draft = " (draft)" if s.get("status") in ("stub", "in_development") else ""
    w(f"<h1>{esc(s['name'])}{draft}</h1>")
    if s.get("tagline"): w(f'<p class="tagline">{esc(s["tagline"])}</p>')
    pop = s.get("population") or {}
    w('<div class="facts">')
    w(f"<p><strong>Inhabitants:</strong> {pop.get('total', '?')} ({esc(s.get('type','').replace('_',' '))}). {esc(pop.get('mix'))}</p>")
    for k, label in [("ruler", "Ruler"), ("strangers", "Strangers"), ("equipment", "Equipment")]:
        if s.get(k): w(f"<p><strong>{label}:</strong> {esc(s[k])}</p>")
        elif k == "equipment": w('<p class="gap"><strong>Equipment:</strong> not recorded.</p>')
    if s.get("faiths"): w(f"<p><strong>Faiths:</strong> {esc('; '.join(s['faiths']))}.</p>")
    w("</div>")
    p = s.get("palette")
    if p:
        w('<h2 class="section">Arrival</h2><div class="pal">')
        def row(name, items):
            items = list(items)
            if not items: return ""
            *plain, last = items
            parts = [esc(x) for x in plain] + [f"<em>{esc(last)}</em>"] if len(items) > 1 else [esc(last)]
            return f"<p><strong>{name}:</strong> " + " · ".join(parts) + "</p>"
        for ring in ["far", "near", "threshold", "within", "leaving"]:
            if p.get("constants", {}).get(ring): w(row(ring.capitalize(), p["constants"][ring]))
        w("</div>")
        bt = p.get("by_time") or {}
        if bt:
            w('<div class="table-wrap"><table class="grid"><thead><tr><th></th><th>Dawn</th><th>Day</th><th>Dusk</th><th>Night</th></tr></thead><tbody>')
            for ring in ["far", "near", "threshold", "within", "leaving"]:
                if ring in bt:
                    cells = "".join(f"<td>{' · '.join(esc(x) for x in bt[ring].get(t, []))}</td>" for t in ["dawn", "day", "dusk", "night"])
                    w(f"<tr><td>{ring.capitalize()}</td>{cells}</tr>")
            w("</tbody></table></div>")
        w('<div class="pal">')
        months = {"winter": "Voarn–Thunor", "spring": "Arkun–Ulkar", "summer": "Sarnath–Keltoi", "autumn": "Ragaia–Eshmun"}
        for season, items in (p.get("seasons") or {}).items():
            w(f"<p><strong>{season.capitalize()}</strong> <em>({months[season]})</em>: " + " · ".join(esc(x) for x in items) + "</p>")
        for sit in p.get("situations") or []:
            when = f" <em>({esc(sit['when'])})</em>" if sit.get("when") else ""
            w(f"<p><strong>{esc(sit['name'])}</strong>{when}: " + " · ".join(esc(x) for x in sit["descriptors"]) + "</p>")
        w("</div>")
    if s.get("itself"):
        w('<h2 class="section">What Makes It Itself</h2>')
        for i in s["itself"]:
            rule = f" <em>Rule:</em> {esc(i['rule'])}" if i.get("rule") else ""
            w(f"<p><strong>{esc(i['title'])}.</strong> {esc(i['text'])}{rule}</p>")
    enc = s.get("encounters")
    if enc:
        w('<h2 class="section">Encounters</h2>')
        for when in ["day", "night"]:
            w(f'<div class="table-wrap"><table><caption>d6 {esc(s["name"])} by {when}</caption><thead><tr><th class="die">d6</th><th>Encounter</th></tr></thead><tbody>')
            for i, e in enumerate(enc[when], 1): w(f'<tr><td class="die">{i}</td><td>{npc_md(e, *NPC_INDEX)}</td></tr>')
            w("</tbody></table></div>")
    r = s.get("response")
    if r:
        w('<h2 class="section">Response</h2>')
        for k, label in [("watch", "The watch"), ("arrival_day", "By day"), ("arrival_night", "By night"), ("reinforcements", "Reinforcements")]:
            if r.get(k): w(f"<p><strong>{label}:</strong> {esc(r[k])}</p>")
        strength = esc(r.get("strength_now") or "")
        if r.get("strength_founding"): strength += f" (founded with {esc(r['strength_founding'])})"
        if r.get("strength"): strength += f". {esc(r['strength'])}"
        w(f"<p><strong>Strength:</strong> {strength}</p>")
        w(f"<p><strong>Bribery:</strong> {esc(r['bribery'])}</p>" if r.get("bribery") else '<p class="gap"><strong>Bribery:</strong> not recorded.</p>')
    locs = s.get("locations") or []
    people = npcs_for(sid)
    placed = {}
    loose = []
    for n in people:
        lid = place(n, locs)
        (placed.setdefault(lid, []) if lid else loose).append(n)
    if locs:
        w('<h2 class="section">Places</h2>')
        for i, l in enumerate(locs, 1):
            w(f'<section class="loc"><h3><span class="num">{i}.</span>{esc(l["name"])}</h3>')
            w(f"<p>{esc(l['look'])}</p>")
            for k, v in (l.get("labels") or {}).items():
                cls = ' class="gap"' if "pending" in v else ""
                w(f"<p{cls}><strong>{LABEL(k)}:</strong> {esc(v)}</p>")
            if l.get("hidden"): w(f'<p class="hidden"><strong>Hidden:</strong> {esc(l["hidden"])}</p>')
            for n in placed.get(l["id"], []): w(npc_card(n))
            w("</section>")
    if loose:
        w('<h2 class="section">About Town</h2>')
        for n in loose: w(npc_card(n))
    legacy = s.get("npcs_legacy") or {}
    if legacy:
        w('<h2 class="section">Not Yet Converted</h2><p class="gap">Old-format NPC entries, shown briefly until converted.</p>')
        for k, n in legacy.items():
            w(f'<div class="npc"><p class="head"><span class="nm">{esc(n.get("moniker") or k)}</span> <span class="meta">· {esc(str(n.get("faction") or ""))}</span></p>'
              f"<p>{esc(n.get('appearance'))}</p><p><strong>Wants:</strong> {esc(n.get('wants'))}</p></div>")
    if s.get("factions"):
        w('<h2 class="section">Factions in Town</h2>')
        for f in s["factions"]:
            bits = [f"<em>{k.capitalize()}:</em> {esc(f[k])}" for k in ["purpose", "membership", "scheme"] if f.get(k)]
            w(f"<p><strong>{esc(f['id'].replace('-', ' ').title())}.</strong> " + " ".join(bits) + "</p>")
    if s.get("trouble"):
        w('<h2 class="section">Trouble</h2><ul>' + "".join(f"<li>{esc(t)}</li>" for t in s["trouble"]) + "</ul>")
    if s.get("neighbors"):
        w('<h2 class="section">Neighbors</h2><p>')
        lines = []
        for n in s["neighbors"]:
            other = S.get(n["settlement"], {"name": n["settlement"].title()})
            dirs = {"N": "north", "NE": "northeast", "E": "east", "SE": "southeast", "S": "south", "SW": "southwest", "W": "west", "NW": "northwest"}
            note = f" {esc(n['notes'])}" if n.get("notes") else ""
            lines.append(f"<strong>{esc(other['name'])}:</strong> {n['miles']:g} miles {dirs.get(n.get('direction'), '')} via {esc(n['path'].replace('-', ' '))}.{note}")
        w("<br>".join(lines) + "</p>")
    steads = [x for x in S.values() if x.get("parent") == sid]
    if steads:
        w('<h2 class="section">Steadings</h2>')
        for x in steads: w(f"<p><strong>{esc(x['name'])}</strong> ({esc(x.get('kind'))}): {esc(x.get('tagline'))} <em>Why here:</em> {esc(x.get('why_here'))}</p>")
    return "\n".join(out)

NPC_INDEX = build_index()
STYLE = (ROOT / "style" / "examples" / "dravesa.html").read_text()
HEAD = STYLE[: STYLE.index("<main>")]

if __name__ == "__main__":
    sid = sys.argv[1]
    S = load_settlements()
    head = re.sub(r"<title>.*?</title>", f"<title>{S[sid]['name']}</title>", HEAD, count=1)
    head = head.replace("</style>\n\n", ".hidden{border-left:2px solid var(--accent);padding-left:.6rem}\n</style>\n\n", 1) if ".hidden" not in head else head
    head = head.replace("</head>", "") + "<style>.npcref{font-variant:small-caps;letter-spacing:.03em}.npctag{color:var(--ink-soft)}</style>\n"
    body = "<main>\n" + render(sid) + "\n</main>\n"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "style" / "examples" / f"{sid}.html"
    out.write_text(head + body)
    print(out)
