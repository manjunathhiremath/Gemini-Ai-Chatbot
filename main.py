import os 

import streamlit as st
from streamlit_option_menu import option_menu

from utills import load_gemini_pro_model

working_dir = os.path.dirname(os.path.abspath(__file__))

print(working_dir)

# Setting up the page configuration

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🧠",
    layout="centered")

with st.sidebar:
    selected =option_menu(menu_title= "  Gemini AI Chatbot",
                          options=["Chatbot","Image Captioning","Embedded Text","Ask Me Anything"],
                          menu_icon="robot",icons=['chat-dots-fill','image-fill','textarea-t',
                                                   'patch-question-fill'],

                        default_index=0             
                          )
    
# Function to translate role between gemini pro model and streamlit terminology

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role
    
if selected == "Chatbot":

    model = load_gemini_pro_model()

    if 'chat_session' not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("🤖 Chatbot")

    # For displaying chat hhistory
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # User input
    user_prompt = st.chat_input("Ask Gemini Pro .....")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display the gemini response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)