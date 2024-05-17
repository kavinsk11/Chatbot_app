import streamlit as st
import streamlit as st
def login_page():
    st.title("Login to Chatbot")
    chat_id = st.text_input("Enter your Chat ID")
    if st.button("Login"):
        if chat_id:  # In real scenario, you'd validate this against a database
            st.session_state['logged_in'] = True
            st.session_state['chat_id'] = '13a040e6ba949f5c9fc3bb2e8c44941193b60bbbde1ff277e575d686da62af18'
        else:
            st.error("Please enter a valid Chat ID")

def main_page():
    st.title("ChatBot AI")
    chat_id = st.session_state['chat_id']
    st.write(f"Welcome, {chat_id}")
    
    # Chatbot Q/A functionality
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    user_input = st.text_input("You:", key="input")

    if st.button("Send"):
        if user_input:
            st.session_state['messages'].append(f"You: {user_input}")
            # Here you would send user_input to your chatbot model and get the response
            response = f"Chatbot: Echoing '{user_input}'"  # Mock response
            st.session_state['messages'].append(response)
            st.session_state['input'] = ''  # Clear input box

    for message in st.session_state['messages']:
        st.write(message)

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login_page()
    else:
        main_page()

if __name__ == "__main__":
    main()

