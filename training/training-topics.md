# AI Weather Agent - Complete Training Curriculum

## Overview

This file contains the **complete training plan** with all modules and lessons outlined. This is the "blueprint" for the entire learning journey.

**Note**: The actual progress is tracked in `current-training.md`

---

## 📚 Table of Contents

### Quick Navigation
- [Overview](#overview)
- [Complete Curriculum Summary](#complete-curriculum-summary)
- [Success Criteria](#success-criteria)
- [Notes for AI Assistants](#notes-for-ai-assistants)

### All Modules

1. **[Module 1: The Big Picture](#module-1-the-big-picture)**
   - [Lesson 1.1: What is TDD?](#lesson-11-what-is-tdd-test-driven-development)
   - [Lesson 1.2: What is an AI Agent?](#lesson-12-what-is-an-ai-agent)
   - [Lesson 1.3: What is LangGraph?](#lesson-13-what-is-langgraph)
   - [Lesson 1.4: What is Scenario Testing?](#lesson-14-what-is-scenario-testing)
   - [Lesson 1.5: The Development Tools](#lesson-15-the-development-tools)
   - [Lesson 1.6: How It All Works Together](#lesson-16-how-it-all-works-together)
   - [Lesson 1.7: Your Project Structure](#lesson-17-your-project-structure)
   - [Understanding Check 1.1](#understanding-check-11)

2. **[Module 2: Hands-On with Development Tools](#module-2-hands-on-with-development-tools)**
   - [Lesson 2.1: ruff Hands-On (Part 1 - Finding Issues)](#lesson-21-ruff-hands-on-part-1---finding-issues)
   - [Lesson 2.2: ruff Hands-On (Part 2 - Fixing Automatically)](#lesson-22-ruff-hands-on-part-2---fixing-automatically)
   - [Lesson 2.3: ruff Configuration](#lesson-23-ruff-configuration)
   - [Understanding Check 2.1](#understanding-check-21)
   - [Lesson 2.4: pre-commit Hands-On (Part 1 - Installation)](#lesson-24-pre-commit-hands-on-part-1---installation)
   - [Lesson 2.5: pre-commit Hands-On (Part 2 - Using It)](#lesson-25-pre-commit-hands-on-part-2---using-it)
   - [Lesson 2.6: pre-commit Configuration](#lesson-26-pre-commit-configuration)
   - [Understanding Check 2.2](#understanding-check-22)
   - [Lesson 2.7: pytest-watch Hands-On (Part 1 - Starting Watch Mode)](#lesson-27-pytest-watch-hands-on-part-1---starting-watch-mode)
   - [Lesson 2.8: pytest-watch Hands-On (Part 2 - The Loop)](#lesson-28-pytest-watch-hands-on-part-2---the-loop)
   - [Lesson 2.9: The TDD Loop in Action](#lesson-29-the-tdd-loop-in-action)
   - [Understanding Check 2.3](#understanding-check-23)
   - [Lesson 2.10: Integration - All Three Tools Together](#lesson-210-integration---all-three-tools-together)
   - [Understanding Check 2.4](#understanding-check-24)

3. **[Module 3: Deep Dive into LangGraph](#module-3-deep-dive-into-langgraph)**
   - [Lesson 3.1: StateGraph Concept](#lesson-31-stategraph-concept)
   - [Lesson 3.2: Nodes](#lesson-32-nodes)
   - [Lesson 3.3: Edges and Routing](#lesson-33-edges-and-routing)
   - [Lesson 3.4: The Complete Graph](#lesson-34-the-complete-graph)
   - [Lesson 3.5: Weather Agent Structure](#lesson-35-weather-agent-structure)
   - [Understanding Check 3.1](#understanding-check-31)
   - [Lesson 3.6: MessagesState Deep Dive](#lesson-36-messagesstate-deep-dive)
   - [Lesson 3.7: Tool Calling](#lesson-37-tool-calling)
   - [Lesson 3.8: The Agent Loop](#lesson-38-the-agent-loop)
   - [Understanding Check 3.2](#understanding-check-32)

4. **[Module 4: Scenario Testing Framework](#module-4-scenario-testing-framework)**
   - [Lesson 4.1: Why Scenario Testing?](#lesson-41-why-scenario-testing)
   - [Lesson 4.2: Scenario Test Structure](#lesson-42-scenario-test-structure)
   - [Lesson 4.3: UserSimulatorAgent](#lesson-43-usersimulatoragent)
   - [Lesson 4.4: JudgeAgent](#lesson-44-judgeagent)
   - [Lesson 4.5: Writing Good Criteria](#lesson-45-writing-good-criteria)
   - [Lesson 4.6: Scenario Test Execution](#lesson-46-scenario-test-execution)
   - [Understanding Check 4.1](#understanding-check-41)
   - [Lesson 4.7: Multi-Turn Conversations](#lesson-47-multi-turn-conversations)
   - [Lesson 4.8: Testing Tool Calling](#lesson-48-testing-tool-calling)
   - [Lesson 4.9: Edge Cases in Testing](#lesson-49-edge-cases-in-testing)
   - [Understanding Check 4.2](#understanding-check-42)

5. **[Module 5: Build Weather Agent (TDD - RED → GREEN → REFACTOR)](#module-5-build-weather-agent-tdd---red--green--refactor)**
   - [Lesson 5.1: RED Phase (Write Failing Test)](#lesson-51-red-phase-write-failing-test)
   - [Lesson 5.2: GREEN Phase (Write Minimal Code)](#lesson-52-green-phase-write-minimal-code)
   - [Lesson 5.3: GREEN Phase Continued](#lesson-53-green-phase-continued)
   - [Lesson 5.4: REFACTOR Phase (Improve Code)](#lesson-54-refactor-phase-improve-code)
   - [Lesson 5.5: More Tests (Expand Coverage)](#lesson-55-more-tests-expand-coverage)
   - [Understanding Check 5.1](#understanding-check-51)
   - [Lesson 5.6: Code Quality Check](#lesson-56-code-quality-check)
   - [Lesson 5.7: Git Commit](#lesson-57-git-commit)
   - [Understanding Check 5.2](#understanding-check-52)

6. **[Module 6: Fix & Complete ai-wheather-agent Project](#module-6-fix--complete-ai-wheather-agent-project)**
   - [Lesson 6.1: Current Status Review](#lesson-61-current-status-review)
   - [Lesson 6.2: Fix Import Paths](#lesson-62-fix-import-paths)
   - [Lesson 6.3: Implement Tools Module](#lesson-63-implement-tools-module)
   - [Lesson 6.4: Implement Agent Module](#lesson-64-implement-agent-module)
   - [Lesson 6.5: Write Scenario Tests](#lesson-65-write-scenario-tests)
   - [Understanding Check 6.1](#understanding-check-61)
   - [Lesson 6.6: Code Quality](#lesson-66-code-quality)
   - [Lesson 6.7: Git Commit](#lesson-67-git-commit)
   - [Understanding Check 6.2](#understanding-check-62)

7. **[Module 7: Scale Up - Multi-Agent Systems](#module-7-scale-up---multi-agent-systems)**
   - [Lesson 7.1: Multiple Tools](#lesson-71-multiple-tools)
   - [Lesson 7.2: Agent-to-Agent Communication](#lesson-72-agent-to-agent-communication)
   - [Lesson 7.3: State and Memory](#lesson-73-state-and-memory)
   - [Lesson 7.4: Error Handling](#lesson-74-error-handling)
   - [Lesson 7.5: Monitoring and Debugging](#lesson-75-monitoring-and-debugging)
   - [Understanding Check 7.1](#understanding-check-71)
   - [Lesson 7.6: Testing Complex Systems](#lesson-76-testing-complex-systems)
   - [Lesson 7.7: Performance Considerations](#lesson-77-performance-considerations)
   - [Understanding Check 7.2](#understanding-check-72)

8. **[Module 8: Deploy & Monitor - Production Patterns](#module-8-deploy--monitor---production-patterns)**
   - [Lesson 8.1: LangSmith Integration](#lesson-81-langsmith-integration)
   - [Lesson 8.2: Observability](#lesson-82-observability)
   - [Lesson 8.3: CI/CD Pipeline](#lesson-83-cicd-pipeline)
   - [Lesson 8.4: Environment Configuration](#lesson-84-environment-configuration)
   - [Lesson 8.5: Versioning and Deployment](#lesson-85-versioning-and-deployment)
   - [Understanding Check 8.1](#understanding-check-81)
   - [Lesson 8.6: Cost Optimization](#lesson-86-cost-optimization)
   - [Lesson 8.7: User Analytics](#lesson-87-user-analytics)
   - [Lesson 8.8: Continuous Improvement](#lesson-88-continuous-improvement)
   - [Understanding Check 8.2](#understanding-check-82)

### Final Steps
- [Final Project](#final-project)
- [Success Criteria](#success-criteria)

---

## Complete Curriculum Summary

# MODULE 1: The Big Picture

## Goal
Understand what we're building and why we're using the tools we chose.

## Lessons

### Lesson 1.1: What is TDD? (Test-Driven Development)
- Traditional way vs TDD way
- RED → GREEN → REFACTOR cycle
- Why TDD is better (confidence, maintainability, fewer bugs)
- Real example with weather agent

### Lesson 1.2: What is an AI Agent?
- Simple definition: receives messages, decides actions, uses tools, responds
- Weather agent flow diagram
- Key concept: Tools (functions agents can call)
- Agent autonomy and decision-making

### Lesson 1.3: What is LangGraph?
- Definition: Framework for building agents
- Graph structure (nodes, edges, state, entry points)
- Visual flowchart of agent decision-making
- Key components explained

### Lesson 1.4: What is Scenario Testing?
- Problem with regular unit tests for AI agents
- Solution: Scenario tests simulate real conversations
- UserSimulatorAgent and JudgeAgent
- Why scenario testing is better than unit tests

### Lesson 1.5: The Development Tools
- **ruff**: Code cleaner (finds and fixes code problems)
- **pre-commit**: Guardian (runs checks before commits)
- **pytest-watch**: Watcher (runs tests automatically on save)

### Lesson 1.6: How It All Works Together
- Complete TDD workflow with tools
- START WATCH MODE → Write test → Write code → Refactor → Commit
- Result: instant feedback, clean code, tests always pass

### Lesson 1.7: Your Project Structure
- Directory layout of ai-wheather-agent
- Where code goes, where tests go, where config goes
- Important files explained

### Understanding Check 1.1
**Question**: "Can you explain in your own words (in 2-3 sentences) what TDD is and why it's better than writing code first?"

---

# MODULE 2: Hands-On with Development Tools

## Goal
Learn how to USE ruff, pre-commit, and pytest-watch in practice.

## Lessons

### Lesson 2.1: ruff Hands-On (Part 1 - Finding Issues)
- Run `ruff check .` to find issues
- Understand error codes (E, W, F, I, B, UP)
- Read error messages and fix suggestions
- Activity: Run ruff check and identify issues in project

### Lesson 2.2: ruff Hands-On (Part 2 - Fixing Automatically)
- Run `ruff check . --fix` to auto-fix issues
- Run `ruff format .` to format code (like black)
- Compare before/after code
- Understand what changed and why
- Activity: Fix all ruff issues in the project

### Lesson 2.3: ruff Configuration
- Understand `pyproject.toml` ruff section
- Which rules are enabled (E, W, F, I, B, UP)
- Line length setting (120 characters)
- Why these specific rules were chosen

### Understanding Check 2.1
**Question**: "What does ruff do? Name 3 types of issues it can find and fix."

---

### Lesson 2.4: pre-commit Hands-On (Part 1 - Installation)
- What are git hooks?
- Install pre-commit: `pre-commit install`
- Understand `.pre-commit-config.yaml` file
- What happens when you try to commit

### Lesson 2.5: pre-commit Hands-On (Part 2 - Using It)
- Make a git commit and watch pre-commit run
- See ruff checks run automatically
- See other pre-commit hooks (formatting, trailing whitespace, etc)
- Experience blocked commit due to issues
- Fix issues and commit successfully

### Lesson 2.6: pre-commit Configuration
- Review `.pre-commit-config.yaml`
- Which hooks are enabled
- How hooks are configured
- Why each hook matters

### Understanding Check 2.2
**Question**: "What does pre-commit do? When does it run? How does it help prevent bad code?"

---

### Lesson 2.7: pytest-watch Hands-On (Part 1 - Starting Watch Mode)
- Run `just watch` to start watch mode
- Understand what's happening (pytest-watch monitoring files)
- See initial test output

### Lesson 2.8: pytest-watch Hands-On (Part 2 - The Loop)
- Edit a test file
- Save the file
- Watch tests re-run automatically
- See results instantly
- Repeat with code file

### Lesson 2.9: The TDD Loop in Action
- Start watch mode
- Edit test → Save → Tests run → See results
- Edit code → Save → Tests run → See results
- Experience sub-second feedback
- Understand why this is better than running tests manually

### Understanding Check 2.3
**Question**: "How does pytest-watch help you develop faster? Why is instant feedback important for TDD?"

---

### Lesson 2.10: Integration - All Three Tools Together
- Run `just qa` to see all three working together
- Understand the pipeline: format → lint → type-check → test
- Make a change that breaks something
- See all three tools catch it
- Fix the issue and watch it pass

### Understanding Check 2.4
**Question**: "Can you explain the complete workflow: Write test → Write code → Refactor → Commit?"

---

# MODULE 3: Deep Dive into LangGraph

## Goal
Understand how LangGraph works and how it enables AI agents.

## Lessons

### Lesson 3.1: StateGraph Concept
- What is a StateGraph?
- State: the data passed between nodes (messages, memory, context)
- MessagesState: predefined state for conversation agents
- How state flows through the graph

### Lesson 3.2: Nodes
- What is a node? (a processing step)
- Creating nodes: `graph.add_node(name, function)`
- What happens in a node (processes state, returns updated state)
- Node examples: agent node, tool node, decision node

### Lesson 3.3: Edges and Routing
- What is an edge? (connection between nodes)
- Direct edges: `graph.add_edge(from, to)`
- Conditional edges: `graph.add_conditional_edges(from, function)`
- Function decides which node to go to next
- Entry point: `graph.set_entry_point(node_name)`

### Lesson 3.4: The Complete Graph
- How graph.compile() works (turns blueprint into runnable agent)
- How graph.invoke() works (passes state through the graph)
- How the graph executes step by step
- Debugging: understanding what happens at each node

### Lesson 3.5: Weather Agent Structure
- Our specific graph: Agent Node → Decision → Tool Node → Loop back
- How messages flow through our weather agent
- Where the LLM thinks (Agent Node)
- Where the tool gets called (Tool Node)
- How results feed back

### Understanding Check 3.1
**Question**: "Explain in your own words: What is a StateGraph? How do nodes connect? How does the graph execute?"

---

### Lesson 3.6: MessagesState Deep Dive
- What is MessagesState?
- The "messages" list (stores conversation history)
- How to access last message: `state["messages"][-1]`
- How to add messages: return `{"messages": [new_message]}`
- Why this matters (LLM needs full conversation history)

### Lesson 3.7: Tool Calling
- How LLMs call tools (tool_calls attribute)
- How agents decide to use tools
- Accessing tool information: `tool_call["name"]`, `tool_call["args"]`
- How to check if tool was called: `if s["messages"][-1].tool_calls`

### Lesson 3.8: The Agent Loop
- Agent thinks → Decides to use tool → Tool runs → Result added to state
- Agent thinks again → Decides to respond → Returns answer
- Why looping is important (agent can refine thinking with tool results)
- Maximum turns to prevent infinite loops

### Understanding Check 3.2
**Question**: "How does the agent decide whether to use a tool or respond? How does the loop work?"

---

# MODULE 4: Scenario Testing Framework

## Goal
Learn how to write tests specifically for AI agents.

## Lessons

### Lesson 4.1: Why Scenario Testing?
- Problem: Regular tests don't work well for AI agents
- Solution: Simulate real user conversations
- Test realistic interactions, not just function inputs/outputs
- Criteria-based evaluation (does output meet requirements?)

### Lesson 4.2: Scenario Test Structure
- @scenario.test() decorator
- Three main parts:
  1. Description (what the test does)
  2. Agents (UserSimulatorAgent, JudgeAgent)
  3. max_turns (conversation length limit)
- Basic syntax and structure

### Lesson 4.3: UserSimulatorAgent
- What it does: simulates a user asking questions
- How it works: uses LLM to generate natural questions
- Why it's useful: tests realistic user behavior
- How to control it: initial_message parameter

### Lesson 4.4: JudgeAgent
- What it does: evaluates agent responses against criteria
- Criteria (requirements the response must meet):
  - Example: "Response includes temperature"
  - Example: "No hallucinations"
  - Example: "Mentions the specific location"
- Uses LLM to evaluate (not exact string matching)
- Why this matters: flexible, realistic evaluation

### Lesson 4.5: Writing Good Criteria
- Criteria should be specific and measurable
- Examples of good criteria vs bad criteria
- How to avoid false positives/negatives
- Tips for criteria that actually work

### Lesson 4.6: Scenario Test Execution
- How `scenario.run()` works
- What result.success means
- How to interpret results
- Common issues and how to debug them

### Understanding Check 4.1
**Question**: "What is the difference between a unit test and a scenario test? Why is scenario testing better for AI agents?"

---

### Lesson 4.7: Multi-Turn Conversations
- max_turns parameter (number of back-and-forths)
- Why multi-turn matters (agent might need multiple questions)
- Conversation flow in tests
- Setting appropriate max_turns

### Lesson 4.8: Testing Tool Calling
- Criteria to verify tools are being called
- Example: "Tool 'get_weather' was called exactly once"
- Testing that correct tools are used
- Testing that tool results are incorporated

### Lesson 4.9: Edge Cases in Testing
- What happens if agent doesn't understand?
- What if agent hallucinates (makes up data)?
- What if agent doesn't use tools when it should?
- Writing criteria that catch these issues

### Understanding Check 4.2
**Question**: "How do you test that an agent called a specific tool? How do you prevent hallucinations in tests?"

---

# MODULE 5: Build Weather Agent (TDD - RED → GREEN → REFACTOR)

## Goal
Apply everything learned to build a working weather agent from scratch using TDD.

## Lessons

### Lesson 5.1: RED Phase (Write Failing Test)
- Write first scenario test for weather agent
- Test: "User asks for weather in Tokyo"
- Test should fail (agent doesn't exist yet)
- Understand what the test expects
- Activity: Write and run failing test

### Lesson 5.2: GREEN Phase (Write Minimal Code)
- Implement minimal weather agent
- Create agents/weather.py
- Create StateGraph with agent and tool nodes
- Test should pass (even if agent is hardcoded)
- Activity: Make test pass with minimal code

### Lesson 5.3: GREEN Phase Continued
- Implement get_current_weather tool
- Create tools/weather.py
- Mock weather data (Tokyo: 22°C sunny, etc)
- Integrate tool into agent
- Activity: Tests still pass, agent uses tool

### Lesson 5.4: REFACTOR Phase (Improve Code)
- Review code for clarity
- Add type hints
- Improve function names
- Add comments where needed
- Activity: Refactor while tests pass

### Lesson 5.5: More Tests (Expand Coverage)
- Write test for London weather
- Write test for handling unknown location
- Write test for multiple questions (multi-turn)
- Activity: Add more scenario tests

### Understanding Check 5.1
**Question**: "Walk through the TDD cycle: What is RED? What is GREEN? What is REFACTOR? Why is this better than writing all code first?"

---

### Lesson 5.6: Code Quality Check
- Run `just qa` to check full pipeline
- Fix any ruff issues
- Ensure tests pass
- Ensure type checking passes
- Activity: Make code pass all quality checks

### Lesson 5.7: Git Commit
- Stage changes: `git add .`
- Commit: `git commit -m "feat: implement weather agent"`
- Watch pre-commit hooks run
- Fix any pre-commit issues
- Activity: Successfully commit your work

### Understanding Check 5.2
**Question**: "You've built a working weather agent! What did you learn from building it with TDD instead of writing all the code first?"

---

# MODULE 6: Fix & Complete ai-wheather-agent Project

## Goal
Apply TDD to the actual project and get it working completely.

## Lessons

### Lesson 6.1: Current Status Review
- Understand what exists vs what's missing
- Identify all issues (import paths, missing modules, etc)
- Plan the work
- Activity: Review project structure

### Lesson 6.2: Fix Import Paths
- Issue: Tests import from `agents.weather` (doesn't exist)
- Solution: Create proper module structure
- Fix: Create `src/ai_wheather_agent/agents/` directory
- Activity: Fix all import paths

### Lesson 6.3: Implement Tools Module
- Create `src/ai_wheather_agent/tools/weather.py`
- Implement get_current_weather function
- Add mock weather data
- Activity: Tools module complete

### Lesson 6.4: Implement Agent Module
- Create `src/ai_wheather_agent/agents/weather.py`
- Build weather agent using LangGraph
- Integrate with tools
- Activity: Agent module complete

### Lesson 6.5: Write Scenario Tests
- Create comprehensive tests in `tests/test_weather_agent.py`
- Test: Simple weather query
- Test: Unknown location handling
- Test: Multi-turn conversation
- Activity: Write 3-5 good tests

### Understanding Check 6.1
**Question**: "What was the most challenging part of fixing the project? How did TDD help ensure it works correctly?"

---

### Lesson 6.6: Code Quality
- Run ruff check and fix all issues
- Run type checking and fix all issues
- Run full `just qa` pipeline
- Activity: Pass all quality checks

### Lesson 6.7: Git Commit
- Commit the complete weather agent
- Write good commit message
- Ensure pre-commit hooks pass
- Activity: Working weather agent committed

### Understanding Check 6.2
**Question**: "The weather agent is now complete and tested! What's the difference between how it works and the first agent you built?"

---

# MODULE 7: Scale Up - Multi-Agent Systems

## Goal
Learn patterns for building more complex agent systems.

## Lessons

### Lesson 7.1: Multiple Tools
- Extending agent to use multiple tools
- Tool decision logic (which tool to use when?)
- Calling different tools for different questions
- Activity: Add more tools (time, search, etc)

### Lesson 7.2: Agent-to-Agent Communication
- When agents need to talk to each other
- Passing messages between agents
- Orchestrating multiple agents
- Activity: Design multi-agent system

### Lesson 7.3: State and Memory
- Persistent state across conversations
- User profiles and history
- Context management in multi-turn
- Activity: Implement memory for agent

### Lesson 7.4: Error Handling
- What happens when tools fail?
- Graceful degradation
- Retry logic
- User-friendly error messages
- Activity: Add error handling to agent

### Lesson 7.5: Monitoring and Debugging
- How to understand what agent is doing
- Adding logging
- Debugging tool calls
- Understanding conversation flow
- Activity: Add logging to agent

### Understanding Check 7.1
**Question**: "How would you design an agent system with multiple tools? How does the agent decide which tool to use?"

---

### Lesson 7.6: Testing Complex Systems
- Testing with mocked tools
- Testing error cases
- Testing multi-agent interactions
- Activity: Write tests for complex scenarios

### Lesson 7.7: Performance Considerations
- Cost of API calls (tokens matter!)
- Optimizing agent decisions
- Caching and memoization
- Activity: Optimize agent for performance

### Understanding Check 7.2
**Question**: "What patterns did you learn for building more complex agent systems? What challenges might arise at scale?"

---

# MODULE 8: Deploy & Monitor - Production Patterns

## Goal
Learn how to prepare agents for production use.

## Lessons

### Lesson 8.1: LangSmith Integration
- What is LangSmith? (tracing and monitoring)
- Setting up LangSmith
- Tracing agent execution
- Viewing traces in dashboard
- Activity: Set up LangSmith tracing

### Lesson 8.2: Observability
- What to log and monitor
- Metrics that matter (latency, cost, success rate)
- Setting up alerts
- Dashboard creation
- Activity: Create monitoring dashboard

### Lesson 8.3: CI/CD Pipeline
- GitHub Actions setup
- Running tests on every commit
- Automated checks before deployment
- Activity: Set up GitHub Actions workflow

### Lesson 8.4: Environment Configuration
- Secrets management (API keys)
- Environment variables
- Configuration for different environments (dev, staging, prod)
- Activity: Set up proper configuration

### Lesson 8.5: Versioning and Deployment
- Semantic versioning
- How to version agents
- Deploying new versions safely
- Rollback strategies
- Activity: Version and deploy agent

### Understanding Check 8.1
**Question**: "What does it mean to make an agent 'production-ready'? What are the key concerns?"

---

### Lesson 8.6: Cost Optimization
- Measuring token usage
- Optimizing prompts for fewer tokens
- Caching responses where possible
- Cost monitoring
- Activity: Optimize agent cost

### Lesson 8.7: User Analytics
- Tracking user interactions
- Understanding which features are used
- Identifying issues from user behavior
- Activity: Add user analytics

### Lesson 8.8: Continuous Improvement
- A/B testing different agent behaviors
- Gathering feedback
- Iterating based on data
- Activity: Design improvement experiment

### Understanding Check 8.2
**Question**: "You've learned how to build, test, and deploy agents. What's the most important thing you learned overall?"

---

# Final Project

## Capstone: Build Your Own AI Agent

After completing all 8 modules, you'll:

1. **Plan** a new agent (e.g., customer service agent, code assistant)
2. **Design** using TDD principles
3. **Implement** all 8 lessons you learned
4. **Deploy** following production patterns
5. **Monitor** and improve based on data

---

# Success Criteria

By the end of this training, you should be able to:

- ✅ Write code using TDD (RED → GREEN → REFACTOR)
- ✅ Build AI agents using LangGraph
- ✅ Test agents using Scenario framework
- ✅ Use development tools (ruff, pre-commit, pytest-watch)
- ✅ Write clean, maintainable code
- ✅ Design multi-agent systems
- ✅ Deploy agents to production
- ✅ Monitor and improve agents

---

# Notes for AI Assistants

When continuing this training:

1. **Check current-training.md** for what's been covered
2. **Reference this file** for what comes next
3. **Follow the understanding checks** - don't skip them
4. **Be interactive** - ask the student to explain concepts
5. **Use examples** - show code, not just theory
6. **Encourage practice** - have them run commands
7. **Adjust as needed** - if student is confused, spend more time

---

**Next Step**: Student should answer the understanding check from Module 1.1 before moving forward.
