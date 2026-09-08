# Medical Chatbot — RAG over a Medical Knowledge Base

![Python](https://img.shields.io/badge/Python-3.14-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

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

## Features

- Retrieval-Augmented Generation (RAG)

- Semantic Search using Embeddings

- Pinecone Vector Database Integration

- Local LLM Inference using Ollama

- Flask-based Web Interface

- Medical PDF Knowledge Base

- Explicit refusal when retrieval returns nothing relevant

- Fully Open Source Stack

- Research-Oriented Architecture

## System architecture

```
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

## RAG workflow

### Offline phase

- Load medical PDFs
- Split into chunks
- Generate embeddings
- Store vectors in Pinecone

### Online phase

- User asks query
- Query embedding generated
- Similar chunks retrieved
- Context injected into prompt
- LLM generates grounded response — **or refuses**, if nothing retrieved clears the grounding bar

## Tech stack

| Component       | Technology       |
| --------------- | ---------------- |
| LLM             | Llama 3.2        |
| Embeddings      | nomic-embed-text |
| Framework       | LangChain        |
| Vector DB       | Pinecone         |
| Backend         | Flask            |
| Language        | Python           |
| Local Inference | Ollama           |

## Project structure

```
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
├── app.py
├── store_index.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mdhumayun7/medical-chatbot.git
cd medical-chatbot
```

---

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama models

### Pull the embedding model

```bash
ollama pull nomic-embed-text
```

### Pull the LLM

```bash
ollama pull llama3.2
```

### Verify

```bash
ollama list
```

## Environment variables

Create a `.env` file:

```
PINECONE_API_KEY=your_api_key_here
```

## Add medical PDFs

Place all medical PDF files inside:

```
data/
```

## Create the vector index

Run the ingestion pipeline:

```bash
python store_index.py
```

## Run the application

```bash
python app.py
```

## Open in a browser

```
http://localhost:8080
```

## Docker

### Build the image

```bash
docker build -t medical-chatbot .
```

### Run the container

```bash
docker run -p 8080:8080 medical-chatbot
```

## Pipeline parameters

The values that actually determine how this system behaves:

| Property                | Value                                                        |
| ----------------------- | ------------------------------------------------------------ |
| Corpus                  | 1,152 pages of medical reference material                     |
| Chunking                | 500 characters, overlapping                                   |
| Retrieval               | top-3, cosine similarity                                      |
| Embedding dimension     | 768 (`nomic-embed-text`)                                      |
| Generation temperature  | 0.4                                                           |
| Out-of-corpus behaviour | explicit refusal, no fallback to parametric memory            |

Chunk size and overlap are quietly the most consequential parameters here. 500-character overlapping chunks keep enough context inside a single chunk to be self-explanatory, while staying small enough that top-3 retrieval returns focused text rather than three pages of noise.

## The design decision that matters

Most RAG demos pass retrieved context to the model and hope it uses it. If the
retriever returns nothing relevant, the model falls back on what it absorbed
during training and answers anyway — fluently, and wrongly.

Here the prompt chain is **constrained to retrieved context with an explicit
refusal path**. An out-of-corpus question produces a refusal rather than a
confident guess. In a medical setting that is the correct output, and it is the
behaviour this project exists to demonstrate.

## Key concepts

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Similarity Search
- Prompt Engineering
- Approximate Nearest Neighbor Search
- LLM Orchestration
- Context Grounding

## Limitations and disclaimer

**This is not a medical device and does not provide clinical advice.** It is an
engineering demonstration of grounded retrieval.

- Answer quality is bounded entirely by the ingested corpus. The system cannot
  answer what the corpus does not contain — which is the intended behaviour, not
  a shortcoming.
- Grounding is demonstrated, not benchmarked. There is no evaluation against a
  labelled question set, so no claim is made about factual accuracy rates.
- Retrieval is dense-only, so it misses cases where exact lexical overlap
  matters more than semantic similarity.
- Single-turn only. There is no conversation memory, so follow-up questions lose
  the context of what came before.

## Future improvements

- Hybrid search (dense + lexical)
- Conversation memory
- Streaming responses
- Source citation in the UI
- FastAPI migration
- RAGAS evaluation against a labelled question set
- Authentication & security

## Security notes

Never commit:

- `.env`
- API keys
- `venv/`
- any secret

## Author

**MD Humayun**
M.Tech — Computer Science (Information Security & Privacy), SVNIT Surat

[Portfolio](https://mdhumayun7.github.io/MD-HUMAYUN-PORTFOLIO/) ·
[GitHub](https://github.com/mdhumayun7) ·
[LinkedIn](https://www.linkedin.com/in/md-humayun-82051521a/)

## References

1. Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020)
2. LangChain Documentation
3. Pinecone Documentation
4. Ollama Documentation
5. Vaswani et al., *Attention Is All You Need* (2017)

## License

This project is licensed under the MIT License.
