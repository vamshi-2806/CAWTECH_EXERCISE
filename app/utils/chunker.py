def semantic_chunking(text, max_chunk_size=500):
    paragraphs = text.split('\n')
    chunks, current = [], ""

    for para in paragraphs:
        if len(current) + len(para) < max_chunk_size:
            current += para + "\n"
        else:
            if current.strip():
                chunks.append(current.strip())
            current = para
    if current.strip():
        chunks.append(current.strip())
    return chunks
