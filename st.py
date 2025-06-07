import streamlit as st

# 🧠 Smarter chatbot logic
def simple_bot_response(user_input):
 user_input = user_input.lower()

 if "hello" in user_input or "hi" in user_input:
 return "👋 Hi there! How can I help you today?"
 elif "how are you" in user_input:
 return "😊 I'm doing great! Hope you're well too."
 elif "your name" in user_input:
 return "🤖 I'm a logic-based chatbot created with Streamlit!"
 elif "what can you do" in user_input or "help" in user_input:
 return "📚 I can answer greetings, tell you my name, chat with you, and more!"
 elif "bye" in user_input or "goodbye" in user_input:
 return "👋 Bye! Have a great day ahead!"
 elif "thanks" in user_input or "thank you" in user_input:
 return "🙏 You're welcome!"
 elif "joke" in user_input:
 return "😂 Why did the computer get cold? Because it left its Windows open!"
 elif "who made you" in user_input:
 return "🛠️ I was made by someone learning Streamlit with love!"
 else:
 return "🤔 I'm not sure how to respond to that. Try 'joke', 'hello', 'bye', or 'help'."

# 🎨 App UI
st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")
st.title("🤖 Simple Chatbot (No API Required)")
st.caption("This chatbot uses rule-based logic and works fully offline!")

# 🧠 Chat history
if "chat_history" not in st.session_state:
 st.session_state.chat_history = []

# 🧹 Clear chat button
st.sidebar.button("🧹 Clear Chat", on_click=lambda: st.session_state.chat_history.clear(), key="clear_chat")

# 🎯 Optional quick buttons
st.markdown("### 👉 Quick Questions")
col1, col2, col3 = st.columns(3)
with col1:
 if st.button("Tell me a joke 🤣", key="joke"):
 st.session_state.chat_history.append(("user", "Tell me a joke"))
 st.session_state.chat_history.append(("bot", simple_bot_response("Tell me a joke")))
with col2:
 if st.button("What's your name? 🤖", key="name"):
 st.session_state.chat_history.append(("user", "What is your name?"))
 st.session_state.chat_history.append(("bot", simple_bot_response("What is your name?")))
with col3:
 if st.button("Say hi 👋", key="sayhi"):
 st.session_state.chat_history.append(("user", "Hi"))
 st.session_state.chat_history.append(("bot", simple_bot_response("Hi")))

# 💬 Chat input
user_input = st.chat_input("Type your message here...", key="chat_input")

# 🧠 Process chat input
if user_input:
 st.session_state.chat_history.append(("user", user_input))
 response = simple_bot_response(user_input)
 st.session_state.chat_history.append(("bot", response))

# 💬 Display chat history
for sender, msg in st.session_state.chat_history:
 with st.chat_message("user" if sender == "user" else "assistant"):
 st.markdown(msg)
