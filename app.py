import streamlit as st 
from PIL import Image 

st.title("Intro")

st.header("Esta es mi primera aplicación")
st.write("Pintura de la noche estrellada")
image = Image.open('Pintura.jpg')

st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe tu opinión sobre la pintura:', 'Escribe aqui') 
st.write('Que bonita pintura', texto)
