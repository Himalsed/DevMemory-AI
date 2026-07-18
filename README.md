# DevMemory AI 🧠

A local AI assistant that helps developers remember and search their own codebase.

Developers work on multiple projects and often forget where they wrote a specific function, how a feature was implemented, or where a certain logic exists. DevMemory AI solves this by creating a searchable memory of your code using embeddings, vector search, and a local LLM.

The project runs locally, meaning your code stays on your machine.

---

## Features

- 🔍 Search your codebase using natural language
- 🧠 AI-powered answers based on your own code
- 💾 Local vector memory using ChromaDB
- 🤗 Hugging Face embeddings for semantic search
- 🦙 Local Llama model support through Ollama
- ⚡ Fast terminal-based workflow
- 🔒 Privacy-focused (no code upload required)

---

## How it works

DevMemory AI follows a simple RAG (Retrieval-Augmented Generation) pipeline.

```
Your Code
    |
    ↓
File Scanner
    |
    ↓
Code Parser
    |
    ↓
Hugging Face Embeddings
    |
    ↓
ChromaDB Vector Database
    |
    ↓
Semantic Search
    |
    ↓
Llama Local Model
    |
    ↓
AI Answer
```

### Example

Instead of manually searching:

```
Where did I create authentication?
```

You can ask:

```bash
devmemory ask "Where is authentication implemented?"
```

DevMemory searches your stored code and explains the relevant files.

---

# Project Structure

```
DevMemory-AI/

│
├── app/
│   │
│   ├── ai.py              # Handles Llama AI responses
│   ├── cli.py             # Terminal commands
│   ├── embeddings.py      # Creates vector embeddings
│   ├── parser.py          # Reads and processes code files
│   ├── scanner.py         # Finds project files
│   └── vector_store.py    # ChromaDB operations
│
├── vector_db/             # Local vector database (generated)
│
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variable example
├── .gitignore
├── LICENSE
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/Himalsed/DevMemory-AI.git
```

Move into the project:

```bash
cd DevMemory-AI
```

---

## 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Local AI Model

DevMemory uses Ollama to run Llama locally.

Install Ollama:

https://ollama.com


Download the model:

```bash
ollama pull llama3.2
```

Check:

```bash
ollama list
```

---

# Environment Setup

Create a `.env` file:

```bash
cp .env.example .env
```

Add your Hugging Face token:

```env
HF_TOKEN=your_token_here
```

The token is optional for public models but recommended for better download limits.

---

# Usage

## Index a project

Go to the project you want DevMemory to remember.

Example:

```bash
python main.py index /path/to/project
```

DevMemory will:

- scan files
- split code into chunks
- create embeddings
- store them in ChromaDB

---

## Ask questions

Example:

```bash
python main.py ask "Where is database connection handled?"
```

Example output:

```
DevMemory AI:

The database connection is handled in:

database.py

The file creates the database client
and manages connection settings.
```

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main language |
| Typer | CLI interface |
| ChromaDB | Vector database |
| Hugging Face | Text/code embeddings |
| Sentence Transformers | Embedding generation |
| Ollama | Local Llama model |
| RAG | AI retrieval pipeline |

---

# Why this project?

Most code search tools depend on cloud services or require uploading your source code.

DevMemory AI focuses on:

- keeping code private
- running locally
- creating personal AI memory for developers

The goal is to make working with large codebases easier.

---

# Future Improvements

- Support more programming languages
- Git history integration
- Automatic documentation generation
- Code explanation command
- VS Code extension
- Team shared memory

---

# License

This project is licensed under the MIT License.

Feel free to use, modify, and improve it.
