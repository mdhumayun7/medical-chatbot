# store_index.py
import warnings
warnings.filterwarnings("ignore")

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import time

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

print("Step 1: PDF load ho raha hai...")
extracted_data = load_pdf_file("data/")
print(f"  Total pages loaded: {len(extracted_data)}")

print("Step 2: Text chunks ban rahe hain...")
text_chunks = text_split(extracted_data)
print(f"  Total chunks: {len(text_chunks)}")

print("Step 3: Embedding model load ho raha hai...")
embeddings = download_hugging_face_embeddings()
print("  Ready!")

print("Step 4: Pinecone initialize ho raha hai...")
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medicalbot"

existing_indexes = [idx.name for idx in pc.list_indexes()]

if index_name not in existing_indexes:
    print(f"  Index bana rahe hain...")
    pc.create_index(
        name=index_name,
        dimension=768,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    time.sleep(10)
    print("  Index ready!")
else:
    print(f"  Index already exists!")

print("Step 5: Vectors upload ho rahe hain...")
index = pc.Index(index_name)

# Chunks ko embed karke manually upsert karenge
batch_size = 100
vectors = []

for i, chunk in enumerate(text_chunks):
    # Har chunk ko embed karo
    embedding = embeddings.embed_query(chunk.page_content)
    vectors.append({
        "id": f"chunk_{i}",
        "values": embedding,
        "metadata": {
            "text": chunk.page_content,
            "source": chunk.metadata.get("source", "unknown"),
            "page": chunk.metadata.get("page", 0)
        }
    })
    
    # Batch mein upsert karo
    if len(vectors) == batch_size:
        index.upsert(vectors=vectors)
        print(f"  Uploaded {i+1}/{len(text_chunks)} chunks...")
        vectors = []

# Remaining vectors upload karo
if vectors:
    index.upsert(vectors=vectors)
    print(f"  Uploaded remaining chunks!")

print(f"\n✅ DONE! {len(text_chunks)} chunks Pinecone mein store ho gaye!")
print(f"   Index: {index_name}")