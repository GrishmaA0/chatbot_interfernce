import streamlit as st
import openai

# 🔐 Set your OpenAI API key
openai.api_key = ""  # Replace this with your actual API key

# 🎨 Optional basic styling
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Title and Clear Chat button
st.title("🤖 AI Chatbot")

if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()

# 🧠 Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🙋 Greeting if first load
if not st.session_state.messages:
    st.markdown("👋 **Hi! I'm your chatbot. How can I help you today?**")

# 🧠 Get bot response using OpenAI
def get_bot_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a professional and friendly assistant."},
            *[
                {"role": msg["role"], "content": msg["text"]}
                for msg in st.session_state.messages
            ],
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content

# 📥 Chat input field
user_input = st.chat_input("Type your message here...")

# ✅ Input validation and processing
if user_input and user_input.strip() != "" and len(user_input) < 500:
    # Add user message
    st.session_state.messages.append({"role": "user", "text": user_input})

    # Spinner while thinking
    with st.spinner("🤔 Thinking..."):
        bot_reply = get_bot_response(user_input)
        st.session_state.messages.append({"role": "assistant", "text": bot_reply})
elif user_input:
    st.warning("⚠️ Please enter a valid message (not empty or too long).")

# 💬 Display full chat history with avatars
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["text"])
 
 
