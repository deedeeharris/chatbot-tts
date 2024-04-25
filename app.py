import streamlit as st
import time

# Set page configuration
st.set_page_config(layout="wide")

# Define the avatar video URL
avatar_video_url = "sacks.mp4"

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

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

with col2:
    st.title("Avatar")
    st.video(avatar_video_url, start_time=0, loop_start=0, loop_end=0, format="mp4", width=300, height=300)
