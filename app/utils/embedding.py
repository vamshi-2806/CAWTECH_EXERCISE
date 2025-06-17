from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(chunks):
    valid_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    embeddings = model.encode(valid_chunks, convert_to_tensor=False)
    return embeddings, valid_chunks
