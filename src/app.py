import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# messages = []

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit" or user_input.lower() == "0":
#         break

#     messages.append({"role": "user", "content": user_input})

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",   
#         messages=messages
#     )

#     responseMessage = response.choices[0].message["content"]

#     messages.append({"role": "assistant", "content": responseMessage})

#     print("AI:", responseMessage)

st.title("ChatBot personal")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola! soy chatGPT, ¿En que puedo ayudarte?"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("role").write(user_input)

    