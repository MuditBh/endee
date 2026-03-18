import json
from embedder import get_embedding
from database import store_error

def initialize_database():
    with open("data/errors.json", "r") as file:
        error_data = json.load(file)

    print("🔄 Loading data into vector database...")

    for idx, item in enumerate(error_data):
        embedding = get_embedding(item["error"])
        store_error(str(idx), embedding, item)

    print(f"✅ Loaded {len(error_data)} errors successfully")

    return len(error_data)