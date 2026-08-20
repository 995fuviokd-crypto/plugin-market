# RikkaHub 插件市场

RikkaHub 官方插件索引仓库。客户端通过本仓库根目录的 `plugins.json` 读取插件列表，并从 `plugins/<id>-<version>.zip` 下载安装。

## 结构

```
plugin-market/
├── plugins.json            # 插件索引（客户端读取）
├── plugins/                # 插件包（zip，根目录含 plugin.json）
│   └── <id>-<version>.zip
└── plugins-src/            # 插件源文件（便于审阅与修改）
```

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

1. 克隆本仓库
2. 在 `plugins-src/<id>/` 下编写插件（根目录放 `plugin.json`）
3. 打包为 `plugins/<id>-<version>.zip`
4. 在 `plugins.json` 中追加对应条目（`downloadUrl` 指向 `https://github.com/995fuviokd-crypto/plugin-market/raw/main/plugins/<id>-<version>.zip`）
5. 提交 PR

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
