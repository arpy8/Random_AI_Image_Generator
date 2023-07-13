import time
import streamlit as st
from brain import generate_image, temp_prompt, prompt_generated, image_generated

######################### STREAMLIT #########################


st.set_page_config(page_title="RandAi")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

prompt_loading_text = st.empty()
prompt_loading_text.caption("# Cooking an amazing prompt...🤩")

prg = st.empty()

prg1 = prg.progress(0)
for i in range(100):
    time.sleep(0.12)
    prg1.progress(i + 1)
    if prompt_generated:
        break

prompt_loading_text.caption("# Generating a beautiful image...✨")

prg1 = prg.progress(0)
for i in range(100):
    time.sleep(0.15)
    prg1.progress(i + 1)
    if image_generated:
        break

prompt_loading_text.caption("# Finalizing everything...⚙️")

prg1 = prg.progress(0)
for i in range(100):
    time.sleep(0.1)
    prg1.progress(i + 1)
prg.empty()

prompt_loading_text.caption("#  Here's your amazing ai generated image 💘")

generate_image()
st.image("temp.png")

if temp_prompt.split()[0] == "Create":
    temp_prompt = temp_prompt.replace("Create", "")
st.caption(f"""{temp_prompt.capitalize()}""")

