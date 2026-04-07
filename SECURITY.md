# 安全说明

## 不要公开这些内容

- 你的 `openclaw.json`
- gateway token
- bot `appId` / `clientSecret`
- 任意模型 API key
- 含真实私密信息的 demo 原文

## 推荐发布习惯

- skill 单独一个公开仓库
- 本地运行配置不要进仓库
- 发布前手动检查最近一次提交
- demo 材料全部使用脱敏文本或虚构样例

## 最低检查清单

发布前至少确认：

1. 仓库里没有 `openclaw.json`
2. 仓库里没有 `.env`、token、secret、cookie
3. 所有截图和示例输出都去掉真实账号、头像、联系方式
4. 如果用了 QQ bot / webhook，发布前重置相关凭证

## 运行时建议

- 把高权限工具集中给 `coder` 一类 agent
- 主聊天 agent 尽量只保留组织和汇总能力
- 用本地媒体抽取替代把原始音视频直接发给远端模型
