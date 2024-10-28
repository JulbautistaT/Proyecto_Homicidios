# Archivo con la conexión de MySQUL y sus debidas consultas en la base de datos

import pandas as pd
import plotly.express as px
import mysql.connector
import streamlit as st


# Configuración de la conexión a la base de datos
config = {
    'user': 'root',
    'password': '1234',  # Contraseña según MySQL
    'host': '127.0.0.1',  # IP del host (localhost)
    'port': 3306,  # Puerto de MySQL
    'database': 'Homicidios'  # Base de datos 
}

try:
    # Establecer la conexión
    conn = mysql.connector.connect(**config)
    st.write("Conexión exitosa a la base de datos.")
    
    
    # Query1 Cantidad de accidentes por departamento
    def consulta_cantidad_departamento(conn):
        st.write('**Gráfico cantidad de accidentes por departamento**')
    
        query_1 = """
            SELECT COUNT(a.cantidad_accidentes) AS 'Cantidad accidentes', la.departamento 
            FROM accidente a
            JOIN lugar_accidente la ON a.id_lugar = la.id_lugar
            GROUP BY la.departamento 
            ORDER BY COUNT(a.cantidad_accidentes) DESC;
            """  
     
        data_query1 = pd.read_sql_query(query_1, conn)  # Usar pandas para leer el resultado del dataframe
        
        # Establecer el índice del DataFrame
        data_query1.set_index('departamento', inplace=True)
        

        # Mostrar el gráfico de barras
        st.bar_chart(data_query1['Cantidad accidentes'])
        
    
    # Query2 Distribución de Homicidios por Género
    def consulta_genero(conn):
    
        query_2 = """
            SELECT COUNT(a.cantidad_accidentes) AS 'Cantidad accidentes', p.genero
            FROM accidente a
            JOIN persona p ON a.id_persona = p.id_persona
            GROUP BY p.genero
            ORDER BY COUNT(a.cantidad_accidentes);
            """  
     
        data_query2 = pd.read_sql_query(query_2, conn)  # Usar pandas para leer el resultado del dataframe
        
        # Crear gráfico de pastel
        fig = px.pie(data_query2, names='genero', values='Cantidad accidentes',
                     title='Distribución de Homicidios por Género', 
                     color_discrete_sequence=px.colors.sequential.RdBu)
        
        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)
        
    

    # Query3 Tendencia de Homicidios por Año
    def consulta_tendencia(conn):
    
        query_3 = """
            SELECT YEAR(fecha_hecho) AS Año, COUNT(cantidad_accidentes) AS 'Cantidad accidentes'
            FROM accidente 
            GROUP BY Año
            ORDER BY Año;
            """  
     
        data_query3 = pd.read_sql_query(query_3, conn)  # Usar pandas para leer el resultado del dataframe

        
        fig1 = px.line(data_query3, x='Año', y='Cantidad accidentes',
                      title='Tendencia de Homicidios por Año',
                      labels={'Año': 'Año', 'Cantidad accidentes': 'Cantidad'},
                      markers=True)

        fig1.update_traces(line=dict(color='royalblue', width=4))
        
        st.plotly_chart(fig1)

    
    # Query4 Homicidios por Grupo Etario
    def consulta_grupo(conn):
    
        query_4 = """
            SELECT COUNT(a.cantidad_accidentes) AS 'Cantidad accidentes', p.grupo_etario
            FROM accidente a
            JOIN persona p ON a.id_persona = p.id_persona
            GROUP BY grupo_etario
            ORDER BY COUNT(a.cantidad_accidentes) DESC;
            """  
     
        data_query4 = pd.read_sql_query(query_4, conn)  # Usar pandas para leer el resultado del dataframe
        
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
    def consulta_armas(conn):
    
        query_5 = """
            SELECT COUNT(cantidad_accidentes) AS 'Cantidad accidentes', armas_medio
            FROM accidente 
            GROUP BY armas_medio
            ORDER BY COUNT(cantidad_accidentes) DESC;
            """  
     
        data_query5 = pd.read_sql_query(query_5, conn)  # Usar pandas para leer el resultado del dataframe
        
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
    def consulta_accidente_mes(conn):
    
        query_6 = """
            SELECT MONTH(fecha_hecho) AS Mes, SUM(cantidad_accidentes) AS 'Cantidad accidentes'
            FROM accidente WHERE YEAR(fecha_hecho) = '2023'
            GROUP BY Mes
            ORDER BY Mes;
            """  
     
        data_query6 = pd.read_sql_query(query_6, conn)  # Usar pandas para leer el resultado del dataframe

        # Generar gráfico de línea
        fig4 = px.line(data_query6, x='Mes', y='Cantidad accidentes',
                      title="Gráfico 6: Accidentes de Tránsito por Mes del Año 2023",
                      labels={'Mes': 'Mes', 'Cantidad accidentes': 'Cantidad de Accidentes'},
                      markers=True)

        fig4.update_traces(line=dict(color='darkorange', width=4))
        st.plotly_chart(fig4)
    
    
    # Query7 Los 5 Municipios con Mayor Cantidad de Homicidios
    def consulta_top_municipios(conn):
    
        query_7 = """
            SELECT COUNT(a.cantidad_accidentes) AS 'Cantidad accidentes', la.municipio
            FROM accidente a
            JOIN lugar_accidente la ON a.id_lugar = la.id_lugar
            GROUP BY la.municipio
            ORDER BY COUNT(a.cantidad_accidentes) DESC 
            LIMIT 5;
            """  
     
        data_query7 = pd.read_sql_query(query_7, conn)  # Usar pandas para leer el resultado del dataframe
        fig = px.bar(data_query7,
                     x='municipio', y='Cantidad accidentes',
                     title="Gráfico 7: Los 5 Municipios con Mayor Cantidad de Homicidios",
                     labels={'municipio': 'Municipio', 'Cantidad accidentes': 'Cantidad de Homicidios'},
                     color='Cantidad accidentes',
                     color_continuous_scale='Reds')

        fig.update_layout(xaxis_title='Municipio', yaxis_title='Cantidad de Homicidios',
                          xaxis_tickangle=-45)
        st.plotly_chart(fig)
    
    
    # Llamar las funciones
    consulta_cantidad_departamento(conn)
    consulta_genero(conn)
    consulta_tendencia(conn)
    consulta_grupo(conn)
    consulta_armas(conn)
    consulta_accidente_mes(conn)
    consulta_top_municipios(conn)
    



except mysql.connector.Error as err:
    st.write(f"Error al conectar con la base de datos: {err}")
    
finally:
    # Cerrar la conexión si se estableció correctamente
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        st.write("Conexión cerrada.")
