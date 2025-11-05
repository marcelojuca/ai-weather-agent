 # PROMPT
 I am learning AI and new software development concepts. I asked the best practices to develop an AI agentic solution using python, tdd and test framework as the current websites and trainings do not have such things or I wasn't able to find any training in such thing. Grok introduced me to new concepts (ruff pre-commit pytest langwatch-scenario pytest pytest-watch) and I was able to get a git clone from a project that uses such technologies. I would like you to be my tutor on these tecnologies and drive me through the code base, concepts and technologies used in this project. Feel free to review Grok answer and evaluate a better approach. Create a plan and to-do list so we can go through this and I can learn on how to create ai agents in a TDD mode to expedite my development and ensure I can have tests on them.

Create a file (@training/training-topics.md) with the lectures/topics to be covered (training plan) and keep track of the training progress in abother file (@training/current-training.md). This approach will allow to know what have already been covered and what is pending, otherwise, when I turn off the computer or close this session, your memory is gone forever. The idea is to make this training "interactive, beginner-friendly learning guide" and as the trainining progress, the file @training/training-topics.md can be adjusted.

Create a table of contents to @training/training-topics.md with hiperlinks. For hyperlinks, remember that VS Code preview doesn't support the {#anchor} syntax, so use HTML anchors instead. Example: in the Quick Jump Navigation section " - ✅ [Lesson 2.4 - pre-commit Understanding](#lesson-2-4-pre-commit-understanding)" and later in the document "<a id="lesson-2-5-pre-commit-setup"></a>".

At the end of each completed lesson, add a hyperlink to the "quick jump navigation" section labeled "↑ Back to Quick Jump Navigation".

Add to the very top of the file @training/current-training.md a hyperlink to facilitate the user to click and go directly to the lesson this student needs to focus on, otherwise the student might get lost in this document. See example below:

Add a complete hyperlink guide to current-training.md file. And when you (ai agente) refer to lessons in the student terminal messages, you (ai agent) includes clickable links that jump directly to those sections! This allow

Ensure the headings into (@training/current-training.md) are set up correctly where Markdown automatically creates anchors from headings.  Add a hyperlink guide section to the end of this document with a comprehensive guide showing how to use hyperlinks in future communications (ai agent vs student through terminal). This way, when the ai agent refers to lessons in terminal messages, the ai agent will include clickable links that jump directly to those sections facilitanting student's nagivation!
Example:  "Read: training/current-training.md#lesson-2-5-pre-commit-hands-on-part-2---setting-up"


## ----- Start of example to the @training/current-training.md -----

## 🎯 Quick Jump Navigation

**Where you are right now:**

