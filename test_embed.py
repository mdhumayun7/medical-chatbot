import warnings
warnings.filterwarnings("ignore")

from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text")
result = embeddings.embed_query("What is hypertension?")
print(f"SUCCESS! Dims = {len(result)}")