# MODULE 3: Deep Dive into LangGraph

## 🎯 Goal
Understand how LangGraph works and how it enables AI agents to think, make decisions, and use tools.

## What You'll Learn

In Module 2, you learned the **development workflow** (TDD with pytest-watch, code quality with ruff, commit gates with pre-commit).

In Module 3, you'll learn **how to build AI agents** - specifically how LangGraph lets you create agents that:
- 🤖 Think about user input (using an LLM)
- 🔧 Decide whether to use tools (weather API, search, etc.)
- 🔄 Loop back to refine answers (agent can think again with tool results)
- 📨 Maintain conversation history (know what happened before)

## The Big Picture

You already know that an **AI agent** is:
```
User Input → Agent Thinks → Decides → Uses Tools → Responds
```

**LangGraph** is the framework that makes this easy. It lets you build this workflow as a **graph**:

```
┌──────────────┐
│  Agent Node  │ ← Agent thinks, decides what to do
│              │
└──────┬───────┘
       ↓
    Should use tool?
       ├─→ YES → ┌──────────────┐
       │         │  Tool Node   │ ← Tool gets called
       │         └──────┬───────┘
       │                ↓
       │         Result added to state
       │                ↓
       │         Loop back to Agent Node
       │
       └─→ NO  → ┌──────────────┐
                 │ Return Answer│ ← Done!
                 └──────────────┘
```

This is exactly what you'll build in the coming lessons!

## Module 3 Structure

### Lesson 3.1: StateGraph Concept
- What is a StateGraph (the blueprint for agents)
- What is State (data passed between nodes)
- Understanding MessagesState

### Lesson 3.2: Nodes
- Creating processing steps (nodes)
- Agent node, Tool node, Decision node examples
- How nodes process state

### Lesson 3.3: Edges and Routing
- Connecting nodes with edges
- Direct edges vs conditional edges
- How the graph decides where to go next

### Lesson 3.4: The Complete Graph
- Compiling the graph (blueprint → executable)
- Invoking the graph (running it with user input)
- Seeing the graph execute step by step

### Lesson 3.5: Weather Agent Structure
- Real example: how your weather agent will be structured
- Agent node (thinks about question)
- Tool node (calls weather API)
- Decision logic (should we use tools or respond?)

### Lesson 3.6: MessagesState Deep Dive
- How conversation history is stored
- Accessing the last message
- Adding new messages to state

### Lesson 3.7: Tool Calling
- How LLMs tell agents to use tools
- Extracting tool name and arguments
- Checking if a tool was called

### Lesson 3.8: The Agent Loop
- Complete RED → GREEN → REFACTOR cycle for agents
- Writing tests for agents (scenario testing)
- Understanding infinite loop prevention

## Skills You'll Gain

By the end of Module 3, you'll understand:
- ✅ How to structure an agent as a graph
- ✅ How state flows through nodes
- ✅ How to make decisions (should we call a tool?)
- ✅ How to loop back and refine answers
- ✅ How to test agents with scenarios

## Prerequisites

You already have everything you need:
- ✅ Module 1: Understand TDD (write tests first)
- ✅ Module 2: Know how to code with instant feedback (pytest-watch)
- ✅ This module: Learn WHAT to build (LangGraph agents)

Next modules will teach you:
- Module 4: HOW to test AI agents (scenario testing)
- Module 5: BUILD your first complete agent (weather agent)

---

**Ready? Let's start Lesson 3.1!** 🚀

---

<a id="lesson-3-1-stategraph-concept"></a>

## Lesson 3.1: StateGraph Concept

### What You'll Learn
What a StateGraph is, why it matters, and how it becomes an AI agent.

### The Big Question: What Makes an Agent?

Think about a human solving a problem:
```
Person: "What's the weather in Tokyo?"
↓
Brain: "I need to look up weather. Let me check my weather source."
↓
Action: Looks up weather information
↓
Brain: "I found the weather. Now I can answer."
↓
Response: "Tokyo is 22°C and sunny."
```

