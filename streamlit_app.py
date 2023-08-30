import openai
import streamlit as st

# Set your OpenAI API key here
openai_api_key = "YOUR_OPENAI_API_KEY"

st.title("Language Learning Chatbot")

language_prompt = st.text_input("Enter the language you would like to learn:")
if not language_prompt:
    st.info("Please enter a language you would like to learn.")
    st.stop()

lesson_prompt = f"You have chosen to learn {language_prompt}. Let's start with the basics of {language_prompt} grammar and vocabulary."

st.session_state.messages = [{"role": "assistant", "content": "Welcome to your language learning lesson! I'm here to help you learn."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if st.session_state.messages[-1]["role"] == "assistant":
    st.session_state.messages.append({"role": "assistant", "content": lesson_prompt})

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Continue the conversation with GPT-3.5-Turbo
    openai.api_key = openai_api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )
    assistant_msg = response.choices[0].message
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg["content"]})
    st.chat_message("assistant").write(assistant_msg["content"])
