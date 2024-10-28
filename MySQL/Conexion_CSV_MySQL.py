from sqlalchemy import create_engine

# Configuración de la conexión
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/Homicidios')

# Probar la conexión
try:
    connection = engine.connect()
    print("Conexión exitosa")
    connection.close()
    
except Exception as e:
    print(f"Error al conectar: {e}")
    
import pandas as pd
from sqlalchemy import create_engine

# Cargar el archivo CSV con los datos limpios
file_path = 'C:/Users/telle/Downloads/Homicidios_limpio.csv'
df = pd.read_csv(file_path)

# Visualización de los datos
print(df.head()) 

# Confirmar el tipo de datos para la tabla de MySQL
print(df.dtypes)
df['Fecha_hecho'] = pd.to_datetime(df['Fecha_hecho'], format='%d/%m/%Y')
df['Cantidad'] = df['Cantidad'].astype(int)
print(df.dtypes)


# Insertar los datos en la tabla de MySQL
try:
    df.to_sql('datos_inicio', con=engine, if_exists='append', index=False)
    print("Datos insertados exitosamente.")
except Exception as e:
    print(f"Error al insertar los datos: {e}")