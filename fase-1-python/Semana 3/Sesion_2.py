import pandas as pd
def clasificar_sueldo(sueldo):
    if sueldo > 15000:
        return 'Alto'
    elif sueldo >= 8000:
        return 'Medio'
    else:
        return 'Bajo'
def seleccion(sueldo):
    if sueldo > 5000:
        return 'premium'
    elif sueldo >= 500:
        return 'estandar'
    else:
        return 'economico'
traduccion = {
    'Alto': 'High',
    'Medio': 'Medium',
    'Bajo': 'Low'
}
emojis = {
    'Laptop' : '💻',
    'Mouse' : '🖱️',
    'Teclado' : '⌨️',
    'Monitor' : '🖥️',
    'Audífonos': '🎧'
}
#PIVOT TABLE
ventas = pd.DataFrame({
    'vendedor': ['Ana', 'Ana', 'Luis', 'Luis', 'Ana', 'Luis'],
    'producto': ['Laptop', 'Mouse', 'Laptop', 'Mouse', 'Laptop', 'Laptop'],
    'monto': [15000, 300, 14000, 250, 16000, 15500]
})
tabla = pd.pivot_table(ventas, values='monto', index='vendedor', columns='producto', aggfunc='mean')
print(tabla)
print("---------------------------------------------------")
#APPLY
empleados = pd.DataFrame({
    'nombre': ['Ana', 'Luis', 'Marco', 'Sofía'],
    'sueldo': [12000, 8000, 25000, 15000]
})
empleados['categoria'] = empleados['sueldo'].apply(clasificar_sueldo)
print(empleados)
print("---------------------------------------------------")
#MAP
empleados['categoria_en'] = empleados['categoria'].map(traduccion)
print(empleados)
print("---------------------------------------------------")
#EJERCICIO
productos = pd.DataFrame({
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Audífonos'],
    'precio': [15000, 250, 450, 4000, 800],
    'categoria': ['Tech', 'Tech', 'Tech', 'Tech', 'Tech']
})
productos['rango_precio'] = productos['precio'].apply(seleccion)
productos['emoji'] = productos['producto'].map(emojis)
print(productos)
