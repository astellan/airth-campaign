"""Tag named NPCs in rendered text: **Ilmath** -> ILMATH, high fire-seer · Malac Orthodox, Dravesa.

Used by the settlement and road renderers. A bolded phrase is tagged when it matches an NPC
file by name, by title + name ("Captain Durvin", "Mother Yaleth"), or by a unique first name.
Bold that matches no NPC (counts like **1d4 orcs**) is left as plain bold.
"""
import html, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "airth"
SKIP_FACTIONS = {"independent", "none", None, ""}

def _norm(s):
    return re.sub(r"[’'`]", "", (s or "")).lower().strip()

def _settlement_names():
    out = {}
    for p in (A / "settlements").glob("*.json"):
        d = json.loads(p.read_text())
        out[d.get("id", p.stem)] = d.get("name", p.stem)
    return out

def build_index():
    towns = _settlement_names()
    npcs = [json.loads(p.read_text()) for p in sorted((A / "npcs").glob("*.json"))]
    index, firsts = {}, {}
    for n in npcs:
        name = n["name"]
        keys = {_norm(name)}
        mon = n.get("moniker") or ""
        first = name.split()[0]
        if mon:
            keys.add(_norm(f"{mon} {name}"))
            keys.add(_norm(f"{name} {mon}"))
            keys.add(_norm(f"{first} {mon}"))
            if _norm(first) in _norm(mon):  # moniker already holds the name: "Old Borric", "Brother Kellis"
                keys.add(_norm(mon))
                keys.add(_norm(mon[: _norm(mon).index(_norm(first)) + len(first)]))
        role = (n.get("role") or "").split()
        if role:
            keys.add(_norm(f"{role[-1]} {name}"))  # "militia captain" -> "Captain Seretta"
        for k in keys:
            index[k] = n
        firsts.setdefault(_norm(name.split()[0]), []).append(n)
    for k, lst in firsts.items():
        if len(lst) == 1:
            index.setdefault(k, lst[0])
    return index, towns

def tag(n, towns):
    bits = []
    fac = n.get("faction")
    if fac not in SKIP_FACTIONS:
        bits.append(fac.replace("-", " ").title())
    home = n.get("home_settlement")
    if home and home != "itinerant":
        bits.append(towns.get(home, home.title()))
    elif home == "itinerant":
        bits.append("itinerant")
    where = ", ".join(bits)
    role = html.escape(n.get("role") or "")
    return f", {role} · {html.escape(where)}" if where else f", {role}"

def md(text, index=None, towns=None, seen=None):
    """Escape text, render **bold**, and tag the first mention of each NPC."""
    if index is None:
        index, towns = build_index()
    seen = set() if seen is None else seen
    s = html.escape(text or "")
    def sub(m):
        inner = m.group(1)
        n = index.get(_norm(html.unescape(inner)))
        if not n or n["name"] in seen:
            return f"<strong>{inner}</strong>"
        seen.add(n["name"])
        return f'<strong class="npcref">{inner}</strong><span class="npctag">{tag(n, towns)}</span>'
    out = re.sub(r"\*\*(.+?)\*\*", sub, s)
    # Close the tag with a comma when the sentence carries on: "HALBET, master potter · Nemetra, rides east"
    return re.sub(r'(<span class="npctag">[^<]*)</span>(?=\s+[\w<(])', r"\1,</span>", out)

def unmatched(texts):
    """Bold phrases that look like names (no digits) but match no NPC — for checking data."""
    index, _ = build_index()
    out = set()
    for t in texts:
        for b in re.findall(r"\*\*(.+?)\*\*", t or ""):
            if not re.search(r"\d", b) and _norm(b) not in index:
                out.add(b)
    return sorted(out)
