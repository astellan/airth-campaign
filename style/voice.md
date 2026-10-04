# Voice

Rules for everything Claude writes: stored prose fields and rendered output alike. Type-specific files in `style/` build on this one.

## Prose voice

Write in-world, present-tense, matter-of-fact. No hedging, no narrator commentary, no "seems to" or "appears to" — state it as fact even when the fact is strange. Let specific, concrete detail carry tone instead of adjectives: "ink-stained scar-ridged fingers" does more work than "a scholarly appearance." Humor and pathos come from understatement, not from the text calling attention to itself.

Economy of words: never use three words where two will do. Cut qualifiers, throat-clearing, and redundant modifiers on the first pass. Short sentences, not fragments.

**No sentence fragments.** Every sentence has a subject and a verb. Fragments are allowed only in lists: comma-separated details ("Stone blocks, 15′ ceiling"), bullet items, table cells, stat blocks, and short labelled fields (`wants`, `offers`). Quoted speech is exempt; people talk in fragments.
- *Good:* Distant pick-work stops, but starts again a minute later.
- *Bad:* Distant pick-work stops. Starts again a minute later.
- *Bad:* Beneath it, the parish cellars and the vault.

Illustrative, not drawn from an existing NPC — good: *"Trades in favors, never coin. Coin can be traced."* Avoid: *"He has an interesting policy of avoiding cash because he worries about being tracked."* — same fact, but narrated instead of shown, and padded with "interesting" and "he worries."

Don't foreshadow story beats or write toward a planned outcome ("this will become important later"). A field describes what's true now, not what the DM intends to happen.

## Registers

One voice, tuned to the job. Pick the register by what the text is for.

**Reference.** Keyed areas, NPC fields, faction notes, stat blocks. Read by the DM mid-session, so the most actionable thing comes first. Short, complete sentences. Lead with a bolded noun, then detail.
- *Good:* **Iron door:** It has rusted shut and opens only to a combined STR of 30+.
- *Bad:* There is an old iron door here which has rusted shut over the years.

**Narrative.** Montages, travel, recaps, backstory. Read once, aloud or in prep. Short, plain sentences, one image each. No connective padding.
- *Good:* It rains for 3 days. The mud reaches the knee, and the mule dies on the second.
- *Bad:* The journey takes three days, during which it rains constantly and the mule unfortunately dies.

**Read-aloud.** Initial area descriptions and arrival scenes. Only what PCs perceive. No secrets, no conclusions, no PC actions or feelings. Lead with the senses.
- *Good:* The air is cold and smells of tallow. 4 robed figures kneel around a dry well.
- *Bad:* You feel uneasy as you notice cultists performing a ritual.

**Dialogue.** Lines an NPC says. Short and in character; fragments are fine here. One or two sample lines per NPC, not speeches. Dialect through word choice, not phonetic spelling.
- *Good:* "Coin first. Then you can ask."
- *Bad:* "Well, ah, I s'pose I could tell ye, if ye've got the coin."

## Vocabulary

**DM.** Always "DM," never "GM" or "referee."

**AD&D terms only.** Standard AD&D vocabulary for all game terms; no Airth-specific substitutes.
- Classes: magic-user, thief, cleric, fighter. Not wizard, rogue, priest.
- Time: round (1 minute), turn (10 minutes). Never "turn" for a single action.
- Chances: X-in-6, roll under ability score, percentile. Never "check."
- Saves: OSRIC's five categories, named in full.
- Coin: gp, sp, cp, ep, pp. Weight in coins.

**Banned 5e terms:** DC, advantage, disadvantage, short rest, long rest, proficiency, skill check, cantrip, inspiration, bonus action, concentration, CR.
- *Good:* 2-in-6 chance to spot the tripwire.
- *Bad:* DC 15 Perception check to notice the tripwire.

**Proper nouns.** Names of places, factions, NPCs, and gods come from the repo exactly as written. Never coin a new one without permission.

**Plain over grand.** Old, short, concrete words. "Rot," not "decomposition." "The dead," not "undead entities." No modern idiom, no corporate or game-designer jargon ("mechanic," "engagement," "lore drop").

## Emphasis & notation

**Bold**
- Key feature nouns where first named: **iron sarcophagus**.
- Monsters with their count: **3 ghouls**.
- Lead-ins for area actions and multi-action features: **Entering:**, **Opening:**.
- Saving throws: **save vs. spells**.
- Nothing else. Never bold for tone.

