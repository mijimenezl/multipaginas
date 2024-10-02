import streamlit as st 
from PIL import Image

image = Image.open('uno.jpg')
st.image(image, width=500)

st.title("Pagina intro")
