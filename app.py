import streamlit as st 
from PIL import Image 

st.title("Intro")

st.header("Esta es mi primera aplicación")
st.write("Pintura de la noche estrellada")
image = Image.open('gatito.jpeg')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto') 
st.write('El texto escrito es', texto)
