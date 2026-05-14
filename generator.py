import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from retriever import retriever,vectorstore

load_dotenv()

GROQ = os.getenv("GROQ_API_KEY")

os.environ["GROQ_API_KEY"] = GROQ
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

system_prompt = (
    "You are MediAssist, a medical information assistant.\n"
    "Use the following pieces of retrieved context to answer the user's question.\n"
    "If you don't know the answer based on the context, say that you don't know. Do not hallucinate.\n"
    "CRITICAL: You MUST cite the source document and page number for every piece of information used (e.g., [Files/Obesity1.pdf, Page 3]).\n"
    "CRITICAL: At the very end of your response, you MUST append this exact text:\n"
    "'MEDICAL DISCLAIMER: This information is for educational purposes only and should not replace professional medical advice.'\n\n"
    "Context:\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

