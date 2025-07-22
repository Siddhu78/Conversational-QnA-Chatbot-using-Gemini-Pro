from dotenv import load_dotenv          ### command to run stramlit app- streamlit run qachat.py ###
load_dotenv()

import streamlit as st  
import os
import google.generativeai as genai

#  Load API key from .env file securely
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#  Correct model name
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask the Question")

if submit and input:
    response_text = get_gemini_response(input)

    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    st.write(response_text)
    st.session_state['chat_history'].append(("Bot", response_text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
