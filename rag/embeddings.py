from sentence_transformers import SentenceTransformer

from text_chunker import chunks


# ==========================================
# LOAD EMBEDDING MODEL
# ==========================================

model = SentenceTransformer(

    "all-MiniLM-L6-v2"

)


# ==========================================
# GENERATE EMBEDDINGS
# ==========================================

print("\nGenerating embeddings...\n")

embeddings = model.encode(chunks)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n========== EMBEDDING RESULTS ==========\n")

print(f"Total embeddings: {len(embeddings)}")

print(f"Embedding dimension: {len(embeddings[0])}")