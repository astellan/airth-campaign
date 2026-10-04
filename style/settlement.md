# Settlement Presentation

Follows `style/voice.md`. Covers settlements and steadings. Storage rules in CLAUDE.md; fields in `schema/settlement.schema.json`.

## Steadings

A steading is a satellite of a settlement: a hamlet, an eccentric remote extended family, a seasonal site, or a place settled only for a resource or a trade too offensive for settled areas.

- Always has a `parent` settlement.
- `kind`: `hamlet` | `family` | `seasonal` | `resource` | `noxious_trade`.
- `why_here`: the single reason it exists, in one line. *"Tannery pits too foul for Dravesa's walls."*
- One file per steading in `airth/settlements/`, linked by `parent`. Never nested inside the parent's file.
- Uses the same fields as a settlement, and renders shorter.

## Palette

The arrival palette is a stock of descriptors the DM grabs from in the moment, not prose to read aloud. Arriving, leaving, and passing through are half the game; the palette gives them life.

**Rings.** Arrival is a zoom:
- **Far:** what announces the place a mile out.
- **Near:** outskirts, fields, steadings, the road filling up.
- **Threshold:** the gate, wall, or edge.
- **Within:** streets, people, noise.
- **Leaving:** the last thing noticed looking back.

**Senses.** Within each ring, draw on sight, sound, smell, feel (ground, air, temperature), and people (faces, dress, how strangers are read).

**Format.** Descriptors separated by ` · `. At most one per row gets a short italic phrase of detail. Fragments are correct here.

**Three layers:**
1. **Constants:** descriptors that never change.
2. **Time-of-day grid:** ring × dawn / day / dusk / night. Only rings and cells that vary.
3. **Overlays:** one line each, layered on the grid.
   - **Seasons:** the standard four, labelled with Airth months — Winter (Voarn–Thunor), Spring (Arkun–Ulkar), Summer (Sarnath–Keltoi), Autumn (Ragaia–Eshmun).
   - **Situations:** custom per settlement — feast days from the Calendar of Airth, local events, crises.

In play, read down the time-of-day column, then add the season line and any situation.

### Example

**Constants**
**Far:** pine tar · woodsmoke · *stone walls, the only ones in the Marches*
**Leaving:** smoke over the walls · *tar on your boots for a day after*

| | Dawn | Day | Dusk | Night |
|---|---|---|---|---|
| **Threshold** | gates opening · carts queued | *watch reads pendants: flame-drop, sun-disk, or neither* | last carts hurried in | gates shut · pass required |
| **Within** | temple bell · Schismatic dawn rite | market calls · dye-works stink | Gilded Ash filling | watch lanterns · *singing behind Schismatic shutters* |

**Winter** *(Voarn–Thunor)*: walls rimed · smoke hangs low · *axes silent, wood yards stacked to the eaves*
**Malzûn** *(2 Belghaen)*: both temples full · *Orthodox and Schismatic processions timed not to meet*
