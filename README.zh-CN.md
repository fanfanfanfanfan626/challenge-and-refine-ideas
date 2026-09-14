# Idea Council（想法议事会）

[产品网页](https://fanfanfanfanfan626.github.io/challenge-and-refine-ideas/) · [English](README.md) · [AI 安装说明](AI_INSTALL.md) · [使用示例](EXAMPLES.md) · [兼容性证据](COMPATIBILITY.md) · [下载 v2.0.3 ZIP](dist/challenge-and-refine-ideas-v2.0.3.zip) · [更新记录](CHANGELOG.md)

`challenge-and-refine-ideas` 是一个在实施之前帮助用户探索、完善、比较、反证和决定想法的 Agent Skill。它始终由一个主持人面对用户，并根据真正影响决策的不确定性，选择最轻量的推理视角或隔离顾问组合。

它优先适配 Codex，也可以迁移到支持本地 Skill 的其他 Agent 平台；如果需要真正独立的顾问会议，平台还必须支持干净的子 Agent 上下文。目录格式兼容不等于已经完成真实宿主验证，边界见 [COMPATIBILITY.md](COMPATIBILITY.md)。

## 核心特点

- 正式讨论前先确认当前问题框架，避免围绕错误命题深入讨论。
- 探索阶段可以保持开放，不强行生成推荐或结论。
- 反方必须攻击当前最新方案，而不是用户已经放弃的旧草案。
- 顾问独立性和外部现实证据分开报告。
- 每个重要反对意见都有稳定编号和规范状态，不能在总结时消失。
- 当事实才是瓶颈时，优先寻找真正会改变决定的支持与反证。
- 高风险事项不能因为多个 Agent 同意就越过专业、法律、安全或授权门禁。
- 只有证据对准确范围足够，并且人类明确授权，才能交给执行流程。

## 五种会议目的

| 目的 | 含义 |
| --- | --- |
| `explore` | 打开可能性、发现真正含义，不强迫收敛 |
| `refine` | 完善当前方案，补上真正影响结果的缺口 |
| `compare` | 按人类拥有的标准比较真实备选方案 |
| `challenge` | 先强化当前候选方案，再尝试拒绝或重塑它 |
| `decide` | 明确选择、异议、证据充分性和下一项承诺 |

系统会自动选择 `quick-refine`、`guided-workshop`、`independent-council`、`evidence-first` 或 `decision-review`，不会把 Agent 数量、拓扑和模型预算丢给用户配置。

## 独立性不等于证据

顾问独立性分为：

| 等级 | 含义 |
| --- | --- |
| `L0` 串行视角 | 同一上下文应用多个视角，快速但相关性较高 |
| `L1` 隔离备忘录 | 独立顾问只收到有限任务包，不继承其他意见 |
| `L2` 盲反证 | 反方在看不到主持人主张的情况下攻击中性的当前方案 |

外部依据另行标记为 `none`、`primary-source`、`field`、`experimental` 或 `operational`。多个 Agent 得出同一结论，绝不会自动变成市场、法律、医疗、技术或用户证据。

## 三轴状态系统

Idea Charter 分开记录三件不同的事：

```text
想法成熟度：raw → framed → expanded → challenged → decision-ready
证据状态：discussion-useful | test-needed | review-needed | sufficient-for-scope
人类态度：undecided | adopted | parked | rejected
```

因此它可以准确表达：方案已经充分反证，人类暂时采用方向，但因为还缺法律或安全审查，不能进入上线阶段。

## 在 Codex 中安装

真正可安装的目录是 [`skill/challenge-and-refine-ideas`](skill/challenge-and-refine-ideas)。仓库文档和发布工具没有混入 Skill 本体。

### Windows PowerShell

```powershell
git clone https://github.com/fanfanfanfanfan626/challenge-and-refine-ideas.git
$destination = Join-Path $env:USERPROFILE ".codex\skills\challenge-and-refine-ideas"
New-Item -ItemType Directory -Force (Split-Path $destination) | Out-Null
Copy-Item ".\challenge-and-refine-ideas\skill\challenge-and-refine-ideas" $destination -Recurse
```

### macOS 或 Linux

```bash
git clone https://github.com/fanfanfanfanfan626/challenge-and-refine-ideas.git
mkdir -p ~/.codex/skills
cp -R challenge-and-refine-ideas/skill/challenge-and-refine-ideas ~/.codex/skills/challenge-and-refine-ideas
```

重启 Codex 后可以这样调用：

```text
使用 $challenge-and-refine-ideas 探索这个想法，暂时不要强迫得出结论。找出实质不同的解释，并问一个最可能改变方向的问题。
```

仓库还提供经过审查的独立分发包：[`dist/challenge-and-refine-ideas-v2.0.3.zip`](dist/challenge-and-refine-ideas-v2.0.3.zip)。包内包含 MIT 许可证。

```text
SHA-256: 24D940A87FD45DDF1608BBE734999A9E2168526DFDCD1DE6D5BF55266470A11F
```

如果让另一个 AI 安装，请把 [AI_INSTALL.md](AI_INSTALL.md) 交给它。

## 边界

- Skill 只负责完善和反证意图；没有单独的明确请求时，不会进入实施。
- 未得到用户同意并确定路径前，不创建或覆盖 Idea Charter 文件。
- 不模拟庞大董事会，不用投票制造真相，也不以平衡措辞抹掉异议。
- Agent 会议不能替代真实用户、实验、市场证据、专业人士、知情同意或法律授权。
- 平台不能提供干净隔离上下文时，即使出现多个 Agent 名称，也必须标记为 `L0`。

可直接复制的探索、比较、反证和高风险场景见 [EXAMPLES.md](EXAMPLES.md)。

## 本地验证

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_release.py
```

发布验证器会检查目录结构、frontmatter、显示元数据、引用文件、核心协议不变量、本机路径和密钥泄漏，以及 ZIP 内容和公开 SHA-256。GitHub Actions 会在每次推送和拉取请求时自动执行。

## 开源协议

MIT，见 [LICENSE](LICENSE)。

问题与参与规则见 [SUPPORT.md](SUPPORT.md)、[CONTRIBUTING.md](CONTRIBUTING.md) 和 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。敏感问题请按 [SECURITY.md](SECURITY.md) 处理，不要公开提交细节。

## 相关项目

- [Mastery Tutor](https://github.com/fanfanfanfanfan626/mastery-tutor)：让兼容的 AI Agent 成为本地优先的掌握式学习导师。
- [Persistent AI Studio](https://github.com/fanfanfanfanfan626/orchestrate-agent-organization)：把已授权的产品工作从发现阶段延续到交付、运营和维护。
- [Skill Governor](https://github.com/fanfanfanfanfan626/skill-governor)：审计和维护存在重叠的 Agent Skill 库。
