# A Real Teacher From Your Slide

[English](README.md) | [中文](README.zh-CN.md)

A Real Teacher From Your Slide 是一个基于用户上传课程资料工作的学习 Skill。它可以把用户上传的学习材料转化成讲解、复习、练习、模拟考试和正式学习资料。

它适合用户上传 lecture slides、lecture notes、problem sheets、solutions、formula sheets、sample exams、past exams、revision guides 和老师给出的复习范围后使用。

GitHub 仓库名是 `real-teacher-from-your-slide`。Skill package / frontmatter 名称是 `a-real-teacher-from-your-slide`。

## 设计理念

1. 从用户上传的课程资料出发，而不是泛泛讲课。
2. 先帮助学生理解，再压缩成应试模板。
3. 用题目暴露薄弱点。
4. 生成 PDF、PPT、Markdown 等文件前先由用户确认。
5. 在不影响阅读体验的前提下保留资料依据。

## 快速开始

1. 先上传课程资料。
2. 选择基础学习路径、考试复习路径，或直接选择单个模式。
3. 选择输出形式：聊天、Markdown、PDF、PPT、公式表、练习题包或模拟卷。
4. 如果要生成长文件，先确认目录草案。
5. 根据需要继续使用讲题、批改、练习、模拟考试、抽背和考前压缩。

## 安装 / 使用

这个仓库采用平台无关设计。你可以在任何能够读取 Skill-style instruction bundle 或结构化 prompt workflow 的环境中使用它。

### 下载 Skill 安装包

