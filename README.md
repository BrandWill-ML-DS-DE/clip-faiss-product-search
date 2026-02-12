# 🛍️ Semantic Product Search Engine

A high-performance, multi-modal search engine built with **CLIP** and **FAISS (HNSW)**. This project allows users to search for physical products using natural language descriptions (e.g., "blue running shoes") instead of just keywords.



## 🚀 Technical Highlights
* **Model:** OpenAI's CLIP (`clip-ViT-B-32`) used for multi-modal embeddings.
* **Vector Database:** FAISS (Facebook AI Similarity Search) using an **HNSW (Hierarchical Navigable Small World)** index for $O(\log N)$ search complexity.
* **Backend:** FastAPI for high-concurrency request handling.
* **Frontend:** Streamlit for a clean, interactive user experience.

## 🏗️ System Architecture
1.  **Ingestion:** Images are processed through a Vision Transformer to create 512-dimension vectors.
2.  **Indexing:** Vectors are inserted into a proximity graph (HNSW) to allow for sub-20ms retrieval.
3.  **Inference:** Natural language queries are encoded into the same vector space, and a "Nearest Neighbor" search finds the most relevant images.



## 🛠️ Installation & Usage
1. `pip install -r requirements.txt`
2. `python setup_data.py`  # Downloads professional dataset
3. `python build_index.py` # Generates vector embeddings
4. `uvicorn api:app`       # Starts the backend
5. `streamlit run app.py`  # Starts the UI
