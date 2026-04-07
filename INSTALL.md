# 安装说明

这份公开包默认把 `后裔.skill` 当成一个可复制安装的 OpenClaw skill。

## 前置条件

- 已安装 OpenClaw
- 已有一个可写的 skills 目录
- 如果要跑本地媒体链路：
  - `ffmpeg`
  - `whisper`

## 方式一：Linux / macOS / WSL

在仓库根目录执行：

```bash
chmod +x ./scripts/install-skill.sh
./scripts/install-skill.sh
```

默认安装逻辑：

1. 如果检测到 `~/.openclaw/workspaces/life/skills`
   就安装到这个目录
2. 否则安装到 `~/.openclaw/skills`

手动指定目标目录：

```bash
./scripts/install-skill.sh ~/.openclaw/workspaces/life/skills
```

## 方式二：Windows PowerShell

在仓库根目录执行：

```powershell
./scripts/install-skill.ps1
```

默认安装逻辑：

1. 如果检测到 `$HOME\.openclaw\workspaces\life\skills`
   就安装到这个目录
2. 否则安装到 `$HOME\.openclaw\skills`

手动指定目标目录：

```powershell
./scripts/install-skill.ps1 -TargetDir "$HOME\.openclaw\skills"
```

## 安装后验证

先跑结构检查：

```bash
python3 ./scripts/smoke-test.py
```

如果本机已经装好 `ffmpeg` 和 `whisper`，再跑媒体链路检查：

```bash
python3 ./scripts/smoke-test.py --check-media
```

## 挂到 agent

如果你已经有自己的 agent 配置，只需要把 skill 名字加进去：

```json
{
  "skills": [
    "relationship-descendant"
  ]
}
```

如果你要参考双 agent 结构，看：

- `templates/openclaw-dual-agent.example.json`

推荐分工：

- `life`：接收用户输入、组织材料、输出最终人格
- `coder`：运行本地脚本、做媒体抽取、生成 evidence bundle

## 媒体链路建议

如果主聊天 agent 不允许 `exec/process`：

- 不要强行给它提权
- 让它把媒体抽取任务转交给一个能跑脚本的 agent

推荐流程：

1. `life` 收到图片 / 音频 / 视频
2. `coder` 运行 `scripts/extract-media-bundle.py`
3. `coder` 返回 evidence bundle 路径和摘要
4. `life` 再调用 `relationship-descendant` 做人格合成

## 最后检查

公开发布前，至少确认：

- README 可读
- `agents/openai.yaml` 已同步
- `scripts/smoke-test.py` 通过
- 没把你自己的 `openclaw.json`、token、bot secret 一起发出去
