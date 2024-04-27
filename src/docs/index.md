# Welcome to Blacksheep Template


## Description

A basic example application template for Blacksheep-based APIs.
Blacksheep is an extremely fast Python web framework with dependency injection,
parameter validation with dataclasses or Pydantic, some security-related presets and other useful features.

### Features

- Separated requirements.txt files for the app, for development and for documentation.
- Using environment variables for separated development and production execution
- Path-based API versioning
- Class-based views and endpoints
- Fast JSON serializer from orjson
- Async template rendering
- Built-in anti-forgery
- MkDocs for documentation
    - Automated source code docstring extraction
    - API documentation from openapi.json
    - Clear structure

## Usage

- Development setup: ```python -m venv venv && source venv/bin/activate && pip install -r requirements.txt -r dev-requirements.txt -r docs-requirements.txt```
- Start development server: ```cd backend; APP_ENV=dev python -m app.server```
- For documentation writing: ```cd backend; mkdocs serve -w docs -w app```
- For documentation build: ```cd backend; mkdocs build```
