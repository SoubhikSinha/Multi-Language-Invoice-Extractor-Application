from dotenv import load_dotenv 

load_dotenv() # To load environment variable from the ".env" file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai


# Configuring the API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Model Vision
model = genai.GenerativeModel('gemini-2.0-flash') # Using the "gemini-2.0-flash" model

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file): # Converting the uploaded image into bytes
    if uploaded_file is not None:
        # Reaidng the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded.")


# Streamlit Application Set-up (INITIALIZATION)
st.set_page_config(page_title = "Multi-Language Invoice Extractor (powered by Google Gemini)")
st.header("Multi-Language Invoice Extractor (powered by Google Gemini)")
input = st.text_input("Input Prompt : ", key="input")
uploaded_file = st.file_uploader("Choose an Image of an INVOICE : ", type = ["jpg", "jpeg", "png"]) # File Uploader

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file) # Open and store the uploaded file
    st.image(image, caption="Uploaded Image.", use_container_width=True) # Displaying the uploaded image

submit = st.button("Prompt Response for INVOICE")


# Input Prompt given to the LLM
input_prompt = """
You are an expert in understanding invoices. We will upload an image as invoice
and you will have to answer any question based on the uploaded invoice image.
"""

# If the submit button is clicked
if submit:
    image_data = input_image_details(uploaded_file=uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is : ")
    st.write(response)