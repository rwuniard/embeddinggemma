# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

POC for using Google's EmbeddingGemma model through Ollama for text embeddings.

## Development Setup

This project uses `uv` for Python dependency management.

### Running the Code

```bash
uv run python main.py
```

### Prerequisites

- Ollama must be installed and running locally (`ollama serve`)
- The embeddinggemma model must be pulled: `ollama pull embeddinggemma`

## Architecture

### Core Components

- **main.py**: Entry point demonstrating basic embedding generation using Ollama's Python client
- **Ollama Integration**: Uses the `ollama` Python package (>=0.6.0) to communicate with local Ollama service

### Ollama API Response Structure

The `ollama.Client().embed()` method returns an `EmbedResponse` Pydantic model, not a dictionary. Access response data through object attributes, not dictionary keys:

```python
response = ollama_client.embed(model="embeddinggemma", input="text")
# Correct: response.embeddings or response.embedding (check actual attribute name)
# Incorrect: response["embedding"]
```

To inspect the response structure:
```python
print(dir(response))  # Shows available attributes
print(response)       # Shows full object representation
```

## Python Requirements

- Python >=3.12
- Dependencies managed through `pyproject.toml`
