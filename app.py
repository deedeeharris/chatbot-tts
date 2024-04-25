import streamlit as st
import time

# Set page configuration
st.set_page_config(layout="wide")

# Define the avatar video URL
avatar_video_url = "sacks.mp4"

# Render the chatbox and avatar
col1, col2 = st.columns(2)

with col1:
    st.title("Chatbot")
    with st.chat_message("user", avatar="https://example.com/user_avatar.png"):
        user_input = st.text_input("Enter your message")
    st.button("Send")

with col2:
    st.title("Avatar")
    st.video(avatar_video_url, start_time=0, loop_start=0, loop_end=0, format="mp4", width=300, height=300)
