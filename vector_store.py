import chromadb

client = chromadb.PersistentClient( path="vector_db")

collection = client.get_or_create_collection(name="code_memory")

def store_documents(documents, embeddings):
   
    ids = []
    texts = []
    metadata = []

    for i, doc in enumerate(documents):

        ids.append(str(i) )

        texts.append(doc["content"])

        metadata.append(doc["metadata"] )



    collection.add( ids=ids,documents=texts,embeddings=embeddings,metadatas=metadata)

def search_memory(embedding, limit=5):

    return collection.query(

        query_embeddings=[embedding],n_results=limit
)