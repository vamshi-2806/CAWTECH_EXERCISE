import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))


model = genai.GenerativeModel("models/gemini-1.5-pro")

def generate_answer(context, question):
    if not context.strip():
        return {"answer": "No relevant context found."}
    try:
        prompt = f"Use the context below to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}"
        response = model.generate_content(prompt)
        return {"answer": response.text}
    except Exception as e:
        return {"error": str(e)}
