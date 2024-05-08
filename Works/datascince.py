import pandas as pd
import os

# Cargar el archivo de Excel
archivo_entrada = 'H:\OCTUBRE\Indice de octubre del 2023.xlsx'

# Ruta de la carpeta que deseas explorar
ruta_carpeta = 'H:\OCTUBRE\quincena2319'

# Leer el archivo de Excel y crear un DataFrame
df = pd.read_excel(archivo_entrada)

# Obtener la lista de nombres de archivos en la carpeta
nombres_archivos = os.listdir(ruta_carpeta)

# Seleccionar solo las columnas que deseas para trabajar
columnas_seleccionadas = ['QUINCENA', 'ANOMINA', 'REPORTE', 'NARCHIVO', 'ARCHIVO', 'DEPENDEN', 'SUB_DEP', 'VALIDACIÓN']
df = df[columnas_seleccionadas]

# Eliminar las columnas que no necesitas
columnas_a_eliminar = ['ANOMINA', 'NARCHIVO', 'ARCHIVO', 'VALIDACIÓN']
df = df.drop(columns=columnas_a_eliminar)

# Crear un DataFrame con los nombres de los archivos
df_archivos = pd.DataFrame({'Nombre de Archivo': nombres_archivos})

# Verificar si el valor en la columna "SUB_DEP" es un número y reemplazarlo por un valor nulo si no lo es
df['SUB_DEP'] = df['SUB_DEP'].apply(lambda x: x if isinstance(x, int) else " ")

# Crear una nueva columna en el DataFrame con los nombres de las nomenclaturas
df['Nomenclatura'] = df.apply(lambda row: f"{row['REPORTE'][:3]}_{row['REPORTE'][-4:]}_{row['REPORTE'][3]}_{row['DEPENDEN']}_{row['SUB_DEP']}" if isinstance(row['SUB_DEP'], int) else f"{row['REPORTE'][:3]}_{row['REPORTE'][-4:]}_{row['REPORTE'][3]}_{row['DEPENDEN']}" if pd.notnull(row['SUB_DEP']) else f"{row['REPORTE'][:3]}_{row['REPORTE'][-4:]}_{row['REPORTE'][3]}_{row['DEPENDEN']}_", axis=1)

# Quitar la extensión de los nombres de archivo en el DataFrame
df_archivos['Nombre de Archivo'] = df_archivos['Nombre de Archivo'].apply(lambda x: os.path.splitext(x)[0])

# Mostrar los primeros registros del nuevo DataFrame
print(df_archivos.head())

# Mostrar los primeros registros del DataFrame después de la lipieza
print(df.head())


