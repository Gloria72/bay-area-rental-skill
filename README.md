# Bay Area Rental Skill

A Codex skill for screening Bay Area apartment options, auditing review risk, and ranking exact units by quietness, security, light, privacy, and day-to-day fit.

Distilled from user-provided rental PDFs/CSV plus the Gemini share on Bay Area rental safety/property screening, with later user corrections treated as higher priority than earlier AI recommendations.

## What It Contains

- `SKILL.md`: main skill workflow and usage rules.
- `references/preference-profile.md`: renter preference model, red flags, scoring, and unit heuristics.
- `references/property-notes.md`: distilled historical notes from provided rental PDFs/CSV and the Gemini share.
- `agents/openai.yaml`: UI metadata for Codex skill discovery.

## Use

Install by copying this folder into your Codex skills directory:

```bash
cp -R . ~/.codex/skills/bay-area-rental
```

Then ask Codex to use `$bay-area-rental`.
