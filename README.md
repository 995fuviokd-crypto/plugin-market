# RikkaHub 插件市场

RikkaHub 官方插件索引仓库。客户端通过本仓库根目录的 `plugins.json` 读取已上架插件列表，并从 `plugins/<id>-<version>.zip` 下载安装。

## 结构

```
plugin-market/
├── plugins.json            # 已上架插件索引（客户端读取，仅含审核通过的插件）
├── submissions.json        # 提交审核队列（pending / approved / rejected）
├── plugins/                # 已上架插件包（zip，根目录含 plugin.json）
│   └── <id>-<version>.zip
├── submissions/            # 待审核插件包
│   └── <id>/<id>-<version>.zip
└── plugins-src/            # 插件源文件（便于审阅与修改）
```

## 插件提交与审核流程

1. **提交**：插件作者通过 RikkaHub 客户端「提交插件」功能（或提交仓库源码打包），将插件包上传到 `submissions/<id>/`，并在 `submissions.json` 登记 `status: pending` 条目（含名称、版本、作者、GitHub 仓库链接、提交者与提交时间）。
2. **审核**：管理员在审批后台（RikkaHub Plugin Review）审核待提交插件：通过则把包移入 `plugins/`、在 `plugins.json` 追加条目并标记 `approved`；拒绝则标记 `rejected` 并记录备注。只有 `plugins.json` 中列出的插件才会在客户端市场上架展示。
3. **收录 GitHub 高星插件**：审批后台支持搜索 GitHub 上高星的 MCP / Skill / 插件仓库并一键收录到待审核队列（要求仓库包含 `plugin.json` / `skills/` / `mcp.json` / `SKILL.md` 中至少一种可安装清单）。

## 插件包格式

一个插件是一个 zip 包，根目录必须有 `plugin.json`：

```json
{
  "id": "plugin-id",
  "name": "插件名称",
  "version": "1.0.0",
  "description": "插件描述",
  "author": "作者",
  "category": "development",
  "systemPrompt": "启用后注入助手系统提示的文本",
  "actions": [{ "label": "快捷操作", "prompt": "注入输入框的提示词" }],
  "type": "plugin",
  "tags": ["tag1", "tag2"]
}
```

- `type` 取值：`plugin` / `skill` / `mcp` / `json` / `other`
- 可选内容：`skills/` 目录（SKILL.md 技能）、`mcp.json`（MCP 服务器配置）、`extensionPoints`（设置页/主页动态入口）

## 如何贡献插件

1. 在 `plugins-src/<id>/` 下编写插件（根目录放 `plugin.json`），打包为 zip
2. 在 RikkaHub 客户端「提交插件」中上传，等待管理员审核
3. 审核通过后自动上架到 `plugins/` 与 `plugins.json`

## 已收录插件

| 插件 | 类型 | 说明 |
|------|------|------|
| web-search-pro | plugin | 联网搜索增强：多来源查证、权威优先、来源标注 |
| document-master | plugin | 文档解析助手：PDF/Word/PPT/EPUB 总结与要点提取 |
| code-reviewer | plugin | 代码审查助手：缺陷、安全、性能检查 |
| translation-pro | plugin | 翻译润色专家：中英互译、术语统一、格式保留 |
| prompt-optimizer | plugin | 提示词优化助手：结构化与对比优化 |
| mcp-fetch-sample | mcp | MCP 服务器配置示例（Fetch / Filesystem） |
| workflow-planner | skill | 任务规划技能：目标拆解与持续跟踪 |
