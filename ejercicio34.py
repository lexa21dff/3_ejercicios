matriz1 = []
matriz2 = []
suma_matrices = []
b = 0
n = int (input('ingrese un valor')) #filas
m = int (input('ingrese un valor')) #columnas

for i in range(n):
    matriz1.append([])
    matriz2.append([])
    suma_matrices.append([])
    while True:
        b += 1

        for t in range(m):
            m1 = int (input('ingrese un valor a la matriz uno'))
            m2 = int(input('ingrese un valor a la matriz dos'))
            # ingresar datos a la matriz1 m1
            matriz1[i].append(m1)
            # ingresar datos a la matriz2 m2
            matriz2[i].append(m2)
            # suma de la matriz1 y matriz2
            suma = matriz1[i][t] * matriz2[i][t]
            suma_matrices[i].append(suma)
        if b == 1:
            b = 0
            break


print('matriz uno ',matriz1)
print('matriz dos ',matriz2)
print('suma de la matriz uno y dos ',suma_matrices)