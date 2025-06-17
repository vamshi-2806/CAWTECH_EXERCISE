# Intelligent Document Q&A System

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Set your Google Gemini API key in `.env`:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Run the app:
```
uvicorn app.main:app --reload
```

4. Open the browser:
```
http://127.0.0.1:8000/docs
```

Upload documents and ask questions using the API.

## Features

- PDF/DOCX/TXT ingestion
- Semantic chunking and embedding
- Google Gemini for Q&A
- Feedback mechanism