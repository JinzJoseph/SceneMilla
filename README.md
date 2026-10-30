# SceneMilla
 SceneMilla IT support system that uses Retrieval-Augmented Generation (RAG) and autonomous AI agents to help employees resolve technical issues efficiently. It retrieves relevant information from enterprise documents, provides context-aware troubleshooting solutions, automates task, and escalates complex issues to human technicians


# First we have to create a virtual env 
    #python -m venv venv
# Activate it
venv\Scripts\activate.ps1

#install requirement file 
#pip install requirements.txt  


# create the folder structure accordinaliy

SceneMilla/
app/
main.py
data/ 
static/ 
templates/ 
tests/ 
uploads/ 
venv/
.git/ 
.env
.gitignore
create_project.py
ingest_sample_kb.py
README.md
requirements.txt
run.py


# create your API KEY
  OPENAI_API_KEY="your-api-key"
  TAVILY_API_KEY="your-api-key"
  PINECONE_API_KEY="your-api-key"
  PINCONE_INDEX_NAME="your-api-key"
  PINCONE_NAMESPACE="your-api-key"
  OPENAI_MODEL="model"
  EMBEDDIBNG_MODEL=""


# 🚀 SceneMilla – AI-Powered Enterprise IT Support Assistant

**SceneMilla** is an AI-powered Enterprise IT Support Assistant built using **Agentic RAG (Retrieval-Augmented Generation)**. It helps employees resolve common IT-related issues by retrieving relevant information from enterprise knowledge documents and generating context-aware solutions using Large Language Models (LLMs).

The system aims to reduce the workload of IT support teams, improve response times, and provide employees with reliable technical assistance.

## ✨ Features

- **AI-Powered IT Support:** Get answers to common IT issues using an AI assistant.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from enterprise documents before generating answers.
- **Document Ingestion:** Load and process company IT documents such as PDF, TXT, Markdown and DOCX files.
- **Vector Search:** Store and retrieve document embeddings using Pinecone.
- **Semantic Search:** Find relevant information based on the meaning of employee questions.
- **Agentic Workflow:** Use LangGraph to orchestrate AI agent workflows.
- **LLM Integration:** Generate responses using Groq API.
- **Local Embeddings:** Generate document embeddings using Hugging Face models.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend development |
| FastAPI | Backend API framework |
| LangChain | LLM and RAG integration |
| LangGraph | Agent workflow orchestration |
| Groq API | Large Language Model inference |
| Hugging Face | Text embedding generation |
| Pinecone | Vector database |
| Sentence Transformers | Embedding model |
| python-dotenv | Environment variable management |

### AI Models and Services

- **LLM:** Groq API – GPT-OSS 20B (or another supported Groq model)
- **Embedding Model:** `sentence-transformers/all-MiniLM-L6-v2`
- **Embedding Dimension:** 384
- **Vector Database:** Pinecone

## 🏗️ Project Architecture

```text
SceneMilla/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── llm.py
│   │
│   ├── rag/
│   │   ├── ingestion.py
│   │   └── vectorestore.py
│   │
│   ├── agents/
│   │   └── ...
│   │
│   └── tools/
│       └── ...
│
├── data/
│   └── sample_kb/
│       └── company_it_handbook.md
│
├── run.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

*Note: The architecture above is a suggested project structure. Adjust filenames and folders to match your actual repository.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SceneMilla
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root directory.

```env
GROQ_API_KEY=your_groq_api_key

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=scenemilla-384
PINECONE_NAMESPACE=default

PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
```

**API Keys:**

- Groq: https://console.groq.com/
- Pinecone: https://app.pinecone.io/

Never upload your actual `.env` file or API keys to GitHub.

### 6. Run the application

```bash
python run.py
```

## 🔄 How SceneMilla Works

### Phase 1: Document Ingestion

1. Load enterprise IT support documents.
2. Extract text from the documents.
3. Split large documents into smaller text chunks.
4. Generate embeddings using Hugging Face.
5. Store the embeddings and document metadata in Pinecone.

### Phase 2: User Query Processing

1. An employee submits an IT-related question.
2. The question is converted into an embedding.
3. Pinecone searches for relevant document chunks.
4. The retrieved context is passed to the LLM through Groq.
5. The LLM generates a context-aware response.
6. The employee receives the suggested solution.

### RAG Workflow

```text
Employee Question
       |
       v
Query Embedding
       |
       v
Pinecone Vector Search
       |
       v
Retrieve Relevant Documents
       |
       v
LangGraph Agent Workflow
       |
       v
Groq LLM
       |
       v
AI-Generated Answer
       |
       v
Employee
```

## 📚 Example Use Cases

SceneMilla can assist employees with:

- How to connect to the company VPN.
- How to reset a company password.
- Troubleshooting Wi-Fi connectivity issues.
- Resolving email configuration problems.
- Accessing internal company portals.
- Understanding common IT policies and procedures.

## 🔮 Future Enhancements

- [ ] Interactive React-based user interface.
- [ ] Multi-agent IT support workflow.
- [ ] Automated IT support ticket creation.
- [ ] Human technician escalation.
- [ ] Employee authentication and authorization.
- [ ] Conversation history and memory.
- [ ] Admin dashboard for managing knowledge documents.
- [ ] Feedback and response evaluation system.

## 🔐 Security

- API keys are stored in environment variables.
- Sensitive credentials should never be committed to GitHub.
- Enterprise documents should be accessible only to authorized users.
- Retrieved information should be validated before performing sensitive operations.

## 👨‍💻 Developer

**Developed as a project focused on Agentic AI, Retrieval-Augmented Generation (RAG), and Enterprise IT Support Automation.**

---

⭐ If you find this project interesting, consider giving the repository a star!

**Project:** SceneMilla – Enterprise IT Support Agentic RAG Application