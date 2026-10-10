# NPC Presentation

Follows `style/voice.md`. Storage rules for NPC files are in CLAUDE.md; field list in `schema/npc.schema.json`.

## Render order

```
**Name Moniker**, role · Settlement, N. Location · faction

Appearance. And yet.

"Saying."

**Wants:** …
**Doesn't want:** …
**Knows:** …
**Offers:** …
**Found:** …

—

**Oddly also:** …
**Dreams:** …
**Thinks with:** …
**Family:** …
**Anecdote:** …
**Tragedy:** …
**DM:** …
```

1. **Header:** name and moniker, role, location, faction. Location reads as settlement, then the location's number and name in file order: *Nemetra, 4. Pig Pens*. With no `location`, use `home`.
2. **First sight:** appearance, then and-yet.
3. **First words:** sayings.
4. **Running them:** wants, doesn't want, knows, offers, found.
5. **Dash.**
6. **Depth:** for prep, not mid-session. `dm_notes` renders last, as **DM:**.

Hide empty fields. Never print "Not established" or a blank label. A sparse NPC renders as header, appearance, wants — 3 lines is fine.

## Fields

| Field | Req. | Length | What it is |
|---|---|---|---|
| `name` | yes | as needed | Full proper name. |
| `moniker` | no | 1–3 words | What locals call them: epithet, title, nickname. |
| `role` | yes | 1–3 words | What they do. Everyone has one, even "drifter." |
| `home` | yes | 2–6 words | Where they live or work. |
| `home_settlement` | yes | id | Settlement id, adventure-site id (for denizens), or `itinerant`. |
| `location` | no | id | Location id inside `home_settlement` (`pig-pens`). Settlement renders place the NPC card here. |
| `found` | no | 3–12 words | Where to find them: a named location first, then when or doing what. *Warden’s Hall, sharpening his knife at dusk.* Used for placement only when `location` is empty. |
| `gender` | yes | 1 word | |
| `faction` | yes | id | From `airth/config/npc.json`. |
| `thinks_with` | yes | enum | From the schema enum. |
| `appearance` | yes | 3 details, <15 words | Only what PCs see at first glance. |
| `and_yet` | no | 2–7 words | One detail contradicting the appearance. About the look only. |
| `sayings` | no | 1–7 lines, <12 words each | Quips players will remember and repeat. |
| `wants` | yes | 2–7 words | Now. Concrete; PCs could help or hinder this month. |
| `does_not_want` | yes | 2–7 words | Now. |
| `dreams` | no | 3–10 words | A life goal. Possibly never reached. |
| `oddly_also` | no | 3–12 words | One surprising trait or habit that doesn't fit the rest. |
| `knows` | no | 3–12 words | Something useful they know. No secrets, no price. |
| `offers` | no | 2–4 words | What they can give: goods, services, coin, people. |
| `family` | no | 1–2 sentences | Plain facts. |
| `anecdotes` | no | ≤3 entries, 1–3 sentences each | Things they did. |
| `tragedies` | no | ≤3 entries, 1–3 sentences each | Things they lost. |
| `dm_notes` | no | 1–3 sentences | The answer to every hook, secret, or odd detail on the card. DM eyes only. |

## Writing rules

**Appearance.** Build, age, clothing, marks, carried objects. Nothing that takes familiarity to notice.
- *Good:* 40s. Strong hands. Ale-stained apron.
- *Bad:* Never sits.

**And yet.** The twist on the look.
- *Good:* Huge, scarred, tattooed. *And yet:* hums lullabies while he works.

**Sayings.** The line players quote after the session. Voice lives here — manner shows through the words, not phonetic spelling. If the NPC touches a faction or an adventure hook, the saying points at it.
- *Good:* "Coin first. Then you can ask."
- *Good (hook):* "Pigs don't scream at nothing. Mine scream every night."
- *Weak (no hook):* "Pigs know. Pigs always know."

**Wants vs. dreams.** Split by horizon.
- *Wants:* Her inn kept theology-free.
- *Dreams:* Daughter takes over the inn.

**Wants touch the trouble.** Wants or doesn't-want touches one of the home settlement's `trouble` entries, or a faction the party can deal with. Something PCs could help or hinder this month.
- *Good:* 10 sober men for a patrol past the second hill.
- *Weak:* A quiet life.

**Oddly also.** Only a trait that can come up in play. Literacy, a fine sense of touch, a favourite colour: cut.

**Ties are rare.** A link to another NPC or faction is optional. Add one only when it is a hook the party can use, and never more than one per NPC. Never record an absence: "has never spoken to him" never comes up.

**DM notes.** Every hook, secret or odd detail on the card gets its answer here (see CLAUDE.md, no dead-end mysteries). The answer fits who the NPC is: a crone who keeps the old ways knows what her offering does.
- *Good:* Deliberate. Her mother kept the stone before her.
- *Bad:* Not tribute; habit. Nobody asked for it.

**Anecdotes and tragedies.** Specific past events with names, numbers, and consequences attached — not generic backstory. Not "lost people close to him in tomb collapses" but a named event: who died, when, how, and what habit the survivor still carries because of it. The named version gives a DM something to reference in play; the generic version doesn't. Full sentences with subjects (see voice.md, Backstory).

**Gender.** The campaign keeps the traditional roles of the early middle ages. Ratios follow the role: hunters, soldiers, smiths, and raiders skew heavily male; herb-wives, midwives, and spinners skew female; innkeepers and traders are mixed. Exceptions exist and are rare; never generate them at even odds.

**Never name PCs or session events** in any field. NPC files describe the NPC, not the campaign's current state.

**Empty is fine.** Leave optional fields `null` rather than invent detail. Let it emerge at the table.

## NPCs named outside their card

In encounter tables, road tables, and anywhere else an NPC is named away from their own card, the name carries a tag: **ILMATH**, high fire-seer · Malac Orthodox, Dravesa. Name in small caps, then role, faction (omitted when independent), and home town ("itinerant" if they have none).

The renderers add the tag from `airth/npcs/` (`tools/npcref.py`), so stored text just bolds the name: `**Ilmath**`. Don't put a possessive on a bolded name (`**Halbet**'s apprentice`); write `an apprentice of **Halbet**`, so the tag reads cleanly. A named person with no NPC file gets no tag; give their tie in the text instead (*Bren Duvall of the Gilded Ash*).
