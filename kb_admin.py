import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from ingest import load_and_chunk_documents
from retriever import embeddings

def get_database():
    """Loads the existing FAISS database."""
    if not os.path.exists("faiss_index"):
        print("Error: Knowledge Base not found. Run ingest.py first.")
        return None
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

def add_documents_to_kb(file_paths):
    """Adds new documents to the existing database without retraining."""
    vectorstore = get_database()
    if not vectorstore: return

    print(f"\nProcessing new documents: {file_paths}")
    new_chunks = load_and_chunk_documents(file_paths)
    
    if new_chunks:
        print("Adding chunks to the database...")
        vectorstore.add_documents(new_chunks)
        vectorstore.save_local("faiss_index")
        print("Success! Documents added and KB saved.")
    else:
        print("No valid documents found to add.")

def remove_document_from_kb(filename):
    """Removes all chunks associated with a specific file without retraining."""
    vectorstore = get_database()
    if not vectorstore: return

    print(f"\nSearching database for chunks from '{filename}'...")
    
    docstore_dict = vectorstore.docstore._dict
    
    # Find all IDs that match the target filename
    ids_to_delete = []
    for doc_id, document in docstore_dict.items():
        if document.metadata.get("source") == filename:
            ids_to_delete.append(doc_id)
            
    if ids_to_delete:
        print(f"Found {len(ids_to_delete)} chunks belonging to '{filename}'. Deleting...")
        vectorstore.delete(ids_to_delete)
        vectorstore.save_local("faiss_index")
        print("Success! Document removed and KB saved.")
    else:
        print(f"Error: No chunks found for '{filename}'. Check the exact file path.")


    