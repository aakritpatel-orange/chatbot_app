import streamlit as st
from openai import OpenAI
import os

# App config
st.set_page_config(page_title="Obfuscated Engineering Manager Bot", layout="centered")
st.title("🧠 Engineering Manager (Obfuscated Mode) Chatbot")

# Sidebar for API key
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
st.sidebar.markdown("🚀 This bot replies in ultra-technical, jargon-heavy language.")

# Create OpenAI client dynamically
client = None
if api_key:
    client = OpenAI(api_key=api_key)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a chatbot that role-plays as a hardcore, ultra-technical, overly complex engineering manager. "
                "You respond in highly technical jargon, using complex and obscure language, unnecessary abbreviations, "
                "and engineering slang. You never simplify. Every reply must sound like a tech memo from a cryptic software "
                "architect. Use long sentences, nested technical terms, and buzzwords. Never explain yourself. Stay in character."
            )
        }
    ]

# User input
user_input = st.chat_input("Type your message here...")

# Send user message and get response
if user_input and client:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"API Error: {e}")

# Display the chat messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