**Italics**
- Spells: *sleep*, *dispel magic*.
- Magic items: *staff of wizardry*.
- Book and tome titles.
- Never italics for tone.

**Quotation marks.** Inscriptions, spoken lines, written signs: "The Accursed Gate of Doom."

**Numbers**
- Numerals always: 3 ghouls, 10′ pit, 5 days.
- Ranges with an en dash: 2–3, levels 1–3.
- Levels as ordinals: 5th-level magic-user.

**Units**
- Feet with the prime mark in rendered text: 10′, 120′ move. (Stored data uses "ft"; see CLAUDE.md.)
- Coin with no space: 350gp. Weight in coins: weighs 50 coins.

**Dice and chances**
- Dice: 1d6, 2d4+1, d% for percentile.
- Chances: 2-in-6.
- Ability scores in caps, always in AD&D order: STR, INT, WIS, DEX, CON, CHA.

*Example:* **3 ghouls** crouch over a **broken litter**. The wall bears an inscription: "Rest is earned." Each ghoul carries 2d6gp.

## Structure

**Bolded lead-in.** The basic unit of reference text: a bolded element, then its detail. Encounter beats, features, NPC traits, area actions.
- *Good:* **Ferryman:** He is blind, and knows every voice that has crossed in 20 years.

**Order.** Most actionable first, then general to specific. A DM glancing mid-session gets what they need from the first line.

**Prose, bullets, or tables**
- *Prose:* read-aloud, narrative, initial descriptions. Short paragraphs — 3 sentences max in reference text.
- *Bullets:* discrete, parallel facts. Sub-items of a feature, contents of a chest, an NPC's wants. One level of nesting max.
- *Tables:* anything rolled, and comparisons across shared attributes. Nothing else.

**Random tables**
- Die size in the header: **d6 Rumours**.
- Die matches entry count: d4, d6, d8, d10, d12, d20, d100.
- One line per entry. Detail goes elsewhere, cross-referenced.

| d4 | Sound in the dark |
|---|---|
| 1 | Dripping water, too regular. |
| 2 | **2 giant rats** fighting over a boot. |
| 3 | A bell, once, far below. |
| 4 | Nothing. Total silence for 1 turn. |

**Headings.** Shallow: three levels max.

**Cross-references.** In parentheses: (Area 7), (see Ossek).

**Split, don't sprawl.** An entry that needs more than one screen becomes sub-entries.

## Typography (artifacts)

**Face.** EB Garamond throughout; fallback Garamond, then Georgia. Italic for dialogue, spells, magic items, monster descriptions.

**Column.** Single reading column, ~65 characters wide. Same on phone and laptop.

**Headings.** Small caps. Area numbers in the accent colour.

**Rules**
- Full-width dark rule above each area.
- Short centred rule for the dash between area actions and features.

**Dialogue.** Indented, italic, in quotation marks. Speaker's name above in small caps.

**Sidebars.** Tinted box, thin border. Stat blocks, new magic items, other sidebar material. Stat blocks as a label/value grid, small-caps labels.

**Tables.** Hairline rows, dark rules top and bottom. Die column narrow, in the accent colour.

**Colour.** Ink on off-white, plus one muted green accent — numbers and box headings only. Light and dark modes both.

**No decoration.** No icons, emoji, drop caps, or ornaments.

## Don'ts

A final pass before anything goes out. Cut on sight:

- **Foreshadowing.** "This will matter later." Describe what's true now.
- **Narrator commentary.** "Ominously," "strangely enough," "a grim reminder."
- **Hedging.** "Seems to," "appears to," "perhaps," "somewhat."
- **Filler adjectives.** "Ancient," "mysterious," "eerie," "dark" on their own. Earn tone with a concrete detail.
- **Telling PCs how they feel.** "You feel a sense of dread." Give the cause, not the reaction.
- **Balanced-encounter framing.** "A challenging fight for a level 3 party." No CR thinking.
- **Story protection.** No "if the PCs fail, the villain escapes anyway." Outcomes stay open.
- **Explaining the joke.** Understatement only; don't point at it.
- **Throat-clearing.** "It is worth noting that," "In this area you will find."
- **Modern idiom.** "Vibe," "okay," "on the same page."
- **Padding to fill.** Empty is fine. Leave it for the table.

*Example*
- *Bad:* An ancient, eerie crypt. You feel a sense of dread. This place seems important; perhaps it will matter later.
- *Good:* Dust covers 10 sarcophagi. One lid is already open.
