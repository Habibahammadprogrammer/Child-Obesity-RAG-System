from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="emilyalsentzer/Bio_ClinicalBERT",encode_kwargs={'normalize_embeddings': True})

print("Loading FAISS database...")

vectorstore = FAISS.load_local(
    "faiss_index", 
    embeddings, 
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 5, 
        "score_threshold": 0.65
    }
)


