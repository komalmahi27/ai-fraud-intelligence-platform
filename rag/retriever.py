# ==========================================
# RETRIEVAL FUNCTION
# ==========================================

def retrieve_relevant_chunks(query, top_k=3):

    import pickle
    import numpy as np
    import faiss

    from sentence_transformers import SentenceTransformer


    # ==========================================
    # LOAD LIGHTWEIGHT EMBEDDING MODEL
    # ==========================================

    model = SentenceTransformer(
        "all-MiniLM-L6-v2",
        device="cpu"
    )


    # ==========================================
    # LOAD FAISS INDEX
    # ==========================================

    index = faiss.read_index(
        "rag/faiss_index/fraud_knowledge.index"
    )


    # ==========================================
    # LOAD CHUNKS
    # ==========================================

    with open(
        "rag/faiss_index/chunks.pkl",
        "rb"
    ) as file:

        chunks = pickle.load(file)


    # ==========================================
    # GENERATE QUERY EMBEDDING
    # ==========================================

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    ).astype("float32")


    # ==========================================
    # SEARCH VECTOR DATABASE
    # ==========================================

    distances, indices = index.search(
        query_embedding,
        top_k
    )


    # ==========================================
    # RETRIEVE MATCHED CHUNKS
    # ==========================================

    retrieved_chunks = [

        chunks[idx]

        for idx in indices[0]

    ]


    return retrieved_chunks