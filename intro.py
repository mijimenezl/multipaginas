import streamlit as st 
from PIL import Image

st.title("Pagina intro")

image = Image.open('uno.jpg')
st.image(image, width=500)
