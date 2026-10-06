"""Render a road encounter table to printable HTML (same look as settlement renders).

Usage: python tools/render_road.py <table-id> [out.html]
Category rows point at sub-tables: ones embedded in the file, or shared files in
airth/encounter_tables/. Every sub-table is printed, so the page stands alone.
"""
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from npcref import build_index, md as npc_md

ROOT = Path(__file__).resolve().parent.parent
T = ROOT / "airth" / "encounter_tables"

NPC_INDEX = build_index()

def md(s):
    return npc_md(s, *NPC_INDEX)

def load_tables():
    out = {}
    for p in T.glob("*.json"):
        d = json.loads(p.read_text())
        if d.get("id"):
            out[d["id"]] = d
    return out

def roll(r):
    return f"{r['roll']}–{r['roll_to']}" if r.get("roll_to") else str(r["roll"])

def table(t, caption):
    h = [f'<div class="table-wrap"><table><caption>{html.escape(t["die"])} {html.escape(caption)}</caption>'
         f'<thead><tr><th class="die">{html.escape(t["die"])}</th><th>Encounter</th></tr></thead><tbody>']
    for r in t["table"]:
        cls = ' class="gap"' if (t.get("status") == "stub") else ""
        h.append(f'<tr><td class="die">{roll(r)}</td><td{cls}>{md(r["encounter"])}</td></tr>')
    h.append("</tbody></table></div>")
    return "\n".join(h)

def render(tid):
    A = load_tables(); t = A[tid]
    subs = {s["id"]: s for s in t.get("subtables", [])}
    draft = " (draft)" if t.get("status") in ("stub", "in_development") else ""
    w = []
    w.append(f'<p class="sample-note">Rendered from <code>airth/encounter_tables/</code>. Grey rows are placeholders.</p>')
    w.append(f"<h1>{html.escape(t['name'])}{draft}</h1>")
    facts = [x for x in [t.get("terrain"), t.get("frequency"), t.get("description")] if x]
    w.append('<p class="tagline">' + " ".join(html.escape(x) for x in facts) + "</p>")
    w.append('<div class="cat">' + table(t, "Encounter type") + "</div>")
    for r in t["table"]:
        sid = r.get("subtable")
        s = subs.get(sid) or A.get(sid)
        if not s:
            w.append(f'<p class="gap">Missing sub-table: {html.escape(sid or "")}</p>')
            continue
        shared = " · shared" if s.get("shared") else ""
        w.append(f'<h2 class="section">{roll(r)} {html.escape(r["encounter"])}<span class="ref">{shared}</span></h2>')
        w.append(table(s, s["name"]))
    return "\n".join(w)

STYLE = (ROOT / "style" / "examples" / "dravesa.html").read_text()
HEAD = STYLE[: STYLE.index("<main>")]
EXTRA = ("<style>.npcref{font-variant:small-caps;letter-spacing:.03em}.npctag{color:var(--ink-soft)}.cat{column-span:all}.cat table{width:60%}td.die,th.die{width:2.4rem;white-space:nowrap}.table-wrap{break-inside:auto}tr{break-inside:avoid}h2.section .ref{font-weight:400;font-size:9pt;margin-left:.4em}"
         "table caption{display:none}</style>\n")

if __name__ == "__main__":
    tid = sys.argv[1]
    A = load_tables()
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(A[tid]['name'])}</title>", HEAD, count=1) + EXTRA
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "style" / "examples" / f"{tid}.html"
    out.write_text(head + "<main>\n" + render(tid) + "\n</main>\n")
    print(out)
