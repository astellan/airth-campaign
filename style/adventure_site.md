# Adventure Site Presentation

How to render an adventure site for reading: on screen in prep, or scanned mid-session. Data lives in `airth/adventure_sites/`; this file governs how it's written out. Based on the Necrotic Gnome Adventure Area Description Format (2025-07-10), adapted for OSRIC 3.0.

## Area entry shape

```
N. Area Title

Initial description, with **bolded** features.

**Area action:** Notes on the area as a whole.

—

**Feature:** Detail, in order of appearance above.
```

Initial description, then area actions, then a dash, then features. Any part may be absent except the title and initial description.

## Sentences

**No sentence fragments in adventure sites.** Every sentence has a subject and a verb. Fragments are allowed only in lists: comma-separated basics ("Stone blocks, 15′ ceiling"), bullet items, table cells, stat blocks, and the stat/hp line of a monster entry. Quoted speech is exempt. This overrides the fragment guidance in `voice.md` for adventure-site text.
- *Good:* Distant pick-work stops, but starts again a minute later.
- *Bad:* Distant pick-work stops. Starts again a minute later.
- *Bad:* Beneath it, the parish cellars and the vault.

## Area number

- Sequential from 1. Don't restart on new levels.
- Drafting: use tags (`<doom_gate>`) until numbering is final.

## Area title

A few evocative words naming the main feature or function. "Purple Pool," "Scarlet Crypt."

## Initial description

- Everything PCs perceive on first look. Usable as read-aloud.
- Nothing hidden. Hints are fine.
- Concise, evocative, complete sentences. Comma-listed basics (walls, floor, ceiling) are the one exception.
- Lead with walls, floor, ceiling, then scene-setting.
- Then features in order of obviousness, importance, immediacy. Monsters usually first.
- Monsters: say what they're doing when PCs arrive. If they're using a feature, describe both in one sentence.
- Skip anything the map shows: dimensions, ordinary exits, object placement.
- Referee notes in parentheses: "A bronze door (to Area 5)."

## Area actions

Qualities of the whole area, not tied to a feature, not obvious on sight. Bolded lead-in.

- **Entering:** what happens on entry.
- **Sound:** how noise behaves.
- **Time:** what happens after a duration.
- **Chances:** X-in-6 of a creature or event.
- **Hidden:** secret doors or ambushers not tied to a feature.

## Features

- Heading matches the bolded phrase from the initial description, in the same order.
- Give what closer inspection reveals, and the result of obvious actions.
- Multiple actions on one feature: each gets a bolded 1–3 word lead-in (**Touching**, **Opening**). A single action isn't bolded.
- Optional bullet list for sub-items.

## Monsters

- Every monster in the initial description gets a feature paragraph.
- Format: count and name in bold, stat location, rolled hp per individual, then disposition.
  - "**3 orcs:** Stats in sidebar. hp 4, 6, 7. They are dicing and ignore noise from Area 4."
- Roll hp: d8 per HD, plus any modifier. Never average.
- Numerals for counts: "3 orcs," not "three."
- Personality, desires, bargaining positions: bullets under the feature.

## Stat blocks

- Always print a full stat block in rendered output, even for stock OSRIC monsters. The repo stores stock monsters as name + source; expand on render.
- OSRIC GMG block convention, trimmed to in-play fields only, in this order: AC, Move, HD, Attacks, Damage, Special Attacks, Special Defences, Magic Resistance, Intelligence, Alignment, Size. Omit Frequency, No. Appearing, % in Lair, Treasure Type, XP value.
- Descending AC only. Movement in feet.
- Description sits with the stat block, not in the area text.
- Monsters in more than one area: one shared block, referenced from each area.

## Treasure

- Exact counts: coins, gems, jewellery. Never a bare treasure type.
- Value in parentheses right after: "(350gp each)."
- Weight in coins for unusual items: "Dented gold mermaid statuette (500gp, weighs 50 coins)."
- Every valuable gets at least one evocative adjective.
- Magic items in italics by name: *staff of wizardry*. Don't reprint stock item text.
- New magic items get their own sidebar.

## Saving throws

OSRIC categories only, in bold:

- **save vs. aimed magic items**
- **save vs. breath weapons**
- **save vs. death, paralysis, poison**
- **save vs. petrification, polymorph**
- **save vs. spells**

## References

- Areas: "Area X."
- OSRIC page numbers: sparingly, only where the rule is obscure enough to look up mid-session.
- Sidebars: mark in drafts with `[SIDEBAR]`. In artifacts, render as boxed panels.

## Splitting down

An area with too many features or actions becomes several numbered sub-areas.

## Examples

**3. Scarlet Crypt**

Stone blocks, 15′ ceiling. **10 sarcophagi** of black-veined stone emit a flickering scarlet glow. Dust covers everything.

**Sound:** Noise is muffled, as if the air wants silence.

—

**10 sarcophagi:** Heavy stone lids push back.

- **X (on map):** A **wight**: stats in sidebar, hp 22. It lies dormant, wakes when exposed to light, and hates the living.
- **Others:** These are empty.

**6. Moss Cavern**

Natural cavern, 30′ ceiling. Stalagmites rise from a floor carpeted in **black moss**. **Secret door to Area 9:** It opens when pushed.

—

**Black moss:** It is dry and smells of camphor.
