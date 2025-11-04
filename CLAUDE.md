# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI Weather Agent is a Python CLI application built with Typer that provides weather-related functionality. The project uses modern Python tooling with `uv` for dependency management and includes comprehensive testing and linting infrastructure.

## Development Commands

The project uses Just for command management. All commands are defined in the `justfile`:

### Testing
- `just test` - Run tests using pytest (supports passing pytest arguments, e.g., `just test -v` or `just test tests/test_file.py`)
- `just test *ARGS` - Run tests with custom arguments
- `just testall` - Run tests across all supported Python versions (3.10, 3.11, 3.12, 3.13)
- `just pdb *ARGS` - Run tests with debugger on failure (`ipdb` enabled)
- `just coverage` - Generate test coverage report (outputs HTML to `htmlcov/`)

### Code Quality
- `just qa` - Run complete quality assurance: formatting, linting, type checking, and tests
  - Runs `ruff format` for code formatting
  - Runs `ruff check --fix` for linting fixes
  - Runs import sorting with `ruff check --select I`
  - Runs type checking with `ty check`
  - Runs all tests with `pytest`

### Build & Release
- `just build` - Build the project distribution (creates `dist/` directory)
- `just version` - Print current project version
- `just tag` - Tag the current version in git and push to GitHub
- `just clean` - Remove all build, test, coverage, and Python artifacts

## Project Structure

```
ai-wheather-agent/
├── src/ai_wheather_agent/       # Main package source
│   ├── __init__.py               # Package metadata (author, email)
│   ├── cli.py                    # Typer CLI entry point (command definitions)
│   ├── ai_wheather_agent.py      # Core module (currently empty, main logic here)
│   ├── utils.py                  # Utility functions
│   └── __main__.py               # Script entry point
├── tests/                        # Test suite
│   ├── __init__.py
│   └── test_ai_wheather_agent.py # Main test file (currently sparse)
├── docs/                         # Documentation
├── pyproject.toml                # Project configuration and dependencies
├── justfile                      # Command definitions
├── CONTRIBUTING.md               # Contributing guidelines
└── README.md                     # Project overview
```

## Key Technologies & Dependencies

- **Python**: 3.10+ (tested on 3.10, 3.11, 3.12, 3.13)
- **CLI Framework**: Typer (for building CLI applications)
- **Package Manager**: uv (for fast, reliable dependency management)
- **Testing**: pytest, coverage
- **Linting**: ruff (with rules: E, W, F, I, B, UP)
- **Type Checking**: ty (strict type checking)
- **Debugging**: ipdb
- **Output**: rich (for colored console output)

## Code Quality Standards

- **Line Length**: 120 characters (configured in `ruff`)
- **Linting Rules**: Enabled via ruff:
  - E: pycodestyle errors
  - W: pycodestyle warnings
  - F: Pyflakes
  - I: isort (import sorting)
  - B: flake8-bugbear
  - UP: pyupgrade
- **Type Checking**: Strict mode enabled with ty (all rules are "error" by default)
- **Python Version**: Tests run on 3.12 and 3.13 in CI, but support 3.10+

## CLI Architecture

The CLI is built with Typer and defined in [cli.py](src/ai_wheather_agent/cli.py):
- Main entry point is the `app` Typer instance
- Commands are defined as decorated functions with `@app.command()`
- Uses Rich Console for formatted output
- Package entry point is `ai_wheather_agent` command (defined in `pyproject.toml` as `ai_wheather_agent = "ai_wheather_agent.cli:app"`)

## CI/CD

GitHub Actions workflow (`.github/workflows/test.yml`) runs on:
- Python 3.12 and 3.13
- Ubuntu latest
- On push to main/master and pull requests
- Performs linting, testing, and installation validation

## Installation for Development

### Initial Setup
1. Create and activate virtual environment:
```bash
uv venv
source .venv/bin/activate
```

2. Install dependencies with test extras:
```bash
uv sync --extra test
```

### Development Workflow

The project uses several tools for development:

- **pytest-watch**: Automatically re-run tests on file changes
```bash
uv run pytest-watch
```

- **pytest**: Run tests manually with custom arguments
```bash
uv run pytest
uv run pytest tests/test_file.py -v
```

- **ruff**: Code formatting and linting (configured to 120 char line length)
```bash
uv run ruff format .
uv run ruff check . --fix
```

- **ty**: Type checking in strict mode
```bash
uv run ty check .
```

- **coverage**: Test coverage reporting
```bash
uv run coverage run -m pytest .
uv run coverage report -m
uv run coverage html  # Generates HTML report in htmlcov/
```

### Just Commands
Use Just for streamlined command execution:
- `just watch` - Run tests continuously with pytest-watch
- `just qa` - Run complete quality assurance pipeline
- `just test` - Run tests with optional arguments
- `just coverage` - Generate coverage report
- `just build` - Build distribution
- `just clean` - Clean artifacts
