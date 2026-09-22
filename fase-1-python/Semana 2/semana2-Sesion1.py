import numpy as np
#Lista normal de Python
lista = [1,2,3,4,5]
# Array de NumPy
arr = np.array([1,2,3,4,5])
print(type(lista))
print(type(arr))
print(arr)
# Array 2D (matriz)
matriz = np.array([[1,2,3],
                  [4,5,6]])
print(matriz.shape)
print(matriz.ndim)
print(matriz.dtype)
print(matriz.size)
#OPERACIONES
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(a * 2)
print(a ** 2)
#SLICING E INDEXING
m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(m[0, 1])      # un elemento
print(m[1, :])      # fila completa
print(m[:, 2])      # columna completa
print(m[0:2, 0:2])  # submatriz
#PROPIEDADES
print(m.shape)
print(m.ndim)
print(m.dtype)
print(m.size)
