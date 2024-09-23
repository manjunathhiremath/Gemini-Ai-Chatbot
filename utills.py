import os
import json

import google.generativeai as genai

working_dir = os.path.dirname(os.path.abspath(__file__))

config_file = f"{working_dir}/config.json"
config_data = json.load(open(config_file))

# Loading the API key

Google_Api_key = config_data["GOOGLE_API_KEY"]

# Configuring google generativeai with api kay
genai.configure(api_key=Google_Api_key)

def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-pro")
    return gemini_pro_model