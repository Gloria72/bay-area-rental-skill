# 湾区租房排雷 Skill

<p align="center">
  <img src="assets/logo.svg" alt="Bay Area Rental Skill Logo" width="400">
</p>

<h2 align="center">BARS - Bay Area Rental Skill</h2>

<p align="center">
  中文 | <a href="README.en.md">English</a>
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

> 给 AI 助手用的一份湾区租房排雷小抄：少看漂亮官网，多看真实评论、地图位置、车库、包裹、外卖和具体房号。

湾区找房最累的地方不是没有选择，而是每个公寓官网都长得很安全、很干净、很高级。真正影响生活的东西，往往藏在 Google Maps/Yelp/ApartmentRatings 的差评里，藏在 Caltrain、El Camino、San Tomas、SJC 航线、Levi's Stadium、车库入口、垃圾房和 amenity courtyard 旁边。

这个 repo 做的事很简单：把这些碎片信息整理成一套给 AI 助手用的判断框架。你把公寓名单、评论、房型图、unit map 或 listing 丢进去，它帮你按“安静睡眠、车库安全、快递外卖、自然光、隐私、管理靠谱程度”重新排序，然后直接告诉你：值得看、只能特定房号、还是删掉。

它可以在 Codex 里安装成 skill，也可以复制到 ChatGPT、Claude、Gemini 或任何支持项目指令的 AI 助手里用。

如果它帮你少踩一个坑，欢迎点个 Star，让更多在湾区找房的人能搜到它。

## 适合谁

- 你在 Sunnyvale、Mountain View、Santa Clara、North San Jose、Cupertino 附近找房。
- 你不想再被 `luxury apartment`、样板间、官网照片和高星均分带着走。
- 你很在意安静、楼上脚步、车库砸车、包裹丢失、外卖被拿、虫害、隐形费用和 move-out 扣款。
- 你手里已经有几个候选公寓，但不想自己一条条翻评论、看地图、对 floorplan。
- 你想让 AI 别讲场面话，直接告诉你哪个能看、哪个要条件通过、哪个直接 pass。

## 它不会做什么

- 它不是实时房源网站。价格、空房、优惠、评论都要重新查。
- 它不是法律/租约/安全专业意见。
- 它默认不帮你写 leasing 邮件。这个项目的默认模式是筛选和排雷，不是谈判。
- 它不会把历史笔记当真理。旧结论必须让位给最新评论、真实地图和具体房号。

## 最短用法

如果你用 Codex：

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

然后直接问：

```text
Use $bay-area-rental.
帮我比较 The Village、Cherry Orchard、Madrone、The Marlo。
我的优先级：安静睡眠 > 车库安全 > 快递外卖 > 自然光 > 价格。
预算 3900 以下，最好 1B >= 700 sqft。
```

如果你用 ChatGPT / Claude / Gemini：

1. 打开 [skills/bay-area-rental/SKILL.md](skills/bay-area-rental/SKILL.md)。
2. 把它放进 custom GPT、Claude Project、Gem 或项目 system prompt。
3. 如果想保留更完整的偏好和公寓记忆，再附上：
   - [preference-profile.md](skills/bay-area-rental/references/preference-profile.md)
   - [property-notes.md](skills/bay-area-rental/references/property-notes.md)

## 你会得到什么

它的输出会尽量长这样，而不是绕来绕去：

| Rank | Apartment / Unit | Verdict | Why | Risks | Conditions |
|---|---|---|---|---|---|
| 1 | The Village Residences | 主推候选 | 位置后撤、Shea、包裹/维护信号好 | 木结构、Caltrain 距离需复核 | 顶层 + 内院/遮挡 |
| 2 | Cherry Orchard | 主推候选 | 价值感、Shea、社区纵深 | 薄墙、远离 El Camino 才行 | 顶层 + 深处楼栋 |
| 3 | Cobalt | 不推荐 | 管理和硬件不够抵消风险 | San Tomas/Saratoga 噪音、短租、车库投诉 | 除非只剩顶层内院 |

它会用这些标签：

- `主推`: 可以优先花时间看，但仍要复核当前评论和具体房号。
- `条件保留`: 只有满足特定楼层/朝向/房号才行。
- `备选`: 不是最优，但比明显踩雷的好。
- `不推荐`: 和核心需求不匹配。
- `淘汰`: 直接踩中硬雷。

## 这个 skill 关心什么

- 评论里有没有重复出现砸车、包裹丢、外卖丢、虫害、薄墙、火警、管理不理人。
- 地图上是不是贴着 Caltrain/BART/VTA、El Camino、San Tomas、SJC、Levi's、public garage。
- 车库是不是只是“有门禁”，还是最近真的没有 tailgating/break-in 问题。
- 包裹是 Luxer One/Amazon Hub/礼宾管，还是堆在 lobby/走廊。
- 外卖员能不能合法临停、找不找得到门、会不会把饭放在门禁外。
- 房号是不是靠垃圾房、电梯、车库门、loading dock、泳池、BBQ、gym、fire pit。
- 建筑到底是 Type I concrete，还是常见的 wood/podium。

## 文档和示例

- [筛选清单](docs/screening-checklist.md)：看评论、地图、车库、包裹、楼层朝向时按这个过一遍。
- [资料源和核验方式](docs/data-sources.md)：哪些信息可以信，哪些只当营销。
- [Prompt 库](docs/prompt-library.md)：中文、英文、bilingual、房型图、评论审计、最终签约判断。
- [示例输出](examples/)：看看输出大概长什么样。
- [路线图](docs/roadmap.md)：后续可以继续补的东西。
- [贡献指南](CONTRIBUTING.md)：怎么补公寓、修规则、加示例。

## 目录结构

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

## 想贡献的话

欢迎补新的公寓排雷、评论 pattern、房型图判断案例、英文 prompt 或文档改进。最好写“为什么”和“什么条件下可以看”，不要只写一句“好/不好”。

也请不要提交个人隐私、租约、未打码地址、电话、邮箱、完整原始聊天记录，或者大段复制的评论原文。

## License

Apache-2.0. SPDX: `Apache-2.0`.
