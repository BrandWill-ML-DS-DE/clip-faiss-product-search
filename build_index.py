import os
import pickle
import numpy as np
import faiss
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from PIL import Image

# 1. Load CLIP Model
model = SentenceTransformer("clip-ViT-B-32")

image_folder = "data/images"
image_paths = []
embeddings = []

print("🤖 Encoding images into vectors...")
for file in tqdm(os.listdir(image_folder)):
    if file.endswith(".jpg"):
        path = os.path.join(image_folder, file)
        try:
            img = Image.open(path).convert("RGB")
            feat = model.encode(img)
            embeddings.append(feat)
            image_paths.append(path)
        except: continue

embeddings = np.array(embeddings).astype("float32")
faiss.normalize_L2(embeddings)

# 2. Build HNSW Index (The Pro Way)
dim = embeddings.shape[1]
index = faiss.IndexHNSWFlat(dim, 32) # 32 connections per node
index.add(embeddings)

# 3. Save
faiss.write_index(index, "vector.index")
with open("metadata.pkl", "wb") as f:
    pickle.dump(image_paths, f)
print("✅ Index built successfully!")
