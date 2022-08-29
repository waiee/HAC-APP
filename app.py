import streamlit as st
from PIL import Image

st.title("House & Car Price Calculator (RM)")


#Hide streamlit trademark
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
 