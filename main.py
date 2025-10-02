import ollama

ollama_client = ollama.Client()

response = ollama_client.embed(model="embeddinggemma", input="Hello, world!")
embedding = response.embeddings[0]
print(embedding)


