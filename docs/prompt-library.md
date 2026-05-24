# Prompt Library / Prompt 库

Copy these prompts into Codex, ChatGPT, Claude, Gemini, or another AI assistant after loading `bay-area-rental` as a skill/project instruction.

## 中文：公寓横评

```text
Use bay-area-rental.
帮我比较下面这些湾区公寓，直接给主推/条件保留/备选/不推荐/淘汰。

我的优先级：
1. 安静睡眠
2. 车库和包裹安全
3. 外卖不容易丢
4. 自然光和隐私
5. 价格

预算：
城市/通勤：
户型：
候选：
- 公寓 A：
- 公寓 B：
- 公寓 C：
```

## 中文：评论排雷

```text
Use bay-area-rental.
我贴一些 Google Maps/Yelp/ApartmentRatings 评论给你。
请只做筛选，不要写 leasing 邮件。
帮我提取重复风险：砸车、包裹、外卖、噪音、虫害、管理、费用、搬出扣款。
最后给结论：继续看 / 条件保留 / 删掉。
```

## 中文：房型图/房号排序

```text
Use bay-area-rental.
根据这个 floorplan/site map 排房号。
重点看：楼层、朝向、窗户、内院/街道、垃圾房、电梯、车库门、amenity、Caltrain/expressway/SJC/Levi's。
输出表格：Rank / Unit / Verdict / Why / Risks / Conditions。
```

## English: Apartment Comparison

```text
Use bay-area-rental.
Compare these Bay Area apartments and label each as top pick, conditional, backup, not recommended, or eliminate.

Priorities:
1. Quiet sleep
2. Garage/package safety
3. Food delivery reliability
4. Natural light and privacy
5. Price

Budget:
Cities / commute:
Unit type:
Candidates:
- Apartment A:
- Apartment B:
- Apartment C:
```

## Bilingual Output

```text
Use bay-area-rental.
Rank these units in a bilingual Chinese/English table.
Keep apartment names and streets in English.
Explain risks in Chinese first, then short English notes.
```

## Final Sign/Apply Decision

```text
Use bay-area-rental.
我准备 apply/sign 之前最后确认。
请用最严格标准检查：
- 有没有近期严重差评？
- exact unit 有没有硬噪音源？
- 车库/包裹/外卖是否符合我的风险承受？
- 有哪些必须重新确认的信息？
最后只给：可以签 / 条件通过才签 / 不建议签。
```
