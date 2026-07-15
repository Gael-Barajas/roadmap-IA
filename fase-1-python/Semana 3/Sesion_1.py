import pandas as pd
clientes = pd.DataFrame({
    'id_cliente' : [1 , 2, 3, 4],
    'nombre' : ['Ana', 'Luis', 'Marco', 'Sofia']
})
compras = pd.DataFrame({
    'id_cliente' : [1, 2, 2, 5],
    'producto' : ['Laptop', 'Mouse', 'Teclado', 'Monitor']
})
#JOINS
resultado = pd.merge(clientes, compras, on = 'id_cliente' , how = 'inner')
print(resultado)
print("___________________________________________________")
resultado_left = pd.merge(clientes, compras, on='id_cliente', how='left')
print(resultado_left)
print("___________________________________________________")
resultado_right = pd.merge(clientes, compras, on='id_cliente', how='right')
print(resultado_right)
print("___________________________________________________")
resultado_outer = pd.merge(clientes, compras, on='id_cliente', how='outer')
print(resultado_outer)
print("___________________________________________________")
#ANTI-JOIN
resultado = pd.merge(clientes, compras, on='id_cliente', how='outer', indicator=True)
solo_diferentes = resultado[resultado['_merge'] != 'both']
print(solo_diferentes)
print("---------------------------------------------------")
#CONCAT
ventas_enero = pd.DataFrame({
    'producto': ['Laptop', 'Mouse'],
    'cantidad': [5, 20]
})

ventas_febrero = pd.DataFrame({
    'producto': ['Teclado', 'Monitor'],
    'cantidad': [8, 3]
})
resultado = pd.concat([ventas_enero, ventas_febrero], ignore_index = True) #Ignore index hace que se reinicien los indices
print(resultado)
print("---------------------------------------------------")
#CONCAT AXIS
nombres = pd.DataFrame({'nombre': ['Ana', 'Luis']})
edades = pd.DataFrame({'edad': [23, 31]})
resultado2 = pd.concat([nombres, edades], axis=1)
print(resultado2)
print("---------------------------------------------------")
#EJERCICIO
empleados = pd.DataFrame({
    'id' : [1,5,3,4],
    'nombre': ['Francisco', 'Ulises', 'Said', 'Natalia'],
    'departamento' : ['RH','RH', 'Produccion', 'Finansas']
})
salarios = pd.DataFrame({
    'id' : [1,2,3,4],
    'sueldo' : [12000, 20000, 5000, 6000]
})
resultadoA = pd.merge(empleados, salarios, on = 'id' , how = 'left')
resultadoB = pd.merge(empleados, salarios, on = 'id' , how = 'outer', indicator = True)
sin_match = resultadoB[resultadoB['_merge'] != 'both']
print(resultadoA)
print(sin_match)
