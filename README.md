# EmbeddingGemma POC

A proof-of-concept project demonstrating text embedding generation using Google's EmbeddingGemma model through Ollama.

## What is EmbeddingGemma?

EmbeddingGemma is Google's lightweight embedding model that converts text into numerical vectors (embeddings). These embeddings can be used for:

- Semantic search
- Text similarity comparison
- Clustering and classification
- Retrieval-augmented generation (RAG) applications

## Prerequisites

1. **Python 3.12+**
2. **Ollama** - Install from [ollama.ai](https://ollama.ai)
3. **EmbeddingGemma model** - Pull the model after installing Ollama:
   ```bash
   ollama pull embeddinggemma
   ```

## Setup

This project uses `uv` for dependency management:

```bash
# Clone the repository
git clone https://github.com/rwuniard/embeddinggemma.git
cd embeddinggemma

# Run the example (uv will handle dependencies automatically)
uv run python main.py
```

## Usage

The basic example in `main.py` demonstrates how to generate embeddings:

```python
import ollama

ollama_client = ollama.Client()

response = ollama_client.embed(model="embeddinggemma", input="Hello, world!")
embedding = response.embeddings[0]
print(embedding)
```

The output is a 768-dimensional vector representing the semantic meaning of the input text.

## How It Works

1. **Ollama Server**: Runs locally and manages the EmbeddingGemma model
2. **Python Client**: Sends text to Ollama via the `ollama` Python package
3. **Embedding Generation**: The model converts text into a numerical vector
4. **Response**: Returns an `EmbedResponse` Pydantic model with the embedding array

## Use Cases

- **Semantic Search**: Find similar documents by comparing embedding vectors
- **Question Answering**: Match questions to relevant answers
- **Recommendation Systems**: Find similar items based on text descriptions
- **Data Clustering**: Group similar text content together

## License

MIT
