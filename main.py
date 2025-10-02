import ollama

ollama_client = ollama.Client()

response = ollama_client.embed(model="embeddinggemma", input="Hello, world!")
print("Response type:", type(response))
print("Response attributes:", dir(response))
print("Full response:", response)


