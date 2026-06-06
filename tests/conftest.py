"""
Shared fixtures for the Airth campaign test suite.
Loads JSON data files once and makes them available to all tests.
"""

import json
import pytest
from pathlib import Path

ROOT = Path(__file__).parent.parent
AIRTH = ROOT / "airth"
SCHEMA = ROOT / "schema"


@pytest.fixture(scope="session")
def npcs():
    result = {}
    for path in (AIRTH / "npcs").glob("*.json"):
        result[path.stem] = json.loads(path.read_text())
    return result


@pytest.fixture(scope="session")
def schema():
    with open(SCHEMA / "npc.schema.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def airth_npc_config():
    with open(AIRTH / "config" / "npc.json") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def settlements():
    result = {}
    for path in (AIRTH / "settlements").glob("*.json"):
        result[path.stem] = json.loads(path.read_text())
    return result


@pytest.fixture(scope="session")
def npc_schema(schema):
    """The NPC definition block from the generic schema."""
    return schema["definitions"]["npc"]
