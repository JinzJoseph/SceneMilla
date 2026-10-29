import time
from pinecone import Pinecone , ServerlessSpec
from langchain_openai import OpenAIEmbeddings, PinconeVectorStore
from app.core.config import get_settings

settings=get_settings()

_embeddings=None
_vectorstore=None


EMBEDDING_DIMENSIONS={
    "text-embedding-3-small":1536,
    "text-embedding-3-large":3072,
    "text-embedding-ada-002":1536,
    "all-minilm-16-v2":384
}


def get_embedding_dimensions(model_name:str | None=None)->int:
    name=(model_name or settings.embedding_model or "").strip()
    if not name:
        raise RuntimeError("Embedding model is not configured")
    normalized=name.lower()
    if normalized in EMBEDDING_DIMENSIONS:
        return EMBEDDING_DIMENSIONS[normalized]
    if "text-embedding-3-small" in normalized:
        return 1536
    if "text-embedding-3-large" in normalized:
        return 3072
    if "text-embedding-ada-002" in normalized:
        return 1536
    if "all-minilm-16-v2" in normalized:
        return 384
    raise ValueError(f"Unsupported embedding model: {name}") 

def get_embedding():
    global _embeddings
    if _embeddings is None:
        if not settings.openai_api_key:
            raise RuntimeError("OpenAI API key is not configured")
        _embeddings = OpenAIEmbeddings(
            openai_api_key=settings.openai_api_key,
            model=settings.embedding_model
        )
    return _embeddings

def ensure_index():
    # checking setting class contain pinecone api key or not
    if not settings.pinecone_api_key:
        raise RuntimeError("PINECONE_API_KEY is missing")
# getting the dimension of the embedding model and creating a pinecone index if it does not exist
    desired_dimension = get_embedding_dimensions()
    pc = Pinecone(api_key=settings.pinecone_api_key)
    # getting the indexing name from pinecone
    names = [x["name"] for x in pc.list_indexes()]
# index  doesnt exists in pinecone ,it creates one with the specified dimension and metric 
    if settings.pinecone_index_name in names:
        index_info = pc.describe_index(settings.pinecone_index_name)
        current_dimension = getattr(index_info, "dimension", None)
        if current_dimension is None and isinstance(index_info, dict):
            current_dimension = index_info.get("dimension")
# 
        if current_dimension is not None and current_dimension != desired_dimension:
            pc.delete_index(name=settings.pinecone_index_name)
            while settings.pinecone_index_name in [x["name"] for x in pc.list_indexes()]:
                time.sleep(1)
# if exists ,gives the attributes
    if settings.pinecone_index_name not in [x["name"] for x in pc.list_indexes()]:
        pc.create_index(
            name=settings.pinecone_index_name,
            dimension=desired_dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        while not pc.describe_index(settings.pinecone_index_name).status["ready"]:
            time.sleep(1)

    return pc.Index(settings.pinecone_index_name)





