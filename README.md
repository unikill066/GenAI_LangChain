# GenAI_LangChain

## LangChain & LangGraph Examples

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/) [![LangChain](https://img.shields.io/badge/langchain-v0.3.25-orange)](https://github.com/hwchase17/langchain) [![LangGraph](https://img.shields.io/badge/langgraph-v0.4.8-green)](https://github.com/langgraph/langgraph)

A curated collection of Python scripts showcasing key patterns and integrations with **LangChain** and **LangGraph**. These examples cover everything from basic chat invocations and prompt templates to Retrieval-Augmented Generation (RAG), recursive agent loops, data summarization, Firebase-backed chat history, and simple graph-based workflows.

## Table of Contents
* Scripts Overview
  * [0\_langchain\_basics.py](#0_langchain_basicspy)
  * [1\_mutiple\_chat\_model\_integration.py](#1_mutiple_chat_model_integrationpy)
  * [1\_rag\_basics.py](#1_rag_basicspy)
  * [2\_rag\_basics.py](#2_rag_basicspy)
  * [2\_recursive\_chat\_with\_llms.py](#2_recursive_chat_with_llmspy)
  * [2\_summarize\_cells\_using\_gpt.py](#2_summarize_cells_using_gptpy)
  * [2\_summarize\_sheets\_using\_gpt.py](#2_summarize_sheets_using_gptpy)
  * [3\_recursive\_chat\_with\_llms\_firebase.py](#3_recursive_chat_with_llms_firebasepy)
  * [4\_langchain\_rag1.py](#4_langchain_rag1py)
  * [5\_langgraph\_simple\_graph.py](#5_langgraph_simple_graphpy)


## Prerequisites
* Python **3.10+**
* A valid LLM API key (e.g., **OPENAI\_API\_KEY**, **ANTHROPIC\_API\_KEY**, **GOOGLE\_API\_KEY**) in a `.env` file
* (Optional) Firebase service account JSON for Firestore examples

## Installation
1. **Clone the repository**

   ```bash
   git clone https://github.com/unikill066/GenAI_LangChain.git
   cd GenAI_LangChain
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   .\.venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:

   ```bash
   OPENAI_API_KEY="your_openai_key"
   ANTHROPIC_API_KEY="your_anthropic_key"
   GOOGLE_API_KEY="your_google_key"
   ```

   (Optionally, add `GOOGLE_APPLICATION_CREDENTIALS` for Firebase.)

## Usage
Each script can be run directly with Python. For example:

```bash
python 0_langchain_basics.py
```

Follow on-screen logs and prompts. Some scripts require input files or directories:
* RAG basics: place `.docx` resumes under `resumes/` or text books under `books/`
* Summarization: ensure the target Excel or CSV file is in the working directory
* Firebase chat: provide `service-account.json` and set `GOOGLE_APPLICATION_CREDENTIALS`

## Scripts Overview
### 0\_langchain\_basics.py

* Demonstrates direct calls to **OpenAI** via `langchain_openai.ChatOpenAI`
* Uses `ChatPromptTemplate` for templated System + Human messages

### 1\_mutiple\_chat\_model\_integration.py

* Shows integration with **OpenAI**, **Anthropic**, and **Google Gemini** chat models
* Compares translations across different providers

### 1\_rag\_basics.py

* Loads a `.docx` resume, splits text into chunks, and builds a **Chroma** vector store
* Performs basic RAG retrieval based on similarity threshold

### 2\_rag\_basics.py

* Reads multiple `.txt` files from a `books/` directory with metadata
* Splits, embeds via `OpenAIEmbeddings`, and persists a **Chroma** store

### 2\_recursive\_chat\_with\_llms.py

* Implements a REPL loop storing conversation context
* Demonstrates recursive chat with `ChatOpenAI` and customizable exit command

### 2\_summarize\_cells\_using\_gpt.py

* Summarizes long text in Excel cells up to a word threshold
* Uses **pandas** and logs progress to a file + console

### 2\_summarize\_sheets\_using\_gpt.py

* Extends cell summarization to multi-sheet Excel files
* Writes results to a new summarized workbook

### 3\_recursive\_chat\_with\_llms\_firebase.py

* Persists chat history to **Firestore** using `FirestoreChatMessageHistory`
* Demonstrates end-to-end loop with human input and AI responses

### 4\_langchain\_rag1.py

* Uses **WebBaseLoader** to scrape web pages, split text, and embed chunks
* Indexes data into an in-memory vector store and builds a **LangGraph** graph

### 5\_langgraph\_simple\_graph.py

* Defines a minimal `StateGraph` with conditional edges based on random logic
* Illustrates node-based state transitions in **LangGraph**

## License
This project is licensed under the [MIT License](LICENSE).