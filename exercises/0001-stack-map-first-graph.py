"""Lesson 0001 exercise: build the stack's smallest shapes from memory.

Run:  .venv/bin/python exercises/0001-stack-map-first-graph.py
Win:  all checks print PASS. No API key needed.

Fill each TODO, then re-run. Checks tell you immediately what's wrong.
"""

from langgraph.graph import  MessagesState, START, END


# Check tools ---------------------------------------------------------------
_passed, _failed = 0, 0


def check(name, cond):
    global _passed, _failed
    if cond:
        _passed += 1
        print(f"PASS  {name}")
    else:
        _failed += 1
        print(f"FAIL  {name}")


# TODO 1: import StateGraph (extend the import above).
# Hint: from langgraph.graph import StateGraph, MessagesState, START, END
try:
    from langgraph.graph import StateGraph, MessagesState, START, END
    g = StateGraph(MessagesState)
except NameError:
    StateGraph = None  # TODO: fix the import so this line is unnecessary

check("TODO1: StateGraph imported", StateGraph is not None)


# TODO 2: write the stub node. It must return {"messages": [...]} with one
# ai message whose content is "hello world".
def mock_llm(state: MessagesState):
    # TODO: return {"messages": [{"role": "ai", "content": "hello world"}]}
    return {"messages": [{"role": "ai", "content": "hello world"}]}  # <-- replace this line


out_probe = mock_llm({"messages": [{"role": "user", "content": "hi"}]})
check(
    "TODO2: node returns one ai 'hello world' message",
    out_probe.get("messages", [{}])[-1].get("content") == "hello world"
    if out_probe.get("messages") else False,
)


# TODO 3: wire the graph — one node, START -> node -> END — then compile.
# Hint: g = StateGraph(MessagesState); g.add_node(...); g.add_edge(...); app = g.compile()
g = StateGraph(MessagesState) # initialize the graph
g.add_node("llm", mock_llm)  # add the mock_llm
g.add_edge(START, "llm")  # connect START to mock_llm/llm node
g.add_edge('llm', END)  # connect mock_llm/llm node to END

"""
start -> llm (mock_llm) -> end
"""

app = g.compile() # TODO: replace with your compiled graph
# --- your code here ---
# ----------------------

check("TODO3: graph compiled", app is not None)
if app is not None:
    out = app.invoke({"messages": [{"role": "user", "content": "hi"}]})
    check(
        "TODO3: invoke ends with 'hello world'",
        out["messages"][-1].content == "hello world",
    )


# TODO 4 (no code — one sentence, as a string): which layer for
# "research agent with planning + subagents + filesystem out of the box"?
# Set ANSWER4 to exactly one of: "langchain" | "langgraph" | "deepagents"
ANSWER4 = "deepagents"  # TODO: e.g. ANSWER4 = "deepagents"  (only if that's your answer)

check("TODO4: correct layer picked", ANSWER4 == "deepagents")


print(f"\n{_passed} passed, {_failed} failed.")
if _failed:
    raise SystemExit(1)
print("All green — lesson 0001 exercise complete.")
