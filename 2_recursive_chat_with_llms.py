# imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()  # load environment variables from .env file

conversion_list, llm = list(), ChatOpenAI(model="gpt-3.5-turbo")
system_message = SystemMessage(content="Translate english to spanish.")
conversion_list.append(system_message)

print(" * This agent can translate English to Spanish *  (  ^ _ ^) ~ Meow")

# recursive loop
while True:
    query = input("Human: ")
    if query.lower() == "quit":
        break
    conversion_list.append(HumanMessage(content=query))
    result = llm.invoke(conversion_list)
    conversion_list.append(AIMessage(content=result.content))
    print(f"AI: {result.content}")

# prints all the snapshot of messages during the the converstation
# print(conversion_list)