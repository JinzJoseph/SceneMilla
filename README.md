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