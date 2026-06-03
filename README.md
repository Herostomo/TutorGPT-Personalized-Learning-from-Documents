# TutorGPT – Personalized Learning from Documents

TutorGPT is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF and DOCX documents and interact with them through a modern chat interface. The system uses semantic search with FAISS and Sentence Transformers to retrieve relevant information and generates answers locally using Ollama and Llama 3.

---

## Features

* Upload PDF documents
* Upload DOCX documents
* Automatic document chunking
* Semantic search using Sentence Transformers
* FAISS vector database for fast retrieval
* Local LLM inference using Ollama
* CustomTkinter graphical user interface
* Retrieval-Augmented Generation (RAG)
* Privacy-friendly local execution

---

## Tech Stack

### Frontend

* CustomTkinter

### Backend

* Python

### AI Components

* Ollama
* Llama 3
* Sentence Transformers
* FAISS

### Document Processing

* PyPDF
* python-docx
* LangChain Text Splitters

---

## Project Structure

```text
TutorGPT/
│
├── documents/
│   └── Uploaded PDFs and DOCX files
│
├── vector_db/
│   ├── faiss.index
│   └── chunks.pkl
│
├── build_index.py
├── rag_engine.py
├── gui.py
├── requirements.txt
└── README.md
```

---

## How It Works

1. User uploads one or more documents.
2. Documents are parsed and split into chunks.
3. Each chunk is converted into embeddings using Sentence Transformers.
4. Embeddings are stored in a FAISS vector database.
5. User asks a question through the GUI.
6. Relevant chunks are retrieved from FAISS.
7. Retrieved context is passed to Llama 3 through Ollama.
8. TutorGPT generates an answer based only on the document content.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Herostomo/TutorGPT-Personalized-Learning-from-Documents.git
cd TutorGPT-Personalized-Learning-from-Documents
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama:

https://ollama.com

Pull the Llama 3 model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama run llama3
```

---

## Usage

### Step 1: Build Vector Database

Place documents inside the `documents` folder and run:

```bash
python build_index.py
```

### Step 2: Launch Application

```bash
python gui.py
```

### Step 3: Upload Documents

* Click **Upload Document**
* Select PDF or DOCX files
* The vector database will be updated automatically

### Step 4: Chat with Documents

Ask questions about the uploaded documents directly from the chat interface.

---

## Example Questions

* What are the responsibilities mentioned in the internship offer?
* Summarize this document.
* What skills are required?
* What is the project timeline?
* Extract important points from the document.

---

## Future Enhancements

* Multi-document chat
* Streaming responses
* Chat history persistence
* Source citations
* Drag-and-drop file upload
* Dark/Light themes
* PDF export of conversations
* Support for additional document formats

---

## Screenshots

### Main Interface

Add your application screenshot here:

```text
screenshots/main_gui.png
```

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Local LLM Deployment
* Prompt Engineering
* GUI Development with CustomTkinter
* End-to-End AI Application Development

---

## Author

Kshitij Hedau

GitHub:
https://github.com/Herostomo

---

## License

This project is licensed under the MIT License.
