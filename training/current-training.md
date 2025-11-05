# AI Weather Agent - Interactive TDD Learning Journey

## 🎯 Quick Jump Navigation

**Where you are right now:**

- ✅ [Module 1 - COMPLETED](#module-1-the-big-picture) - The Big Picture (TDD, Agents, LangGraph, Tools)
- ✅ [Module 2 - COMPLETED](#module-2-hands-on-with-development-tools) - Hands-On with Development Tools
  - ✅ [Lesson 2.1 - ruff Finding Issues](#lesson-2-1-ruff-finding-issues)
  - ✅ [Lesson 2.2 - ruff Fixing Issues](#lesson-2-2-ruff-fixing-issues)
  - ✅ [Lesson 2.3 - ruff Configuration](#lesson-2-3-ruff-configuration)
  - ✅ [Lesson 2.4 - pre-commit Understanding](#lesson-2-4-pre-commit-understanding)
  - ✅ [Lesson 2.5 - pre-commit Setup](#lesson-2-5-pre-commit-setup)
  - ✅ [Lesson 2.6 - pre-commit Configuration](#lesson-2-6-pre-commit-configuration)
  - ✅ [Lesson 2.7 - pytest-watch Understanding](#lesson-2-7-pytest-watch-understanding)
  - ✅ [Lesson 2.8 - pytest-watch Hands-On](#lesson-2-8-pytest-watch-hands-on)
  - ✅ [Lesson 2.9 - The Complete TDD Cycle](#lesson-2-9-the-tdd-cycle-with-pytest-watch)
  - ✅ [Lesson 2.10 - Putting It All Together](#lesson-2-10-integrating-all-tools)
- 🔄 **Module 3 - STARTING NEXT** - Deep Dive into LangGraph ← YOU ARE HERE!

**Completed Modules:**
- ✅ [Module 1 Understanding Check](#understanding-check-11---passed-)
- ✅ [Module 2 Understanding Checks](#module-2-hands-on-with-development-tools)

**Coming Up Next:**
- 🔄 Module 3 - Deep Dive into LangGraph
- ⏳ Module 4 - Scenario Testing Framework
- ⏳ Module 5 - Build Weather Agent
- ⏳ Module 6 - Fix ai-wheather-agent Project
- ⏳ Module 7 - Scale Up Multi-Agent Systems
- ⏳ Module 8 - Deploy & Monitor

---

## Welcome! 👋

This document guides you through learning **Test-Driven Development (TDD) with AI Agents** from scratch. Each section builds on the previous one. **After each section, I will ask you if you understood it before moving forward.**

---

## Project Overview

### What Are We Building?
A **weather AI agent** that:
1. Listens to user questions like "What's the weather in Tokyo?"
2. Uses tools to fetch weather data
3. Returns formatted responses

### Why This Project?
It teaches you:
- **TDD** (Test-Driven Development): Write tests BEFORE code
- **AI Agents**: How to build agents that can use tools
- **Modern Python Dev**: Industry-standard tools and practices

### The Technology Stack

| Component | Purpose | Example |
|-----------|---------|---------|
| **LangGraph** | Build the AI agent | Manages conversation flow, tool calling |
| **pytest + scenario** | Write tests for AI agents | Test if agent works correctly |
| **ruff** | Catch bugs & format code | Fixes style issues automatically |
| **pre-commit** | Prevent bad commits | Runs checks before git commit |
| **pytest-watch** | See test results instantly | Tests re-run when you save files |

You'll learn each of these step-by-step.

---

## Your Learning Journey

### The 8 Modules (High Level)

| Module | What You'll Learn | Status |
|--------|------------------|--------|
| **1** | The Big Picture - understand what we're building | ⏳ Starting now |
| **2** | Development Tools - ruff, pre-commit, pytest-watch | ⏳ After Module 1 |
| **3** | LangGraph - how agents work under the hood | ⏳ After Module 2 |
| **4** | Scenario Testing - testing AI agents properly | ⏳ After Module 3 |
| **5** | Build First Agent - RED → GREEN → REFACTOR | ⏳ After Module 4 |
| **6** | Fix Your Project - make weather agent work | ⏳ After Module 5 |
| **7** | Scale Up - multiple agents, real patterns | ⏳ After Module 6 |
| **8** | Deploy & Monitor - production-ready code | ⏳ After Module 7 |

---

## How to Use This Training

### ✅ Your Responsibilities
1. **Read each section carefully**
2. **Run the commands shown**
3. **Answer "yes" or "no" when asked "Did you understand?"**
   - Say **"yes"** → we move to the next topic
   - Say **"no" or ask questions** → I'll explain more

### ✅ My Responsibilities
1. **Explain clearly** with examples
2. **Ask you to run commands** to see concepts in action
3. **Check your understanding** before moving forward
4. **Adjust explanations** if you're confused

### ⚡ Pro Tips
- Don't memorize - focus on understanding concepts
- Run every command shown to you
- Ask questions if anything is unclear
- Each module builds on the previous one

---

---

<a id="module-1-the-big-picture"></a>

# MODULE 1: The Big Picture

<a id="lesson-1-1-what-is-tdd"></a>

## Lesson 1.1: What is TDD? (Test-Driven Development)

### The Traditional Way (❌ Most people do this)
```
1. Write code
2. Hope it works
3. Test it (maybe)
4. Fix bugs you find
5. Ship and pray
```

### The TDD Way (✅ Professional developers do this)
```
1. Write a TEST that fails (RED)
2. Write minimal code to make test pass (GREEN)
3. Improve the code (REFACTOR)
4. Repeat
```

### Why TDD is Better

Imagine you're building a weather agent. With TDD:

**STEP 1: RED (Write failing test)**
```python
# Test file
def test_weather_agent_tokyo():
    # "Agent should answer 'What's the weather in Tokyo?'"
    result = run_agent("What's the weather in Tokyo?")
    assert "22°C" in result  # We expect this but it's not implemented yet - TEST FAILS
```

**STEP 2: GREEN (Write minimal code to pass)**
```python
# Agent code
def weather_agent(question):
    if "Tokyo" in question:
        return "Tokyo: 22°C, sunny"  # Minimal code to pass the test
```

**STEP 3: REFACTOR (Make code better)**
```python
# Improved agent code
def weather_agent(question):
    location = extract_location(question)
    weather = get_weather_from_api(location)
    return format_response(location, weather)
```

### Why This Matters
- ✅ You KNOW your code works (tests prove it)
- ✅ You can refactor safely (tests catch regressions)
- ✅ Code is cleaner and more maintainable
- ✅ Fewer bugs make it to production

---

<a id="lesson-1-2-what-is-an-ai-agent"></a>

## Lesson 1.2: What is an AI Agent?

### Simple Definition
An **AI agent** is a program that:
1. Receives messages from users
2. Decides what to do (use a tool, respond, ask more questions)
3. Can use TOOLS (functions) to get information
4. Responds to the user

### Example: Weather Agent Flow

```
User: "What's the weather in Tokyo?"
        ↓
Agent: "The user is asking about weather in Tokyo"
        ↓
Agent: "I need to call the weather_tool with location='Tokyo'"
        ↓
Tool: Returns {"temp": "22°C", "condition": "sunny"}
        ↓
Agent: Formats and returns "Tokyo: 22°C, sunny"
        ↓
User Sees: "Tokyo: 22°C, sunny"
```

### Key Concept: Tools
**Tools** are functions the agent can call. Think of them like a toolkit:
- 🔧 `get_weather_tool` - Get weather for a location
- 🔧 `get_time_tool` - Get current time
- 🔧 `search_tool` - Search the internet

The agent DECIDES which tools to use based on the user's question.

---

<a id="lesson-1-3-what-is-langgraph"></a>

## Lesson 1.3: What is LangGraph?

### Simple Definition
**LangGraph** is a framework that makes building agents easy. It's like a blueprint system for agents.

### How It Works: The Graph

Think of an agent as a graph (like a flowchart):

```
┌─────────────┐
│   START     │
└──────┬──────┘
       ↓
┌──────────────────────┐
│  AGENT NODE          │
│ (Think about answer) │
└──────┬───────────────┘
       ↓
   Does agent need
   to use a tool?
       ├─→ YES → ┌──────────────────┐
       │         │  TOOL NODE       │
       │         │ (Call the tool)  │
       │         └──────┬───────────┘
       │                ↓
       │         ┌──────────────────────┐
       │         │ Send result back to  │
       │         │ AGENT NODE (loop)    │
       │         └──────────────────────┘
       │
       └─→ NO  → ┌──────────────────┐
                 │  RETURN ANSWER   │
                 │ (Done!)          │
                 └──────────────────┘
```

### Key Components

| Part | What It Does | Example |
|------|--------------|---------|
| **Nodes** | Processing steps | Agent node, Tool node |
| **Edges** | Connections between nodes | "From Agent to Tool" |
| **State** | Information passed around | Messages, conversation history |
| **Entry Point** | Where to start | Always start at Agent |

---

<a id="lesson-1-4-what-is-scenario-testing"></a>

## Lesson 1.4: What is Scenario Testing?

### The Problem with Regular Tests

Regular tests (unit tests) test individual functions:
```python
# Regular test - not good for AI agents
def test_weather_function():
    result = get_weather("Tokyo")
    assert result["temp"] == "22"
```

This doesn't test if the AGENT works correctly in a real conversation!

### The Solution: Scenario Tests

**Scenario** tests simulate a REAL USER CONVERSATION with your agent:

```python
# Scenario test - good for AI agents
@scenario.test(
    description="User asks for weather in Tokyo",
    agents=[
        scenario.UserSimulatorAgent(),        # Simulates a user
        scenario.JudgeAgent(criteria=[        # Evaluates the response
            "Response includes temperature",
            "Response includes condition (sunny, rainy, etc)",
            "No hallucinations (made-up weather)"
        ])
    ]
)
def test_weather_agent():
    result = scenario.run(weather_agent)
    assert result.success
```

This:
1. 🤖 Simulates a user asking questions
2. 🤖 Runs your agent
3. 🤖 Judges if the response is good based on criteria

### Why This Matters for AI Agents
- ✅ Tests realistic user interactions
- ✅ Judges output using AI (not just exact matching)
- ✅ Prevents hallucinations (fake data)
- ✅ Much better than unit tests for agents

---

<a id="lesson-1-5-the-development-tools"></a>

## Lesson 1.5: The Development Tools

### Tool 1: ruff (The Code Cleaner)

**What it does**: Finds and fixes code problems automatically

```bash
# Find problems
ruff check .

# Fix problems automatically
ruff check . --fix

# Format code nicely
ruff format .
```

**Problems it catches**:
- ❌ Unsorted imports
- ❌ Unused variables
- ❌ Missing blank lines
- ❌ Code style issues

### Tool 2: pre-commit (The Guardian)

**What it does**: Runs checks BEFORE you commit code to git

```bash
# Install pre-commit hooks
pre-commit install

# Now when you git commit, hooks run automatically
git commit -m "your message"  # ruff, tests, etc run automatically
```

**Benefit**: Bad code never gets committed

### Tool 3: pytest-watch (The Watcher)

**What it does**: Runs tests automatically when you save files

```bash
# Start watch mode
just watch

# Now when you save any file:
# → Tests run automatically
# → You see results instantly
# → Sub-second feedback loop
```

**Benefit**: Instant feedback while coding (perfect for TDD)

---

<a id="lesson-1-6-how-it-all-works-together"></a>

## Lesson 1.6: How It All Works Together

### The TDD Workflow with Our Tools

```
1. START WATCH MODE
   just watch

2. WRITE FAILING TEST (RED)
   tests/test_weather_agent.py
   → Save file
   → pytest-watch detects change
   → Tests run → FAIL (expected)

3. WRITE MINIMAL CODE (GREEN)
   src/ai_wheather_agent/weather.py
   → Save file
   → pytest-watch detects change
   → Tests run → PASS!

4. REFACTOR (IMPROVE)
   src/ai_wheather_agent/weather.py
   → Make code better
   → Save file
   → pytest-watch runs
   → Tests still pass ✅

5. GIT COMMIT
   git commit -m "feat: weather agent works"
   → pre-commit hooks run automatically
   → ruff formats and fixes code
   → Tests run
   → If all pass → commit succeeds
   → If any fail → commit blocked (fix first!)
```

### The Result
- ✅ Instant feedback (sub-second test runs)
- ✅ Code always follows style rules (ruff)
- ✅ Tests always pass (pre-commit blocks bad commits)
- ✅ You code with confidence

---

<a id="lesson-1-7-your-project-structure"></a>

## Lesson 1.7: Your Project Structure

```
ai-wheather-agent/
├── src/ai_wheather_agent/          ← Where agent code goes
│   ├── weather.py                  ← Agent definition
│   ├── tools/
│   │   └── weather.py              ← Weather tool (to create)
│   ├── cli.py                      ← Command-line interface
│   └── ...
│
├── tests/                           ← Where test code goes
│   ├── test_weather_agent.py       ← Scenario tests (to create)
│   └── ...
│
├── training/                        ← Training materials (this file)
│   ├── training.md                 ← You are here!
│   └── context.md                  ← Grok's advice
│
├── pyproject.toml                   ← Project config & dependencies
├── justfile                        ← Commands (watch, test, qa, etc)
├── .pre-commit-config.yaml         ← Pre-commit config (to create)
└── ...
```

---

## 🎯 Module 1 Summary

You've learned:

1. **TDD** - Write tests first, code second, then refactor
2. **AI Agents** - Programs that think and use tools
3. **LangGraph** - Framework for building agents
4. **Scenario Testing** - Test AI agents with realistic conversations
5. **Development Tools**:
   - **ruff** - Finds and fixes code problems
   - **pre-commit** - Runs checks before commits
   - **pytest-watch** - Runs tests automatically on save
6. **The Workflow** - TDD cycle with instant feedback

---

<a id="understanding-check-11---passed-"></a>

## ❓ Understanding Check 1.1 - PASSED ✅

**Your Answer:**
> "TDD is when the developer starts creating tests aligned with the business needs and then develops the code to cover the tests scenarios. This will guide the development on the business requirements in an effective way allowing the developer to be laser-focus."

**Evaluation:** ✅ EXCELLENT - You clearly understand:
- Tests come FIRST (business requirements)
- Code comes SECOND (to satisfy the tests)
- Benefits: Laser-focused on requirements, effective guidance
- This is exactly right!

**You're Ready for Module 2!** 🚀

---

## Notes for Future Sessions

When returning to this project:

1. Read this file first
2. Check the "Session Progress" section below
3. Run `just test` to see current status
4. Pick up where you left off

---

## Session Progress

### Session 1: Setup & Module 1 Complete ✅
- ✅ Verified all tools installed (uv, Python 3.13, ruff, pre-commit, pytest)
- ✅ Installed just command runner
- ✅ Explored project structure
- ✅ Completed Module 1: The Big Picture (7 lessons)
- ✅ Understanding Check 1.1: PASSED

### Session 2: Module 2 COMPLETE - Hands-On with Development Tools ✅
- ✅ Lesson 2.1: ruff Finding Issues - COMPLETED
- ✅ Lesson 2.2: ruff Fixing Issues - COMPLETED
- ✅ Lesson 2.3: ruff Configuration - COMPLETED
- ✅ Lesson 2.4: pre-commit Understanding - COMPLETED
- ✅ Lesson 2.5: pre-commit Setup - COMPLETED
- ✅ Lesson 2.6: pre-commit Configuration - COMPLETED
- ✅ Lesson 2.7: pytest-watch Understanding - COMPLETED (Understanding Check PASSED)
- ✅ Lesson 2.8: pytest-watch Hands-On (Getting Started) - COMPLETED
  - ✅ Activity 2.8.1: Start Watch Mode - COMPLETED
  - ✅ Activity 2.8.2: Make a File Change - COMPLETED
  - ✅ Activity 2.8.3: Create a Failing Test - COMPLETED
  - ✅ Activity 2.8.4: Fix the Test - COMPLETED
  - ✅ Activity 2.8.5: Stop Watch Mode - COMPLETED
  - ✅ Understanding Check 2.8a: PASSED
- ✅ Lesson 2.9: The Complete TDD Cycle with pytest-watch - COMPLETED
  - ✅ Understanding Check 2.9a: PASSED (Excellent RED → GREEN → REFACTOR example with real code)
- ✅ Lesson 2.10: Putting It All Together - COMPLETED
  - ✅ Understanding Check 2.10a: PASSED (Perfect understanding of complete development workflow)

**Module 2 Summary:**
✅ Mastered ruff (finding and fixing code issues)
✅ Mastered pre-commit (quality gates for commits)
✅ Mastered pytest-watch (instant feedback for TDD)
✅ Mastered complete development workflow (all tools working together)
✅ 10 lessons + 10 understanding checks - ALL PASSED! 🎓

**Next: Module 3 - Deep Dive into LangGraph**

---

---

<a id="module-3-deep-dive-into-langgraph"></a>

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

<a id="module-2-hands-on-with-development-tools"></a>

# MODULE 2: Hands-On with Development Tools

## Goal
Learn how to USE ruff, pre-commit, and pytest-watch in practice. Not just theory - actual hands-on coding!

---

<a id="lesson-2-1-ruff-finding-issues"></a>

## Lesson 2.1: ruff Hands-On (Part 1 - Finding Issues)

### What You'll Learn
How to use ruff to **find** code problems automatically

### The Command
```bash
ruff check .
```

This command scans your entire project and reports any issues it finds.

### Let's Try It!

**Activity 1.1**: Run ruff check in your project

```bash
# Navigate to your project
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent

# Run ruff check
ruff check .
```

**What you'll see**: A list of issues (if any exist)

### Understanding the Error Codes

When ruff reports issues, it uses codes like:
- **E** = Errors (syntax, style problems)
- **W** = Warnings (pycodestyle warnings)
- **F** = Pyflakes (unused imports, undefined variables)
- **I** = isort (import sorting issues)
- **B** = bugbear (potential bugs)
- **UP** = pyupgrade (outdated Python syntax)

Each issue has a code like `E001`, `W292`, `I001`, etc.

### Example Output

```
I001 [*] Import block is un-sorted or un-formatted
 --> src/ai_wheather_agent/weather.py:2:1
  |
2 | / from langgraph.graph import StateGraph, MessagesState
3 | | from langchain_openai import ChatOpenAI
4 | | from tools.weather import get_current_weather
  | |_____________________________________________^
```

**What this means**:
- **I001** = Import sorting issue
- **src/ai_wheather_agent/weather.py:2:1** = File location (line 2, column 1)
- **What's wrong** = Imports aren't sorted alphabetically
- **[*]** = ruff can auto-fix this

### Reading the Error Message

1. **Error Code** (e.g., I001) - tells you what type of issue
2. **File Location** (src/file.py:line:col) - where to find it
3. **The Problem** - what's wrong
4. **[*] Fixable** - whether ruff can auto-fix it

### Your Turn!

**Activity 1.2**: Read the ruff output

Run ruff check again and:
1. Look at the errors reported
2. Find the error code (E, W, F, I, B, or UP)
3. Find the file location
4. Understand what's wrong

Write down: **What issues did ruff find in your project?**

---

### Understanding Check 2.1a - PASSED ✅

**Your Answer:**
> "ruff can solve this issue that is a W-arning located at row 21, column 57. There is no newline at end of file. Ruff can create the new line."

**Evaluation:** ✅ PERFECT! You showed mastery of:
- Reading error codes (W = Warning)
- Understanding file locations (line, column)
- Identifying what's wrong (missing newline)
- Recognizing ruff can auto-fix it

**You're Ready for Lesson 2.2!** 🚀

---

<a id="lesson-2-2-ruff-fixing-issues"></a>

## Lesson 2.2: ruff Hands-On (Part 2 - Fixing Automatically)

### What You'll Learn
How to use ruff to **automatically fix** code problems

### The Commands

There are two main commands for fixing:

```bash
# Method 1: Auto-fix issues
ruff check . --fix

# Method 2: Format code (like black)
ruff format .
```

**What's the difference?**
- `ruff check --fix` = Fix specific rule violations (imports, unused variables, etc)
- `ruff format .` = Format code style (spacing, line breaks, indentation)
- **Usually you use BOTH** to get everything fixed

### Let's Try It!

**Activity 2.2.1**: Auto-fix the issues

Run these commands one at a time:

```bash
# First, format the code
ruff format .

# Then, fix linting issues
ruff check . --fix
```

**What you'll see**:
- Lines like "3 files reformatted"
- Lines like "Found X errors (X fixed)"

### Let's Verify It Worked

After fixing, check if there are any issues left:

```bash
ruff check .
```

**What you should see**:
```
All checks passed!
```

### Activity 2.2.2: Look at the Changes

The files were modified! Let's see what changed.

Look at `tests/test_weather_agent.py` - it should now have a newline at the end.

**Tell me:**
1. Did the commands run successfully?
2. What files were modified?
3. Did `ruff check .` say "All checks passed!"?
4. What changed in the files?

---

### Understanding Check 2.2a - PASSED ✅

**Your Answer:**
> "ruff format . formats all project files in terms of line breaks and spacing. ruff check . --fix checks all project files in terms of imports, unused variables and fix them"

**Evaluation:** ✅ EXCELLENT - You showed clear understanding of:
- `ruff format .` = Formatting (appearance: spacing, line breaks)
- `ruff check . --fix` = Fixing violations (logic: imports, unused vars)
- That they serve different purposes

**You're Ready for Lesson 2.3!** 🚀

---

<a id="lesson-2-3-ruff-configuration"></a>

## Lesson 2.3: ruff Configuration

### What You'll Learn
Why ruff works the way it does - understanding the configuration in `pyproject.toml`

### The Configuration File

Ruff's behavior is controlled by settings in `pyproject.toml`. Let's look at what's configured for your project:

### Activity 2.3.1: Open and Read the Configuration

Open `pyproject.toml` and find the `[tool.ruff]` section:

```bash
# Navigate to your project
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent

# Open the file (or just look at it with cat)
cat pyproject.toml | grep -A 20 "\[tool.ruff\]"
```

You should see something like:

```toml
[tool.ruff]
line-length = 120

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # Pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "UP",  # pyupgrade
]
```

### Understanding Each Setting

#### 1. Line Length: 120

```toml
line-length = 120
```

**What it means**: Lines should be max 120 characters long

**Why?**
- Professional standard (not too short, not too long)
- Fits nicely on modern screens
- Readable without wrapping

**Example**:
```python
# ✅ GOOD (under 120 chars)
result = get_weather_agent(location="Tokyo", temperature_unit="celsius", include_forecast=False)

# ❌ BAD (over 120 chars - would be wrapped)
result = get_weather_agent_with_full_history_and_all_options(location="Tokyo", temperature_unit="celsius", include_forecast=False, time_range="7_days")
```

#### 2. Rules Selected: E, W, F, I, B, UP

```toml
select = [
    "E",   # pycodestyle errors (spacing, indentation)
    "W",   # pycodestyle warnings (trailing whitespace, blank lines)
    "F",   # Pyflakes (unused imports, undefined variables)
    "I",   # isort (import sorting)
    "B",   # flake8-bugbear (potential bugs)
    "UP",  # pyupgrade (outdated Python syntax)
]
```

**What each rule catches:**

| Rule | What It Catches | Example |
|------|-----------------|---------|
| **E** | Syntax/Style Errors | Missing spaces, indentation wrong |
| **W** | Warnings | Trailing whitespace, blank lines |
| **F** | Code Errors | `import os` but never use it |
| **I** | Import Ordering | `from x import y` before `import x` |
| **B** | Potential Bugs | Using mutable default arguments |
| **UP** | Old Python | Using `list()` instead of `[]` |

### Activity 2.3.2: Understand Your Configuration

Look at your `pyproject.toml` and answer:

1. **What is the line length set to?** (Find `line-length =`)
2. **Which rules are enabled?** (Count them - there should be 6)
3. **Why do you think the project chose these specific rules?**

Tell me your answers!

---

### The Big Picture: Why Configuration Matters

Your project's ruff configuration is **intentional**:
- ✅ Line length of 120 means readable code
- ✅ E, W, F, I, B, UP rules catch most common issues
- ✅ These are the **industry standard** rules
- ✅ Everyone on the team uses the same rules (consistency)

This is why when you run `ruff check .` and `ruff format .`, they behave the same way every time - they follow this configuration!

---

### Understanding Check 2.3a - PASSED ✅

**Your Answer:**
> "it is important to have ruff configured to keep a standard way to all dev team. Otherwise, each one would bring a different standard. It would be chaos and inconsistency."

**Evaluation:** ✅ PERFECT! You showed mastery of:
- Unified team standards through configuration
- Preventing chaos and inconsistency
- Professional best practice thinking

**You've mastered ruff!** 🎓 You now understand:
- How to FIND issues (Lesson 2.1)
- How to FIX issues (Lesson 2.2)
- Why configuration matters (Lesson 2.3)

**Next: pre-commit!** 🚀

---

<a id="lesson-2-4-pre-commit-understanding"></a>

## Lesson 2.4: pre-commit Hands-On (Part 1 - Installation)

### What You'll Learn
How to install and set up pre-commit hooks so checks run automatically before commits

### The Problem pre-commit Solves

Imagine this scenario:
```
Developer writes code
↓
Forgets to run ruff check
↓
Commits bad code
↓
Code review finds issues
↓
Has to fix and recommit
↓
Wasted time! ❌
```

### The Solution: pre-commit

pre-commit automatically runs checks **BEFORE you commit**:
```
Developer writes code
↓
Tries to git commit
↓
pre-commit runs automatically:
  - ruff format
  - ruff check --fix
  - other checks
↓
If all pass → commit succeeds ✅
If any fail → commit blocked, fix first ❌
```

**Result**: Bad code NEVER gets into git history!

### What is a Git Hook?

A **git hook** is a script that runs automatically at certain git events:
- `pre-commit` hook: runs BEFORE you commit
- `post-commit` hook: runs AFTER you commit
- `pre-push` hook: runs BEFORE you push

We're using `pre-commit` (the tool) to manage these hooks automatically.

### Activity 2.4.1: Check pre-commit Status

First, let's see if pre-commit is installed:

```bash
pre-commit --version
```

You should see something like:
```
pre-commit 4.3.0
```

Good news: **pre-commit is already installed!** ✅

### Activity 2.4.2: Understand the Configuration File

pre-commit uses a file called `.pre-commit-config.yaml` to know which checks to run.

Check if it exists:

```bash
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent
ls -la | grep pre-commit
```

**If it exists**, it will show:
```
-rw-r--r-- .pre-commit-config.yaml
```

**If it doesn't exist**, we'll need to create one.

Tell me: **Does `.pre-commit-config.yaml` exist in your project?**

---

### Understanding Check 2.4a - PASSED ✅

**Your Answer:**
> "pre-commit hook is a git hook that runs before git code commit. It automates the call to 'ruff format' 'ruff check --fix' and allows the code to be committed only if it pass such commands that brings consistency/standard to the code created by developers (eg: missing spaces, identation, trailing whitespaces, blank lines, unused import/variables, outdated Python syntax, potential bugs, import sorting)."

**Evaluation:** ✅ PERFECT! You showed mastery of:
- Clear definition of pre-commit hooks
- Understanding of automation (automates ruff calls)
- Blocking mechanism (code must pass checks)
- Team benefits (consistency/standards)
- Comprehensive knowledge of what it checks (all rule types!)

**You understand pre-commit deeply!** 🎓

---

<a id="lesson-2-5-pre-commit-setup"></a>

## Lesson 2.5: pre-commit Hands-On (Part 2 - Setting Up)

### What You'll Do
Create the `.pre-commit-config.yaml` file and install pre-commit hooks. It will work as an "automated quality gate".

### Step 1: Create the Configuration File

We'll create a `.pre-commit-config.yaml` file that tells pre-commit what checks to run.

**Activity 2.5.1**: Create the file

```bash
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent

# Create the .pre-commit-config.yaml file with this content:
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.8
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
EOF
```

**What this file does:**
- Tells pre-commit to use ruff for linting and formatting
- Tells pre-commit to check for trailing whitespace
- Tells pre-commit to fix files that need end-of-file fixes
- Tells pre-commit to validate YAML and TOML files

### Step 2: Verify the File Was Created

```bash
cat .pre-commit-config.yaml
```

You should see the configuration you just created.

### Step 3: Install the Pre-commit Hooks

Now install the hooks into git:

```bash
pre-commit install
```

**What you should see:**
```
pre-commit installed at .git/hooks/pre-commit
```

**Good news**: Pre-commit is now INSTALLED! ✅

### Understanding What Happened

When you run `pre-commit install`, it:
1. Creates a file at `.git/hooks/pre-commit`
2. This file will run automatically when you try to `git commit`
3. It will run all the checks defined in `.pre-commit-config.yaml`
4. If any check fails, the commit is blocked

### Step 4: Test That It's Working

Let's make a test commit to verify pre-commit works!

First, create a small test change:

```bash
# Add a simple change to a file (for testing)
echo "# test" >> README.md
```

Now try to commit:

```bash
# Stage the change
git add README.md

# Try to commit
git commit -m "test: verify pre-commit works"
```

**What will happen:**
- pre-commit hooks will run
- They'll check your changes
- If all pass → commit succeeds
- If any fail → commit blocked, fix needed

**Tell me:**
1. Did you create the `.pre-commit-config.yaml` file successfully?
2. Did `pre-commit install` work?
3. What happened when you tried to commit?

---

### Understanding Check 2.5a - PASSED ✅

**Your Answer:**
| Hook | Action |
|------|--------|
| ruff | Lint Python code, auto-fix issues, fail if fixes made |
| ruff-format | Auto-format Python code |
| trailing-whitespace | Remove extra spaces at end of lines |
| end-of-file-fixer | Add missing newline at EOF |
| check-yaml | Validate YAML syntax |
| check-toml | Validate TOML syntax |
| check-added-large-files | Block large file additions |

**Evaluation:** ✅ PERFECT! You showed mastery of:
- Understanding what `.pre-commit-config.yaml` does in every commit
- Comprehensive knowledge of all hooks and their purposes
- Clear, organized explanation of automation and prevention

**Pre-commit setup complete!** 🎓

---

<a id="lesson-2-6-pre-commit-configuration"></a>

## Lesson 2.6: pre-commit Configuration (Part 3 - Understanding the Config)

### What You'll Learn
How to understand and customize the `.pre-commit-config.yaml` file for your project

### Activity 2.6.1: Review Your Configuration

Open the `.pre-commit-config.yaml` file you created:

```bash
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent
cat .pre-commit-config.yaml
```

You should see something like:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.8
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
```

### Understanding the Configuration

#### Section 1: ruff-pre-commit Repository

```yaml
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.6.8
  hooks:
    - id: ruff
      args: [--fix, --exit-non-zero-on-fix]
    - id: ruff-format
```

**What this does:**
- Uses the official ruff pre-commit hooks from GitHub
- `rev: v0.6.8` = Version of ruff to use
- `id: ruff` = Runs ruff linting with fixes
- `args: [--fix, --exit-non-zero-on-fix]` = Fix issues automatically, but fail if fixes were needed
- `id: ruff-format` = Runs ruff code formatter

**Why this matters:**
- Ensures code is automatically fixed before commit
- Prevents bad code from entering git history
- Uses the exact version you specify (reproducible)

#### Section 2: pre-commit-hooks Repository

```yaml
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0
  hooks:
    - id: trailing-whitespace
    - id: end-of-file-fixer
    - id: check-yaml
    - id: check-toml
    - id: check-added-large-files
```

**What each hook does:**
- `trailing-whitespace` = Removes trailing spaces at end of lines
- `end-of-file-fixer` = Ensures files end with a newline
- `check-yaml` = Validates YAML file syntax
- `check-toml` = Validates TOML file syntax
- `check-added-large-files` = Prevents committing large files

**Why this matters:**
- Catches common formatting issues automatically
- Prevents invalid configuration files from being committed
- Catches accidental large file commits

### Activity 2.6.2: Test Pre-commit Manually

You can run pre-commit checks manually without committing:

```bash
pre-commit run --all-files
```

This runs all hooks against all files in your project. Useful for testing!

### The Big Picture: Configuration as Code

Your `.pre-commit-config.yaml` is like a "contract" for your team:
- ✅ Everyone uses the same tools and versions
- ✅ Everyone runs the same checks before committing
- ✅ No surprises - everyone knows the rules
- ✅ Problems caught early (at commit time)

### Understanding Check 2.6a - PASSED ✅

**Your Answer:**
> ".pre-commit-config.yaml controls what needs to be called (ruff --fix, ruff-format) while pyproject.toml has details about ruff rules to be executed (line lenght, E, W, F, I, B, UP)"

**Evaluation:** ✅ EXCELLENT! You showed clear understanding of:
- `.pre-commit-config.yaml` = **Orchestration layer** (what to call and when)
- `pyproject.toml` = **Configuration layer** (how tools behave)
- They work together: pre-commit calls the tools, pyproject.toml configures their behavior
- Both are necessary for a complete setup

**You've mastered Module 2!** 🚀 You now fully understand:
- How to find issues with ruff
- How to fix issues with ruff
- How to configure ruff
- How to set up pre-commit hooks
- How pre-commit and pyproject.toml work together

---

<a id="lesson-2-7-pytest-watch-understanding"></a>

## Lesson 2.7: pytest-watch Understanding - COMPLETED ✅

### Understanding Check 2.7a - PASSED ✅

**Your Answer:**
> "The benefit of pytest-watch is the automated execution of tests allowing the developer focus on coding instead of context shifting to execute commands."

**Evaluation:** ✅ PERFECT! You demonstrated mastery of:
- ✅ **Automated execution** - Tests run without manual action
- ✅ **Developer focus** - Staying focused on writing code
- ✅ **No context switching** - Breaking flow is the enemy of productivity
- ✅ **Understanding the WHY** - This is exactly what makes TDD productive!

**You're Ready for Lesson 2.8!** 🚀

---

### What You'll Learn
How `pytest-watch` enables **instant feedback** during development - the key to productive TDD

### The Problem: Slow Feedback Loop

Imagine you're writing code using TDD:

```
1. Write failing test (RED)
2. Save the file
3. Manually run: pytest
4. Wait for tests
5. See results
6. Write code to fix test (GREEN)
7. Save the file
8. Manually run: pytest again
9. Wait for tests
10. See results
11. Refactor and repeat...
```

**Problem**: Step 3, 8, 9 require MANUAL action each time. You're constantly switching context.

### The Solution: pytest-watch (Automatic Test Running)

`pytest-watch` (installed as `ptw`) **automatically runs your tests** whenever you save a file:

```
1. Start watch mode: just watch
2. Write failing test (RED)
3. Save → pytest-watch detects change → Tests run automatically
4. Write code to fix test (GREEN)
5. Save → pytest-watch detects change → Tests run automatically
6. See results instantly without manual action
7. Refactor and repeat...
```

**Benefit**: Sub-second feedback loop. You focus on coding, not on running commands!

### How pytest-watch Works

**Traditional workflow:**
```
You save file → You run pytest → Pytest runs → Results appear (manual)
```

**With pytest-watch:**
```
You save file → pytest-watch detects change → Pytest runs automatically → Results appear immediately
```

### Real-Time Example

Imagine you're writing a weather agent test:

**Your IDE (left side):**
```python
def test_weather_agent_tokyo():
    result = run_agent("What's weather in Tokyo?")
    assert "22°C" in result
    # Cursor here, you type
```

**Terminal (right side with pytest-watch):**
```
tests/test_weather_agent.py:1: test_weather_agent_tokyo FAILED

FAILED tests/test_weather_agent.py::test_weather_agent_tokyo
assert "22°C" in result
```

The moment you save the file, pytest-watch detects the change and runs tests. **You see the results in real-time** without leaving your editor!

### Key Concept: The Watch Loop

```
┌─────────────────────────────────┐
│  You: Open your editor          │
│  Run: just watch                │
│  → pytest-watch starts          │
└────────────┬────────────────────┘
             ↓
┌─────────────────────────────────┐
│  Watch Loop (runs forever)      │
│  1. Monitor all project files   │
│  2. Detect file changes         │
│  3. Run pytest automatically    │
│  4. Show results                │
│  5. Go back to step 1           │
└─────────────────────────────────┘
```

### Why pytest-watch is Perfect for TDD

| Workflow Step | Without pytest-watch | With pytest-watch |
|---|---|---|
| Write failing test | Manually run pytest | Auto-runs, see results immediately |
| Write minimal code | Manually run pytest | Auto-runs, see results immediately |
| Refactor code | Manually run pytest | Auto-runs, see results immediately |
| **Feedback time** | 5-10 seconds per iteration | Sub-second feedback |
| **Developer experience** | Interrupted, context switching | Flow state, continuous feedback |

The difference is **huge** for TDD. You enter a "flow state" where you're constantly seeing instant feedback.

### How It Integrates with Your Development Tools

**Your complete development workflow:**

```
Terminal 1: just watch (pytest-watch)
  ↓ (Automatic test feedback)

IDE: You write tests and code
  ↓
pytest-watch: Detects file save
  ↓
pytest: Runs tests
  ↓
Results appear in Terminal 1 (sub-second)
```

**When you commit:**
```
git commit
  ↓
pre-commit hooks run (ruff, tests, etc)
  ↓
If all pass → Commit succeeds
If any fail → Commit blocked
```

### Understanding Check 2.7a

**Question:** "What's the main benefit of pytest-watch compared to manually running pytest each time? Why does it matter for TDD?"

Think about:
- How often do you save files when coding?
- How would instant feedback change your development experience?
- Why is speed important for the TDD cycle?

Answer this question, then we'll move to Lesson 2.8 where we'll actually use pytest-watch!

---

<a id="lesson-2-8-pytest-watch-hands-on"></a>

## Lesson 2.8: pytest-watch Hands-On (Part 1 - Getting Started)

### What You'll Do
Start `pytest-watch` and see it run tests automatically as you make changes

### Activity 2.8.1: Start Watch Mode

Open a terminal and run:

```bash
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent

just watch
```

You should see output like:
```
[PYTEST WATCH] Starting pytest in watch mode...
================================ test session starts =================================
...
================================ 1 passed in 0.23s =================================

Now watching...
```

**What this means:**
- Pytest ran all tests
- 1 test passed (your existing test)
- pytest-watch is now in "watch mode"
- It's monitoring all files for changes

### Activity 2.8.2: Make a File Change

While pytest-watch is running, open a Python file and make a small change:

**Option 1: Add a comment to a test file**
```bash
# In another terminal, or in your editor:
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent
echo "# test comment" >> tests/test_weather_agent.py
```

**Option 2: Or just save a file in your editor** (any Python file)

Watch your pytest-watch terminal - it should **automatically re-run tests** without you doing anything!

You should see:
```
File change detected: tests/test_weather_agent.py
Rerunning tests...
================================ test session starts =================================
...
================================ 1 passed in 0.23s =================================

Now watching...
```

### Activity 2.8.3: Create a Failing Test

Let's experience the TDD cycle with pytest-watch. Create a simple failing test:

In `tests/test_weather_agent.py`, add this test:

```python
def test_placeholder_that_fails():
    """This test demonstrates the RED phase"""
    assert False, "This test intentionally fails"
```

Save the file. Watch pytest-watch automatically detect the change and run tests:

```
File change detected: tests/test_weather_agent.py
Rerunning tests...
================================ test session starts =================================

test_weather_agent.py::test_placeholder_that_fails FAILED

FAILED tests/test_weather_agent.py::test_placeholder_that_fails
assert False, "This test intentionally fails"

================================ 1 failed in 0.15s ==================================

Now watching...
```

**What just happened:**
1. You saved the file
2. pytest-watch detected the change
3. Tests ran automatically
4. You saw the failure immediately (RED phase)

### Activity 2.8.4: Fix the Test

Now fix the test by changing `assert False` to `assert True`:

```python
def test_placeholder_that_fails():
    """This test demonstrates the GREEN phase"""
    assert True  # Now it passes
```

Save the file. Watch pytest-watch automatically re-run and show the test passing:

```
File change detected: tests/test_weather_agent.py
Rerunning tests...
================================ test session starts =================================
...
================================ 2 passed in 0.18s =================================

Now watching...
```

**What just happened:**
1. You saved the file
2. pytest-watch detected the change
3. Tests ran automatically
4. You saw the pass immediately (GREEN phase)

This is the **magic of TDD with pytest-watch** - instant feedback!

### Activity 2.8.5: Stop Watch Mode

To stop pytest-watch, press `Ctrl+C` in the terminal.

### Understanding Check 2.8a

**Question:** "What did you observe when pytest-watch was running? How quickly did tests re-run after you saved files?"

Tell me:
1. Did tests run automatically after each file save?
2. How fast was the feedback loop?
3. How did it feel compared to manually running pytest?

---

<a id="lesson-2-9-the-tdd-cycle-with-pytest-watch"></a>

## Lesson 2.9: The Complete TDD Cycle with pytest-watch

### What You'll Learn
How to combine RED → GREEN → REFACTOR cycle with pytest-watch for maximum productivity

### The TDD Cycle Visualized

```
START HERE
    ↓
┌───────────────┐
│     RED       │ Write failing test
│ (Failing)     │ Save file → pytest-watch runs
│               │ See test FAIL ✗
└───────┬───────┘
        ↓
┌───────────────┐
│     GREEN     │ Write minimal code to pass test
│ (Passing)     │ Save file → pytest-watch runs
│               │ See test PASS ✓
└───────┬───────┘
        ↓
┌───────────────┐
│   REFACTOR    │ Improve code (don't change behavior)
│  (Improving)  │ Save file → pytest-watch runs
│               │ Tests still PASS ✓
└───────┬───────┘
        ↓
    Is code done?
    ├─ YES → Commit to git → Done! ✓
    └─ NO → Write next failing test → Loop back to RED
```

### RED Phase: Write Failing Test

**Goal:** Write a test that **fails** because the feature doesn't exist yet

```python
# tests/test_weather_agent.py
def test_agent_returns_string():
    """Agent should return a string response"""
    from src.ai_wheather_agent.weather import WeatherAgent

    agent = WeatherAgent()
    result = agent.run("What's the weather?")
    assert isinstance(result, str)
```

**What happens:**
- You save the file
- pytest-watch detects change
- Pytest runs → FAILS (WeatherAgent doesn't exist yet)
- You see: `FAILED - ModuleNotFoundError`

This is **intentional and good**! You're in RED phase.

### GREEN Phase: Write Minimal Code

**Goal:** Write the **smallest possible code** to make the test pass

```python
# src/ai_wheather_agent/weather.py
class WeatherAgent:
    def run(self, question: str) -> str:
        return "Response"  # Minimal code to pass
```

**What happens:**
- You save the file
- pytest-watch detects change
- Pytest runs → PASSES ✓
- You see: `1 passed`

You're now in GREEN phase. The test passes!

### REFACTOR Phase: Improve Code

**Goal:** Make the code better **without changing behavior**

```python
# src/ai_wheather_agent/weather.py
class WeatherAgent:
    """A weather agent that answers weather questions"""

    def run(self, question: str) -> str:
        """
        Run the agent with a question.

        Args:
            question: The user's question

        Returns:
            The agent's response
        """
        return self._generate_response(question)

    def _generate_response(self, question: str) -> str:
        """Generate a response to the question"""
        return "Response"
```

**What happens:**
- You save the file
- pytest-watch detects change
- Pytest runs → PASSES ✓ (behavior unchanged)
- You see: `1 passed`

You're in REFACTOR phase. Code is better but tests still pass!

### Why This Matters

The **TDD cycle with pytest-watch** creates a powerful development experience:

1. **RED** - Quick feedback that test fails (problem identified)
2. **GREEN** - Quick feedback that test passes (problem solved)
3. **REFACTOR** - Quick feedback that tests still pass (improvement verified)

Each cycle takes **seconds**, not minutes. You stay in "flow state" because the feedback is instant.

### Real-World Example: Build a Simple Weather Function

Let's trace through a real example:

**Iteration 1: RED**
```python
# tests/test_weather_agent.py
def test_get_temperature_tokyo():
    from src.ai_wheather_agent.weather import get_temperature
    temp = get_temperature("Tokyo")
    assert temp == "22°C"
```
→ Save → pytest-watch runs → FAIL (function doesn't exist) ✗

**Iteration 1: GREEN**
```python
# src/ai_wheather_agent/weather.py
def get_temperature(city: str) -> str:
    return "22°C"  # Minimal code
```
→ Save → pytest-watch runs → PASS ✓

**Iteration 1: REFACTOR**
```python
# src/ai_wheather_agent/weather.py
def get_temperature(city: str) -> str:
    """Get temperature for a city."""
    # Minimal implementation (same behavior)
    return "22°C"
```
→ Save → pytest-watch runs → PASS ✓

**Iteration 2: RED** (Add more functionality)
```python
# tests/test_weather_agent.py
def test_get_temperature_varies_by_city():
    from src.ai_wheather_agent.weather import get_temperature
    assert get_temperature("Tokyo") == "22°C"
    assert get_temperature("New York") == "15°C"
```
→ Save → pytest-watch runs → FAIL (New York returns "22°C") ✗

**Iteration 2: GREEN**
```python
# src/ai_wheather_agent/weather.py
def get_temperature(city: str) -> str:
    """Get temperature for a city."""
    if city == "Tokyo":
        return "22°C"
    elif city == "New York":
        return "15°C"
    return "Unknown"
```
→ Save → pytest-watch runs → PASS ✓

**Iteration 2: REFACTOR**
```python
# src/ai_wheather_agent/weather.py
TEMPERATURES = {
    "Tokyo": "22°C",
    "New York": "15°C",
}

def get_temperature(city: str) -> str:
    """Get temperature for a city."""
    return TEMPERATURES.get(city, "Unknown")
```
→ Save → pytest-watch runs → PASS ✓

And so on... Each iteration gets you closer to a real implementation!

### Understanding Check 2.9a

**Question:** "Walk through one RED → GREEN → REFACTOR cycle. What was the test? What was the minimal code? How did you refactor?"

Describe a cycle you've experienced or imagine one based on the example above.

---

<a id="lesson-2-10-integrating-all-tools"></a>

## Lesson 2.10: Putting It All Together - Your Complete Workflow

### What You'll Learn
How ruff, pre-commit, and pytest-watch work together for professional development

### The Complete Workflow

```
┌──────────────────────────────────────────────────────────┐
│                    YOUR DEVELOPMENT FLOW                 │
└──────────────────────────────────────────────────────────┘

STEP 1: Start Development Session
  ├─ Open terminal 1: just watch (pytest-watch)
  ├─ Open terminal 2 or IDE for editing
  └─ Ready to code!

STEP 2: TDD Cycle (RED → GREEN → REFACTOR)
  ├─ Write failing test
  │  └─ Save → pytest-watch runs → RED (fail) ✗
  ├─ Write minimal code
  │  └─ Save → pytest-watch runs → GREEN (pass) ✓
  ├─ Refactor code
  │  └─ Save → pytest-watch runs → STILL GREEN ✓
  └─ Repeat for next feature

STEP 3: Before Committing
  ├─ Stop pytest-watch (Ctrl+C)
  ├─ Run quality assurance: just qa
  │  ├─ ruff format .     (Format code)
  │  ├─ ruff check --fix  (Fix linting)
  │  ├─ Type checking
  │  └─ Full test suite
  └─ All checks pass ✓

STEP 4: Git Commit
  ├─ git add .
  ├─ git commit -m "feat: your feature"
  ├─ pre-commit hooks run automatically:
  │  ├─ ruff (check & format)
  │  ├─ ruff-format
  │  ├─ trailing-whitespace
  │  ├─ end-of-file-fixer
  │  ├─ check-yaml
  │  ├─ check-toml
  │  └─ check-added-large-files
  ├─ If all pass → Commit succeeds ✓
  └─ If any fail → Commit blocked, fix & retry

STEP 5: Push to GitHub
  ├─ git push
  └─ Ready for code review!
```

### Tool Integration Breakdown

**pytest-watch** (Terminal 1)
```
your-project$ just watch
[PYTEST WATCH] Starting pytest...
1 passed in 0.15s
Now watching...
```
**Purpose:** Instant feedback during development (TDD enabled)

**ruff + pre-commit** (Automatic at commit time)
```
your-project$ git commit -m "feat: weather agent"
ruff.........................................................Passed
ruff-format.................................................Passed
trailing-whitespace.........................................Passed
...
[feature/01 abc123] feat: weather agent
```
**Purpose:** Code quality gate before code enters git

**just qa** (Before committing)
```
your-project$ just qa
✓ Formatting code with ruff...
✓ Fixing issues with ruff...
✓ Type checking with ty...
✓ Running tests with pytest...
All checks passed!
```
**Purpose:** Comprehensive check before attempting commit

### Example: Real Development Session

**Time: 9:00 AM - Start coding**
```bash
# Terminal 1
$ just watch
1 passed in 0.15s
Now watching...
```

**9:05 AM - Write failing test**
```python
# Your editor - tests/test_weather_agent.py
def test_weather_agent_accepts_question():
    agent = WeatherAgent()
    result = agent.run("What's the weather in Tokyo?")
    assert isinstance(result, str)
    assert len(result) > 0
```

```bash
# Terminal 1 automatically shows:
File change detected: tests/test_weather_agent.py
FAILED tests/test_weather_agent.py::test_weather_agent_accepts_question
```

**9:10 AM - Write minimal code (GREEN)**
```python
# Your editor - src/ai_wheather_agent/weather.py
class WeatherAgent:
    def run(self, question: str) -> str:
        return "Default response"
```

```bash
# Terminal 1 automatically shows:
File change detected: src/ai_wheather_agent/weather.py
2 passed in 0.18s
```

**9:15 AM - Refactor**
```python
# Your editor - improved version
class WeatherAgent:
    """AI agent for weather queries"""

    def run(self, question: str) -> str:
        """Process a weather question and return response"""
        return self._get_response(question)

    def _get_response(self, question: str) -> str:
        return "Default response"
```

```bash
# Terminal 1 automatically shows:
File change detected: src/ai_wheather_agent/weather.py
2 passed in 0.20s
```

**5:00 PM - Ready to commit**
```bash
# Terminal 1
$ <Ctrl+C> (stop watch)

# Terminal 2
$ just qa
✓ Formatting code with ruff...
✓ Fixing issues with ruff...
✓ Type checking...
✓ Running tests...
All checks passed!

$ git add .
$ git commit -m "feat: add WeatherAgent class"
ruff.........................................................Passed
ruff-format.................................................Passed
[feature/01 12345ab] feat: add WeatherAgent class
```

**Done!** Your code is:
- ✅ Tested (pytest-watch verified)
- ✅ Formatted (ruff)
- ✅ Linted (ruff check)
- ✅ Type-checked (ty)
- ✅ Pre-commit verified (all hooks passed)

### Pro Tips for Productivity

| Tip | Why It Matters |
|-----|----------------|
| Keep `just watch` running all day | Instant feedback = flow state |
| Save files frequently (Ctrl+S every few seconds) | Tests run constantly, catch regressions fast |
| Write small tests | Tests run faster, feedback is quicker |
| Use descriptive test names | Understand failures at a glance |
| Refactor with tests watching | Know immediately if you break anything |
| Run `just qa` before every commit | Catch issues before pre-commit does |

### Understanding Check 2.10a

**Question:** "Describe your ideal development session using all three tools (pytest-watch, ruff, pre-commit). What tools are you using when?"

Think about:
- When do you start pytest-watch?
- When do you run ruff/just qa?
- When does pre-commit run automatically?
- How do these tools work together?

---

## Quick Reference Commands

```bash
# Navigate to project
cd /Users/mhcj/Downloads/github/generic/ai-wheather-agent

# View available commands
just list

# TDD Development
just watch          # Start watch mode (tests re-run on save)
just test           # Run tests once
just test -v        # Run tests with verbose output

# Code Quality
ruff check .        # Find issues
ruff check . --fix  # Auto-fix issues
ruff format .       # Format code

# Full QA Pipeline
just qa             # Format, lint, type-check, test

# Build
just build          # Build distribution
just clean          # Remove artifacts
```

---

## Important Files

| File | What It Does |
|------|--------------|
| `pyproject.toml` | Project config, dependencies, tool settings |
| `justfile` | Commands for testing, linting, etc |
| `src/ai_wheather_agent/weather.py` | Agent code (TO BUILD) |
| `src/ai_wheather_agent/tools/weather.py` | Weather tool (TO CREATE) |
| `tests/test_weather_agent.py` | Tests (TO WRITE) |
| `training/training.md` | This file |

---

## Hints for Understanding

- **Confused about agents?** Think of them like a robot that can think and use tools
- **Confused about TDD?** Think "Test First, Code Second"
- **Confused about LangGraph?** Think "flowchart for agents"
- **Confused about scenario?** Think "real conversation simulation"
