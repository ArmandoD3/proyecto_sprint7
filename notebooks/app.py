import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np 
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
# Eliminar filas con valores nulos en la columna "odometer"
car_data = car_data.dropna(subset=['odometer'])

st.header("visualizacion de histogramas de vehiculos", divider = "gray")

#Boton 1
#hist_button = st.button('Construir histograma') # crear un botón
#Casilla1
hist_button = st.checkbox('Construir un histograma')
        
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
#Boton 2
#hist_button2 = st.button('Construir dispersión') # crear un botón

#Casilla 2
hist_button2 = st.checkbox('Construir dispersión')
        
if hist_button2:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)