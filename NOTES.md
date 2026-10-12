# Notes

- Python-only. All lessons run in `.venv` (`source .venv/bin/activate` or `.venv/bin/python`).
- Prefers fundamentals-first, step-by-step, occasional eagle's-eye view. Light gamification welcome.
- Wants honest critique, not agreement. Verify package names/URLs before instructing.
- Learning mode: code-by-writing. Every lesson ships a runnable `exercises/*.py` script (uv venv) with TODOs + built-in PASS/FAIL checks; Jupyter optional, scripts default. Lesson HTML links the exercise.
- Open lessons with: `open lessons/<file>.html` (macOS).
- After every finished lesson: run `sh scripts/finish-lesson.sh "<lesson> <outcome>"` (commit + push). Never push `.env` (gitignored — the script respects it).
