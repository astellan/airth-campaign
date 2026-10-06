# NPC Presentation

Follows `style/voice.md`. Storage rules for NPC files are in CLAUDE.md; field list in `schema/npc.schema.json`.

## Render order

```
**Name Moniker**, role · home · faction

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
```

1. **Header:** name and moniker, role, home, faction.
2. **First sight:** appearance, then and-yet.
3. **First words:** sayings.
4. **Running them:** wants, doesn't want, knows, offers, found.
5. **Dash.**
6. **Depth:** for prep, not mid-session.

Hide empty fields. Never print "Not established" or a blank label. A sparse NPC renders as header, appearance, wants — 3 lines is fine.

## Fields

| Field | Req. | Length | What it is |
|---|---|---|---|
| `name` | yes | as needed | Full proper name. |
| `moniker` | no | 1–3 words | What locals call them: epithet, title, nickname. |
| `role` | yes | 1–3 words | What they do. Everyone has one, even "drifter." |
| `home` | yes | 2–6 words | Where they live or work. |
| `home_settlement` | yes | id | Settlement id, adventure-site id (for denizens), or `itinerant`. |
| `found` | no | 3–12 words | Where to find them: a named location first, then when or doing what. *Warden’s Hall, sharpening his knife at dusk.* Settlement renders place the NPC card at this location. |
| `gender` | yes | 1 word | |
| `faction` | yes | id | From `airth/config/npc.json`. |
| `thinks_with` | yes | enum | From the schema enum. |
| `appearance` | yes | 3 details, <15 words | Only what PCs see at first glance. |
| `and_yet` | no | 2–7 words | One detail contradicting the appearance. About the look only. |
| `sayings` | no | 1–2 lines, <12 words each | Quips players will remember and repeat. |
| `wants` | yes | 2–7 words | Now. Concrete; PCs could help or hinder this month. |
| `does_not_want` | yes | 2–7 words | Now. |
| `dreams` | no | 3–10 words | A life goal. Possibly never reached. |
| `oddly_also` | no | 3–12 words | One surprising trait or habit that doesn't fit the rest. |
| `knows` | no | 3–12 words | Something useful they know. No secrets, no price. |
| `offers` | no | 2–4 words | What they can give: goods, services, coin, people. |
| `family` | no | 1–2 sentences | Plain facts. |
| `anecdotes` | no | ≤3 entries, 1–3 sentences each | Things they did. |
| `tragedies` | no | ≤3 entries, 1–3 sentences each | Things they lost. |

## Writing rules

**Appearance.** Build, age, clothing, marks, carried objects. Nothing that takes familiarity to notice.
- *Good:* 40s. Strong hands. Ale-stained apron.
- *Bad:* Never sits.

**And yet.** The twist on the look.
- *Good:* Huge, scarred, tattooed. *And yet:* hums lullabies while he works.

**Sayings.** The line players quote after the session. Voice lives here — manner shows through the words, not phonetic spelling.
- *Good:* "Coin first. Then you can ask."

**Wants vs. dreams.** Split by horizon.
- *Wants:* Her inn kept theology-free.
- *Dreams:* Daughter takes over the inn.

**Anecdotes and tragedies.** Specific past events with names, numbers, and consequences attached — not generic backstory. Not "lost people close to him in tomb collapses" but a named event: who died, when, how, and what habit the survivor still carries because of it. The named version gives a DM something to reference in play; the generic version doesn't.

**Gender.** The campaign keeps the traditional roles of the early middle ages. Ratios follow the role: hunters, soldiers, smiths, and raiders skew heavily male; herb-wives, midwives, and spinners skew female; innkeepers and traders are mixed. Exceptions exist and are rare; never generate them at even odds.

**Never name PCs or session events** in any field. NPC files describe the NPC, not the campaign's current state.

**Empty is fine.** Leave optional fields `null` rather than invent detail. Let it emerge at the table.

## NPCs named outside their card

In encounter tables, road tables, and anywhere else an NPC is named away from their own card, the name carries a tag: **ILMATH**, high fire-seer · Malac Orthodox, Dravesa. Name in small caps, then role, faction (omitted when independent or none), and home town ("itinerant" if they have none).

The renderers add the tag from `airth/npcs/` (`tools/npcref.py`), so stored text just bolds the name: `**Ilmath**`. Don't put a possessive on a bolded name (`**Halbet**'s apprentice`); write `an apprentice of **Halbet**`, so the tag reads cleanly. A named person with no NPC file gets no tag; give their tie in the text instead (*Bren Duvall of the Gilded Ash*).
