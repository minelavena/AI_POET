#pip install python-dotenv
#pip install langchain-openai
#pip install streamlit


from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

subjenct = "AI"
result = chat_model.invoke(subject + "ai에 대한 시를 써줘")
print(result.content)

import streamlit as st

st.title("인공지능 시인")