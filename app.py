import streamlit as st 
from PIL import Image 

st.title("APP")

st.header("En este espacio comienzo a desarrollar mis aplicaciones")
st.write("Para realizar cosas")
image = Image.open('gatito.jpg')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto') 
st.write('El texto escrito es', texto)