- ✅ [Module 1 - COMPLETED](#module-1-the-big-picture) - The Big Picture (TDD, Agents, LangGraph, Tools)
- 🔄 **[Module 2 - IN PROGRESS](#module-2-hands-on-with-development-tools)** ← YOU ARE HERE!
  - ✅ [Lesson 2.1 - ruff Finding Issues](#lesson-21-ruff-hands-on-part-1---finding-issues)
  - 🔄 [Lesson 2.2 - ruff Fixing Issues](#lesson-22-ruff-hands-on-part-2---fixing-automatically) ← FOCUS ON THIS NOW
  - ⏳ [Lesson 2.3 - ruff Configuration](#lesson-23-ruff-configuration)
  - ⏳ [Lesson 2.4+ - pre-commit & pytest-watch](#lesson-24-pre-commit-hands-on-part-1---installation)

**Completed Modules:**
- ✅ [Module 1 Understanding Check](#understanding-check-11---passed-)

**Coming Up Next:**
- ⏳ Module 3 - Deep Dive into LangGraph
- ⏳ Module 4 - Scenario Testing Framework
- ⏳ Module 5 - Build Weather Agent
- ⏳ Module 6 - Fix ai-wheather-agent Project
- ⏳ Module 7 - Scale Up Multi-Agent Systems
- ⏳ Module 8 - Deploy & Monitor

---

## ----- End of example to the @training/current-training.md -----



# CONVERSATION with GROK AI

what would be the best idea for starting developing a solution using python, tdd, and test framework?Here’s the best, battle-tested idea to start developing a Python solution using TDD + an AI-agent-focused test framework — from zero to production-ready, with maximum speed, safety, and scalability.

The Ultimate Starter Stack: TDD + AI Agents + Python



































LayerToolWhy It’s the BestTest Frameworkpytest + scenarioJest-like DX + full AI agent simulationTDD WorkflowRed → Green → Refactor (AI-driven)Enforced by tests + LLM feedbackAI Agent FrameworkLangGraph (by LangChain)Stateful, debuggable, production-grade agentsProject StructureCookiecutter + pyproject.tomlClean, scalable, CI-readyDev Toolsruff, pre-commit, pytest-watchInstant feedback loop

Step-by-Step: Build Your First AI Agent with TDD
1. Start with the Test (Red Phase)
python# tests/test_weather_agent.py
import pytest
import scenario
from agents.weather import get_weather_agent

@scenario.test(
    description="User asks for weather in Tokyo → agent returns current temp & condition",
    agents=[
        scenario.UserSimulatorAgent(),
        scenario.JudgeAgent(criteria=[
            "Response includes temperature in °C",
            "Response includes condition (e.g., sunny, rainy)",
            "No hallucinations about future dates",
            "Uses weather API tool correctly",
        ])
    ],
    max_turns=3
)
def test_weather_agent():
    result = scenario.run(get_weather_agent())
    assert result.success  # Will fail until agent works

This fails immediately — perfect for TDD.


2. Write Minimal Agent to Pass (Green Phase)
python# agents/weather.py
from langgraph.graph import StateGraph, MessagesState
from langchain_openai import ChatOpenAI
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

Run pytest → Green!


3. Refactor with Confidence

Add logging
Split tools
Add error handling
Tests still pass


Full Project Setup (Copy-Paste Ready)
bash# 1. Create project
cookiecutter https://github.com/Teemu/cookiecutter-pypackage
# → Name: ai-weather-agent, etc.

cd ai-weather-agent

# 2. Install deps
pip install pytest scenario langgraph langchain-openai ruff pre-commit pytest-watch

# 3. Initialize pre-commit
pre-commit install
pyproject.toml (Critical!)
toml[project]
name = "ai-weather-agent"
dependencies = [
    "langgraph",
    "langchain-openai",
    "scenario",
]

[tool.pytest.ini_options]
addopts = "--cov=agents --cov-report=term-missing"

[tool.ruff]
select = ["E", "F", "B", "I"]

TDD Workflow (AI-Agent Optimized)






























PhaseCommandWhat You DoRedptwWrite failing scenario.testGreenpytestMinimal agent + toolsRefactorruff . --fixClean code, add typesRepeatptwWatch mode auto-reruns
bash# Start TDD loop
ptw  # pytest-watch: auto-run on save

Bonus: AI-Powered Test Generation
Use Claude/CodeWhisperer to generate test scenarios:
promptGenerate 5 TDD test scenarios using `scenario` for a weather agent that:
- Handles typos in city names
- Rejects invalid dates
- Uses metric units by default
- Falls back gracefully on API failure
→ Paste into tests/ → Red → Green → Refactor

Why This Is the Best Starting Point





























BenefitHow It’s AchievedFast Feedbackptw + ruff = sub-second loopAI-Agent Safescenario simulates real usersProduction Readylanggraph + observabilityScalableCookiecutter + CI/CD readyFun & ProductiveFeels like Jest + AI superpowers

Next Steps (Scale It)

Add LangSmith for tracing
Add human-in-the-loop approval node
Deploy with FastAPI + LangGraph Cloud
Add evals dashboard with scenario.report()


Start Now:
bashcookiecutter https://github.com/Teemu/cookiecutter-pypackage
# → Add the test above → `ptw`
You’ll have a TDD-driven, AI-agent-powered Python app in <15 minutes.
Want me to generate the full GitHub repo template with CI, docs, and example agent? Just say the word.2swhat is cookiecutter?Cookiecutter is a command-line Python tool that generates projects from reusable templates — like a "project boilerplate generator."
Think of it as "Create React App" or "Vite" for Python — but universal: it works for any kind of project (CLI tools, web apps, data science, AI agents, etc.).

Why Use Cookiecutter?

























ProblemCookiecutter Solves ItYou copy-paste old projects to start new onesGenerates clean, consistent structure every timeTeams have different setups (linting, tests, CI)Enforces best practices across all projectsYou forget to add pyproject.toml, README, testsAuto-includes everything you needStarting from scratch takes 30+ mins< 2 minutes to full project skeleton

How It Works (Simple Example)
bashpip install cookiecutter
bashcookiecutter https://github.com/audreyr/cookiecutter-pypackage
It asks you a few questions:
textproject_name [My Awesome Project]: AI Weather Agent
project_slug [ai_weather_agent]:
author_name [Your Name]: Alice Dev
Then generates this structure instantly:
textai_weather_agent/
├── ai_weather_agent/
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
├── README.md
├── .github/workflows/ci.yml
├── .gitignore
└── LICENSE
All files are pre-filled with your answers.

Best Cookiecutter Templates for Python + TDD + AI






























Use CaseTemplateLinkGeneral Python Packagecookiecutter-pypackagecookiecutter https://github.com/audreyr/cookiecutter-pypackageAI/ML Projectscookiecutter-data-sciencecookiecutter https://github.com/drivendata/cookiecutter-data-scienceFastAPI + AI Agentscookiecutter-fastapicookiecutter https://github.com/rochacbruno/cookiecutter-fastapiLangChain / AI AppsCustom (we’ll make one!)See below

Pro Tip: Make Your Own AI + TDD Template
Create cookiecutter-ai-agent/ with this structure:
textcookiecutter-ai-agent/
├── {{ cookiecutter.project_slug }}/
│   ├── agents/
│   │   └── __init__.py
│   ├── tools/
│   ├── tests/
│   │   └── test_agent.py
│   ├── pyproject.toml
│   └── cookiecutter.json
└── hooks/
cookiecutter.json (the brain):
json{
  "project_name": "AI Agent Project",
  "project_slug": "{{ cookiecutter.project_name|lower|replace(' ', '_') }}",
  "use_langgraph": "y",
  "include_tests": "y",
  "author": "Your Name"
}
Then run:
bashcookiecutter cookiecutter-ai-agent
→ Instant TDD-ready AI agent project with pytest, scenario, langgraph, etc.

Real-World Example (From Earlier)
bashcookiecutter https://github.com/Teemu/cookiecutter-pypackage
# → Name: AI Weather Agent
You get:

pyproject.toml with pytest, ruff
tests/ folder
README.md with badges
CI workflow

Then just add:
bashpip install langgraph scenario
And start TDD immediately.

Install & Use in 30 Seconds
bashpip install cookiecutter
cookiecutter gh:audreyr/cookiecutter-pypackage
Done. You’re ready to code.

TL;DR: Cookiecutter = "Project Starter on Steroids"















Like This→Becomes ThisCopy old folder → edit names → forget files→cookiecutter <template> → perfect project in 60 seconds

Want me to generate a full cookiecutter-ai-agent-tdd template with:

langgraph
scenario tests
ruff + pre-commit
ptw watch mode
GitHub Actions

Just say: "Generate the template" — I’ll give you the full repo-ready version.1.5sgenerate the full GitHub repo templateHere is a complete, ready-to-use GitHub repo template for TDD-driven AI agent development in Python using:

cookiecutter (to generate projects)
pytest + scenario (AI-agent TDD)
LangGraph (stateful agents)
ruff, pre-commit, pytest-watch
Full CI, docs, and example agent


GitHub Repo: cookiecutter-ai-agent-tdd

Link: https://github.com/yourname/cookiecutter-ai-agent-tdd (you’ll create it)
Use it: cookiecutter gh:yourname/cookiecutter-ai-agent-tdd


Project Structure (After Generation)
bashai-weather-agent/                  # ← Your new project
├── ai_weather_agent/
│   ├── __init__.py
│   ├── agents/
│   │   ├── __init__.py
│   │   └── weather_agent.py       # ← LangGraph agent
│   └── tools/
│       ├── __init__.py
│       └── weather.py             # ← Tool (mockable)
├── tests/
│   ├── __init__.py
│   └── test_weather_agent.py      # ← scenario + TDD test
├── .github/
│   └── workflows/
│       └── ci.yml                 # ← GitHub Actions
├── .gitignore
├── pyproject.toml                 # ← Build, deps, ruff, pytest
├── README.md
├── LICENSE
├── cookiecutter.json              # ← Template config
└── hooks/
    └── post_gen_project.py        # ← Auto-setup script

1. cookiecutter.json (Template Config)
json{
  "project_name": "AI Weather Agent",
  "project_slug": "{{ cookiecutter.project_name|lower|replace(' ', '_')|replace('-', '_') }}",
  "author_name": "Your Name",
  "author_email": "you@example.com",
  "description": "A TDD-driven AI agent that answers weather queries using tools.",
  "use_openai": "y",
  "include_langsmith": "n",
  "python_version": "3.11"
}

2. pyproject.toml
toml[project]
name = "{{ cookiecutter.project_slug }}"
version = "0.1.0"
description = "{{ cookiecutter.description }}"
authors = [{name = "{{ cookiecutter.author_name }}", email = "{{ cookiecutter.author_email }}"}]
dependencies = [
    "langgraph",
    "langchain-openai; {{ cookiecutter.use_openai == 'y' }}",
    "scenario",
    "httpx"
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-cov",
    "pytest-watch",
    "ruff",
    "pre-commit",
    "scenario"
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
select = ["E", "F", "B", "I"]
ignore = []
fixable = ["ALL"]
line-length = 100

[tool.pytest.ini_options]
addopts = "--cov=ai_weather_agent --cov-report=term-missing -ra"
testpaths = ["tests"]
python_paths = ["."]

[tool.coverage.run]
branch = true
source = ["ai_weather_agent"]

3. ai_weather_agent/tools/weather.py
pythonfrom typing import Dict

def get_current_weather(location: str) -> Dict[str, str]:
    """Mockable weather tool."""
    # In real app: call OpenWeatherMap API
    mock_data = {
        "Tokyo": {"temp": "22", "condition": "sunny"},
        "London": {"temp": "15", "condition": "rainy"},
        "New York": {"temp": "18", "condition": "cloudy"},
    }
    return mock_data.get(location.capitalize(), {"temp": "unknown", "condition": "unknown"})

4. ai_weather_agent/agents/weather_agent.py
pythonfrom langgraph.graph import StateGraph, MessagesState
from langchain_openai import ChatOpenAI
from ai_weather_agent.tools.weather import get_current_weather
from typing import Literal

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def should_use_tool(state: MessagesState) -> Literal["tools", "__end__"]:
    last_msg = state["messages"][-1]
    return "tools" if last_msg.tool_calls else "__end__"

def call_tool(state: MessagesState):
    tool_call = state["messages"][-1].tool_calls[0]
    if tool_call["name"] == "get_current_weather":
        location = tool_call["args"]["location"]
        result = get_current_weather(location)
        return {"messages": [f"{location}: {result['temp']}°C, {result['condition']}"]}
    return {"messages": ["Error: Unknown tool."]}

graph = StateGraph(MessagesState)
graph.add_node("agent", lambda s: {"messages": [llm.invoke(s["messages"])]})
graph.add_node("tools", call_tool)

graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_use_tool)
graph.add_edge("tools", "agent")

weather_agent = graph.compile()

5. tests/test_weather_agent.py
pythonimport pytest
import scenario
from ai_weather_agent.agents.weather_agent import weather_agent

@scenario.test(
    description="User asks for weather in Tokyo → agent uses tool and responds correctly",
    agents=[
        scenario.UserSimulatorAgent(),
        scenario.JudgeAgent(criteria=[
            "Response includes temperature in °C",
            "Response includes weather condition",
            "Location 'Tokyo' is mentioned",
            "No hallucinations",
            "Tool 'get_current_weather' was called exactly once"
        ])
    ],
    max_turns=4
)
def test_weather_agent_tokyo():
    result = scenario.run(weather_agent, initial_message="What's the weather in Tokyo?")
    assert result.success

6. .github/workflows/ci.yml
yamlname: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install .[dev]
      - name: Lint with ruff
        run: ruff check .
      - name: Test with pytest
        run: pytest

7. hooks/post_gen_project.py (Auto-setup)
python#!/usr/bin/env python
import os
import subprocess

print("Setting up pre-commit...")
subprocess.call(["pre-commit", "install"])

print("Installing dev dependencies...")
subprocess.call(["pip", "install", ".[dev]"])

print("Running initial ruff fix...")
subprocess.call(["ruff", "check", "--fix"])

print("Done! Run: ptw  # to start TDD")

8. README.md (Auto-generated)
markdown# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## TDD Workflow

```bash
ptw  # Watch mode: auto-run tests on save
Run Agent
pythonfrom ai_weather_agent.agents.weather_agent import weather_agent
result = weather_agent.invoke({"messages": [{"role": "user", "content": "Weather in London?"}]})
print(result["messages"][-1].content)
Test
bashpytest
Dev Tools

ruff: Linting & formatting
pre-commit: Git hooks
scenario: AI agent testing
langgraph: Stateful agents

text---

## How to Use This Template

### 1. Create the Repo

```bash
# On your machine
cookiecutter https://github.com/yourname/cookiecutter-ai-agent-tdd
2. Or Use Directly from GitHub
bashcookiecutter gh:yourname/cookiecutter-ai-agent-tdd

Push to GitHub
bashcd ai-weather-agent
git init
git add .
git commit -m "feat: initial TDD AI agent"
git branch -M main
git remote add origin https://github.com/yourname/ai-weather-agent.git
git push -u origin main

Result
You now have:

TDD-first AI agent project
Zero-config testing with scenario
Watch mode (ptw)
CI/CD
Clean architecture
Scalable to multi-agent systems


Want This Live?

Create the repo: github.com/new → Name: cookiecutter-ai-agent-tdd
Copy all files above into it
Push
Use it forever


I’ve included everything — just copy, push, and start TDD.
Say “Deploy to GitHub” and I’ll give you the exact git commands + repo URL setup.2.2swhat is ruff, pre-commit, pytest-watch?Here’s a clear, practical breakdown of the three essential Python dev tools you asked about — Ruff, pre-commit, and pytest-watch — with why they matter, how they work, and real examples.

1. Ruff – The Lightning-Fast Linter & Formatter

Think of it as: black + flake8 + isort + pyupgrade — but 100x faster

What It Does

Lints your code (catches bugs, style issues)
Formats your code (auto-fixes spacing, quotes, etc.)
Replaces 10+ tools in one

Why It’s Amazing

























FeatureBenefitSpeed10–100x faster than flake8/pylintZero configWorks out of the boxAuto-fixruff check --fix = clean code instantlyBuilt-in formatterNo need for black
Example
bash# Install
pip install ruff

# Lint + auto-fix
ruff check . --fix

# Format (like black)
ruff format .
Before (bad.py):
pythonimport  sys,os
def hello():print("hi")
After:
bashruff check bad.py --fix
pythonimport os
import sys


def hello() -> None:
    print("hi")

2. pre-commit – Git Hooks That Run Checks Before You Commit

Think of it as: A guard at the door — “No bad code gets in!”

What It Does

Runs linters, tests, formatters automatically on git commit
Blocks the commit if checks fail

Why It’s Essential





















BenefitExampleNo bad code in historyruff, black, tests run automaticallyTeam consistencyEveryone follows same rulesCatch bugs earlyFail fast
Setup (One-Time)
bashpip install pre-commit
.pre-commit-config.yaml (in your repo):
yamlrepos:
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
bashpre-commit install
Now every git commit runs:
bash→ ruff check --fix
→ ruff format
→ check for trailing spaces
If anything fails → commit blocked until fixed.

3. pytest-watch (ptw) – TDD on Steroids

Think of it as: jest --watch for Python

What It Does

Watches your files
Re-runs pytest automatically when you save
Instant feedback loop

Why You Need It for TDD





















FeatureBenefitSub-second feedbackSave → test runs → see red/greenNo manual pytest typingPure flow statePerfect for AI agent TDDTest complex agent behavior fast
Example
bashpip install pytest-watch
bashptw
# or: ptw -- --cov
You edit test_agent.py → save →
text============================= test session starts ==============================
test_agent.py::test_weather_agent_tokyo PASSED                            [100%]

============================== 1 passed in 0.12s ===============================

How They Work Together (TDD Heaven)
bash# 1. Start TDD loop
ptw

# 2. Write failing test → save
#    → ptw runs pytest → RED

# 3. Write minimal code → save
#    → ptw runs → GREEN

# 4. git commit
#    → pre-commit runs ruff → auto-fixes
#    → commit passes
Full cycle: < 5 seconds

One-Liner Setup (Add to Any Project)
bashpip install ruff pre-commit pytest-watch
echo -e "repos:\n- repo: https://github.com/astral-sh/ruff-pre-commit\n  rev: v0.6.8\n  hooks:\n  - id: ruff\n    args: [--fix]\n  - id: ruff-format" > .pre-commit-config.yaml
pre-commit install

Summary Table





























ToolReplacesCommandWhen It RunsRuffblack, flake8, isortruff check --fixOn save or commitpre-commitManual checksgit commitBefore commitpytest-watchManual pytestptwOn file save

TL;DR: Install These 3 Lines
bashpip install ruff pre-commit pytest-watch
pre-commit install
ptw  # ← Start TDD now
You now have:

Blazing fast linting/formatting
Zero bad commits
Instant test feedback

You’re now 10x faster at TDD — especially with AI agents.
Want me to generate a .devcontainer, VS Code settings, or GitHub Actions that include all 3? Just say the word.2.3sgenerate a .devcontainer, VS Code settings, and GitHub Actions that include all 3Here is a complete, production-ready setup for VS Code + Dev Containers + GitHub Actions that includes:

ruff (linter & formatter)
pre-commit (git hooks)
pytest-watch (TDD loop)
scenario + langgraph (AI agent TDD)
Auto-install on container start
Full CI/CD


1. .devcontainer/devcontainer.json
json{
  "name": "AI Agent TDD (Python)",
  "image": "mcr.microsoft.com/devcontainers/python:3.11",
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  },
  "postCreateCommand": "pip install --no-cache-dir ruff pre-commit pytest-watch scenario langgraph langchain-openai && pre-commit install",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.black-formatter",
        "charliermarsh.ruff",
        "ms-vscode.test-adapter-converter"
      ],
      "settings": {
        "python.defaultInterpreterPath": "/usr/local/bin/python",
        "python.linting.enabled": true,
        "python.linting.ruffEnabled": true,
        "python.formatting.provider": "none",
        "[python]": {
          "editor.defaultFormatter": "charliermarsh.ruff",
          "editor.formatOnSave": true,
          "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "explicit",
            "source.organizeImports.ruff": "explicit"
          }
        },
        "ruff.path": ["ruff"],
        "files.watcherExclude": {
          "**/.git/**": true,
          "**/venv/**": true,
          "**/.venv/**": true
        }
      }
    }
  },
  "remoteUser": "vscode"
}

2. .vscode/settings.json (Optional – overrides if not using devcontainer)
json{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "python.formatting.provider": "none",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll.ruff": "explicit",
      "source.organizeImports.ruff": "explicit"
    }
  },
  "ruff.path": ["ruff"],
  "terminal.integrated.defaultProfile.linux": "bash"
}

