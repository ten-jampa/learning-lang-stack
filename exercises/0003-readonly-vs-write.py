"""Lesson 0003 exercise: prove boundaries by absence.

Run:  .venv/bin/python exercises/0003-readonly-vs-write.py
Win:  all checks print PASS. Needs .env key + network (2 small Haiku calls).

Fill each TODO, then re-run. Checks tell you immediately what's wrong.
"""

from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
_passed, _failed = 0, 0


def check(name, cond):
    global _passed, _failed
    if cond:
        _passed += 1
        print(f"PASS  {name}")
    else:
        _failed += 1
        print(f"FAIL  {name}")


def text_of(msg):
    c = msg.content
    if isinstance(c, str):
        return c
    return "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")


ORDERS = {"42": "veg momos x2"}
REFUNDS = []


# TODO 1: define both tools. get_order reads ORDERS (unknown id -> "unknown order").
# issue_refund appends to REFUNDS and returns f"refunded {order_id}".
# Both need docstrings (the model's manual).
def get_order(order_id: str) -> str:
    # TODO: docstring + return ORDERS.get(order_id, "unknown order")
    """for a given order id, retreives the details of the order

    Args:
        order_id (str): _description_

    Returns:
        str: the details of the order if found, otherwise "unknown order"
    """
    return ORDERS.get(order_id, "unknown order")


def issue_refund(order_id: str) -> str:
    # TODO: docstring + REFUNDS.append(order_id) + return f"refunded {order_id}"
    """for a given order with the given order id, issue refund

    Args:
        order_id (str): the id of the order to issue a refund for

    Returns:
        str: confirmation message that the refund has been issued
    """
    REFUNDS.append(order_id)
    return f"refunded {order_id}"


check("TODO1: read tool correct", get_order("42") == "veg momos x2" and get_order("7") == "unknown order")
check("TODO1: both have docstrings", bool(get_order.__doc__) and bool(issue_refund.__doc__))
issue_refund("probe")
check("TODO1: write tool mutates world", REFUNDS == ["probe"])
REFUNDS.clear()


# TODO 2: build the READ-ONLY agent (get_order only) on claude-haiku-5-5.
# Hint: create_agent(model="claude-haiku-5-5", tools=[get_order], system_prompt="You are a support assistant")
readonly = create_agent(
                        model="claude-haiku-5-5",
                        tools=[get_order],
                        system_prompt="You are a support assistant"
                        )  # TODO: replace (don't forget the import)
# --- your code here ---
# ----------------------

check("TODO2: readonly agent built", readonly is not None)


# TODO 3: ask the readonly agent to refund order 42.
# Then prove the boundary held: REFUNDS must still be [].
if readonly is not None:
    r = readonly.invoke({"messages": [{"role": "user", "content": "refund order 42"}]})
    t = text_of(r["messages"][-1]).lower()
    check("TODO3: world untouched (no refund recorded)", REFUNDS == [])
    check("TODO3: agent said it can't", any(w in t for w in ["can't", "cannot", "unable", "only have", "read-only", "read only"]))
else:
    check("TODO3: invoked", False)
    check("TODO3: agent said it can't", False)


# TODO 4: build the FULL agent (both tools) and ask it to refund order 42.
# Prove the grant worked: REFUNDS must equal ["42"].
full = create_agent(
    model="claude-haiku-5-5",
    tools=[get_order, issue_refund],
    system_prompt="You are a support assistant"
)  # TODO: replace with create_agent carrying both tools
# --- your code here ---
# ----------------------

if full is not None:
    full.invoke({"messages": [{"role": "user", "content": "refund order 42"}]})
    check("TODO4: grant worked (refund recorded)", REFUNDS == ["42"])
else:
    check("TODO4: grant worked (refund recorded)", False)


print(f"\n{_passed} passed, {_failed} failed.")
if _failed:
    raise SystemExit(1)
print("All green — lesson 0003 exercise complete.")
