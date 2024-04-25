import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory

# Load the OpenAI API key from the Streamlit secrets
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize the OpenAI LLM
llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

# Initialize the conversation chain with a window-based memory
conversation = ConversationChain(
    llm=llm,
    memory=ConversationBufferWindowMemory(k=5, return_messages=True),
    verbose=True
)

# Set up the Streamlit app
st.set_page_config(layout="wide")

# Define the avatar video URL
video_file = open('sacks.mp4', 'rb')
sacks_video_bytes = video_file.read()

# Render the chatbox and avatar
col1, col2 = st.columns(2)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with col1:
    st.title("Chatbot")
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate a response using the conversation chain
        response = conversation.predict(input=prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

with col2:
    st.markdown(video_html, unsafe_allow_html=True)