3. .vscode/tasks.json – Run TDD with One Click
json{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "TDD: Watch Tests",
      "type": "shell",
      "command": "ptw",
      "group": "test",
      "problemMatcher": [],
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "dedicated"
      },
      "isBackground": true,
      "runOptions": {
        "runOn": "folderOpen"
      }
    },
    {
      "label": "Run Pre-Commit",
      "type": "shell",
      "command": "pre-commit run --all-files",
      "group": "build"
    }
  ]
}

Press Ctrl+Shift+P → "Tasks: Run Task" → "TDD: Watch Tests" → Instant TDD loop!


4. .vscode/launch.json – Debug Tests
json{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug Current Test File",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/tests/${relativeFile}",
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}

5. .github/workflows/ci.yml – Full CI with All 3 Tools
yamlname: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
          cache: "pip"

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install .[dev]

      - name: Install pre-commit
        run: pre-commit install

      - name: Lint with ruff
        run: ruff check . --fix

      - name: Format with ruff
        run: ruff format . --check

      - name: Run pre-commit hooks
        run: pre-commit run --all-files

      - name: Test with pytest
        run: pytest --cov=ai_weather_agent --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4

6. .pre-commit-config.yaml
yamlrepos:
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

7. pyproject.toml (Add [dev] extras)
toml[project.optional-dependencies]
dev = [
  "ruff",
  "pre-commit",
  "pytest",
  "pytest-cov",
  "pytest-watch",
  "scenario",
  "langgraph",
  "langchain-openai"
]

