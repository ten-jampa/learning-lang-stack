## Your first tool-loop with `create_agent`

"""
Four new words, then code


1. Tool
- a python function
2. Tool call
- the mode's structured request. 'call get_weather with city ='sf'.
3. The loop
- create_agent's whole job: send messages to the model →
 if the model requests a tool call, run it and append the result →
 repeat until the model answers directly. You never write this loop; the harness owns it (lesson 1's hook).
4. System Prompt
instrcutions prepended to every run/turn
"""

from json import tool

from dotenv import load_dotenv
load_dotenv()  # load .env file if present
import os

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")

from langgraph.graph import StateGraph, MessagesState, START, END
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """A tool that returns a weather report for a given city."""
    return f"The weather in {city} is sunny and 75 degrees."

def get_time(city: str) -> str:
    """A tool that returns the current time for a given city."""
    return f"The current time in {city} is 2:00 PM EST."

dumb_agent = create_agent(
    model="claude-haiku-5-5",
    tools = [get_weather, get_time],
    system_prompt="You are a helpful assistant that can provide weather and time information.",
)

out = dumb_agent.invoke(
    {'messages': [
        {'role': 'user',
        'content': 'What is the weather in BBoston and the time there?'
        }
        ]
    }
)

print(out['messages'][-1].content)  # should contain the weather report for San Francisco

