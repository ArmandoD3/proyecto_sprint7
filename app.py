import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np 
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
# Eliminar filas con valores nulos en la columna "odometer"
car_data = car_data.dropna(subset=['odometer'])

st.header("visualizacion de histogramas de vehiculos", divider = "gray")

#Casilla 0
checkbox1 = st.checkbox('Tabla')
       
if checkbox1:
   st.write('Incluir fabricantes con menos de 1000 anuncios.')
   st.dataframe(car_data) 






#Boton 1
#hist_button = st.button('Construir histograma') # crear un botón
#Casilla1
checkbox2 = st.checkbox('Construir un histograma')
        
if checkbox2:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig1 = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)


#Boton 2
#hist_button2 = st.button('Construir dispersión') # crear un botón

#Casilla 2
checkbox3 = st.checkbox('Construir dispersión')
        
if checkbox3:
    st.write('Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)