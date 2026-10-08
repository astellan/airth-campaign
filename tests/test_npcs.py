"""
NPC validation tests for the Airth campaign.

Each test checks one rule. Failures report exactly which NPC and field
caused the problem.
"""

ITINERANT = "itinerant"  # universal value for NPCs with no fixed settlement


# ---------------------------------------------------------------------------
# Required fields
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "name", "role", "home", "home_settlement", "gender", "faction",
    "thinks_with", "appearance", "wants", "does_not_want",
]

def test_required_fields_present(npcs):
    """Every NPC must have all required fields."""
    missing = []
    for npc_key, npc in npcs.items():
        for field in REQUIRED_FIELDS:
            if field not in npc:
                missing.append(f"{npc_key}: missing '{field}'")
    assert not missing, "Missing required fields:\n" + "\n".join(missing)


# ---------------------------------------------------------------------------
# Enum: thinks_with (generic schema)
# ---------------------------------------------------------------------------

def test_thinks_with_is_valid_enum(npcs, npc_schema):
    """thinks_with must be a value in the schema enum list."""
    valid = set(npc_schema["properties"]["thinks_with"]["enum"])
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("thinks_with")
        if value and value not in valid:
            invalid.append(f"{npc_key}: '{value}' not in thinks_with enum")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Enum: faction (Airth config)
# ---------------------------------------------------------------------------

def test_faction_is_valid_enum(npcs, airth_npc_config):
    """faction must be a value in the Airth faction list."""
    valid = set(airth_npc_config["faction"]["enum"])
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("faction")
        if value and value not in valid:
            invalid.append(f"{npc_key}: '{value}' not in Airth faction enum")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Reference: home_settlement
# ---------------------------------------------------------------------------

def test_home_settlement_references_exist(npcs, settlements, adventure_site_ids):
    """home_settlement must be a settlement id, an adventure site id, or 'itinerant'."""
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("home_settlement")
        if value and value != ITINERANT and value not in settlements and value not in adventure_site_ids:
            invalid.append(f"{npc_key}: '{value}' not found in airth/settlements/ or airth/adventure_sites/")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Arrays
# ---------------------------------------------------------------------------

def test_anecdotes_are_strings(npcs):
    """All entries in anecdotes must be strings."""
    invalid = []
    for npc_key, npc in npcs.items():
        for i, item in enumerate(npc.get("anecdotes", [])):
            if not isinstance(item, str):
                invalid.append(f"{npc_key}: anecdotes[{i}] is not a string")
    assert not invalid, "\n".join(invalid)


def test_tragedies_are_strings(npcs):
    """All entries in tragedies must be strings."""
    invalid = []
    for npc_key, npc in npcs.items():
        for i, item in enumerate(npc.get("tragedies", [])):
            if not isinstance(item, str):
                invalid.append(f"{npc_key}: tragedies[{i}] is not a string")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Reference: location
# ---------------------------------------------------------------------------

def test_location_references_exist(npcs, settlements):
    """location must be a location id inside the NPC's home_settlement."""
    invalid = []
    for npc_key, npc in npcs.items():
        loc = npc.get("location")
        if not loc:
            continue
        s = settlements.get(npc.get("home_settlement"))
        ids = {l.get("id") for l in (s or {}).get("locations", [])}
        if loc not in ids:
            invalid.append(f"{npc_key}: location '{loc}' not in {npc.get('home_settlement')}")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Prose: backstory sentences have subjects (style/voice.md, Backstory)
# ---------------------------------------------------------------------------

import re

_SUBJECTLESS_OPENERS = set(
    "held took lost found told got kept left went came made ran sold saw chose won fought "
    "led built had knew gave brought bought sent set sets holds keeps takes walks runs "
    "carries sees knows wants says swears pays leaves buries lives works has receives "
    "believes guards talks once never still always".split()
)

def _sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]

def test_backstory_sentences_have_subjects(npcs):
    """Anecdotes, tragedies and dm_notes must not open a sentence on a bare verb."""
    bad = []
    for npc_key, npc in npcs.items():
        for field in ("anecdotes", "tragedies", "dm_notes"):
            value = npc.get(field)
            items = value if isinstance(value, list) else [value] if value else []
            for item in items:
                for s in _sentences(item):
                    words = re.sub(r"[^\w\s'-]", "", s).split()
                    if not words:
                        continue
                    first = words[0].lower()
                    if re.fullmatch(r"[a-z]+ed", first) or first in _SUBJECTLESS_OPENERS:
                        bad.append(f"{npc_key}.{field}: {s}")
    assert not bad, "Subjectless sentences:\n" + "\n".join(bad)
