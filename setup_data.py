import os
import requests
import pandas as pd
from tqdm import tqdm

# Create structure
os.makedirs("data/images", exist_ok=True)

# We'll use a curated sample of product images
# If you have your own CSV/Images, skip this.
print("📥 Downloading sample product metadata...")
csv_url = "https://raw.githubusercontent.com/ardamavi/Fashion-Dataset/master/fashion.csv"
img_base_url = "https://raw.githubusercontent.com/ardamavi/Fashion-Dataset/master/images/"

try:
    df = pd.read_csv(csv_url).head(1000) # Get 1000 products
    print(f"✅ Found {len(df)} products. Downloading images...")
    
    for i, row in tqdm(df.iterrows(), total=len(df)):
        img_id = row['id'] # Adjust based on CSV columns
        img_filename = f"{img_id}.jpg"
        save_path = f"data/images/{img_filename}"
        
        if not os.path.exists(save_path):
            r = requests.get(f"{img_base_url}{img_filename}")
            with open(save_path, 'wb') as f:
                f.write(r.content)
except Exception as e:
    print(f"Error: {e}. Ensure you have an internet connection.")
