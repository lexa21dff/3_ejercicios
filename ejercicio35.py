matriz = []
multiplicacion = []
n = int (input('ingrese un valor pra N'))
m = int (input('ingrese un valor para M'))
numero = int (input('ingrese un numero entero para multiplicarlo por la matriz '))
for i in range(n):
    multiplicacion.append([])
    matriz.append([])
    for t in range(m):
        # ingresar datos a la matriz1 m1
        numeros = int (input('ingrese un valor a la matriz'))
        matriz[i].append(numeros)
        # agregar los datos a la matriz multiplicacion multiplicando 
        multiplicar = matriz[i][t] * numero
        multiplicacion[i].append(multiplicar)



def mostrar_matriz(matriz):
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end=' ')
            if j == m-1:
                print("\n")

print('matriz')
mostrar_matriz(matriz)
print('multilplicacion de la matriz por ',numero,'igual')
mostrar_matriz(multiplicacion)
