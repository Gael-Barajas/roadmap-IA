import pandas as pd
#SERIES
serie = pd.Series([10,20,30,40,50], index = ['a','b','c','d','d'])
print(serie)
print(serie['c'])
#DATAFRAME
print("--------------------------------------------------------------------")
data = {
    'nombre': ['Ana', 'Luis', 'Maria', 'Carlos'],
    'edad': [23,35,28,41],
    'salario': [15000,32000,27000,45000]
}

df = pd.DataFrame(data, index = ['a','b','c','d'])
print(df)
print(df.shape)
print(df.dtypes)
#ACCESO A FILAS Y COLUMNAS
print("--------------------------------------------------------------------")
print(df['nombre'])           # columna por nombre
print(df[['nombre', 'edad']]) # varias columnas
print(df.iloc[1])             # fila por índice
print(df.loc['c'])              # fila por etiquta (en este caso la etiqueta coincide con los índices)
#INFO DE DATASETS
print("--------------------------------------------------------------------")
print(df.info())
print(df.describe())
#EJERCICIO
print("--------------------------------------------------------------------")
peliculas = {
    'titulo': ['Batman', 'Los croods', 'Increibles 2', 'Openhaimmer', 'La odisea'],
    'año': [2013, 2009, 2021, 2024, 2026],
    'duracion_min':[154, 131, 120, 185, 200],
    'calificacion':[91, 85, 80, 99, 100]
}
df_peliculas = pd.DataFrame(peliculas)
print(df_peliculas[df_peliculas['calificacion'] > 90])
print(f"Duracion promedio: {df_peliculas['duracion_min'].mean()}")
print(df_peliculas['calificacion'].argmax())
