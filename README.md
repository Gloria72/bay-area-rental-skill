# 湾区租房排雷 Skill

<p align="center">
  <img src="assets/logo.svg" alt="Bay Area Rental Skill Logo" width="400">
</p>

<h2 align="center">BARS — Bay Area Rental Skill</h2>

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
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/Gloria72/bay-area-rental-skill?style=social">
</p>

> 把公寓名单变成排雷表，把房型图变成签约判断。可用于 Codex，也可作为 ChatGPT / Claude / Gemini / 任意 AI 助手的项目指令。

湾区租房排雷 Skill 是一个中英文可用的 portable AI assistant skill：把 Bay Area 公寓 listing、Google Maps/Yelp/ApartmentRatings 评论、房型图、楼层朝向和个人偏好，蒸馏成可执行的租房筛选结论。

它专门服务“安全、干净、安静、新一点、物业负责、不丢快递/外卖、不砸车”的租房需求，尤其适合筛 Sunnyvale、Mountain View、Santa Clara、North San Jose、Cupertino 一带的 `1B/1B`、studio 和具体房号。

这个 repo 只放蒸馏后的 skill 和参考规则，不包含原始 PDF/CSV/GPT/Gemini 记录全文。

如果它帮你少踩一个坑，欢迎点一个 Star，让更多在湾区找房的人能搜到它。

## 快速开始

1. 安装 skill：

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

2. 在 AI 助手里直接问：

```text
Use bay-area-rental.
帮我比较 The Village、Cherry Orchard、Madrone、The Marlo。
我的优先级：安静睡眠 > 车库安全 > 快递外卖 > 自然光 > 价格。
预算 3900 以下，最好 1B >= 700 sqft。
```

3. 得到这种结构化结论：

| Rank | Apartment / Unit | Verdict | Why | Risks | Conditions |
|---|---|---|---|---|---|
| 1 | The Village Residences | 主推候选 | 位置后撤、Shea、包裹/维护信号好 | 木结构、Caltrain 距离需复核 | 顶层 + 内院/遮挡 |
| 2 | Cherry Orchard | 主推候选 | 价值感、Shea、社区纵深 | 薄墙、远离 El Camino 才行 | 顶层 + 深处楼栋 |
| 3 | Cobalt | 不推荐 | 管理和硬件不够抵消风险 | San Tomas/Saratoga 噪音、短租、车库投诉 | 除非只剩顶层内院 |

## 它能做什么

- 对比公寓候选：输出 `主推 / 条件保留 / 备选 / 不推荐 / 淘汰`。
- 背调评论风险：优先看近期差评、砸车、包裹丢失、虫害、薄墙、管理跑路、隐形费用。
- 排房号和朝向：结合楼层、窗户、内院/街道、Caltrain/BART/VTA、El Camino、San Tomas、SJC、Levi's、车库、垃圾房和 amenity 噪音。
- 蒸馏偏好记忆：默认避开 Irvine Company；Miro 默认排除，除非用户主动重新打开；不再把 Cobalt 当默认主推。
- 支持中英文输出：中文 prompt 默认中文，English prompt 默认 English，也可以要求 bilingual table。

## 适合谁

- 第一次在 South Bay 找公寓，怕被漂亮官网和样板间带偏的人。
- 对噪音、楼上脚步、车库安全、包裹外卖丢失非常敏感的人。
- 正在比较 Sunnyvale、Mountain View、Santa Clara、North San Jose、Cupertino 房源的人。
- 手里有 floorplan、unit map、Google Maps/Yelp/ApartmentRatings 评论，但不想自己反复交叉排雷的人。

## 不适合什么

- 它不是实时房源数据库。价格、可租房号、优惠、评论都需要实时复核。
- 它不能替代法律、租约或安全专业意见。
- 它不会默认帮你写 leasing 邮件；这个 skill 的默认模式是筛选，而不是谈判。

## 推荐用法

```text
使用 bay-area-rental，帮我筛这几个湾区公寓。

我的硬需求：
- 安全、安静、干净、物业负责
- 不想要快递/外卖丢、车被砸、虫害、薄墙
- 预算：
- 城市/通勤：
- 户型：

候选公寓 / 房号 / 链接 / 评论：
...
```

如果你只有一个房型图或 listing，也可以直接发：

```text
Use bay-area-rental to rank these units in Chinese and English.
Focus on quietness, garage/package safety, natural light, privacy, and whether I should tour/apply/sign.
```

更多可直接复制的 prompt 在 [docs/prompt-library.md](docs/prompt-library.md)，完整示例在 [examples/](examples/)。

## 使用方式

### Codex 安装

如果你使用 Codex，把 skill 文件夹复制到本地 skills 目录：


```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

然后在 Codex 里说：

```text
Use $bay-area-rental to screen these apartments.
```

### 其他 AI 助手

如果你用 ChatGPT、Claude、Gemini 或其他 AI 助手：

1. 打开 [skills/bay-area-rental/SKILL.md](skills/bay-area-rental/SKILL.md)。
2. 把它作为项目指令、system prompt 或自定义 GPT/Claude Project/Gem 的核心指令。
3. 需要更强记忆时，再附上：
   - [preference-profile.md](skills/bay-area-rental/references/preference-profile.md)
   - [property-notes.md](skills/bay-area-rental/references/property-notes.md)

这个 repo 的核心不是绑定某个工具，而是一套可复用的租房筛选判断框架。

## 文档

- [筛选清单](docs/screening-checklist.md)：看评论、地图、车库、包裹、楼层朝向时按这个过一遍。
- [资料源和核验方式](docs/data-sources.md)：哪些信息可以信，哪些只当营销。
- [Prompt 库](docs/prompt-library.md)：中文、英文、bilingual、房型图、评论审计、最终签约判断。
- [路线图](docs/roadmap.md)：后续可扩展的功能和内容。
- [贡献指南](CONTRIBUTING.md)：如何补公寓、修规则、加示例。

## 目录结构

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

## 筛选原则

- 评论和真实地理优先，不迷信官方网页、品牌、楼新或 `luxury` 营销。
- 后来的用户纠错优先于前面的 AI 推荐。
- MV/Sunnyvale/Santa Clara 的新楼大多是 podium/wood，不默认当全水泥 Type I。
- 木结构/混合结构默认死磕顶层 + 内院/遮挡朝向。
- 车库门禁不等于安全；要看砸车、尾随、摄像头、管理响应和短租/企业租客混杂。
- 外卖体验要看司机能否合法临停、是否容易找门、是否有室内监控 pickup 区。

## 贡献

欢迎补充新的公寓排雷、评论样本、房型图判断案例、英文 prompt 和文档改进。请不要提交个人隐私、租约、原始聊天全文、未打码地址或可识别信息。

## License

Apache-2.0. SPDX: `Apache-2.0`.
