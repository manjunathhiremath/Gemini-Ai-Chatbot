import os
import json
# from PIL import Image
import google.generativeai as genai

working_dir = os.path.dirname(os.path.abspath(__file__))

config_file = f"{working_dir}/config.json"
config_data = json.load(open(config_file))

# Loading the API key

Google_Api_key = config_data["GOOGLE_API_KEY"]

# Configuring google generativeai with api kay
genai.configure(api_key=Google_Api_key)

# Function For Chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_pro_model

# Function For image captioning ..
def gemini_pro_vision_response(prompt,image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt,image])
    result= response.text
    return result


# testing model 
# image = Image.open("alok.jpg")
# prompt = "Write short caption for this image"
# output = gemini_pro_vision_response(prompt, image)

# print(output)

# For Text Embedding 
def embedding_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(
        model = embedding_model,
        content = input_text,
        task_type = "retrieval_document"
    )
    embedding_list = embedding['embedding']
    return embedding_list

# output = embedding_model_response("who is Modi")
# print(output)

# Ask me Anything Section ...
def ask_me_anything(user_prompt):
    gemini__pro_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini__pro_model.generate_content(user_prompt)
    result = response.text
    return result

# For testing
output = ask_me_anything("what is machine learning")
print(output)