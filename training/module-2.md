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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)

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
| Run `just qa`, `just clean`  before every commit | Catch issues before pre-commit does |

### Understanding Check 2.10a

**Question:** "Describe your ideal development session using all three tools (pytest-watch, ruff, pre-commit). What tools are you using when?"

Think about:
- When do you start pytest-watch?
- When do you run ruff/just qa?
- When does pre-commit run automatically?
- How do these tools work together?

---

## 📝 Training Notes

**When returning to this project:**
1. Check the **"Quick Jump Navigation"** section above
2. Click on your lesson to jump to it
3. Run `just watch` to start developing with instant feedback
4. Run `just test` to verify all tests pass

---

[↑ Back to Quick Jump Navigation](current-training.md#quick-jump-navigation)
