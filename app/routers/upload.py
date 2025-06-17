from fastapi import APIRouter, UploadFile, File
import os
from app.utils import doc_parser, chunker, embedding
from app.vectorstore import chroma

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    path = f"uploads/{file.filename}"
    with open(path, 'wb') as f:
        f.write(await file.read())

    file_type = file.filename.split(".")[-1].lower()
    text = doc_parser.extract_text(path, file_type)
    chunks = chunker.semantic_chunking(text)
    embeds, valid_chunks = embedding.get_embeddings(chunks)
    meta = [{"source": file.filename, "chunk": i} for i in range(len(valid_chunks))]
    chroma.add_to_chromadb(valid_chunks, embeds, meta)
    return {"status": "success", "filename": file.filename, "total_chunks": len(valid_chunks)}
