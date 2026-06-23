import pandas as pd
#SERIES
serie = pd.Series([10, 20, 30, 40, 50],
                  index=['a', 'b', 'c', 'd', 'e'])

print(serie)
print(serie['c'])
#DATAFRAME
print("--------------------------------------------------------------------")
data = {
    'nombre': ['Ana', 'Luis', 'María', 'Carlos'],
    'edad': [23, 35, 28, 41],
    'salario': [15000, 32000, 27000, 45000]
}

df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.dtypes)
#ACCESO A FILAS Y COLUMNAS
print("--------------------------------------------------------------------")
print(df['nombre'])           # columna por nombre
print(df[['nombre', 'edad']]) # varias columnas
print(df.iloc[1])             # fila por índice
print(df.loc[2])
#INFO DE DATASETS
print("--------------------------------------------------------------------")
print(df.info())
print(df.describe())
#EJERCICIO
print("--------------------------------------------------------------------")
peliculas = {
    'titulo': ["Batman", "AVATAR 3", "El pianista", "Toy Story 5", "Spiderman"],
    'año': [2009, 2025, 2006, 2026, 2021],
    'duracion_min': [146 , 195 , 131, 119, 150],
    'calificacion': [9.5, 7.0, 9.9, 7.9, 8.5]
}
df_peliculas = pd.DataFrame(peliculas)
print(df_peliculas[df_peliculas['calificacion'] > 8])
print(f"Promedio de duracion: {df_peliculas['duracion_min'].mean()}")
print(df_peliculas['calificacion'].argmax())
