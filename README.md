# Bank application – {{STUDENT}} (album {{ALBUM}})

Automated Testing course, University of Gdańsk.

A project developed step by step during the course. You write the code and the tests yourself.

## Running the tests

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest
```

## Structure

| Path | Purpose |
|---|---|
| `src/` | application code |
| `tests/unit/` | unit tests (pytest) |
| `.github/workflows/tests.yml` | CI: tests run on every push and pull request |
| `pytest.ini` | pytest configuration |

## Files for AI agents

| File | For whom | What it does |
|---|---|---|
| `AGENTS.md` | most AI tools | rules: the agent only reviews, it does not write code |
| `CLAUDE.md` | Claude Code | loads `AGENTS.md` |
| `GEMINI.md` | Gemini CLI | loads `AGENTS.md` |

In class, AI is used for code review only. You write the code and the tests yourself.

## Workflow

1. A new branch from `main` for every feature.
2. Test → minimal implementation → refactor → commit.
3. Push and open a pull request; merge once CI is green.
