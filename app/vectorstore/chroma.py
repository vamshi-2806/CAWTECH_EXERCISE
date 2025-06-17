import chromadb
from chromadb.config import Settings
from app.utils import embedding

client = chromadb.Client(Settings())
collection = client.get_or_create_collection("doc_chunks")

def add_to_chromadb(chunks, embeddings, metadata_list):
    for i, (text, embedding, meta) in enumerate(zip(chunks, embeddings, metadata_list)):
        collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[f"chunk-{i}"],
            metadatas=[meta]
        )

def retrieve_relevant_chunks(query, k=5):
    query_embedding, _ = embedding.get_embeddings([query])
    return collection.query(query_embeddings=[query_embedding[0]], n_results=k)
