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
