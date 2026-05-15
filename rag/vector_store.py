import faiss
import numpy as np
import pickle

from embeddings import embeddings
from text_chunker import chunks


# ==========================================
# CONVERT EMBEDDINGS TO NUMPY ARRAY
# ==========================================

embedding_array = np.array(
    embeddings
).astype("float32")


# ==========================================
# CREATE FAISS INDEX
# ==========================================

dimension = embedding_array.shape[1]

index = faiss.IndexFlatL2(dimension)


# ==========================================
# ADD EMBEDDINGS TO INDEX
# ==========================================

index.add(embedding_array)


# ==========================================
# SAVE FAISS INDEX
# ==========================================

faiss.write_index(

    index,

    "rag/faiss_index/fraud_knowledge.index"

)


# ==========================================
# SAVE CHUNKS MAPPING
# ==========================================

with open(

    "rag/faiss_index/chunks.pkl",

    "wb"

) as file:

    pickle.dump(chunks, file)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========== FAISS VECTOR STORE CREATED ==========\n")

print(f"Total vectors stored: {index.ntotal}")

print("\nFAISS index saved successfully.")