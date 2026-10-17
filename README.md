# Aplikacja bankowa – {{STUDENT}} (album {{ALBUM}})

Testowanie automatyczne, Uniwersytet Gdański.

Projekt rozwijany krok po kroku na kolejnych zajęciach. Kod i testy piszesz samodzielnie.

## Uruchomienie testów

```bash
python3 -m pip install -r requirements.txt
python3 -m pytest
```

## Struktura

| Ścieżka | Po co |
|---|---|
| `src/` | kod aplikacji |
| `tests/unit/` | testy jednostkowe |
| `.github/workflows/tests.yml` | CI: testy uruchamiają się na każdym pushu i PR |
| `pytest.ini` | konfiguracja pytest |

## Pliki dla agentów AI

| Plik | Dla kogo | Co robi |
|---|---|---|
| `AGENTS.md` | większość narzędzi AI | zasady: agent robi tylko review, nie pisze kodu |
| `CLAUDE.md` | Claude Code | wczytuje `AGENTS.md` |
| `GEMINI.md` | Gemini CLI | wczytuje `AGENTS.md` |

Na zajęciach używamy AI wyłącznie do review. Kod i testy piszesz sam.

## Workflow

1. Nowa gałąź od `main` dla każdego feature'a.
2. Test → minimalna implementacja → refaktor → commit.
3. Push i pull request, merge po zielonym CI.
