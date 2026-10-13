### Lesson 0003 - Boundaries: read-only vs write-only tools


from dotenv import load_dotenv
load_dotenv()  # load .env file if present

from langgraph.graph import StateGraph, MessagesState, START, END
from langchain.agents import create_agent


ORDERS = {
    '42': "veg momos x2"
}

REFUNDS = []

def get_order(order_id: str) -> str:
    """Look up an order by ID and return its details.

    Args:
        order_id (str): _description_

    Returns:
        str: _description_
    """
    return ORDERS.get(order_id, "unknown order")

def issue_refund(order_id: str) -> str:
    """Issue a refund for an order by ID. WRITES state.

    Args:
        order_id (str): _description_
    """
    REFUNDS.append(order_id)
    return f"Refund issued for order {order_id}"

def text_of(msg):
    """Return the text content of a message dict."""
    c = msg.content
    if isinstance(c, str):
        return c
    return chr(10).join(b.get('text', '') for b in c if isinstance(b, dict) and b.get('type') == 'text')

full = create_agent(
    model="claude-haiku-5-5",
    tools=[get_order, issue_refund],
    system_prompt="You are a support assistant."
)
readonly = create_agent(model='claude-haiku-5-5', tools=[get_order], system_prompt='You are a support assistant')
r1 = full.invoke({'messages': [{'role': 'user', 'content': 'refund order 42'}]})
print('FULL:', text_of(r1['messages'][-1])[:100])
print('REFUNDS:', REFUNDS)
r2 = readonly.invoke({'messages': [{'role': 'user', 'content': 'refund order 42'}]})
print('READONLY:', text_of(r2['messages'][-1])[:200])

# expect: FULL rfunds + REFUNDS ['42']; READONLY refuses, REFUNDS untouched by it