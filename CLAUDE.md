# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
# Setup development environment
./scripts/dev_setup.sh

# Activate virtual environment  
source .venv/bin/activate
```

### Code Quality
```bash
# Format code with ruff
./scripts/format.sh

# Lint and type check
./scripts/validate.sh

# Run tests
./scripts/test.sh
```

### Running the Application
```bash
# Start workspace (FastAPI + Postgres)
ag ws up

# Stop workspace
ag ws down

# Access FastAPI docs at: http://localhost:8000/docs
```

## Architecture Overview

This is a production-grade agentic system built with FastAPI and PostgreSQL (with PgVector extension).

### Core Components

- **API Layer** (`api/`): FastAPI application with versioned routes (`/v1/`)
  - Routes: agents, teams, playground, status
  - Settings-based configuration with environment variable support
  - CORS middleware enabled

- **Agents** (`agents/`): Individual AI agents (operator, sage, scholar)
  - Configurable models (GPT-4, GPT-4-mini, embeddings)
  - Temperature and token limits managed via settings

- **Teams** (`teams/`): Multi-agent teams for complex tasks
  - Finance researcher, multi-language support, operator coordination
  - Model flexibility including free alternatives (e.g., Google Gemini)

- **Workflows** (`workflows/`): Orchestrated multi-step processes
  - Blog post generation, investment report generation
  - Separate settings management from agents/teams

- **Database** (`db/`): PostgreSQL with Alembic migrations
  - PgVector extension for embeddings
  - Structured table definitions in `tables/`

- **Workspace** (`workspace/`): Environment and deployment configuration
  - Agno framework integration for AWS deployment
  - Separate dev/prod resource configurations

### Settings Pattern

Each module (agents, teams, workflows) follows a consistent settings pattern:
- Pydantic BaseSettings for environment variable configuration
- Model configurations (GPT variants, embedding models)
- Default temperature (0) and max completion tokens (16000)
- Settings objects exported as singletons

### Development Environment

- Uses `uv` for Python dependency management
- `ruff` for formatting and linting
- `mypy` for type checking
- `pytest` for testing
- Docker-based local development with `ag ws` commands