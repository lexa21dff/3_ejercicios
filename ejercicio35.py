matriz1 = [[3,4,5,6,2],[3,5,7,2,8,],[1,3,6,2,7]]
multiplicacion_matriz = []
b = 0
n = 3
m = 5
numero = int (input('ingrese un numero entero '))
for i in range(n):
    multiplicacion_matriz.append([])
    while True:
        b += 1
        for t in range(m):
            # ingresar datos a la matriz1 m1
            multiplicar = matriz1[i][t] * numero
            multiplicacion_matriz[i].append(multiplicar)
        if b == 1:
            b = 0
            break

print('matriz')
for i in range (n):
    for j in range (m):
        print(matriz1[i][j], end=" ")
        if j == m - 1:
            print("\n")
print('multilplicacion de la matriz por ',numero,'igual')
for i in range (n):
    for j in range (m):
        print(multiplicacion_matriz[i][j], end=" ")
        if j == m - 1:
            print("\n")