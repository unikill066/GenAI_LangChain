# imports
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# CREATE A .env FILE AND ADD ALL THE NECESSARY KEYS TO THAT FILE
load_dotenv()  # load environment variables from .env file

# 1. invoking a OpenAI model directly
llm = ChatOpenAI(model="gpt-3.5-turbo")
llm.invoke("Hello, world!")

# 2. chatmodels are instances of langchain rannables
# passing messages list to invoke OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage("Translate the following from English into Spanish"),
    HumanMessage("Today is Thursday and the match is tomorrow!"),
]

output = llm.invoke(messages)
# output is a dictionary and contains response metadata
print(output.content)

# 3. invoking OpenAI model using prompt template
system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Spanish", "text": "Today is Friday and the match is tomorrow!"})
print(prompt.to_messages())

llm = ChatOpenAI(model="gpt-3.5-turbo")
output = llm.invoke(prompt)
print(output.content)


# OUTPUT:
# ¡Hoy es jueves y el partido es mañana!
# [SystemMessage(content='Translate the following from English into Spanish', additional_kwargs={}, response_metadata={}), HumanMessage(content='Today is Friday and the match is tomorrow!', additional_kwargs={}, response_metadata={})]
# ¡Hoy es viernes y el partido es mañana!