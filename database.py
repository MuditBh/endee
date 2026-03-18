import faiss
import numpy as np
from endee_client import EndeeClient

# Initialize Endee (simulated layer)
endee = EndeeClient()

# embedding size (MiniLM = 384)
dimension = 384

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Store metadata separately
metadata_store = []


# -------------------------------
# STORE DATA
# -------------------------------
def store_error(id, embedding, metadata):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    metadata_store.append(metadata)


# -------------------------------
# BUILD DATABASE (NEW - IMPORTANT)
# -------------------------------
def build_database(data, embedder):
    embeddings = []

    for i, item in enumerate(data):
        emb = embedder.get_embedding(item["error"])
        embeddings.append(emb)
        store_error(i, emb, item)

    # Insert into Endee (simulated)
    endee.insert_vectors(embeddings, data)


# -------------------------------
# SEARCH FUNCTION (UPDATED)
# -------------------------------
def search_error(query_embedding):
    query = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query, k=3)

    results = []

    # FAISS results
    for idx, dist in zip(indices[0], distances[0]):
        if 0 <= idx < len(metadata_store):
            score = float(1 / (1 + dist))  # convert distance to similarity
            results.append({
                "score": score,
                "error": metadata_store[idx]["error"],
                "solution": metadata_store[idx]["solution"]
            })

    # Endee fallback (simulated)
    if len(results) == 0:
        endee_results = endee.search(query_embedding)

        for match in endee_results:
            results.append({
                "score": match["score"],
                "error": match["metadata"]["error"],
                "solution": match["metadata"]["solution"]
            })

    # Final fallback
    if len(results) == 0:
        results.append({
            "score": 0.0,
            "error": "No exact match found",
            "solution": "Try rephrasing your error or check logs manually."
        })

    return results