# airth-campaign

Canonical data store for a Tuesday-night AD&D (OSRIC 3rd edition) campaign set in the world of Airth, run in Park Slope. This repo is the source of truth — Google Docs are being retired in favor of these JSON files. Claude may be invoked here directly (via `@claude` in issues/PRs) or as a data source fetched by a separate DM-prep assistant.

## Repo shape

```
airth/
  campaign_main.json       campaign-level state: players, ongoing state
  backlog.json              open/closed worldbuilding tasks — check before inventing content
  session_log.json          session history (INCOMPLETE — don't treat gaps as "nothing happened")
  items.json                items
  config/npc.json           enums used by npc validation (faction list, etc.)
  npcs/*.json                one file per NPC, key = npc.schema.json "npc" definition
  settlements/*.json         one file per settlement
  factions/*.json            one file per faction, faction.schema.json
  world_reference/           cosmology, entities, geography, materials, mortals, population, timeline
  adventure_sites/           dungeons, tombs, ruins, lairs
  encounter_tables/
  archive/
schema/                      generic JSON Schemas (npc, settlement, faction, item, dungeon, region, session, encounter_table)
tests/                       pytest validation suite — run before committing new/edited data
characters/                  player-side training docs (not campaign canon)
```

Top-level `adventure_sites/`, `archive/`, `encounter_tables/`, `npcs/`, `schemas/`, `settlements/`, `taxonomy/` aren't tracked in git at all (confirm with `git ls-tree HEAD`) — they're empty, local-only leftovers from before content was restructured into `airth/`. Real data lives under `airth/`. Don't resurrect them. (`characters/` is also untracked but not empty — it holds player-side training docs, gitignored on purpose.)

## Before adding content

1. Check `airth/backlog.json` for an existing open item covering the request.
2. Check existing data (factions, NPCs, settlements) before inventing new ones — extend what exists rather than duplicating.
3. Validate against `schema/*.json` and, for NPCs, `airth/config/npc.json` enums (e.g. `faction`).
4. Run `pytest` (see `tests/`) before committing. Tests check: required NPC fields present, `thinks_with` and `faction` are valid enum values, `home_settlement` resolves to a real settlement or `"itinerant"`, and array fields (`anecdotes`, `tragedies`) contain only strings.

## Faction structure

