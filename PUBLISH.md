# Publish Checklist

## 1. Validate the package structure

```bash
python3 ./scripts/smoke-test.py
```

## 2. Optional: validate the OpenClaw skill format

```bash
python ~/.npm-global/lib/node_modules/openclaw/skills/skill-creator/scripts/quick_validate.py ./skill/relationship-descendant
```

## 3. Review the public-facing metadata

Check:

- `skill/relationship-descendant/SKILL.md`
- `skill/relationship-descendant/agents/openai.yaml`
- `README.md`
- `INSTALL.md`
- `PRIVACY.md`
- `SECURITY.md`

## 4. Make sure the public pitch is clean

Good pitch:

- fictional same-age successor persona studio
- relationship-derived third persona

Bad pitch:

- predicts your real future child
- exposes true psychology from chat logs

## 5. Scrub secrets and local config

Before publish, confirm:

- no `openclaw.json`
- no API keys
- no bot secrets
- no real private chat exports

## 6. Initialize git

```bash
git init
git add .
git commit -m "Initial public release of relationship-descendant"
```

## 7. Push to GitHub

Create a GitHub repo, then:

```bash
git remote add origin <your-repo-url>
git branch -M main
git push -u origin main
```

## 8. Optional ClawHub publish

If you install the `clawhub` CLI and have publish access:

```bash
clawhub auth login
clawhub skill publish ./skill/relationship-descendant --slug relationship-descendant-studio
```

## 9. After publish

Prepare for iteration:

- collect 5 to 10 real prompts
- note where the skill overcommits or gets too vague
- tighten `SKILL.md`
- collect at least 1 image, 1 audio, 1 video real-world media run
- republish updates
