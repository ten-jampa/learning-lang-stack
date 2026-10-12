# LangChain / LangGraph / Deep Agents Resources

## Knowledge

- [LangGraph overview (OSS Python)](https://docs.langchain.com/oss/python/langgraph/overview)
  Canonical layer definitions: LangChain = framework, LangGraph = orchestration runtime, Deep Agents = harness. Use for: every "which layer?" decision.
- [LangChain agents — `create_agent`](https://docs.langchain.com/oss/python/langchain/agents)
  Minimal ReAct harness on top of LangGraph. Use for: tool-loop agents without custom graphs.
- [Deep Agents README](https://github.com/langchain-ai/deepagents/blob/main/README.md)
  Opinionated harness: subagents, filesystem, context mgmt, skills, HITL. Use for: when to reach for `create_deep_agent` vs dropping to LangGraph.
- [Build overview — the stack](https://docs.langchain.com/build-overview)
  One-page map of Build/Test/Deploy/Monitor. Use for: eagle's-eye view of where local code meets LangSmith.
- [Priming repo: `../langgraph/`](file:///Users/tenzinjampa/Documents/learning-repos/langgraph)
  Official monorepo (`libs/langgraph`, `libs/prebuilt`, `libs/checkpoint*`). Use for: reading real `StateGraph`/`create_react_agent` source when docs are vague.

## Wisdom (Communities)

- [LangChain forum / GitHub discussions](https://github.com/langchain-ai/langgraph/discussions)
  High-signal troubleshooting for graph semantics. Use for: stuck-on-behavior questions after a minimal repro.
- [r/LangChain](https://www.reddit.com/r/LangChain/)
  Mixed signal; useful for pattern comparison. Use for: "how are others scoping agent boundaries?" sanity checks.

## Gaps

- Version-pinned API diffs (fast-moving repo) — verify against installed versions (`langgraph 1.2.14`, `langchain 1.4.4`, `deepagents 0.7.24`) before trusting examples.
