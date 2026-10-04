# Voice

Rules for everything Claude writes: stored prose fields and rendered output alike. Type-specific files in `style/` build on this one.

## Prose voice

Write in-world, present-tense, matter-of-fact. No hedging, no narrator commentary, no "seems to" or "appears to" — state it as fact even when the fact is strange. Let specific, concrete detail carry tone instead of adjectives: "ink-stained scar-ridged fingers" does more work than "a scholarly appearance." Humor and pathos come from understatement, not from the text calling attention to itself.

Economy of words: never use three words where two will do. Cut qualifiers, throat-clearing, and redundant modifiers on the first pass. Sentence fragments are encouraged when they land — "No one agrees." does more work than "No one else agrees with him about this."

Illustrative, not drawn from an existing NPC — good: *"Trades in favors, never coin. Coin can be traced."* Avoid: *"He has an interesting policy of avoiding cash because he worries about being tracked."* — same fact, but narrated instead of shown, and padded with "interesting" and "he worries."

Don't foreshadow story beats or write toward a planned outcome ("this will become important later"). A field describes what's true now, not what the DM intends to happen.

## Registers

One voice, tuned to the job. Pick the register by what the text is for.

**Reference.** Keyed areas, NPC fields, faction notes, stat blocks. Read by the DM mid-session, so the most actionable thing comes first. Fragments preferred. Lead with a bolded noun, then detail.
- *Good:* **Iron door.** Rusted shut. Opens on a combined STR of 30+.
- *Bad:* There is an old iron door here which has rusted shut over the years.

**Narrative.** Montages, travel, recaps, backstory. Read once, aloud or in prep. Sparse fragments; grammar optional. Image, then image, no connective tissue.
- *Good:* Three days of rain. Mud to the knee. The mule dies on the second.
- *Bad:* The journey takes three days, during which it rains constantly and the mule unfortunately dies.

**Read-aloud.** Initial area descriptions and arrival scenes. Only what PCs perceive. No secrets, no conclusions, no PC actions or feelings. Lead with the senses.
- *Good:* Cold air. Smell of tallow. 4 robed figures kneel around a dry well.
- *Bad:* You feel uneasy as you notice cultists performing a ritual.

**Dialogue.** Lines an NPC says. Short and in character. One or two sample lines per NPC, not speeches. Dialect through word choice, not phonetic spelling.
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
- *Good:* **Ferryman.** Blind. Knows every voice that's crossed in 20 years.

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
