"""
Shared fixtures for the Airth campaign test suite.
Loads JSON data files once and makes them available to all tests.
"""

import json
import pytest
from pathlib import Path

ROOT = Path(__file__).parent.parent


@pytest.fixture(scope="session")
def npcs():
    with open(ROOT / "airth_npcs.json") as f:
        return json.load(f)["npcs"]


@pytest.fixture(scope="session")
def schema():
    with open(ROOT / "airth_npcs.schema.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def settlements():
    """Load all settlement files from the settlements/ directory."""
    result = {}
    for path in (ROOT / "settlements").glob("*.json"):
        result[path.stem] = json.loads(path.read_text())
    return result


@pytest.fixture(scope="session")
def npc_schema(schema):
    """The NPC definition block from the schema."""
    return schema["definitions"]["npc"]
