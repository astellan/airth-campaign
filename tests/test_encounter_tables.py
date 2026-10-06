"""Road encounter tables: schema-valid, and every category row resolves to a sub-table."""
import json
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "airth" / "encounter_tables"
SCHEMA = json.loads((ROOT / "schema" / "encounter_table.schema.json").read_text())

def _tables():
    out = {}
    for p in TABLES.glob("*.json"):
        d = json.loads(p.read_text())
        if d.get("id"):  # legacy tables without an id are skipped
            out[p.name] = d
    return out

def test_tables_match_schema():
    errors = []
    for name, t in _tables().items():
        for e in jsonschema.Draft7Validator(SCHEMA).iter_errors(t):
            errors.append(f"{name}: {e.message}")
    assert not errors, "\n".join(errors)

def test_subtables_resolve():
    tables = _tables()
    ids = {t["id"] for t in tables.values()}
    missing = []
    for name, t in tables.items():
        local = {s["id"] for s in t.get("subtables", [])}
        for r in t["table"]:
            sid = r.get("subtable")
            if sid and sid not in local and sid not in ids:
                missing.append(f"{name}: roll {r['roll']} -> {sid}")
    assert not missing, "\n".join(missing)
