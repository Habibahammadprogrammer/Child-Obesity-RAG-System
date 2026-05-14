# Knowledge Base AI - Agentic RAG Pipeline
This repository contains an Agentic Retrieval-Augmented Generation (RAG) application developed for the 8th-semester Knowledge Base AI project. It leverages CrewAI to coordinate a multi-agent system that intelligently routes queries, parses course PDFs, performs real-time web searches, and validates responses to ensure zero hallucinations.

# System Architecture
The pipeline employs five specialized agents to handle the RAG lifecycle:

Router: Directs queries to either the internal Knowledge Base (PDFs) or Web Search.

Retriever: Extracts relevant context using semantic search.

Grader: Evaluates the quality and relevance of retrieved documents.

Hallucination Grader: Verifies that the answer is strictly grounded in the provided context.

Generator: Synthesizes the final response into a clear, concise answer.

# Prerequisites
Python 3.12: (Strict requirement; higher versions may cause dependency conflicts).

Groq API Key: For high-speed LLM inference. Get it here.

Tavily API Key: For AI-optimized web searching. Get it here.
 Knowledge Base:
Create a folder named Knowledge_Base in the root directory and place all the necessary course PDFs inside it. The agents will automatically read and index all files in this directory.
## Installation & Setup
1. Clone the repository
   ```bash
   git clone https://github.com/Habibahammadprogrammer/Child-Obesity-RAG-System
   cd Child-Obesity-RAG-System
   ```
2. Set up enviroment
 ```bash
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
   ```
3. Configuration File
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
## Project Structure
tools.py: Configures DirectorySearchTool (RAG) and TavilySearchResults.

agents.py: Defines the CrewAI personas and their specific LLM configurations.

tasks.py: In Mapping agent goals to actionable execution steps.

main.py: The entry point that initializes the Crew and executes the process.
# Roadmap
[x] Agent persona definitions and Tool integration.

[ ] Finalize task logic and output specifications in tasks.py.

[ ] Implement the execution loop and user interface in main.py.

[ ] Integrate PDF Knowledge Base for course-specific queries.
Author: Habiba Hammad
5. 
