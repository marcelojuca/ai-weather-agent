"""Main module for the weather agent."""

from typing import Any

from langchain_core.messages import ToolMessage
from langgraph.graph import StateGraph
from langgraph.graph.message import MessagesState

from ai_weather_agent.tools.ai_weather_tools import get_current_weather


def _get_weather_tool_definition():
    """Get the tool definition for get_current_weather."""
    return {
        "name": "get_current_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": (
                        "The location to get weather for " "(e.g., 'Tokyo', 'New York')"
                    ),
                }
            },
            "required": ["location"],
        },
    }


def ai_weather_tool_node(state: MessagesState):
    tool_call = state["messages"][-1].tool_calls[0]
    if tool_call["name"] == "get_current_weather":
        location = tool_call["args"]["location"]
        weather = get_current_weather(location)
        result = (
            f"{location}: {weather['temp']}{weather['unit']}, {weather['condition']}"
        )
        return {"messages": [ToolMessage(content=result, tool_call_id=tool_call["id"])]}


def get_ai_weather_agent():
    """Create and return a compiled weather agent."""

    # Lazy-create the LLM to avoid import-time side effects and satisfy type checker
    def _create_llm(**kwargs: Any):
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(**kwargs)

    llm = _create_llm(model="gpt-4o-mini")

    # Bind the tool to the LLM so it knows how to call it
    tools = [_get_weather_tool_definition()]
    llm_with_tools = llm.bind_tools(tools)

    graph = StateGraph[MessagesState, None, MessagesState, MessagesState](MessagesState)
    graph.add_node(
        "agent", lambda state: {"messages": [llm_with_tools.invoke(state["messages"])]}
    )
    graph.add_node("tools", ai_weather_tool_node)

    graph.set_entry_point("agent")
    graph.add_conditional_edges(
        "agent", lambda s: "tools" if s["messages"][-1].tool_calls else "__end__"
    )
    graph.add_edge("tools", "agent")

    return graph.compile()
