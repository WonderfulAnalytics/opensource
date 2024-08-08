from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


system_prompt = (
    "You are a helpful assistant. "
    "Answer questions with concise and clear answerss"
    "Use simple words and three sentences maximum and keep the answer concise "
    "Use bullet points when needed."
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("user", "Question: {question}")
    ]
)

# Initialize the Ollama Llama2 model with streaming callback
llm = Ollama(model="gemma:2b", base_url="http://localhost:11434")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit app
st.title("Talk to Google Gemma 2B")
st.write("Ask a question and get a concise, bullet-pointed answer:")

# Input text box
question = st.text_input("What question do you have in mind?")

if question:
    # Get response
    response = chain.invoke({"question": question})
    st.write(f"Response: {response}")
        