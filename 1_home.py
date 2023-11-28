import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
  page_title="Anchetas",
  page_icon="🛒",
  layout="wide"
)

st.write("""
# Anchetas 🛒 Navideñas 🎅🏻 Personalizadas!
""")
col1, col2 = st.columns(2)

with col1:
    suits = st.selectbox(
        "Para cuántas personas será la Ancheta?",
        ("1", "2", "3", "4", "5"),
    )
    rooms = st.radio(
        "Producto Principal de la Ancheta?",
        options=['Bebidas', 'Jamones','Quesos', 'Chocolates', 'Galletas'],
    )
    beds = st.selectbox(
        "Producto Secundario de la Ancheta?",
        ('Bebidas', 'Jamones','Quesos', 'Chocolates', 'Galletas'),
    )

with col2:
    name = st.text_input('Escribe el nombre de quien regala la Ancheta', '''
    ''')
    email = st.text_input('Escribe el nombre de quien recibe la Ancheta', '''
    ''')
    bank_account =  st.text_input('Type your bank account:', '''
    ''')
    phone =  st.text_input('Type your phone number', '''
    ''')
    a = st.selectbox('Forma de Pago', ['PSE', 'Contra entrega', 'Crédito'])


b = st.selectbox('Qué tan grande quieres la ancheta', ['Básica 100.000', 'Media 250.000', 'Grande 500.000€'])

h = st.button('Crear Ancheta Personalizada 🛒 YA')

if h:
  st.write('Tu ancheta personalizada ha sido enviada a tu correo para pagos')