从 v0.2.0 开始，每个版本都会在 [最新 GitHub Release](https://github.com/String020/real-teacher-from-your-slide/releases/latest) 附上校验过的 `a-real-teacher-from-your-slide.zip`。它和本地生成的文件相同，下载后可以直接看下面的安装步骤。

### 生成 Skill 安装包

如果想自己生成 ZIP，安装 Git 和 Python 3.10 或更新版本后，在终端运行以下命令（PowerShell 或 Bash 均可）：

```sh
git clone https://github.com/String020/real-teacher-from-your-slide.git
cd real-teacher-from-your-slide
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python scripts/package_skill.py
```

生成的文件是 `dist/a-real-teacher-from-your-slide.zip`。ZIP 内只有一个名为 `a-real-teacher-from-your-slide` 的顶层文件夹，包含 `SKILL.md`、参考文件、界面元数据和 MIT 许可证。Git 历史、开发工具和这些运行文件目录之外的文件不会打包。请勿把私人课程资料放入仓库的 `references/` 目录。

### 在本地 Codex 中使用

将 ZIP 内的 `a-real-teacher-from-your-slide` 文件夹解压到你选择的本地 Skill 目录。最终路径应为 `.agents/skills/a-real-teacher-from-your-slide/SKILL.md`，不要多嵌套一层同名文件夹。用户级安装的父目录是 `~/.agents/skills`（Windows 下为 `%USERPROFILE%\.agents\skills`）；项目级安装使用该项目的 `.agents/skills` 目录。

这些路径依据 [官方本地 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。如果你的环境或组织另行配置了 Skill 目录，请使用该目录。Codex 应能发现这个 Skill；如果没有显示，可以重启后再试。

安装后可以这样开始：

```text
使用 $a-real-teacher-from-your-slide 讲解附件中的课程笔记。
先用中文讲一个具体例子，保留 English technical terms，再问我一道检查题。
```

更新时，重新下载或生成安装包，保留个人修改后再替换已安装的 Skill 文件夹。卸载时，只删除这个 Skill 文件夹。其他支持 Skill 的环境也可以读取这套指令，但安装方式和文件生成能力可能不同。这个 ZIP 是本地 Skill 包，不是插件市场的 plugin。

### 检查修改

```sh
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

验证器检查 manifest、运行文件、界面元数据结构和参考文件路径。测试还检查解压后的可用性、本地文件排除、错误输入和可重复打包。它们不衡量教学质量，也不证明所有宿主环境兼容。GitHub Actions 会在 Windows 和 Linux 上运行这些检查，并提供 ZIP 工作流产物。只有维护者推送版本 tag 时才会发布 release，见 [发布版本](#发布版本)。

如果当前环境不能直接生成 PDF、PPT 或其他文件，可以让 AI 先输出干净的 Markdown 或可用于生成文件的目录草案。

## 第一次应该上传什么

推荐上传：

- 课堂 slides 或 lecture notes
- syllabus 或 weekly outline
- problem sheets 或 tutorial questions
- applied class materials
- solutions 或 marking guides
- formula sheets
- sample exams 或 mock exams
- past exams
- revision guides 或老师给出的考试范围

如果同时有课程内容资料和题目 / 考试资料，效果最好。

## 学习路径

### 基础学习路径

适合基础薄弱、没怎么学过，或者看课件看不懂的用户。

推荐流程：

`知识大纲 -> 教材式基础讲义 -> 单题教学 -> 练习题生成（基础练习） -> 考点大纲 -> 应试复习包 -> 解法批改 -> 模拟考试 -> 主动回忆 -> 考前压缩`

### 考试复习路径

适合已经学过课程，主要目标是复习考试、刷题和提分的用户。

推荐流程：

`考点大纲 -> 应试复习包 -> 单题教学 -> 解法批改 -> 练习题生成 -> 模拟考试 -> 主动回忆 -> 考前压缩`

这些路径只是建议。用户可以从任意模式开始，也可以跳过、重复或组合多个模式。

## 支持的学习模式

- **知识大纲**：整理课程结构、模块、前置知识和学习顺序。
- **考点大纲**：整理考试相关 topic、题型入口、公式条件和常见失分点。
- **教材式基础讲义**：生成像教材一样的学习资料，包含直观解释、定义、公式来源、例题、常见错误和练习。
- **应试复习包**：生成题型模板、公式使用条件、考试写法和速查表。
- **单题教学**：通过一道题复习相关知识，再详细解题和总结模板。
- **解法批改**：先诊断用户自己的解法，再指出第一个关键错误和正确写法。
- **练习题生成**：按模块、难度、题型或错题生成练习。
- **模拟考试**：根据范围和风格生成限时测试或模拟卷。
- **主动回忆 / 抽背**：一问一答训练公式、定义、方法选择和易错点。
- **考前压缩**：生成最后复习清单、题型入口、公式条件和常见错误。

## 文件生成

这个 Skill 可以在当前环境支持时生成聊天内容、Markdown、PDF、PPT、公式表、练习题包和模拟卷。

对于长 PDF、PPT 或长 Markdown，应该先生成目录或结构草案，等待用户确认后再生成正式内容。

PDF 应该像正式教材或讲义，而不是聊天记录导出。数学公式应使用 LaTeX 环境，中文字体要清晰可读，长文档应包含目录、页码、清晰的章节结构，并检查公式截断、乱码、文字重叠等问题。

## 学习工作区

当前环境可以写文件时，这个 Skill 可以把学习记录保存在你自己的课程文件夹里，下次对话或换一个 agent 也能接着上次继续：

- `teaching-outline.md`：教学知识点大纲，每个知识点有固定编号、学习目标、前置知识和资料出处。
- `progress.md`：每个知识点的掌握状态、依据、薄弱点、带日期的学习记录和下一步。
- `AGENTS.md`：告诉 agent 每次开始时先读这两个文件，以及如何更新它们。
- `CLAUDE.md`：只有一行 `@AGENTS.md`，给读取 `CLAUDE.md` 的环境使用。

只有在你要求或同意后才会创建这些文件，不会覆盖已有文件；知识点状态只会根据你的作答、抽背或测验结果更新。你也可以随时自己修改这些文件。

## 大量课程资料

一门课的文件很多或很长时，这个 Skill 会先快速摸底（文件名、页数、目录、前一两页），并保留每个文件自己的组织方式，不管它是按周、按 lecture、按章节、按主题，还是没有结构。然后：

- 如果装了 [MarkItDown](https://github.com/microsoft/markitdown) 这类本地工具，就用它把文件转成 Markdown，存进 `materials/` 并建索引。以后的对话直接读文字，不用每次重新解析 PDF；
- 当前环境支持子 agent 时，把阅读任务分给多个子 agent（环境允许时用便宜一些的模型），再把它们提取的知识点合并成教学大纲；
- 只有工具处理不了的内容，比如扫描页、乱码公式和重要的图表，才在讲到对应模块时由模型转写。

运行子 agent 或转换工具前会先问你一句，也不会未经允许安装软件。MarkItDown 转 PPTX 会保留幻灯片编号，但转 PDF 不保留页码，公式也需要对照原文件核对，所以 Skill 会补上页码标记，并标出没有文字层的页面。模拟卷还可以交给一个子 agent 独立解一遍，用来发现答案错误。

## 示例指令

### 学习工作区

- “在这个文件夹里给这门课建教学知识点大纲和 progress 文件，再加一个 AGENTS.md。”
- “按我的 progress 继续上次的学习。”

### 上传资料

- “我上传了 lecture slides 和 problem sheets，先告诉我这些资料能支持什么。”
- “根据这些课程资料生成知识大纲。”

### 补基础

- “帮我把这个 module 做成教材式基础讲义，适合基础薄弱学生。”
- “像教科书一样讲这个 topic，包括直观解释、公式来源、例题和常见错误。”

### 考试复习

- “根据这些 sample exams 和 problem sheets 生成考点大纲。”
- “为这个 topic 生成应试复习包，但不要在证据不足时判断高频。”

### 单题教学

- “帮我讲这题，先讲相关知识，再一步步解。”
- “我只是不懂这一步，不要重讲整章。”

### 解法批改

- “这是我的解法，帮我判断第一个错误在哪里。”
- “先批改我的思路，再给正确写法。”

### 练习题

- “根据这个 module 生成练习题，先问我要不要答案。”
- “根据我刚才错的题，生成三道考试风格变式题。”

### 模拟考试

- “帮我生成一个 module test，先问我要不要模仿 sample exam 风格。”
- “生成半套模拟卷，并附 marking guide。”

### PDF / PPT / Markdown

- “把这个 module 做成教材式 PDF，先给我目录草案。”
- “生成一页 Markdown 公式表。”
- “做成快速复习 PPT，不要写成详细教材。”

## 资料依据

正式学习资料应该把资料依据放在单独页面或单独章节，例如“Source Basis”“Resources Used”“Material Coverage”。这样既能保持可信，也不会破坏正文阅读体验。

## 学术诚信

这个项目用于学习、复习、练习、批改和模拟考试。不要用它绕过课程规则、完成正在进行的考试、冒充学生，或生成没有学习目的的可提交答案。

## 免责声明

本项目是学习辅助工具，不是官方课程资料，也不能替代课程政策、评分标准、老师说明或官方考试要求。用户需要自己遵守学术诚信规则。

## 局限性

- 输出质量取决于用户上传资料的完整性和质量。
- 考点优先级分析需要 sample exams、past exams、problem sheets 或老师给出的复习范围作为依据。
- PDF / PPT 等文件生成能力取决于当前环境工具。
- 本 Skill 不包含用户的课程文件。

## 开发者 / 维护者说明

仓库结构：

```text
real-teacher-from-your-slide/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── SKILL.md
├── requirements-dev.txt
├── .github/
│   ├── ISSUE_TEMPLATE/learning-feedback.md
│   └── workflows/
│       ├── validate.yml
│       └── release.yml
├── agents/
│   └── openai.yaml
├── references/
│   ├── mode-router.md
│   ├── material-intake.md
│   ├── knowledge-outline.md
│   ├── exam-outline.md
│   ├── foundation-guide.md
│   ├── exam-strategy-pack.md
│   ├── problem-tutor.md
│   ├── attempt-diagnosis.md
│   ├── practice-generator.md
│   ├── mock-exam.md
│   ├── active-recall.md
│   ├── exam-compression.md
│   ├── artifact-quality.md
│   ├── source-grounding.md
│   ├── study-workspace.md
│   ├── parallel-intake.md
│   ├── example-workflows.md
│   └── academic-integrity.md
├── evals/
│   ├── README.md
│   ├── cases.json
│   └── fixtures/
├── scripts/
│   ├── validate_skill.py
│   ├── package_skill.py
│   └── eval_case.py
└── tests/
    └── test_package_skill.py
```

`SKILL.md` 是 Skill 入口文件，具体模式规则放在 `references/` 中，方便后续独立修改。

### 发布版本

1. 在 `CHANGELOG.md` 中把这次发布的条目放到 `## vX.Y.Z` 标题下，并把这次修改合并到 `main`。
2. 给合并后的提交打 tag 并推送：

   ```sh
   git tag v0.2.0
   git push origin v0.2.0
   ```

3. 发布工作流会先校验和测试安装包，然后发布一个以 tag 命名的 GitHub Release，附上 ZIP，并用该版本的 changelog 小节作为说明。如果 `CHANGELOG.md` 里没有这个 tag 对应的小节，工作流会失败，不会发布。

## 许可证

MIT License。见 [LICENSE](LICENSE)。

## 反馈与贡献

欢迎使用 learning-feedback issue 模板，描述具体的学习问题或有帮助的使用经历，中英文均可。请使用自制示例，不要公开私人课程资料或学生信息。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)，可复现的教学检查方法见 [evals/README.md](evals/README.md)。
