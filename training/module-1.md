
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

## 📝 Training Notes

**When returning to this project:**
1. Check the "Quick Jump Navigation" section at the top
2. See your current location
3. Run `just watch` to start developing with instant feedback
4. Run `just test` to verify all tests pass

---

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)
