import pickle
import faiss
import numpy as np
import ollama

from sentence_transformers import SentenceTransformer

index = faiss.read_index(
    "vector_db/faiss.index"
)

with open(
    "vector_db/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)

embedding_model = SentenceTransformer(
    "  "
)

def ask_question(question):

    query_embedding = embedding_model.encode(
        [question]
    )

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        5
    )

    context = "\n\n".join(
        chunks[i]
        for i in indices[0]
    )

    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{question}

If answer is not present in context,
say:
Information not found in documents.
"""

    response = ollama.chat(
        model=" ",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
