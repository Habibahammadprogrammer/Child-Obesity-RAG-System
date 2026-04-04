# Knowledge Base AI - Agentic RAG Pipeline

This repository contains an Agentic Retrieval-Augmented Generation (RAG) application built for the 8th-semester Knowledge Base AI project. The pipeline uses CrewAI to coordinate multiple AI agents that intelligently route user queries, search through course PDFs, perform web searches, grade the retrieved context, and synthesize a final answer without hallucinations.

## Prerequisites
Before you begin, ensure you have the following installed and set up:
* **Python 3.12** (Strict requirement. Python 3.14 will fail to install certain dependencies).
* **Groq API Key:** Free API key from the [Groq Cloud Console](https://console.groq.com/keys).
* **Tavily API Key:** Free API key from [Tavily](https://tavily.com/).

## Installation Steps
**1. Clone the repository:**
```powershell
git clone [https://github.com/Habibahammadprogrammer/Agentivc_RAG](https://github.com/Habibahammadprogrammer/Agentivc_RAG)
cd Agentivc_RAG
```
**2. Create Virtual Enviroment**
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
## Configuration 
**1. Environment Variables:**
Create a file named exactly .env in the root directory of the project and add your API keys:

- GROQ_API_KEY=your_groq_api_key_here
- TAVILY_API_KEY=your_tavily_api_key_here
(Note: The .env file is excluded from GitHub for security. Never commit your API keys).



## Project Structure & Status
This project is split into four main components:

- tools.py (Completed): Configures the DirectorySearchTool (for parsing PDFs via Groq/HuggingFace embeddings) and the web_search_tool (via Tavily).

- agents.py (Completed): Defines the 5 CrewAI personas: Router, Retriever, Answer Grader, Hallucination Grader, and Answer Generator.

- tasks.py (To Do): Needs to define the specific instructions, expected outputs, and tool assignments for each agent.

- main.py (To Do): Needs to assemble the tools, agents, and tasks into a unified Crew and define the execution logic to run user queries.




2. Knowledge Base:
Create a folder named Knowledge_Base in the root directory and place all the necessary course PDFs inside it. The agents will automatically read and index all files in this directory.
