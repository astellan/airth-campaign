"""
Validation tests for airth_items.json and airth_session_log.json.
"""


# ---------------------------------------------------------------------------
# Items
# ---------------------------------------------------------------------------

def test_party_possession_items_have_no_holder(items):
    """Items the party holds should have holder: null (not assigned to an NPC)."""
    invalid = []
    for item_key, item in items.items():
        if item.get("status") == "party_possession" and item.get("holder") is not None:
            invalid.append(f"{item_key}: status is party_possession but holder is '{item['holder']}'")
    assert not invalid, "\n".join(invalid)


def test_npc_possession_items_have_a_holder(items):
    """Items held by an NPC must name that NPC in the holder field."""
    invalid = []
    for item_key, item in items.items():
        if item.get("status") == "npc_possession":
            holder = item.get("holder")
            if not holder:
                invalid.append(f"{item_key}: status is npc_possession but holder is missing or null")
    assert not invalid, "\n".join(invalid)


# ---------------------------------------------------------------------------
# Session log
# ---------------------------------------------------------------------------

def _session_has_content(session):
    """A session is considered non-blank if it has a non-empty summary."""
    return bool(session.get("summary", "").strip())


def test_sessions_with_content_have_date(session_log):
    """Any session with a summary must also have a date filled in."""
    invalid = []
    for session in session_log:
        if _session_has_content(session) and not session.get("date", "").strip():
            invalid.append(f"Session {session['session_number']}: has summary but no date")
    assert not invalid, "\n".join(invalid)


def test_sessions_with_content_have_in_game_dates(session_log):
    """Any session with a summary must also have in_game_dates filled in."""
    invalid = []
    for session in session_log:
        if _session_has_content(session) and not session.get("in_game_dates", "").strip():
            invalid.append(f"Session {session['session_number']}: has summary but no in_game_dates")
    assert not invalid, "\n".join(invalid)
