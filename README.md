# 后裔.skill

![后裔.skill banner](./assets/banner.svg)

<div align="center">

### 不是生孩子，是先把他聊出来。

如果你们真的有一个孩子，  
他会怎么和你说话？

![License](https://img.shields.io/badge/License-MIT-8BC34A?style=flat-square)
![OpenClaw](https://img.shields.io/badge/OpenClaw-Compatible-2D8BFF?style=flat-square)
![Skill](https://img.shields.io/badge/AgentSkill-Standard-8D52FF?style=flat-square)
![Same Age](https://img.shields.io/badge/Framing-Same--Age-47536F?style=flat-square)
![Creative](https://img.shields.io/badge/Mode-Creative%20Only-F28A58?style=flat-square)

</div>

---

## 2026 年了，所有人都在蒸人格。

但别人蒸的是一个人。  
`后裔.skill` 想做的是另一件事：

把你们两个人，长成第三个人。

不是复制谁。  
不是预测谁。  
不是判断“如果你们有孩子会是什么样”。  

而是：

`先看看你们之间，会不会长出一个能和你聊天的人。`

---

## 1 分钟安装

如果你只是想先装上跑起来，不用自己拼步骤：

```bash
./scripts/install-skill.sh
python3 ./scripts/smoke-test.py
```

如果你已经装好了 `ffmpeg` 和 `whisper`，再跑一次媒体链路验证：

```bash
python3 ./scripts/smoke-test.py --check-media
```

更完整的安装、目标目录选择、双 agent 挂载方式，看：

- [INSTALL.md](./INSTALL.md)
- [templates/openclaw-dual-agent.example.json](./templates/openclaw-dual-agent.example.json)

---

## 它是怎么工作的

你给它这些材料：

- 代表性聊天
- 语音或通话摘要
- 通话录音
- 短视频片段
- 图片描述
- 你自己写的偏向要求

它会输出：

- `portrait`
- `blend-lab`
- `future-snapshot`
- `session-voice`
- `preset-save`

也就是：

`原型 -> 变体 -> 场景 -> 会话人格 -> 可保存 preset`

---

## 现在也支持媒体接入层

这版新增了一个更实际的入口：

- 图片
- 通话录音
- 短视频

skill 会先把媒体整理成证据包，再进入人格合成流程。

如果本地环境有对应工具：

- `ffmpeg`
- `whisper`

它可以进一步做这些事：

- 从视频里抽音轨
- 从视频里抽关键帧
- 从录音里生成转写
- 输出一个结构化 `media-evidence-bundle.json`

如果本地没有这些工具，它也会优雅降级：

- 记录媒体清单
- 标记缺失能力
- 引导用户补 transcript 或 image notes

---

## 稳定运行建议

如果你想把它作为长期可用的公开 skill，而不是一次性 prompt，建议按这套方式跑：

- `life` 负责接收用户请求、维护对话和最终输出
- `coder` 负责本地脚本、媒体抽取、证据包整理
- 原始媒体先转成 `media-evidence-bundle.json`
- 再由 `relationship-descendant` 做人格合成

这样做的好处是：

- 日常对话 agent 不需要直接放开本地执行权限
- 媒体处理失败时更容易定位问题
- 图片 / 音频 / 视频和人格生成可以分层排错

---

## 它适合什么

- 双人关系衍生第三人格
- 同龄后代感角色
- 情侣 / 搭子 / 关系型 persona 设计
- 想把“关系氛围”做成一个能聊天的人格

## 它不适合什么

- 真实未来孩子预测
- 心理诊断
- 精确复刻私人人物
- 把输出当成现实中的谁的替代品

---

## 为什么它更像一个 skill，而不只是一个 prompt

因为它不是只吐一段文字。

它会先拆：

- 谁像谁
- 什么是共同继承
- 什么应该软化
- 什么可以长出新的特征

再决定：

- 做一个版本
- 做多个版本
- 写短场景
- 转会话人格
- 导出 preset

---

## 示例 Prompt

见 [examples.md](./examples.md)

## 演示输入

见 [demo-input.md](./demo-input.md)

## 示例输出

见 [sample-output.md](./sample-output.md)

## 长版 Demo 输出

见 [demo-output.md](./demo-output.md)

## 真实运行版 Demo 输出

见 [demo-output-live.md](./demo-output-live.md)

## 安装与稳定性说明

- [INSTALL.md](./INSTALL.md)
- [PRIVACY.md](./PRIVACY.md)
- [SECURITY.md](./SECURITY.md)

## 视觉素材

如果你要发 GitHub、发群、发动态，已经给你配好了：

- [banner.svg](./assets/banner.svg)
- [social-card.svg](./assets/social-card.svg)
- [cover-tile.svg](./assets/cover-tile.svg)

---

## 对外话术

最短一句：

> 不是生孩子，是先把他聊出来。

第二句：

> 如果你们真的有一个孩子，他会怎么和你说话？

解释句：

> 用你们的聊天、语气和关系氛围，长出一个可长期聊天的后裔感人格。

如果你想挑标题、仓库名或一句话简介，看：

- [naming-options.md](./naming-options.md)
- [store-copy.md](./store-copy.md)
- [launch-copy.md](./launch-copy.md)

---

## 真正的 skill 在哪

真正安装和发布用的是：

`skill/relationship-descendant`

这个目录已经通过基础校验。

---

## 最后一句

别人蒸一个人。  
`后裔.skill` 先把你们的“孩子”聊出来。
