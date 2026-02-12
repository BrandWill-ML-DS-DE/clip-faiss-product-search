import streamlit as st
import requests

st.set_page_config(page_title="AI Fashion Search", layout="wide")
st.title("🛍️ Semantic Product Search")

query = st.text_input("Describe what you want:", "blue summer dress")

if st.button("Search"):
    res = requests.get(f"http://localhost:8000/search?query={query}").json()
    
    st.sidebar.metric("Search Latency", f"{res['latency_ms']} ms")
    
    cols = st.columns(3)
    for i, img_path in enumerate(res['results']):
        with cols[i % 3]:
            st.image(img_path, use_container_width=True)
