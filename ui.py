import streamlit as st
from embedder import get_embedding
from database import search_error
from main import initialize_database

# -------------------------------
# Initialize database (runs once)
# -------------------------------
total_records = initialize_database()

# -------------------------------
# UI Setup
# -------------------------------
st.set_page_config(page_title="AI Debugging Assistant", layout="centered")

st.title("🧠 AI Debugging Assistant")
st.caption(f"Loaded {total_records} known errors into the system")

# -------------------------------
# User Input
# -------------------------------
query = st.text_input("Enter your error:")

# -------------------------------
# Search + Display
# -------------------------------
if query:
    query_embedding = get_embedding(query)
    results = search_error(query_embedding)

    st.subheader("🔍 Suggested Fixes")

    seen = set()

    for result in results:
        error_text = result["error"]
        solution_text = result["solution"]

        # 🚫 Skip duplicates
        if error_text in seen:
            continue

        seen.add(error_text)

        st.write(f"🔹 Score: {result['score']:.2f}")
        st.write(f"❌ Error: {error_text}")
        st.write(f"✅ Solution: {solution_text}")
        st.write("---")