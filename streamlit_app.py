import streamlit as st

class SimpleAgent:
    def respond(self, message: str) -> str:
        return f"You said: {message}"

def main():
    st.title("Personal Site Chatbot")
    st.write("This is a simple Streamlit interface for the personal site agent.")

    if 'agent' not in st.session_state:
        st.session_state.agent = SimpleAgent()

    user_input = st.text_input("Say something", "")
    if user_input:
        response = st.session_state.agent.respond(user_input)
        st.write(response)

if __name__ == '__main__':
    main()
