# Mission: LangChain / LangGraph / Deep Agents stack

## Why
Build AI agents with different purposes, specs, and boundaries (tools, permissions, memory, human-in-the-loop) — and know the stack cold enough to pick the right layer without guessing.

## Success looks like
- Given a spec ("research agent with file writes + approval before shell"), pick LangChain vs LangGraph vs Deep Agents and justify it in one sentence
- Build a minimal LangGraph `StateGraph` (node → edge → compile → invoke) from memory
- Build a `create_agent` tool-looping agent and a `create_deep_agent` with subagents/filesystem, each with a clear boundary (what it can/can't touch)
- Add persistence (checkpointer) + one human-in-the-loop interrupt to a graph

## Constraints
- Python only, in this repo's `uv` venv (`.venv`, Python 3.12)
- Priming repo next door: `../langgraph/` (official monorepo) — read, don't reinstall from it
- Short lessons: one thing per lesson, runnable without an API key unless stated

## Out of scope
- LangSmith deploy/evals deep-dives (until local agents are solid)
- JS/TS SDKs (`sdk-js`, LangGraph.js)
- Postgres checkpointers (SQLite/InMemory only for now)
