"""
NPC validation tests for the Airth campaign.

Each test checks one rule. Failures report exactly which NPC and field
caused the problem.
"""

ITINERANT = "itinerant"  # special value for NPCs with no fixed settlement


# ---------------------------------------------------------------------------
# Required fields
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "moniker", "home", "home_settlement", "gender", "faction",
    "appearance", "and_yet", "wants", "does_not_want", "oddly_also",
    "thinks_with", "family", "self_image", "recreation", "dreams",
    "anecdotes", "tragedies", "pc_leverage",
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
# Enum: thinks_with
# ---------------------------------------------------------------------------

def test_thinks_with_is_valid_enum(npcs, npc_schema):
    """thinks_with must be a value in the blessed enum list."""
    valid = set(npc_schema["properties"]["thinks_with"]["enum"])
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("thinks_with")
        if value and value not in valid:
            invalid.append(f"{npc_key}: '{value}' not in thinks_with enum")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Enum: faction
# ---------------------------------------------------------------------------

def test_faction_is_valid_enum(npcs, npc_schema):
    """faction must be a value in the blessed enum list."""
    valid = set(npc_schema["properties"]["faction"]["enum"])
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("faction")
        if value and value not in valid:
            invalid.append(f"{npc_key}: '{value}' not in faction enum")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Reference: home_settlement
# ---------------------------------------------------------------------------

def test_home_settlement_references_exist(npcs, settlements):
    """home_settlement must be a key in airth_settlements.json, or 'itinerant'."""
    invalid = []
    for npc_key, npc in npcs.items():
        value = npc.get("home_settlement")
        if value and value != ITINERANT and value not in settlements:
            invalid.append(f"{npc_key}: '{value}' not found in airth_settlements.json")
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
