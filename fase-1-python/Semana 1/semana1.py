# Ejercicio 1: Variables y tipos
nombre = 'Gael'
edad = 17
lenguajes = ["JavaScript", "Java", "C++"]
activo = True

print(nombre)
print(edad)
print(lenguajes)
print(type(lenguajes))
print("----------------------------------------------")
# Ejercicio 2: Bucles
for lenguaje in lenguajes:
    print(lenguaje)
print("----")
for i,lenguaje in enumerate(lenguajes):
    print(i,lenguaje)
print("----------------------------------------------")
# Ejercicio 3: Diccionarios
perfil = {
    "nombre": "Gael",
    "edad": 17,
    "lenguajes": ["JavaScript", "Java", "C++"],
    "activo": True
}
print(perfil["nombre"])
print(perfil["lenguajes"][1])
for clave, valor in perfil.items():
    print(clave,": ",valor )
print("----------------------------------------------")
# Ejercicio 4: Funciones
def saludar(nombre , lenguaje="Python"):
    return f"Hola {nombre}, estas aprendiendo {lenguaje}"
print(saludar("Gael"))
print(saludar("Gael", "IA"))
print("----------------------------------------------")
# Ejercicio 5: List comprehensions
numeros = [1,2,3,4,5,6,7,8,9,10]
pares_tradicional = []
for n in numeros:
    if n % 2 == 0:
        pares_tradicional.append(n)
pares_rapido = [n for n in numeros if n % 2 == 0]
print(pares_tradicional)
print(pares_rapido)
print("----------------------------------------------")
# Ejercicio 6: Lambda, map y filter
doble = lambda x : x * 2
dobles = list(map(doble, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(dobles)
print(pares)
print("----------------------------------------------")
# Ejercicio 7: Clases
class Desarrollador:
    def __init__(self, nombre, edad, lenguajes):
        self.edad = edad
        self.nombre = nombre
        self.lenguajes = lenguajes
    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años  y se {', '.join(self.lenguajes)}"
    def agregar_lenguaje(self, lenguaje):
        self.lenguajes.append(lenguaje)
        print(f"{lenguaje} agregado exitosamente")
gael = Desarrollador("Gael", 17, ["JavaScript", "Java", "C++"])
print(gael.presentarse())
gael.agregar_lenguaje("Python")
print(gael.presentarse())
print("----------------------------------------------")
# Ejercicio 8: Herencia
class MLEngineer(Desarrollador):
    def __init__(self, nombre, edad, lenguajes, especialidad):
        super().__init__(nombre, edad, lenguajes)
        self.especialidad = especialidad
    def presentarse(self):
        base = super().presentarse()
        return f"{base} y me especializo en {self.especialidad}"
GAEL = MLEngineer("Gael", 17, ["JavaScript", "Java", "C++"], "Inteligencia Artificial")
print(GAEL.presentarse())
print("----------------------------------------------")
# Ejercicio 9: Excepciones
try:
    numero = int(input("Escribe un numero: "))
    resultado = 100 / numero
    print(f"100 / {numero} = {resultado}")
except ValueError:
    print("Error: eso no es un numero")
except ZeroDivisionError:
    print("Error: no puedes dividir entre 0")
finally:
    print("Esto siempre se ejecuta")
print("----------------------------------------------")
# Ejercicio 10: Archivos
with open("datos.txt", "w") as archivo:
    archivo.write("Gael\n")
    archivo.write("Python\n")
    archivo.write("Inteligencia Artificial\n")

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
