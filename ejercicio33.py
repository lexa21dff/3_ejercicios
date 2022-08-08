matriz1 = []
matriz2 = []
suma_matrices = []
n = int (input('ingrese un valor')) #filas
m = int (input('ingrese un valor')) #columnas

for i in range(n):
    matriz1.append([])
    matriz2.append([])
    suma_matrices.append([])
    for t in range(m):
            m1 = int (input('ingrese un valor a la matriz uno'))
            m2 = int(input('ingrese un valor a la matriz dos'))
            # ingresar datos a la matriz1 m1
            matriz1[i].append(m1)
            # ingresar datos a la matriz2 m2
            matriz2[i].append(m2)
            # suma de la matriz1 y matriz2
            suma = matriz1[i][t]+ matriz2[i][t]
            suma_matrices[i].append(suma)

def mostrar_matriz(matriz):
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end=' ')
            if j == m-1:
                print("\n")

print('matriz uno ')
mostrar_matriz(matriz1)
print('matriz dos ')
mostrar_matriz(matriz2)
print('suma de la matriz uno y dos ')
mostrar_matriz(suma_matrices)