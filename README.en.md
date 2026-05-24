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
  <img alt="Audience" src="https://img.shields.io/badge/audience-Bay%20Area%20Renters-orange">
  <img alt="Workflow" src="https://img.shields.io/badge/workflow-Reviews%20to%20Decision-purple">
</p>

> Turn an apartment list into a risk screen, and a floorplan into a leasing decision.

Bay Area Rental Skill is a bilingual Chinese/English Codex skill for apartment screening in the Bay Area. It turns listings, Google Maps/Yelp/ApartmentRatings reviews, floorplans, unit orientation, and personal preferences into practical rental decisions.

It is designed for renters who care about safety, cleanliness, quiet sleep, a newer apartment feel, responsible property management, secure package/food delivery, and lower car break-in risk. It is especially useful for screening `1B/1B`, studio, and exact-unit options in Sunnyvale, Mountain View, Santa Clara, North San Jose, and Cupertino.

This repository contains only the distilled skill and reference rules. It does not include raw PDFs, CSVs, or GPT/Gemini conversation logs.

## What It Does

- Compares apartment candidates and labels them as `top pick`, `conditional`, `backup`, `not recommended`, or `eliminate`.
- Audits resident-review risk, prioritizing recent negative patterns around car break-ins, package theft, pest issues, thin walls, management failures, surprise fees, and unsafe garages.
- Ranks exact units by floor, window exposure, courtyard/street orientation, Caltrain/BART/VTA, El Camino, San Tomas, SJC, Levi's, public garages, trash rooms, and amenity noise.
- Preserves preference memory: Irvine Company is avoided by default; Miro is excluded unless reopened by the user; Cobalt is no longer treated as a default top pick.
- Supports Chinese, English, or bilingual output depending on the user's prompt.

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

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

Then ask Codex:

```text
Use $bay-area-rental to screen these apartments.
```

## Repository Layout

```text
bay-area-rental-skill/
├── README.md
├── README.en.md
├── LICENSE
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

## License

Apache-2.0
