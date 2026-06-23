import numpy as np

m = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print(m[0, 1])      # un elemento
print(m[1, :])      # fila completa
print(m[:, 2])      # columna completa
print(m[0:2, 0:2])  # submatriz