How to Use (Step-by-Step)
1. Clone & Open in VS Code
bashgit clone https://github.com/yourname/ai-weather-agent.git
code ai-weather-agent
→ VS Code detects .devcontainer → "Reopen in Container"
2. Container Builds & Installs Everything

ruff, pre-commit, pytest-watch, scenario, langgraph
pre-commit install runs automatically

3. Start TDD
Press Ctrl+Shift+P → "Tasks: Run Task" → "TDD: Watch Tests"
Or in terminal:
bashptw
4. Write Test → Save → See Red/Green
python# tests/test_weather_agent.py
@scenario.test(...)
def test_weather_agent_tokyo():
    ...
→ Save → ptw runs → Red → Green → Commit
5. Commit with Confidence
bashgit add .
git commit -m "feat: add weather agent"
# → pre-commit runs ruff + format
# → Commit passes

Final Result





























ToolWhere It RunsruffOn save (VS Code), git commit, CIpre-commitOn git commit, CIpytest-watchOn file save (ptw)scenarioIn pytestlanggraphIn your agent code

Bonus: Recommended VS Code Layout
text[Explorer]     [Editor]     [Terminal: ptw]
ai_weather_agent/   test_*.py   === 1 passed in 0.1s ===

One-Click Setup
Just copy all files above into your repo → push → open in VS Code with Dev Containers.
You now have:

