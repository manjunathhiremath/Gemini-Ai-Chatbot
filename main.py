import os 
import streamlit as st
from streamlit_option_menu import option_menu

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