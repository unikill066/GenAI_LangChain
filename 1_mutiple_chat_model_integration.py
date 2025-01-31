# imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Translate English to Spanish"),
    HumanMessage(content="Today is Saturday and the match is tomorrow."),
]

# ChatGPT for OpenAI
gptmodel = ChatOpenAI(model="gpt-4o")
output = gptmodel.invoke(messages)
print(f"GPT response: {output.content}")

# Gemini from Google
geminimodel = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output = geminimodel.invoke(messages)
print(f"Gemini response: {output.content}")


# OUTPUT:
# GPT response: Hoy es sábado y el partido es mañana.
# Gemini response: Hoy es sábado y el partido es mañana.