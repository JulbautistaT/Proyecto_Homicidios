import pandas as pd
import plotly.express as px
import streamlit as st

# Función para consultar y graficar cantidad de accidentes por departamento
def consulta_cantidad_departamento():
    
    # Cargar los datos desde el archivo CSV
    data_query1 = pd.read_csv('Dashboard/Query_csv/query1.csv')  

    # Establecer el índice del DataFrame 
    data_query1.set_index('departamento', inplace=True)

    # Crear un gráfico de barras con Plotly
    fig = px.bar(data_query1, x=data_query1.index, y='Cantidad accidentes', 
                 labels={'x': 'Departamento', 'Cantidad accidentes': 'Cantidad de Accidentes'},
                 title="Cantidad de Accidentes por Departamento")
    
    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)


# Query2 Distribución de Homicidios por Género
def consulta_genero():
    
        data_query2 = pd.read_csv('Dashboard/Query_csv/query2.csv')

        # Crear gráfico de pastel
        fig = px.pie(data_query2, names='genero', values='Cantidad accidentes',
                     title='Distribución de Homicidios por Género', 
                     color_discrete_sequence = px.colors.sequential.RdBu)
        
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)

# Query3 Tendencia de Homicidios por Año
def consulta_tendencia():
        
    data_query3 = pd.read_csv('Dashboard/Query_csv/query3.csv')
       
    fig1 = px.line(data_query3, x='Año', y='Cantidad accidentes',
                    title='Tendencia de Homicidios por Año',
                    labels={'Año': 'Año', 'Cantidad accidentes': 'Cantidad'},
                    markers=True)

    fig1.update_traces(line=dict(color='royalblue', width=4))
        
    st.plotly_chart(fig1)

# Query4 Homicidios por Grupo Etario
def consulta_grupo():
    
    data_query4 = pd.read_csv('Dashboard/Query_csv/query4.csv')
        
    # Generar gráfico de barras
    fig2 = px.bar(data_query4,
                    x='grupo_etario', y='Cantidad accidentes',
                    title="Gráfico 4: Homicidios por Grupo Etario",
                    labels={'grupo_etario': 'Grupo Etario', 'Cantidad accidentes': 'Cantidad de Homicidios'},
                    color='Cantidad accidentes',
                    color_continuous_scale='Greens')

    fig2.update_layout(xaxis_title='Grupo Etario', yaxis_title='Cantidad de Homicidios')
    st.plotly_chart(fig2)

# Query5 Homicidios por Medios (ARMAS MEDIOS)
def consulta_armas():

    data_query5 = pd.read_csv('Dashboard/Query_csv/query5.csv')
        
    # Generar gráfico de barras
    fig3 = px.bar(data_query5,
                    x='armas_medio', y='Cantidad accidentes',
                    title="Gráfico 5: Homicidios por Medios",
                    labels={'armas_medio': 'Armas/Medios', 'Cantidad accidentes': 'Cantidad de Homicidios'},
                    color='Cantidad accidentes',
                    color_continuous_scale='Oranges')

    fig3.update_layout(xaxis_title='Armas/Medios', yaxis_title='Cantidad de Homicidios',
                          xaxis_tickangle=-45)
    st.plotly_chart(fig3)

    
    
# Query6 Homicidios por Mes del Año
def consulta_accidente_mes():

    data_query6 = pd.read_csv('Dashboard/Query_csv/query6.csv')

    # Generar gráfico de línea
    fig4 = px.line(data_query6, x='Mes', y='Cantidad accidentes',
                    title="Gráfico 6: Accidentes de Tránsito por Mes del Año 2023",
                    labels={'Mes': 'Mes', 'Cantidad accidentes': 'Cantidad de Accidentes'},
                    markers=True)

    fig4.update_traces(line=dict(color='darkorange', width=4))
    st.plotly_chart(fig4)
    
    
# Query7 Los 5 Municipios con Mayor Cantidad de Homicidios
def consulta_top_municipios():
    data_query7 = pd.read_csv('Dashboard/Query_csv/query7.csv')
    fig = px.bar(data_query7,
                    x='municipio', y='Cantidad accidentes',
                    title="Gráfico 7: Los 5 Municipios con Mayor Cantidad de Homicidios",
                    labels={'municipio': 'Municipio', 'Cantidad accidentes': 'Cantidad de Homicidios'},
                    color='Cantidad accidentes',
                    color_continuous_scale='Reds')

    fig.update_layout(xaxis_title='Municipio', yaxis_title='Cantidad de Homicidios',
                          xaxis_tickangle=-45)
    st.plotly_chart(fig)


# Ejecutar la función en Streamlit
consulta_cantidad_departamento()
consulta_genero()
consulta_tendencia()
consulta_grupo()
consulta_armas()
consulta_accidente_mes()
consulta_top_municipios()

