# BARS - Bay Area Rental Skill

<p align="center">
  <img src="assets/logo.svg" alt="Bay Area Rental Skill Logo" width="400">
</p>

<h2 align="center">BARS - Bay Area Rental Skill</h2>

<p align="center">
  <a href="README.md">中文</a> | English
</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v1.1.0-brightgreen">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue">
  <img alt="Audience" src="https://img.shields.io/badge/audience-South%20Bay%20Renters-orange">
  <img alt="Workflow" src="https://img.shields.io/badge/workflow-Review%20Audit%20%E2%86%92%20Unit%20Decision-purple">
  <img alt="Platform" src="https://img.shields.io/badge/platform-Any%20AI%20Assistant-0aa3a3">
  <img alt="Language" src="https://img.shields.io/badge/language-中文%20%7C%20English-informational">
  <img alt="Validate skill" src="https://github.com/Gloria72/bay-area-rental-skill/actions/workflows/validate-skill.yml/badge.svg">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/Gloria72/bay-area-rental-skill?style=social">
</p>

> A practical rental-screening note pack for AI assistants. Less apartment marketing, more review patterns, map reality, garage/package risk, food delivery flow, and exact-unit judgment.

Bay Area apartment hunting is exhausting because every building website looks clean, safe, and "luxury." The problems that actually change daily life are usually hidden in recent reviews, map placement, train/road/airport/stadium exposure, garage design, package rooms, delivery access, and the exact unit location.

This repo turns those messy signals into a reusable judgment framework for AI assistants. Give it apartment names, reviews, listings, floorplans, or unit maps, and it helps decide what is worth touring, what only works under strict unit conditions, and what should be deleted from the shortlist.

It can be installed as a Codex skill, or copied into ChatGPT, Claude, Gemini, or any assistant that supports project instructions.

If it helps you avoid even one bad lease, a Star makes it easier for other Bay Area renters to find.

## Who This Is For

- You are looking around Sunnyvale, Mountain View, Santa Clara, North San Jose, or Cupertino.
- You do not want glossy websites, staged tours, or high average ratings to do the thinking for you.
- You care about quiet sleep, upstairs footsteps, garage safety, package theft, food delivery, pests, surprise fees, and move-out charges.
- You already have a few candidates and want an AI assistant to cross-check reviews, maps, floorplans, and unit exposure.
- You want direct labels: top pick, conditional, backup, not recommended, or eliminate.

## What This Is Not

- It is not a live listing database. Prices, availability, concessions, and reviews must be rechecked.
- It is not legal, lease, or safety advice.
- It does not draft leasing emails by default. The default mode is screening, not negotiation.
- It does not treat historical notes as permanent truth. New reviews, real maps, and exact units win.

## Fastest Way To Use It

If you use Codex:

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

Then ask:

```text
Use $bay-area-rental.
Compare The Village, Cherry Orchard, Madrone, and The Marlo.
My priorities are quiet sleep > garage safety > package/food delivery > natural light > price.
Budget is under 3900, ideally 1B >= 700 sqft.
```

If you use ChatGPT / Claude / Gemini:

1. Open [skills/bay-area-rental/SKILL.md](skills/bay-area-rental/SKILL.md).
2. Add it to your custom GPT, Claude Project, Gem, or project system prompt.
3. For stronger memory, also attach:
   - [preference-profile.md](skills/bay-area-rental/references/preference-profile.md)
   - [property-notes.md](skills/bay-area-rental/references/property-notes.md)

## What The Output Looks Like

The goal is a decision table, not a long essay:

| Rank | Apartment / Unit | Verdict | Why | Risks | Conditions |
|---|---|---|---|---|---|
| 1 | The Village Residences | top candidate | set back, Shea, good package/maintenance signal | wood structure, Caltrain distance needs checking | top floor + shielded exposure |
| 2 | Cherry Orchard | value candidate | Shea, deeper community layout | thin-wall risk, must avoid El Camino exposure | top floor + deep interior building |
| 3 | Cobalt | not recommended | hardware is not enough to offset risk | San Tomas/Saratoga noise, short-term turnover, garage complaints | only if top-floor courtyard is the last option |

Verdict labels:

- `top pick`: worth focusing on, after rechecking current reviews and exact unit.
- `conditional`: works only with strict floor/orientation/unit conditions.
- `backup`: acceptable if stronger options fail.
- `not recommended`: does not fit the core preferences.
- `eliminate`: hits hard red flags.

## What The Skill Checks

- Repeated review patterns around car break-ins, package theft, food delivery issues, pests, thin walls, false alarms, fees, and poor management.
- Real exposure to Caltrain/BART/VTA, El Camino, San Tomas, SJC, Levi's, and public garages.
- Whether "gated garage" actually means safer parking, or just another tailgating risk.
- Whether packages are handled by Luxer One, Amazon Hub, concierge, or lobby piles.
- Whether delivery drivers can legally stop, find the entrance, and leave food in a monitored indoor area.
- Whether the unit sits near trash rooms, elevators, garage gates, loading docks, pools, BBQs, gyms, fire pits, or other noise sources.
- Whether the building is actually Type I concrete or the common wood/podium construction.

## Docs And Examples

- [Screening checklist](docs/screening-checklist.md): review, map, garage, package, floor, and exposure checks.
- [Data sources and verification](docs/data-sources.md): what to trust, what is marketing, and what to recheck.
- [Prompt library](docs/prompt-library.md): Chinese, English, bilingual, floorplan, review audit, and final signing prompts.
- [Examples](examples/): sample output shape.
- [Roadmap](docs/roadmap.md): what could be expanded next.
- [Contributing guide](CONTRIBUTING.md): how to add apartment notes, fix rules, or contribute examples.

## Repository Layout

```text
bay-area-rental-skill/
├── README.md
├── README.en.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── docs/
├── examples/
├── scripts/
├── assets/
│   └── logo.svg
└── skills/
    └── bay-area-rental/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── preference-profile.md
            └── property-notes.md
```

## Contributing

Apartment risk notes, review patterns, floorplan examples, English prompts, and documentation improvements are welcome. Good notes explain both the risk and the exact conditions under which the building might still work.

Please do not commit private leases, unredacted addresses, phone numbers, emails, full raw chat logs, or long copied review text.

## License

Apache-2.0. SPDX: `Apache-2.0`.
