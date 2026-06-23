import numpy as np
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
