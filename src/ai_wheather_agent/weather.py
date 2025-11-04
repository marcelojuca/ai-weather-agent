# agents/weather.py
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, StateGraph
from tools.weather import get_current_weather

llm = ChatOpenAI(model="gpt-4o-mini")


def weather_tool_node(state: MessagesState):
    tool_call = state["messages"][-1].tool_calls[0]
    if tool_call["name"] == "get_current_weather":
        location = tool_call["args"]["location"]
        weather = get_current_weather(location)
        return {"messages": [f"{location}: {weather['temp']}°C, {weather['condition']}"]}


graph = StateGraph(MessagesState)
graph.add_node("agent", lambda state: {"messages": [llm.invoke(state["messages"])]})
graph.add_node("tools", weather_tool_node)

graph.set_entry_point("agent")
graph.add_conditional_edges("agent", lambda s: "tools" if s["messages"][-1].tool_calls else "__end__")
graph.add_edge("tools", "agent")

get_weather_agent = graph.compile()
