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
  <img alt="Audience" src="https://img.shields.io/badge/audience-Bay%20Area%20Renters-orange">
  <img alt="Workflow" src="https://img.shields.io/badge/workflow-Reviews%20to%20Decision-purple">
</p>

> 把公寓名单变成排雷表，把房型图变成签约判断。

湾区租房排雷 Skill 是一个中英文可用的 Codex skill：把 Bay Area 公寓 listing、Google Maps/Yelp/ApartmentRatings 评论、房型图、楼层朝向和个人偏好，蒸馏成可执行的租房筛选结论。

它专门服务“安全、干净、安静、新一点、物业负责、不丢快递/外卖、不砸车”的租房需求，尤其适合筛 Sunnyvale、Mountain View、Santa Clara、North San Jose、Cupertino 一带的 `1B/1B`、studio 和具体房号。

这个 repo 只放蒸馏后的 skill 和参考规则，不包含原始 PDF/CSV/GPT 记录。

## 它能做什么

- 对比公寓候选：输出 `主推 / 条件保留 / 备选 / 不推荐 / 淘汰`。
- 背调评论风险：优先看近期差评、砸车、包裹丢失、虫害、薄墙、管理跑路、隐形费用。
- 排房号和朝向：结合楼层、窗户、内院/街道、Caltrain/BART/VTA、El Camino、San Tomas、SJC、Levi's、车库、垃圾房和 amenity 噪音。
- 蒸馏偏好记忆：默认避开 Irvine Company；Miro 默认排除，除非用户主动重新打开；不再把 Cobalt 当默认主推。
- 支持中英文输出：中文 prompt 默认中文，English prompt 默认 English，也可以要求 bilingual table。

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

## 安装

把 skill 文件夹复制到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills/bay-area-rental
rsync -a skills/bay-area-rental/ ~/.codex/skills/bay-area-rental/
```

然后在 Codex 里说：

```text
Use $bay-area-rental to screen these apartments.
```

## 目录结构

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

## 筛选原则

- 评论和真实地理优先，不迷信官方网页、品牌、楼新或 `luxury` 营销。
- 后来的用户纠错优先于前面的 AI 推荐。
- MV/Sunnyvale/Santa Clara 的新楼大多是 podium/wood，不默认当全水泥 Type I。
- 木结构/混合结构默认死磕顶层 + 内院/遮挡朝向。
- 车库门禁不等于安全；要看砸车、尾随、摄像头、管理响应和短租/企业租客混杂。
- 外卖体验要看司机能否合法临停、是否容易找门、是否有室内监控 pickup 区。

## License

Apache-2.0