An **AI agent** does the same thing, but with code:
```
User: "What's the weather in Tokyo?"
↓
LLM: "I need to use the weather tool. It's located here with these parameters."
↓
Action: Tool executes and returns weather data
↓
LLM: "I have the data. Now I can respond to the user."
↓
Response: "Tokyo is 22°C and sunny."
```

**StateGraph** is the framework that orchestrates this entire flow!

### What is a StateGraph?

**Definition**: A StateGraph is a **blueprint** for how your AI agent thinks and acts. It's like a flowchart that tells the agent:
- 📍 Where to start (entry point)
- 🔧 What processing steps to take (nodes)
- 🔀 How to decide what to do next (edges and routing)
- 🛑 When to stop

### Three Core Concepts

#### 1. **State** - The Information Container

**State** is the data that flows through the agent. Think of it like a backpack that travels from node to node, carrying information.

**Example: Weather Agent State**
```python
state = {
    "messages": [
        {"role": "user", "content": "What's the weather in Tokyo?"},
        {"role": "assistant", "content": "..."},
        # ... conversation history grows here
    ]
}
```

**Key insight**: State carries everything the agent needs to know at any point:
- What the user asked
- What the LLM decided
- What the tool returned
- The full conversation history

#### 2. **MessagesState** - The Conversation Container

**MessagesState** is a special type of state designed for conversation agents. It's specifically built to store a conversation between a user and an AI.

```python
from langgraph.graph import MessagesState

# MessagesState automatically provides this structure:
state: MessagesState = {
    "messages": [
        # Each element is a message in the conversation
        # The LLM reads the ENTIRE messages list to understand context
    ]
}
```

**Why MessagesState matters**:
- 🧠 LLMs need full conversation history to "remember" context
- 📨 Stores both user and assistant messages in order
- 🔄 New messages are appended (conversation grows)
- ✅ Built-in format that LangGraph understands

#### 3. **Nodes** - The Processing Steps

A **Node** is a function that processes the state. Each node:
1. Receives the current state
2. Does some processing (ask LLM, call tool, etc.)
3. Returns updated state

**Simple node example**:
```python
def agent_node(state: MessagesState):
    """A node that uses the LLM to think about the state"""
    messages = state["messages"]

    # Ask the LLM to respond based on all previous messages
    response = llm.invoke(messages)

    # Return updated state with new message
    return {"messages": [response]}
```

**Key principle**: A node doesn't replace state, it **updates** it:
```
Input State:  {"messages": [msg1, msg2]}
       ↓
   Node processes
       ↓
Output State: {"messages": [msg1, msg2, msg3]}  ← Added one message
```

### How StateGraph Works

**Step-by-step visualization**:

```
┌─────────────────────────────────────────────────────────┐
│  Create StateGraph Blueprint                            │
└─────────────────────────────────────────────────────────┘
                        ↓
               graph = StateGraph(MessagesState)
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Define Nodes (processing functions)                    │
└─────────────────────────────────────────────────────────┘
                        ↓
          graph.add_node("agent", agent_function)
          graph.add_node("tools", tools_function)
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Define Edges (connections between nodes)               │
└─────────────────────────────────────────────────────────┘
                        ↓
          graph.set_entry_point("agent")
          graph.add_edge("agent", "tools")
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Compile into Runnable Agent                            │
└─────────────────────────────────────────────────────────┘
                        ↓
              agent = graph.compile()
                        ↓
┌─────────────────────────────────────────────────────────┐
│  Run the Agent with User Input                          │
└─────────────────────────────────────────────────────────┘
                        ↓
         result = agent.invoke({"messages": [user_msg]})
                        ↓
                 Agent processes state
                 through the graph
                        ↓
                  Return final state
```

### Real Example: Weather Agent Graph

Let's see how this works for your weather agent:

