import pickle
from sentence_transformers import SentenceTransformer

# Chargement du modèle d'embedding et de l'index FAISS
model = SentenceTransformer('all-MiniLM-L6-v2')
with open("vector_index.pkl", "rb") as f:
    index = pickle.load(f)

with open("documents.pkl", "rb") as f:
    documents = pickle.load(f)  # Une liste de documents correspondants

def search_documents(query: str, top_k: int = 5) -> list:
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    return [documents[i] for i in indices[0] if i < len(documents)]
