# 🧠 AI Debugging Assistant (Semantic Search System)

## 🚀 Overview
AI Debugging Assistant is a semantic search-based system that helps developers quickly identify and resolve programming errors.

Unlike traditional keyword-based search, this system understands the meaning of error messages using vector embeddings and retrieves the most relevant solutions.

---

## 💡 Problem Statement
Developers often struggle to debug errors efficiently because traditional search methods depend on exact keyword matching.

This project solves that problem using semantic similarity, enabling context-aware and intelligent error resolution.

---

## 🧠 Features
- Semantic search using vector embeddings  
- Fast similarity search using FAISS  
- Endee-compatible vector database architecture  
- Real-time error-to-solution matching  
- Clean and interactive UI using Streamlit  
- Duplicate result filtering  
- Similarity score display  

---

## 🏗️ System Architecture

User Input  
↓  
Embedding Model (Sentence Transformers)  
↓  
Vector Database (FAISS / Endee-compatible)  
↓  
Similarity Search  
↓  
Top Matching Errors & Solutions  

---

## ⚙️ Tech Stack
- Python  
- Sentence Transformers  
- FAISS (Vector Database)  
- Streamlit  

---

## 🔗 Endee Integration

This project is designed with a modular vector database layer that is compatible with Endee Vector Database.

Currently, FAISS is used for local development and fast similarity search.  
A lightweight Endee client layer is implemented to simulate vector storage and retrieval.

This demonstrates how semantic search systems can be seamlessly migrated from FAISS to scalable vector databases like Endee for production-grade deployment.

---

## 📂 Project Structure

ai-debugging-assistant/  
│  
├── data/errors.json  
├── embedder.py  
├── database.py  
├── endee_client.py  
├── ui.py  
├── main.py  
├── requirements.txt  

---

## ▶️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/MuditBh/ai-debugging-assistant  
cd ai-debugging-assistant  
```

### 2. Install dependencies
```bash
pip install -r requirements.txt  
```

### 3. Run the application
```bash
streamlit run ui.py  
```

---

## 🧪 Sample Usage

**Input:**  
null pointer error  

**Output:**  
Score: 1.00  
Error: null pointer error  
Solution: Check for null before accessing object  

---

## ⚡ Performance Considerations
- FAISS enables fast similarity search in high-dimensional vector space  
- Embeddings capture semantic meaning instead of exact keywords  
- Architecture supports migration to scalable vector databases like Endee  

---

## 🧠 Real-World Use Case
This system helps developers debug errors faster by providing context-aware solutions, reducing dependency on manual search and improving productivity.

---

## 🚀 Future Enhancements
- Full Endee API integration  
- Retrieval-Augmented Generation (RAG) using LLMs  
- Language-specific filtering (Java, Python, etc.)  
- Feedback-based learning system  

---

## 🧠 Key Learnings
- Vector embeddings and semantic similarity  
- Efficient search using vector databases  
- Scalable backend system design  
- Building AI-powered developer tools  

---

## 📌 Conclusion
This project demonstrates how semantic search can significantly improve debugging efficiency and developer productivity.

It provides a strong foundation for building scalable AI systems using vector databases like Endee.