```python
from langgraph.graph import StateGraph, MessagesState
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# Step 1: Create StateGraph with MessagesState
graph = StateGraph(MessagesState)

# Step 2: Define nodes (processing functions)
def agent_node(state: MessagesState):
    """Node that thinks about what to do"""
    messages = state["messages"]
    response = llm.invoke(messages)  # LLM looks at all messages, decides what to do
    return {"messages": [response]}

def tool_node(state: MessagesState):
    """Node that calls the weather tool"""
    tool_call = state["messages"][-1].tool_calls[0]  # Get last message's tool call
    location = tool_call["args"]["location"]
    weather = get_current_weather(location)
    return {"messages": [f"Weather for {location}: {weather['temp']}°C, {weather['condition']}"]}

# Step 3: Add nodes to graph
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)

# Step 4: Define edges (connections)
graph.set_entry_point("agent")  # Start at agent node
graph.add_edge("tools", "agent")  # After tool runs, go back to agent

# Step 5: Add conditional edge (decision logic)
def should_use_tool(state: MessagesState):
    """Decide: should we use a tool or respond?"""
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"  # Use tool
    else:
        return "__end__"  # We're done, respond to user

graph.add_conditional_edges("agent", should_use_tool)

# Step 6: Compile into runnable agent
agent = graph.compile()

# Step 7: Use the agent!
result = agent.invoke({
    "messages": [{"role": "user", "content": "What's the weather in Tokyo?"}]
})
```

### The Flow in Action

When you run the agent:

```
User Input: "What's the weather in Tokyo?"
       ↓
    START at agent node
       ↓
State: {"messages": [{"role": "user", "content": "..."}]}
       ↓
agent_node processes:
  - Receives all messages
  - Asks LLM "should I use a tool?"
  - LLM responds "yes, call weather tool"
       ↓
State: {"messages": [..., {"tool_calls": [{"name": "get_weather", "args": {...}}]}]}
       ↓
Conditional edge evaluates: "tool_calls exist? YES"
       ↓
    GO TO tool node
       ↓
tool_node processes:
  - Extracts tool information
  - Calls get_current_weather("Tokyo")
  - Returns weather data
       ↓
State: {"messages": [..., "Tokyo: 22°C, sunny"]}
       ↓
Conditional edge from tool: "go back to agent"
       ↓
agent_node processes again:
  - Receives all messages (including tool result)
  - Asks LLM "should I use tool again?"
  - LLM responds "no, I have answer now"
       ↓
State: {"messages": [..., {"role": "assistant", "content": "Tokyo is 22°C and sunny"}]}
       ↓
Conditional edge evaluates: "tool_calls exist? NO"
       ↓
    END - Return final state
```

### Key Concepts Summary

| Concept | What It Is | Example |
|---------|-----------|---------|
| **StateGraph** | Blueprint for agent | `graph = StateGraph(MessagesState)` |
| **State** | Data container | `{"messages": [msg1, msg2, ...]}` |
| **MessagesState** | Special state for conversations | Stores message history automatically |
| **Node** | Processing function | `agent_node(state)` returns updated state |
| **Edge** | Connection between nodes | "From agent to tools" |
| **Entry Point** | Where to start | `graph.set_entry_point("agent")` |
| **Conditional Edge** | Smart routing | "If tool_calls exist, go to tools, else end" |
| **Compile** | Turn blueprint into runnable | `agent = graph.compile()` |
| **Invoke** | Run the agent | `result = agent.invoke(initial_state)` |

### Understanding Check 3.1a

**Question:** "In your own words, explain what a StateGraph is. How do nodes connect? How does the graph execute?"

Think about:
1. What is the purpose of StateGraph? (What problem does it solve?)
2. How do nodes communicate with each other? (Via what?)
3. How does the graph know where to go next? (What decides the flow?)
4. Why is MessagesState important for AI agents?

Give me your answer! 🎯

---

**[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)**
