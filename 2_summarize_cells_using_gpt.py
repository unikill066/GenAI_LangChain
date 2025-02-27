# imports
from dotenv import load_dotenv
import os, logging, pandas as pd
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()  # load environment variables from .env file

# logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("summarization.log"),
        logging.StreamHandler()
    ]
)

llm = ChatOpenAI(model="gpt-3.5-turbo")
system_message = SystemMessage(content="You are a helpful assistant that summarizes text. Your name is Mittens.")

# # recursive loop
# while True:
#     query = input("Human: ")
#     if query.lower() == "quit":
#         break
#     conversion_list.append(HumanMessage(content=query))
#     result = llm.invoke(conversion_list)
#     conversion_list.append(AIMessage(content=result.content))
#     print(f"AI: {result.content}")

logging.info(" * Hi, I am Mittens and I can summarize text *  (  ^ _ ^) ~ Meow")

def summarize_text(text: str) -> str:
    """
    Summarizes text using the LLM model.
    
    :param text: The input text to summarize.
    :return: The summarized text.
    """
    try:
        messages = [system_message, HumanMessage(content=f"Please summarize the following text:\n\n{text}")]
        result = llm.invoke(messages)
        return result.content
    except Exception as e:
        logging.error(f"Summarization failed: {e}")
        return text

def summarize_if_long(text: str) -> str:
    """
    Summarizes text only if it exceeds 30 words.
    
    :param text: The input text.
    :return: Summarized text if it exceeds 30 words; otherwise, original text.
    """
    if isinstance(text, str) and len(text.split()) > 30:
        return summarize_text(text)
    return text

def process_excel_file(input_file: str, output_file: str):
    """
    Reads an Excel file, summarizes long text entries, and writes the updated data back.
    
    :param input_file: Path to the input Excel file.
    :param output_file: Path to save the processed file.
    """
    try:
        logging.info(f"Reading dataset: {input_file}")
        df = pd.read_excel(input_file)
        text_columns = df.select_dtypes(include=["object"]).columns

        if text_columns.empty:
            logging.warning("No text columns found for summarization.")

        for col in text_columns:
            logging.info(f"Processing column: {col}")
            df[col] = df[col].apply(lambda x: summarize_if_long(x) if pd.notnull(x) else x)
        df.to_excel(output_file, index=False)
        logging.info(f"Summarization complete. File saved as: {output_file}")

    except Exception as e:
        logging.error(f"Processing failed: {e}")


input_excel, output_excel = "CPSP Rodent Model Spreadsheet.xlsx", "CPSP_Rodent_Model_Summarized.xlsx"

# actual run
process_excel_file(input_excel, output_excel)