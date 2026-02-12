from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import faiss, pickle, time, numpy as np

app = FastAPI()
model = SentenceTransformer("clip-ViT-B-32")
index = faiss.read_index("vector.index")
with open("metadata.pkl", "rb") as f:
    paths = pickle.load(f)

@app.get("/search")
async def search(query: str):
    start = time.time()
    
    # Text to Vector
    vec = model.encode([query]).astype("float32")
    faiss.normalize_L2(vec)
    
    # Search the Graph
    dist, indices = index.search(vec, 6)
    
    return {
        "results": [paths[i] for i in indices[0]],
        "latency_ms": round((time.time() - start) * 1000, 2)
    }
