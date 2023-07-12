import os
import openai
import urllib.request
import streamlit as st

# openai.api_key = os.getenv("OPENAI_API")
# secret_text = os.getenv("DALLE_TEXT")

openai.api_key = st.secrets["OPENAI_API"]
secret_text = st.secrets["DALLE_TEXT"]

prompt_generated = False
image_generated = False


def generate_prompt(model="text-davinci-003"):
    global prompt_generated
    response = openai.Completion.create(
        engine=model,
        prompt=secret_text,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.9
    )

    print("################# image prompt generated #################")
    prompt_generated = True
    return response.choices[0].text.split("\n\n")[1]


temp_prompt = generate_prompt()


def generate_image(prompt=temp_prompt):
    global image_generated
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    print("################# loading image #################")
    urllib.request.urlretrieve(response['data'][0]['url'], "temp.png")
    image_generated = True
