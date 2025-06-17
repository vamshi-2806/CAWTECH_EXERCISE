from fastapi import FastAPI
from app.routers import upload, query, feedback

app = FastAPI(title="Document Q&A System with Gemini 1.5 Pro")

app.include_router(upload.router, prefix="/document", tags=["Document"])
app.include_router(query.router, prefix="/qa", tags=["Query Answering"])
app.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])

@app.get("/")
def root():
    return {"message": "Welcome to the Gemini-powered Document Q&A System"}
