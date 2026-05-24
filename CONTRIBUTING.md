# Contributing / 贡献指南

Thanks for helping improve Bay Area Rental Skill. This project is most useful when contributions are specific, evidence-aware, and privacy-safe.

谢谢你帮忙完善湾区租房排雷 Skill。这个项目最需要的是具体、可核验、保护隐私的补充。

## What To Contribute

- Apartment risk notes: noise, package theft, car break-ins, garage tailgating, pest issues, management patterns, fees, and move-out disputes.
- Floorplan/unit examples: anonymized unit maps or notes about floor, direction, trash/elevator/garage/amenity exposure.
- Prompt examples: Chinese, English, and bilingual workflows that produce useful screening output.
- Documentation fixes: clearer install steps, better screening checklists, or better source-verification rules.

## What Not To Commit

- Full leases, personal addresses, phone numbers, emails, tenant names, screenshots with private metadata, or raw chat logs.
- Unverified claims framed as facts.
- Long copyrighted review dumps. Summarize patterns instead.

## Apartment Note Format

When adding a property note, prefer this compact structure:

```md
### Apartment Name, City

Default status: `主推候选 / conditional / not recommended`.

Why: concise positive signal.

Risks: concrete review or geography risks.

Conditions: exact unit/floor/orientation requirements.
```

## Review Standard

- Separate current evidence from historical memory.
- Prefer repeated recent patterns over one-off complaints.
- Call out uncertainty with `需要重新确认 / needs recheck`.
- Later corrections should override earlier optimistic recommendations.

## Validation

Before opening a PR or committing:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/bay-area-rental
```

If that script is not available, at minimum verify:

- `skills/bay-area-rental/SKILL.md` has valid YAML frontmatter.
- Relative links from `SKILL.md` resolve.
- Reference files stay concise and do not contain private raw records.
