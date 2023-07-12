from time import sleep
import streamlit as st
from stqdm import stqdm
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
prompt_loading_text.caption("# Cooking a prompt...")
for _ in stqdm(range(50)):
    sleep(0.3)
    if prompt_generated:
        break

prompt_loading_text.caption("# Generating a beautiful image")
for _ in stqdm(range(50)):
    sleep(0.3)
    if image_generated:
        break

prompt_loading_text.caption("# Finalizing everything...")
for _ in stqdm(range(50)):
    sleep(0.3)

prompt_loading_text.caption("#  Here's a random generated ai generated image")

generate_image()
st.image("temp.png")
st.write(f"""#### Prompt: """)
st.caption(f"""{str(temp_prompt)}""")
