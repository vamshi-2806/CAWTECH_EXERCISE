from fastapi import APIRouter
from app.vectorstore import chroma
import requests

router = APIRouter()

@router.get("/ask/")
def ask_question(question: str):
    try:
        # Step 1: Retrieve context from ChromaDB
        results = chroma.retrieve_relevant_chunks(question)
        context = "\n".join(results['documents'][0]) if results['documents'] else ""

        # Step 2: Create prompt
        prompt = f"""You are a helpful assistant. Use the following context to answer the user's question.

Context:
{context}

Question: {question}
Answer:"""

        # Step 3: Send to Ollama
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "phi3",  # or llama3, mistral, etc.
            "prompt": prompt,
            "stream": False
        })

        result = response.json()
        return {
            "question": question,
            "retrieved_chunks": results['documents'][0],
            "response": result.get("response", "No response from model")
        }

    except Exception as e:
        return {"error": str(e)}



# from fastapi import APIRouter
# from app.vectorstore import chroma
# from app.utils.gemini import generate_answer

# router = APIRouter()

# @router.get("/ask/")
# def ask_question(question: str):
#     results = chroma.retrieve_relevant_chunks(question)
#     context = "\n".join(results['documents'][0]) if results['documents'] else ""
#     return generate_answer(context, question)


# from fastapi import APIRouter
# from app.vectorstore import chroma

# router = APIRouter()

# @router.get("/ask/")
# def ask_question(question: str):
#     try:
#         # Just retrieve relevant chunks — no LLM
#         results = chroma.retrieve_relevant_chunks(question)

#         chunks = results['documents'][0] if results['documents'] else []

#         return {
#             "question": question,
#             "retrieved_chunks": chunks,
#             "num_chunks": len(chunks)
#         }

#     except Exception as e:
#         return {"error": str(e)}


# from fastapi import APIRouter
# from app.vectorstore import chroma
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai

# # Load Gemini API key
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Gemini model
# model = genai.GenerativeModel("gemini-pro")

# router = APIRouter()

# @router.get("/ask/")
# def ask_question(question: str):
#     try:
#         # Step 1: RAG — retrieve from vector store
#         results = chroma.retrieve_relevant_chunks(question)
#         rag_chunks = results['documents'][0] if results['documents'] else []
#         rag_context = "\n".join(rag_chunks)

#         # Step 2: Run Gemini LLM with raw user query
#         llm_response = model.generate_content(question)
#         llm_answer = llm_response.text.strip()

#         # Step 3: Run Gemini with RAG-enhanced prompt
#         if rag_context:
#             prompt_with_rag = f"""Use the following document context to answer the user's question.

# Document Context:
# {rag_context}

# User Question:
# {question}

# Answer:"""
#             rag_response = model.generate_content(prompt_with_rag)
#             rag_answer = rag_response.text.strip()
#         else:
#             rag_answer = "No relevant document chunks found."

#         # Step 4: Optimized final response
#         final_response = f"""🧠 Gemini's own knowledge:
# {llm_answer}

# 📚 Document-based (RAG) answer:
# {rag_answer}
# """
#         return {
#             "question": question,
#             "llm_only_answer": llm_answer,
#             "rag_based_answer": rag_answer,
#             "optimized_response": final_response
#         }

#     except Exception as e:
#         return {"error": str(e)}
