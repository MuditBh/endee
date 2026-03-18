# Simulated Endee Client (API-ready design)

class EndeeClient:
    def __init__(self):
        self.index = {}

    def insert_vectors(self, vectors, metadata):
        for i, vec in enumerate(vectors):
            self.index[i] = {
                "vector": vec,
                "metadata": metadata[i]
            }

    def search(self, query_vector, top_k=3):
        # NOTE: Simulated similarity search (replace with Endee API in production)
        results = []

        for key, value in self.index.items():
            results.append({
                "score": 0.85,
                "metadata": value["metadata"]
            })

        return results[:top_k]