Every faction (`faction.schema.json`) is built around three elements: **goals** (primary/secondary/hidden agenda), **philosophy** (how they operate), and limits (what they will and won't do). Subgroups share the goal but diverge on philosophy/limits — that's where internal conflict lives.

Factions are organized as a node pyramid (`identity`, `goals`, `philosophy`, and a `nodes` array): street-level nodes at the bottom, leadership at the top, each node typed `leadership | operations | support | floating`. Players enter at any level and work upward; lower nodes react as the party advances. This scales fractally from individual NPCs to world powers.

## Content rules

- **No XP or mechanics.** Never add hit points, spell slots, leveling math, or any player-side mechanical tracking to these files. That's the players' responsibility, not campaign data.
- **OSR tone, not 5e.** Gritty, matter-of-fact, Gygaxian. The world is indifferent: no balanced-encounter design, no story protection, no guaranteed dramatic beats. Monsters are dangerous, treasure meaningful, death real.
- **Session log is incomplete.** Absence of a session entry doesn't mean nothing happened — don't infer negative facts from gaps.
- **Never generate new content — NPCs, encounters, locations, lore, anything — without discussing it and getting explicit permission first**, no matter how small. Don't assume scope from a schema fix or bug report.

## Style

### Prose voice

Write in-world, present-tense, matter-of-fact. No hedging, no narrator commentary, no "seems to" or "appears to" — state it as fact even when the fact is strange. Let specific, concrete detail carry tone instead of adjectives: "ink-stained scar-ridged fingers" does more work than "a scholarly appearance." Humor and pathos come from understatement, not from the text calling attention to itself.

Economy of words: never use three words where two will do. Cut qualifiers, throat-clearing, and redundant modifiers on the first pass. Sentence fragments are encouraged when they land — "No one agrees." does more work than "No one else agrees with him about this."

Illustrative, not drawn from an existing NPC — good: *"Trades in favors, never coin. Coin can be traced."* Avoid: *"He has an interesting policy of avoiding cash because he worries about being tracked."* — same fact, but narrated instead of shown, and padded with "interesting" and "he worries."

Don't foreshadow story beats or write toward a planned outcome ("this will become important later"). A field describes what's true now, not what the DM intends to happen.

### Naming & identifiers

- JSON keys: `snake_case` throughout.
- Faction/NPC/settlement `id` fields: lowercase, hyphenated (`malac-schismatics`, `gray-blood-tribes`), matching the `^[a-z0-9-]+$` pattern in `schema/faction.schema.json`.
- NPC file names and object keys: lowercase with underscores, matching the person's working name (`ossek_thrice_buried.json`, `mother_yaleth.json`) — not their full formal title.
- New faction enum values must be added to `airth/config/npc.json` before any NPC references them, or `pytest` will fail on `test_faction_is_valid_enum`.
- Don't invent a new id style per-file — check an existing entry in the same category first and match its pattern.

### Field-writing patterns (NPCs)

Short fields (`wants`, `does_not_want`, `oddly_also`, `and_yet`) run 2-3 words on average; 5-7 words is already on the long end. Terse enough to read aloud without editing on the fly. Illustrative: `wants`: "Quiet, and to be believed." `and_yet`: "Never draws first. Always finishes."

`anecdotes` and `tragedies` are told as specific past events with names, numbers, and consequences attached — not generic backstory. Not "lost people close to him in tomb collapses" but a named event: who died, when, how, and what habit the survivor still carries because of it. The named version gives a DM something to reference in play; the generic version doesn't.

`pc_leverage` is a minor field — only fill it in when there's a real hook tied to the NPC's faction or `wants`/`does_not_want`. Otherwise leave it `null` rather than inventing one.

It's fine for fields to be `null` or "Not established" when the table hasn't generated that detail yet — don't backfill invented detail just to fill the field. Leave it empty and let it emerge at the table.

### Adventure sites

Structure maps onto `dungeon.schema.json` sections as follows:

- **Introduction** → `overview` + `type` + `character_levels`. Lead with level range and site type ("Level 2–3 tomb crawl"), then a short paragraph on the site's overall shape and themes.
- **Random Happenings** → `random_events`. Aim for roughly 50/50 atmospheric (non-encounter) entries vs. actual encounters in each zone's table — the point is texture between fights, not a monster every roll.
- **Denizens** → `factions` + `npcs`. Faction entries cover the group and its relation to others in the site; individual `npcs` entries are for named figures encountered in more than one area.
- **General Notes** → `architecture`. Construction, doors, lighting, scale — whatever's true throughout the site rather than area-specific.
- **Area Descriptions** → `key_locations`. See emphasis and stat-block conventions below.
- **After the Adventure** → `resolution` + `persistent_consequences` + `reuse_notes`. Optional; fill in once outcomes exist, not preemptively.

**Emphasis in `key_locations` descriptions:** bold key feature nouns (`**iron sarcophagus**`). Deeper features — secret doors, container contents, specific triggered events — go in the `features` object rather than buried in prose, so they read as discrete, checkable facts. Monster names are bold (`**giant rat**`); monster counts are numerals ("3 giant rats," not "three").

**Stat blocks** follow the OSRIC 3.0 GMG's own block convention, not the terser OSE inline notation — this campaign has no per-monster THAC0 field or condensed `Att n × w (d)` line; to-hit and saves come off the HD-based tables in the GMG (pp. 6–8), not off the individual monster.

For a stock monster from any OSRIC-compatible sourcebook — OSRIC GMG, AD&D 1e Monster Manual, Fiend Folio, Monster Manual II, etc. — `monster_summary` needs only `name` and `source` (e.g. `"OSRIC GMG p.91"`, `"Monster Manual p.5"`, `"Fiend Folio p.34"`) — don't restate stats the book already has.

For a homebrew or reskinned monster, fill in `move`, `ac`, `hd`, `atk` using GMG value conventions — even if the base creature comes from the Monster Manual or Fiend Folio, convert its stats to these conventions rather than copying that book's own notation (e.g. AD&D 1e movement in inches → feet, AC with no ascending bracket → add one):
- `ac`: descending AC only, no ascending bracket — `"2"`, not `"2 [18]"`. This campaign doesn't use ascending AC.
- `move`: feet, not inches. Converting an old inches-based value (Monster Manual, Fiend Folio): multiply by 10 to get feet per round — `MV 12"` becomes `"120ft"`. Multiple modes: `"120ft; 60ft burrowing"`.
- `hd`: OSRIC-style — plain number or with a modifier, `"2"` or `"4+1"`. Variable-HD creatures can use a range, `"3 to 8 (GM decides, or roll 1d6+2)"`.
- `atk`: prose, not terse notation — `"2 claws (1d8+1 slashing) and 1 bite (1d8+1 piercing)"`.
- `special_attack` / `special_defense`: free text for abilities beyond a basic attack line.

For a monster appearing in only one area, it's fine to skip `monster_summary` and put ac/hd/move/attacks inline in that area's `creatures` entry instead.

## Validation

```
pytest
```

Run from repo root. `tests/conftest.py` loads all NPCs, settlements, and the npc config/schema once per session; add new checks alongside the existing ones in `tests/test_npcs.py` rather than creating parallel fixtures.
