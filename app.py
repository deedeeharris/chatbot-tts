import streamlit as st
import time

# Set page configuration
st.set_page_config(layout="wide")

# Define CSS styles for a more polished look
st.write(
    """
    <style>
        body {
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            font-family: sans-serif;
        }

        .chat-container {
            display: flex;
            flex-direction: column;
            height: calc(100vh - 80px);
            overflow-y: auto;
            padding: 20px;
        }

        .message {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .user-message {
            justify-content: flex-start;
            background-color: #e0e0e0;
            padding: 10px 20px;
            border-radius: 5px;
        }

        .assistant-message {
            justify-content: flex-end;
            background-color: #d0f0c0;
            padding: 10px 20px;
            border-radius: 5px;
        }

        .avatar-container {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            overflow: hidden;
            margin: 20px auto;
        }

        .avatar-video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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

    # Chat message container with styled div
    chat_container = st.empty()

    # Display chat messages from history
    for message in st.session_state.messages:
        with chat_container.subheader(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message
        with chat_container.subheader("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response
        with chat_container.subheader("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


with col2:
    st.title("Avatar")

    # Avatar container with styled div
    avatar_container = st.empty()

    # Continuously display the video using MediaStream
    def play_video():
        with avatar_container.video(sacks_video_bytes):
            time.sleep(1/24)  # Simulate video playback at 24 FPS

    st.sidebar.write("**Loop Video**")
    video_loop_checkbox = st.sidebar.checkbox("Enable Continuous Playback")

    if video_loop_checkbox:
        play_video()

