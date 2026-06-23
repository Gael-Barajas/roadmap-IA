import numpy as np
#BROADCAST
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
fila = np.array([10,20,30])
print(matriz + fila)
#ESTADISTICA
datos = np.array([23, 45, 12, 67, 34, 89, 56, 78, 90, 11])

print(np.mean(datos))    # promedio
print(np.median(datos))  # mediana
print(np.std(datos))     # desviación estándar
print(np.min(datos))     # mínimo
print(np.max(datos))     # máximo
#OPERACIONES CON MATRICES
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
    [7, 8]]
print(np.dot(A, B))

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])

print(np.sort(arr))
print(np.argmax(arr))
print(np.argmin(arr))
