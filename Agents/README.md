# LangGraph Agents

Repository showcasing agent-based applications built with **LangGraph**. Each notebook in the **Agents** directory implements a distinct agent pattern—from a simple conversational bot to a retrieval-augmented document drafter.



## Table of Contents

* [Overview](#overview)
* [Repository Structure](#repository-structure)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [Agents](#agents)
* [Requirements](#requirements)



## Overview

This project demonstrates how to leverage LangGraph for constructing stateful, agent-driven pipelines in Python. You’ll find five Jupyter notebooks, each focusing on a specific agent implementation:

1. **Simple Bot**: A basic conversational agent with no memory.
2. **Simple Bot with Persistent Memory**: Extends the simple bot to store and recall conversation history.
3. **React Agent**: Illustrates a reactive agent pattern that responds to events.
4. **Drafter Agent**: A multi-step drafting agent for structured document creation.
5. **RAG Agent**: A retrieval-augmented generation agent combining LangGraph with a vector store.



## Repository Structure

```
LangGraph-Agents/
├── Agents/                            # agent notebooks
│   ├── simple_bot_langgraph_1.ipynb
│   ├── simple_bot_persistent_memory_langgraph_2.ipynb
│   ├── react_agent_langgraph_3.ipynb
│   ├── drafter_agent_langgraph_4.ipynb
│   └── rag_langgraph_5.ipynb
└── README.md
```

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/unikill066/GenAI_LangChain.git
   cd Agents
   ```
2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .\.venv\Scripts\activate   # Windows
   ```

3. **Set environment variables** (if needed)

   ```bash
   echo "OPENAI_API_KEY=your_key" > .env
   ```



## Usage

* Launch JupyterLab or Jupyter Notebook:

  ```bash
  jupyter lab
  ```
* Open any notebook in **Agents/** and run cells sequentially.
* Modify parameters (e.g., prompts, memory settings) to experiment with agent behaviors.



## Agents

### 1. Simple Bot

A minimal LangGraph agent that processes user input and returns a fixed response.

### 2. Simple Bot with Persistent Memory

Extends the simple bot by storing conversation turns in a persistent state graph.

### 3. React Agent

Shows how to implement an event-driven agent that triggers nodes in response to external stimuli.

### 4. Drafter Agent

A multi-stage pipeline that guides structured document creation (e.g., outlines, sections, final draft).

### 5. RAG Agent

Integrates a vector database lookup into the LangGraph workflow for retrieval-augmented text generation.



## Requirements

**Core dependencies:**

* Python 3.8+
* jupyterlab
* langgraph
* langchain
* openai
* python-dotenv
* chromadb

Feel free to explore, modify, and extend these examples to build your own LangGraph-powered agents!

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citations:
Source: https://github.com/iamvaibhavmehra/LangGraph-Course-freeCodeCamp