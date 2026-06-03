import os
import pickle

from pypdf import PdfReader
from docx import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

import faiss
import numpy as np

DOC_FOLDER = "documents"

all_chunks = []

def read_pdf(path):
    text = ""

    reader = PdfReader(path)

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"

    return text

def read_docx(path):
    doc = Document(path)

    return "\n".join(
        para.text for para in doc.paragraphs
    )

for file in os.listdir(DOC_FOLDER):

    path = os.path.join(DOC_FOLDER, file)

    if file.endswith(".pdf"):
        text = read_pdf(path)

    elif file.endswith(".docx"):
        text = read_docx(path)

    else:
        continue

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    for chunk in chunks:
        all_chunks.append(chunk)

print("Total chunks:", len(all_chunks))

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = embedding_model.encode(
    all_chunks,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype=np.float32
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    "vector_db/faiss.index"
)

with open(
    "vector_db/chunks.pkl",
    "wb"
) as f:
    pickle.dump(all_chunks, f)

print("Vector DB created successfully")