Zero-config TDD
Auto-format on save
No bad commits
Full CI/CD
AI agent testing


Want me to generate a docker-compose.yml or Makefile too?
Or publish this as a public template repo?
Say: "Make it a template repo" — I’ll give you the exact GitHub steps.2.1sdocker-compose.ymlHere is a production-ready docker-compose.yml that integrates perfectly with your TDD + AI Agent + VS Code + Dev Container setup.
It includes:

Python service with ruff, pre-commit, pytest-watch, scenario, langgraph
Auto-install on start
Hot-reload for TDD
Optional: LangSmith tracing, PostgreSQL, Redis (for real agents)
Works with or without VS Code Dev Containers


docker-compose.yml
yamlversion: "3.9"

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: ai-agent-tdd
    container_name: ai-agent
    working_dir: /workspace
    volumes:
      - .:/workspace:cached
      - ~/.cache/pip:/root/.cache/pip
      - ~/.cache/pre-commit:/root/.cache/pre-commit
    environment:
      - PYTHONUNBUFFERED=1
      - PYTHONDONTWRITEBYTECODE=1
      - LANGCHAIN_TRACING_V2=${LANGCHAIN_TRACING_V2:-false}
      - LANGCHAIN_API_KEY=${LANGCHAIN_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    command: sleep infinity  # Keep alive for VS Code / manual runs
    tty: true
    stdin_open: true
    ports:
      - "8000:8000"  # FastAPI if you add it later
    depends_on:
      - redis
      - postgres
    networks:
      - ai-net

  # Optional: For stateful agents
  redis:
    image: redis:7-alpine
    container_name: redis
    ports:
      - "6379:6379"
    command: redis-server --save 60 1 --loglevel warning
    volumes:
      - redis_data:/data
    networks:
      - ai-net

  postgres:
    image: postgres:16-alpine
    container_name: postgres
    environment:
      POSTGRES_USER: agent
      POSTGRES_PASSWORD: agent
      POSTGRES_DB: agentdb
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - ai-net

volumes:
  redis_data:
  postgres_data:

networks:
  ai-net:
    driver: bridge

Dockerfile (Required)
language-DockerfileFROM mcr.microsoft.com/devcontainers/python:3.11

# Install system deps
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set workdir
WORKDIR /workspace

# Copy pyproject.toml first for caching
COPY pyproject.toml .

# Install Python deps
RUN pip install --upgrade pip && \
    pip install .[dev] && \
    pip install pytest-watch

# Install pre-commit
RUN pre-commit install

# Copy rest of code
COPY . .

# Auto-run setup on start (optional)
# CMD ["bash", "-c", "pre-commit install && ptw"]

.env (Example – create in project root)
envOPENAI_API_KEY=sk-...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_...

How to Use
1. Start the Stack
bashdocker compose up -d
2. Attach VS Code
bashcode .
→ VS Code → "Attach to Running Container" → ai-agent
→ Open terminal in VS Code:
bashptw
TDD loop starts instantly.

TDD Workflow (Inside Container)
bash# 1. Start watch mode
ptw

# 2. Edit test → save → see red/green
# 3. git commit → pre-commit runs ruff
# 4. Push → GitHub Actions runs CI

Optional: Add FastAPI Endpoint (Real Agent Server)
python# app/main.py
from fastapi import FastAPI
from ai_weather_agent.agents.weather_agent import weather_agent

app = FastAPI()

@app.post("/ask")
async def ask(question: str):
    result = weather_agent.invoke({"messages": [{"role": "user", "content": question}]})
    return {"answer": result["messages"][-1].content}
bashuvicorn app.main:app --reload --host 0.0.0.0 --port 8000
→ Access at http://localhost:8000

Full Directory Structure
bash.
├── docker-compose.yml
├── Dockerfile
├── .env
├── pyproject.toml
├── .devcontainer/
├── .vscode/
├── .github/
├── ai_weather_agent/
└── tests/

Bonus: Makefile (Optional – One-Command Dev)
makefile.PHONY: up down tdd logs shell

up:
	docker compose up -d

down:
	docker compose down

tdd:
	docker compose exec app ptw

shell:
	docker compose exec app bash

logs:
	docker compose logs -f app

test:
	docker compose exec app pytest

lint:
	docker compose exec app ruff check . --fix

format:
	docker compose exec app ruff format .
→ Now just run:
bashmake tdd

Summary





































FeatureEnabled?ruffYes (on save, commit, CI)pre-commitYes (auto-installed)pytest-watchYes (ptw in container)VS Code ReadyYes (attach + tasks)Hot ReloadYesScalable (Redis, DB)YesProduction-ReadyYes

You now have a complete, containerized, TDD-first AI agent dev environment.
Want me to:

Generate a public GitHub template repo with all files?
Add LangSmith dashboard integration?
Add Jupyter Lab service?

Just say: "Make it a template repo" or "Add Jupyter".
