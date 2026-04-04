import os 
from dotenv import load_dotenv
from crewai import Agent,LLM
load_dotenv()

groq_llm=LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv('GROQ_API_KEY')
)

# Router Agent
router_agent=Agent(
    role="router",
    goal='Route the user query to either store or web search based on content relevance.',
    backstory=(
        "You are an expert at arouting a user question to a vector store or web search. "
        "Use the vector store for questions related to the knowledge base documents. "
        "Use web search for current events or information not found in the documents. "
        ),
    verbose=True,
    llm=groq_llm
)

# Retriver Agent 
retriver_agent=Agent(
    role="retriever",
    goal='Retrieve relevant information from the vector store or web search to answer the query. ',
    backstory=(
        "You are an expert reasearcher. Use the provided tools to extract the most relevatn information based on the user's question. "
    ),
    verbose=True,
    llm=groq_llm 
)

# Answer Grader Agent 
grader_agent=Agent(
    role='Answer Grader',
    goal='Filter out irrelevant retrievals and ensure the documents are relevant to the user query. ',
    backstory=(
        "You are a strict grader assesing the relevance of retrieved documents to a user question."   
        "If the document contains keywords or semantic meaning related to the question, grade it as relevant. "
        "Otherwise, grade it as irrelevant. Only return relevant documents to the user. "
        ),
    verbose=True,
    llm=groq_llm
)

# Hallucination Agent 
hallucination_grader_agent=Agent(
    role='Hallucination Grader',
    goal='Filter out hallucinations and ensure the final answer is perfectly grounded in the retrieved facts. ',
    backstory=(
        "You are an audiotr assesing whether an AI's generated answer is supported by a set of retrieved facts.  "
        "If the answer is factually correct and directly addresses the question, grade it as accurate. "
        "You must ensure the answer does not contain any fabricated information. "
        
    ),
    verbose=True,
    llm=groq_llm
)

#Answer Generator Agent 
answer_generator_agent=Agent(
    role='Answer Generator',
    goal='Generate a concise, accurate and highly readable final answer based on the verified information.  ',
    backstory=(
        "You are an expert synthesizer, you take graded, verified facts and synthesize them into a clear, direct answer."
    ),
    verbose=True,
    llm=groq_llm
)