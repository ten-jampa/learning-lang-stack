"""Lesson 0002 exercise: scope a one-tool agent and run the loop.

Run:  .venv/bin/python exercises/0002-first-tool-loop.py
Win:  all checks print PASS. Final check needs .env key + network.

Fill each TODO, then re-run. Checks tell you immediately what's wrong.
"""

from dotenv import load_dotenv

load_dotenv()

_passed, _failed = 0, 0


def check(name, cond):
    global _passed, _failed
    if cond:
        _passed += 1
        print(f"PASS  {name}")
    else:
        _failed += 1
        print(f"FAIL  {name}")


# TODO 1: define the tool. Plain function + docstring (the model's manual).
# It must accept a city and return "It's always sunny in {city}!".
def get_weather(city: str) -> str:
    # TODO: add docstring "Get weather for a given city." and return the sunny string
    """Get weather for a given city.

    Args:
        city (str): The name of the city to get the weather for.

    Returns:
        str: A string of the weather report for the given city.
    """
    return f"It's always sunny in {city}!"  # <-- replace this line


check("TODO1: docstring present", bool(get_weather.__doc__))
check("TODO1: stub returns sunny string", get_weather("sf") == "It's always sunny in sf!")


# TODO 2: build the agent. Import create_agent, pass model + tools + system prompt.
# Hint: create_agent(model="claude-haiku-5-5", tools=[get_weather], system_prompt="You are a helpful assistant")
from langchain.agents import create_agent
agent = create_agent(
    model="claude-haiku-5-5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant that can provide weather information.",
)   # TODO: replace with your create_agent(...) call
# --- your code here (don't forget the import) ---
# -------------------------------------------------

check("TODO2: agent built", agent is not None)


# TODO 3: run it. Invoke with a user message asking about SF weather.
# Hint: agent.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})
out = agent.invoke(
    {"messages": [{"role": "user", 
                   "content": "what is the weather in sf"
                   }]}
)  # TODO: replace with your invoke call
# --- your code here ---
# ----------------------

if out is not None:
    final = out["messages"][-1].content
    check("TODO3: answer mentions sunny/San Francisco", "sunny" in final.lower())
else:
    check("TODO3: invoked", False)


# TODO 4 (no code — one sentence, as a string): who executes get_weather,
# the model on its servers or the harness locally? Answer: "model" | "harness"
ANSWER4 = "harness"  # TODO: e.g. ANSWER4 = "harness" (only if that's your answer)

check("TODO4: correct executor named", ANSWER4 == "harness")


print(f"\n{_passed} passed, {_failed} failed.")
if _failed:
    raise SystemExit(1)
print("All green — lesson 0002 exercise complete.")
