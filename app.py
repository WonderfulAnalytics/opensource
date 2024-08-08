import streamlit as st
import requests
from requests.exceptions import ConnectionError

# Define the system prompt
system_prompt = (
    "You are a helpful assistant. "
    "Answer questions with concise and clear answers. "
    "Use simple words and three sentences maximum and keep the answer concise. "
    "Use bullet points when needed."
)

# Define the prompt template
prompt = {
    "system": system_prompt,
    "user": "Question: {question}"
}

# Streamlit app
st.title("Talk to Google Gemma 2B")
st.write("Ask a question and get a concise, bullet-pointed answer:")

# Input text box
question = st.text_input("What question do you have in mind?")

if question:
    try:
        # Send the request to the endpoint
        response = requests.post(
            url="http://localhost:11434/generate",
            json={"question": question},
            headers={"Content-Type": "application/json"}
        )

        # Check the response status
        if response.status_code == 200:
            # Get the generated response
            generated_response = response.json()["response"]
            st.write(f"Response: {generated_response}")
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except ConnectionError:
        st.error("Failed to connect to the model server. Please ensure the server is running and accessible.")
    except Exception as e:
        st.error(f"An error occurred: {e}")