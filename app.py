"""
programa que muestra gráficos interactivos con plotly haciendo un click en los botones asignados
"""

import pandas as pd
import streamlit as st
import plotly.express as px

car_info = pd.read_csv('vehicles_us.csv') #lectura de datos
st.header('CONSULTA DE CARACTERISTICAS EN VEHICULOS') #creación de un encabezado
hist_button = st.button('crear histograma') #creación de un botón
disp_button = st.button('crear gráfico de dispersión') #creación de un boton de dispersión

# boton para el histograma
if hist_button:

    st.write('Visualización de un histograma con la información especifica de un coche')

    # argumento para crear un histograma
    fig = px.histogram(car_info, x = 'model_year')

    # plotly interactivo
    st.plotly_chart(fig, use_container_width = True)

# boton para el gráfico de dispersión
if disp_button:
    st.write('Gráfico de dispersión con la información especifica de un coche')

    fig = px.scatter(car_info, x = 'model_year')

    st.plotly_chart(fig, use_container_width = True)
