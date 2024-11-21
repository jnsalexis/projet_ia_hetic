from .retrieval import search_documents
from llm_utils import query_llm


def generate_response(question: str, use_rag: bool = False, temperature: float = 0.7) -> str:
    if use_rag:
        # Récupérer les documents pertinents
        retrieved_docs = search_documents(question)
        context = "\n".join(retrieved_docs)
        prompt = f"Question: {question}\nContext: {context}\nAnswer:"
    else:
        # Pas de récupération, seulement le modèle
        prompt = f"Question: {question}\nAnswer:"

    return query_llm(prompt, temperature)
