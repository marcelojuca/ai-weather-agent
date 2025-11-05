"""Main module for the weather agent."""

from typing import Any

from langgraph.graph import StateGraph
from langgraph.graph.message import MessagesState

from ai_weather_agent.tools.ai_weather_tools import get_current_weather


def ai_weather_tool_node(state: MessagesState):
    tool_call = state["messages"][-1].tool_calls[0]
    if tool_call["name"] == "get_current_weather":
        location = tool_call["args"]["location"]
        weather = get_current_weather(location)
        return {"messages": [f"{location}: {weather['temp']}{weather['unit']}, {weather['condition']}"]}


def get_ai_weather_agent():
    """Create and return a compiled weather agent."""

    # Lazy-create the LLM to avoid import-time side effects and satisfy type checker
    def _create_llm(**kwargs: Any):
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(**kwargs)

    llm = _create_llm(model="gpt-4o-mini")

    graph = StateGraph[MessagesState, None, MessagesState, MessagesState](MessagesState)
    graph.add_node("agent", lambda state: {"messages": [llm.invoke(state["messages"])]})
    graph.add_node("tools", ai_weather_tool_node)

    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", lambda s: "tools" if s["messages"][-1].tool_calls else "__end__")
    graph.add_edge("tools", "agent")

    return graph.compile()
