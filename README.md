
# Local Document Q&A System using RAG + Ollama

A fully local, privacy-first intelligent document assistant that answers questions using uploaded documents.  
It combines **RAG (Retrieval-Augmented Generation)** with **Ollama-powered LLMs** like `phi3`, `llama3`, or `mistral`.

---

## 🚀 Features

- ✅ Upload PDF, DOCX, or TXT documents
- 🧠 Chunk, embed and index content locally with `MiniLM` + `ChromaDB`
- 🔎 Query using FastAPI — retrieves relevant context using RAG
- 🤖 Answer generation via **local Ollama models**
- 📝 Feedback collection endpoint
- ⚡ 100% local — no API keys, no internet required for inference

---

## 🛠️ Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [sentence-transformers](https://www.sbert.net/) for embeddings
- [Ollama](https://ollama.com/) to run LLMs locally
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) and `docx2txt` for document parsing

---

## 📦 Folder Structure

```

📁 app
┣ 📂 routers         # API endpoints
┣ 📂 utils           # Embedding, parsing, chunking
┣ 📂 vectorstore     # ChromaDB integration
┗ main.py            # FastAPI app entrypoint
📁 uploads             # Stores uploaded documents
.env                  # Ollama model key (optional)
requirements.txt

````

---

## 🧪 Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/vamshi-2806/CAWTECH_EXERCISE.git
cd CAWTECH_EXERCISE
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama (first time pulls the model)

```bash
ollama pull phi3
ollama run phi3
```

> 💡 You can swap `phi3` with `llama3`, `mistral`, or any Ollama-supported model.

### 4. Start the backend

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoints (via Swagger UI)

Open browser:

```
http://127.0.0.1:8000/docs
```

### Available Routes:

| Method | Route                   | Description                    |
| ------ | ----------------------- | ------------------------------ |
| GET    | `/`                     | Health check / Welcome message |
| POST   | `/document/upload/`     | Upload a document              |
| GET    | `/qa/ask/?question=...` | Ask a question using local LLM |
| POST   | `/feedback/`            | Submit feedback                |

---

## 📤 Example Usage

1. Upload a document using `/document/upload/`
2. Ask:

```
/qa/ask/?question=What is semantic chunking?
```

3. Get a response like:

```json
{
  "question": "What is semantic chunking?",
  "retrieved_chunks": [...],
  "response": "Semantic chunking is the process of..."
}
```

---

## 🧠 Future Ideas

* Add Streamlit or React frontend
* Persist feedback to file or DB
* Support multi-doc queries
* Add support for Claude, Gemini, or OpenAI (optional)

---

## 🙌 Credits

* Built using [Ollama](https://ollama.com), [FastAPI](https://fastapi.tiangolo.com/), and [ChromaDB](https://www.trychroma.com/)
* Powered by local language models for 100% private document Q\&A

---

