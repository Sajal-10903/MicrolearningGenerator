from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0, openai_api_key=api_key)
try:
    response = llm.invoke("Hello, this is a test.")
    print("API key works! Response:", response)
except Exception as e:
    print("API error:", e)