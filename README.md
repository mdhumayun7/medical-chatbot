# 🩺 Medical Chatbot using LLMs, LangChain, Pinecone & Ollama

![Python](https://img.shields.io/badge/Python-3.14-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 📌 Overview

This project implements a complete **Retrieval-Augmented Generation (RAG) based Medical Chatbot** using:

- Large Language Models (LLMs)
- LangChain
- Pinecone Vector Database
- Ollama
- Flask
- Semantic Search

The chatbot answers medical questions using a curated medical knowledge base instead of relying only on parametric LLM memory. This significantly reduces hallucinations and improves factual grounding.

The system performs:

1. PDF ingestion
2. Text chunking
3. Embedding generation
4. Semantic vector storage
5. Context retrieval
6. Grounded response generation

The entire pipeline runs locally using Ollama for privacy-preserving inference.

---

# 🚀 Features

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search using Embeddings

✅ Pinecone Vector Database Integration

✅ Local LLM Inference using Ollama

✅ Flask-based Web Interface

✅ Medical PDF Knowledge Base

✅ Low Hallucination Responses

✅ Fully Open Source Stack

✅ Research-Oriented Architecture

---

# 🏗️ System Architecture

```text
Medical PDFs
      ↓
PyPDFLoader
      ↓
Text Chunking
      ↓
nomic-embed-text Embeddings
      ↓
Pinecone Vector Database
      ↓
Retriever
      ↓
Prompt Engineering
      ↓
Llama 3.2 via Ollama
      ↓
Flask Chat Interface
```

---

# 🧠 RAG Workflow

## Offline Phase

- Load medical PDFs
- Split into chunks
- Generate embeddings
- Store vectors in Pinecone

## Online Phase

- User asks query
- Query embedding generated
- Similar chunks retrieved
- Context injected into prompt
- LLM generates grounded response

---

# ⚙️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Llama 3.2 |
| Embeddings | nomic-embed-text |
| Framework | LangChain |
| Vector DB | Pinecone |
| Backend | Flask |
| Language | Python |
| Local Inference | Ollama |

---

## 📸 Screenshots

### Chat Interface
![Medical Chatbot UI](screenshots/ui_home.png)

### Real-time RAG Response
![Chat Demo](screenshots/chat_demo.png)



# 📂 Project Structure

```bash
medical-chatbot/
│
├── src/
│   ├── __init__.py
│   └── helper.py
│
├── templates/
│   └── chat.html
│
├── static/
│
├── data/
│
├── screenshots/
│
├── app.py
├── store_index.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🛠️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/medical-chatbot-rag-llm.git
cd medical-chatbot-rag-llm
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama Models

## Pull Embedding Model

```bash
ollama pull nomic-embed-text
```

## Pull LLM Model

```bash
ollama pull llama3.2
```

## Verify Models

```bash
ollama list
```

---

# 🔐 Environment Variables

Create `.env` file:

```env
PINECONE_API_KEY=your_api_key_here
```

---

# 📥 Add Medical PDFs

Place all medical PDF files inside:

```bash
data/
```

---

# 🗂️ Create Vector Index

Run ingestion pipeline:

```bash
python store_index.py
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 🌐 Open Browser

```text
http://localhost:8080
```

---

# 📊 Results

| Test Case | Result |
|---|---|
| Medical Questions | Accurate grounded answers |
| Out-of-domain query | Fallback response |
| Semantic retrieval | Successful |
| Hallucination control | Improved |

---

# 🔬 Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Similarity Search
- Prompt Engineering
- Approximate Nearest Neighbor Search
- LLM Orchestration
- Context Grounding

---

# 🚀 Future Improvements

- Hybrid Search
- Conversation Memory
- Streaming Responses
- Source Citation UI
- Docker Deployment
- FastAPI Migration
- RAGAS Evaluation
- Authentication & Security

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t medical-chatbot .
```

## Run Container

```bash
docker run -p 8080:8080 medical-chatbot
```

---

# 📸 Screenshots

Add screenshots inside:

```bash
screenshots/
```

Example:

- home.png
- result.png
- architecture.png

---

# 🔐 Security Notes

❌ Never push:

- `.env`
- API keys
- `venv/`
- secrets

---

# 👨‍💻 Author

## MD Humayun

M.Tech — Computer Science & Engineering  
SVNIT Surat

---

# 📚 References

1. Retrieval-Augmented Generation (RAG)
2. LangChain Documentation
3. Pinecone Documentation
4. Ollama Documentation
5. Attention Is All You Need

---

# ⭐ GitHub Topics

```text
rag
llm
langchain
pinecone
ollama
medical-chatbot
flask
machine-learning
nlp
generative-ai
python
```

---

# 📄 License

This project is licensed under the MIT License.

---

# 🌟 If you found this project useful, give it a star!