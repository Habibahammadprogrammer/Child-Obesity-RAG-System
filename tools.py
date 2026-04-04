import os
from dotenv import load_dotenv
from crewai_tools import DirectorySearchTool
from langchain_community.tools.tavily_search import TavilySearchResults
from crewai import tool
# Load the environment variables from your .env file
load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# Initialize the tool to search through the entire directory of PDFs
# We configure it to use Groq for the language model and HuggingFace for free embeddings
rag_tool = DirectorySearchTool(
    directory='./Knowledge_Base',
    config=dict(
        llm=dict(
            provider="groq",
            config=dict(
                model="llama-3.3-70b-versatile", 
                api_key=GROQ_API_KEY
            ),
        ),
        embedder=dict(
            provider="huggingface",
            config=dict(
                model="BAAI/bge-small-en-v1.5"
            ),
        ),
    )
)
@tool 
def web_search_tool(query: str) -> str:
    """
    A tool to perform web search using the SerpAPI.
    """
    web_search_tool=TavilySearchResults(k=3)
    return web_search_tool.run(query)