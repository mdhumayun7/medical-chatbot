# app.py
import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request, jsonify
from src.helper import download_hugging_face_embeddings
from pinecone import Pinecone
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# ─── 1. Embeddings ───────────────────────────────────────────
print("Loading embeddings...")
embeddings = download_hugging_face_embeddings()

# ─── 2. Pinecone se connect karo (already stored vectors) ────
print("Connecting to Pinecone...")
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pc.Index("medicalbot")

# LangChain vectorstore wrapper
docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)

# ─── 3. Retriever ─────────────────────────────────────────────
retriever = docsearch.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# ─── 4. Prompt Template ───────────────────────────────────────
PROMPT_TEMPLATE = """
You are a helpful medical assistant. 
Use the following context to answer the question.
If you don't know the answer from the context, say "I don't have enough information about this topic."
Never make up medical information.

Context: {context}

Question: {question}

Helpful Answer:"""

prompt = PromptTemplate(
    template=PROMPT_TEMPLATE,
    input_variables=["context", "question"]
)

# ─── 5. LLM (Ollama - Free & Local) ──────────────────────────
print("Loading LLM...")
llm = OllamaLLM(
    model="llama3.2",
    temperature=0.4
)

# ─── 6. RAG Chain ─────────────────────────────────────────────
print("Building RAG chain...")
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)
print("✅ Chatbot ready!")

# ─── 7. Flask Routes ──────────────────────────────────────────
@app.route("/")
def index_page():
    return render_template("chat.html")

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(f"User: {msg}")
    
    result = qa_chain({"query": msg})
    answer = result["result"]
    
    print(f"Bot: {answer}")
    return str(answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)