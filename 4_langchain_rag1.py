# imports
from langchain import hub
import os, sys, getpass, bs4
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain.chat_models import init_chat_model
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# CREATE A .env FILE AND ADD ALL THE NECESSARY KEYS TO THAT FILE
load_dotenv()  # load environment variables from .env file

llm = init_chat_model("gpt-4o-mini", model_provider="openai")  # chat model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")  # embedding model
vector_store = InMemoryVectorStore(embeddings)  # vector-store




loader = WebBaseLoader(
    web_paths=("https://inturinikhilnageshwar.netlify.app/",
               "https://www.linkedin.com/in/nikhilinturi/",
               "https://github.com/unikill066"),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)

docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

_ = vector_store.add_documents(documents=all_splits)  # index chunks

