# Prefers learning by writing code (TODO scripts/notebooks)

User wants every lesson paired with a runnable code exercise — scripts with TODOs and/or Jupyter notebooks with TODOs — so they learn by writing, not just reading.

Evidence: user request 2026-10-12 ("learn by writing the code as well").
Implications: default to `exercises/NNNN-slug.py` per lesson (runs in `.venv`, built-in checks, no API key unless stated); link it from the lesson HTML; reach for notebooks only when visualization/iteration pays for the extra dependency.
