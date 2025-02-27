# imports
import os, firebase_admin
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from firebase_admin import credentials, firestore
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()  # load environment variables from .env file


# Load Firebase service account key
cred = credentials.Certificate("extreme-clone-449518-h8-firebase-adminsdk-fbsvc-2d9feef05c.json")
firebase_admin.initialize_app(cred)

client = firestore.client()  # initialize firestore-client

PROJECT_ID = "extreme-clone-449518-h8"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "testing"

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Current Chat History:", chat_history.messages)

llm = ChatOpenAI()

print("Start chatting with the AI. Type 'exit' to quit.")

while True:
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    chat_history.add_user_message(human_input)
    llm_output = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(llm_output.content)
    print(f"AI: {llm_output.content}")