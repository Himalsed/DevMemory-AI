import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer


load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# Hugging Face 
model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5",
    token=HF_TOKEN
)
def create_embeddings(texts):
    """
    Convert multiple code chunks into vector embeddings.
    """
    embeddings = model.encode(texts, batch_size=16,   show_progress_bar=True   )
    return embeddings.tolist()

def create_single_embedding(text):
    """
    Convert a single query into a vector embedding.
    """
    embedding = model.encode(text  )
    return embedding.tolist()