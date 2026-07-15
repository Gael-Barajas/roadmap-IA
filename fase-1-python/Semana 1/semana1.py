# Manejo de archivos
# Escribir un archivo
with open("datos.txt", "w") as archivo:
    archivo.write("Gael\n")
    archivo.write("Python\n")
    archivo.write("Inteligencia Artificial\n")

# Leer el archivo
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
