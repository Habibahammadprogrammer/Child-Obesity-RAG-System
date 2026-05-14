import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_and_chunk_documents(file_paths):
    documents = []
    
    for path in file_paths:
        if path.endswith(".pdf") and os.path.exists(path):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())
            print(f"Loaded PDF: {path}")
        else:
            print(f"Skipped or not found: {path}")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"\nSuccess! Generated {len(chunks)} chunks.")
    return chunks

if __name__ == "__main__":

    my_files = ["Files/Obesity1.pdf", "Files/Obesity2.pdf", "Files/Obesity3.pdf", "Files/Obesity4.pdf", "Files/Obesity5.pdf", "Files/Obesity6.pdf", "Files/Obesity7.pdf", "Files/Obesity8.pdf", "Files/Obesity9.pdf", "Files/Obesity10.pdf", "Files/Obesity11.pdf", "Files/Obesity12.pdf", "Files/Obesity13.pdf"] 
    doc_chunks = load_and_chunk_documents(my_files)
    if doc_chunks:
        print("\nInitializing BioBERT Embeddings (This will download the model on the first run)...")
        embeddings = HuggingFaceEmbeddings(model_name="emilyalsentzer/Bio_ClinicalBERT", encode_kwargs={'normalize_embeddings': True})
        print("Building the FAISS database...")
        vectorstore = FAISS.from_documents(doc_chunks, embeddings)
        vectorstore.save_local("faiss_index")
        print("Success! Database saved locally in the 'faiss_index' folder.")