"""
Settlement validation tests. Settlements in the new format (those with a
`tagline`) are validated against the schema; legacy files are skipped until
migrated (see backlog).
"""
import jsonschema


def _new_format(settlements):
    return {k: s for k, s in settlements.items() if "tagline" in s}


def test_new_format_matches_schema(settlements, settlement_schema):
    errors = []
    for key, s in _new_format(settlements).items():
        try:
            jsonschema.validate(s, settlement_schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{key}: {e.message}")
    assert not errors, "\n".join(errors)


def test_location_labels_match_type(settlements, settlement_config):
    types = settlement_config["location_types"]
    bad = []
    for key, s in _new_format(settlements).items():
        for loc in s.get("locations", []):
            t = loc.get("type")
            if t not in types:
                bad.append(f"{key}/{loc.get('id')}: unknown type '{t}'")
                continue
            allowed = types[t]
            if allowed is None:
                continue
            for label in loc.get("labels", {}):
                if label not in allowed:
                    bad.append(f"{key}/{loc['id']}: label '{label}' not allowed for {t}")
    assert not bad, "\n".join(bad)


def test_parent_exists(settlements):
    bad = [f"{k}: parent '{s['parent']}' not found"
           for k, s in settlements.items() if s.get("parent") and s["parent"] not in settlements]
    assert not bad, "\n".join(bad)


def test_neighbors_are_two_way(settlements):
    bad = []
    for key, s in settlements.items():
        for n in s.get("neighbors", []):
            other = settlements.get(n["settlement"])
            if not other or "neighbors" not in other:
                continue  # neighbor not yet migrated
            if not any(m["settlement"] == key for m in other["neighbors"]):
                bad.append(f"{key} -> {n['settlement']} has no link back")
    assert not bad, "\n".join(bad)
