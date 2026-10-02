import streamlit as st

st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖"
)
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }

    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 Rule-Based AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">A simple chatbot built using Python and predefined rules</div>',
    unsafe_allow_html=True
)

st.write("Ask me something or type **bye** to end the conversation.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Type your message...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    text = user_input.lower().strip()

    # Rule-based responses
    if "hello" in text or "hi" in text or "hey" in text:
        response = "Hello! 👋 How can I help you?"

    elif "your name" in text or "who are you" in text:
        response = "I am a Rule-Based AI Chatbot."

    elif "how are you" in text:
        response = "I'm doing great! 😊 Thanks for asking."

    elif "help" in text:
        response = "I can answer greetings, basic questions, and simple queries."

    elif "what can you do" in text or "your capabilities" in text:
        response = "I can respond to greetings, answer basic questions, and provide simple information."

    elif "thank you" in text or "thanks" in text:
        response = "You're welcome! 😊"

    elif "who created you" in text or "who made you" in text:
        response = "I was created as a Rule-Based Chatbot project."

    elif "internship" in text:
        response = "This chatbot is developed as part of an AI internship task."

    elif "bye" in text or "goodbye" in text or "exit" in text:
        response = "Goodbye! Have a great day! 👋"

    else:
        response = "Sorry, I don't understand that. Try typing 'help'."

    # Display bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)