import streamlit as st 
from PIL import Image

st.title("Pagina 1")

image = Image.open('pag1.jpg')
st.image(image, width=500)
