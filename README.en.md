# BARS — Bay Area Rental Skill

<p align="center">
  <img src="assets/logo.svg" alt="Bay Area Rental Skill Logo" width="400">
</p>

<h2 align="center">BARS — Bay Area Rental Skill</h2>

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

> Turn an apartment list into a risk screen, and a floorplan into a leasing decision. Works with Codex, ChatGPT, Claude, Gemini, or any AI assistant that supports project instructions.

Bay Area Rental Skill is a bilingual Chinese/English portable AI assistant skill for apartment screening in the Bay Area. It turns listings, Google Maps/Yelp/ApartmentRatings reviews, floorplans, unit orientation, and personal preferences into practical rental decisions.

It is designed for renters who care about safety, cleanliness, quiet sleep, a newer apartment feel, responsible property management, secure package/food delivery, and lower car break-in risk. It is especially useful for screening `1B/1B`, studio, and exact-unit options in Sunnyvale, Mountain View, Santa Clara, North San Jose, and Cupertino.

This repository contains only the distilled skill and reference rules. It does not include raw PDFs, CSVs, or full GPT/Gemini conversation logs.

If this helps you avoid even one bad lease, a Star helps other Bay Area renters find it.

## Quick Start

1. Install the skill:

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

2. Ask your AI assistant:

```text
Use bay-area-rental.
Compare The Village, Cherry Orchard, Madrone, and The Marlo.
My priority is quiet sleep > garage safety > packages/food delivery > natural light > price.
Budget is under 3900, ideally 1B >= 700 sqft.
```

3. Expect a compact decision table:

| Rank | Apartment / Unit | Verdict | Why | Risks | Conditions |
|---|---|---|---|---|---|
| 1 | The Village Residences | top candidate | set back, Shea, good package/maintenance signal | wood structure, Caltrain distance needs checking | top floor + shielded exposure |
| 2 | Cherry Orchard | value candidate | Shea, deeper community layout | thin-wall risk, must avoid El Camino exposure | top floor + deep interior building |
| 3 | Cobalt | not recommended | hardware is not enough to offset risk | San Tomas/Saratoga noise, short-term turnover, garage complaints | only if top-floor courtyard is the last option |

## What It Does

- Compares apartment candidates and labels them as `top pick`, `conditional`, `backup`, `not recommended`, or `eliminate`.
- Audits resident-review risk, prioritizing recent negative patterns around car break-ins, package theft, pest issues, thin walls, management failures, surprise fees, and unsafe garages.
- Ranks exact units by floor, window exposure, courtyard/street orientation, Caltrain/BART/VTA, El Camino, San Tomas, SJC, Levi's, public garages, trash rooms, and amenity noise.
- Preserves preference memory: Irvine Company is avoided by default; Miro is excluded unless reopened by the user; Cobalt is no longer treated as a default top pick.
- Supports Chinese, English, or bilingual output depending on the user's prompt.

## Who It Is For

- Renters looking in South Bay who do not want to be fooled by glossy apartment websites or staged tours.
- Light sleepers and risk-sensitive renters who care about upstairs footsteps, garage safety, package theft, and food delivery flow.
- People comparing Sunnyvale, Mountain View, Santa Clara, North San Jose, and Cupertino units.
- Anyone with floorplans, unit maps, Google Maps/Yelp/ApartmentRatings reviews, and not enough patience to cross-check everything manually.

## What It Is Not

- It is not a live availability database. Prices, units, concessions, and reviews must be rechecked.
- It is not legal, lease, or safety advice.
- It does not draft leasing emails by default. The default mode is screening, not negotiation.

## Recommended Usage

```text
Use bay-area-rental to screen these Bay Area apartments.

My hard requirements:
- Safe, quiet, clean, responsible management
- Avoid package/food theft, car break-ins, pests, thin walls
- Budget:
- Cities / commute:
- Unit type:

Candidate apartments / units / links / reviews:
...
```

If you only have a floorplan or listing, you can also ask:

```text
Use bay-area-rental to rank these units in Chinese and English.
Focus on quietness, garage/package safety, natural light, privacy, and whether I should tour/apply/sign.
```

More copy-paste prompts live in [docs/prompt-library.md](docs/prompt-library.md), with full examples in [examples/](examples/).

## Usage Options

### Codex Install

If you use Codex, copy the skill folder into your local skills directory:

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

Then ask Codex:

```text
Use $bay-area-rental to screen these apartments.
```

### Other AI Assistants

If you use ChatGPT, Claude, Gemini, or another AI assistant:

1. Open [skills/bay-area-rental/SKILL.md](skills/bay-area-rental/SKILL.md).
2. Use it as project instructions, a system prompt, or the core instruction for a custom GPT/Claude Project/Gem.
3. For stronger memory, also attach:
   - [preference-profile.md](skills/bay-area-rental/references/preference-profile.md)
   - [property-notes.md](skills/bay-area-rental/references/property-notes.md)

The core of this repo is not tied to one tool; it is a reusable rental-screening judgment framework.

## Docs

- [Screening checklist](docs/screening-checklist.md): review, map, garage, package, floor, and exposure checks.
- [Data sources and verification](docs/data-sources.md): what to trust, what to treat as marketing, and what to recheck.
- [Prompt library](docs/prompt-library.md): Chinese, English, bilingual, floorplan, review audit, and final signing prompts.
- [Roadmap](docs/roadmap.md): planned content and feature expansions.
- [Contributing guide](CONTRIBUTING.md): how to add apartment notes, fix rules, or contribute examples.
- GitHub workflow: automatically runs `python scripts/validate_skill.py .` to validate the public skill package.

## Repository Layout

```text
bay-area-rental-skill/
├── .github/
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

## Screening Principles

- Reviews and real geography beat official pages, brands, newness, and `luxury` marketing.
- Later user corrections override earlier AI recommendations.
- New-looking Mountain View, Sunnyvale, and Santa Clara apartments are often podium/wood, not true all-concrete Type I.
- For wood or mixed-structure buildings, prefer top floor plus interior/courtyard/shielded exposure.
- Gated parking is not enough; check car break-ins, tailgating, cameras, management response, and short-term/corporate rental turnover.
- Food delivery quality depends on legal short-term parking, building wayfinding, and whether there is a monitored indoor pickup area.

## Contributing

Contributions are welcome: apartment risk notes, anonymized review patterns, floorplan examples, English prompts, and documentation improvements. Please do not commit private leases, raw chat logs, unredacted addresses, or personally identifiable information.

## License

Apache-2.0. SPDX: `Apache-2.0`.
