import pandas as pd
#Detectación de datos null
data_sucia = {
    'nombre' : ['Ana', 'Luis', None, 'Carlos' , 'Maria'],
    'edad' : [23 , None, 28, 41, 25],
    'salario' : [15000, 32000, 27000, None, 45000]
}
df_sucio = pd.DataFrame(data_sucia)
print(df_sucio)
print(df_sucio.isnull().sum())
print("---------------------------------------------------")
#Manejo de los datos null
# Eliminar filas con nulos
df_sin_nulos = df_sucio.dropna()
print(df_sin_nulos)
print("___________________________________________________")
# Rellenar nulos con un valor
df_relleno = df_sucio.fillna({'edad' : df_sucio['edad'].mean(),
                              'salario' : df_sucio['salario'].mean(),
                              'nombre' : 'Desconocido'})
print(df_relleno)
print("---------------------------------------------------")
#Agrupaciones
data_ventas = {
    'vendedor': ['Ana', 'Luis', 'Ana', 'Carlos', 'Luis', 'Ana'],
    'region': ['Norte', 'Sur', 'Norte', 'Sur', 'Norte', 'Sur'],
    'ventas': [1500, 2300, 1800, 900, 2100, 1200]
}

df_ventas = pd.DataFrame(data_ventas)
#print(df_ventas)
print(df_ventas.groupby('vendedor')['ventas'].sum())
print("___________________________________________________")
print(df_ventas.groupby('vendedor')['ventas'].mean())
print("___________________________________________________")
print(df_ventas.groupby('region')['ventas'].sum())
print("---------------------------------------------------")
#Ordenar y filtrar combinados
df_ordenado = df_ventas.sort_values('ventas', ascending=False)
print(df_ordenado)
print("___________________________________________________")
df_norte = df_ventas[df_ventas['region'] == 'Norte']
print(df_norte)
print("---------------------------------------------------")
#EJERCICIO
data_estudiantes = {
    'nombre' : ['Gael', 'Natalia', 'Santiago', 'Adrian', 'Sofia', 'Nicolas'],
    'materia' : ['Quimica', 'Fisica', 'matematicas' , 'Fisica', 'matematicas', 'sociales'],
    'calificacion' : [None, 97, 85, None, 45, 80]
}
df_estudiantes = pd.DataFrame(data_estudiantes)
df_estudiantes_rellenada = df_estudiantes.fillna({'calificacion' : df_estudiantes['calificacion'].mean()})
print(df_estudiantes_rellenada)
print("___________________________________________________")
print(df_estudiantes_rellenada.groupby('materia')['calificacion'].mean())
print("___________________________________________________")
df_calificaciones_altas = df_estudiantes_rellenada[df_estudiantes_rellenada['calificacion'] > 80.0]
print(df_calificaciones_altas)
