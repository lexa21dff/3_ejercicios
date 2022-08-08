#matriz de NxN
matriz = []
#matriz triangular es igual a la matriz 
matriz_triangular = []
while True:
    n = int (input('ingrese un valor para N'))
    if n >= 2 :
        break
    
    else:
        print('el numero ingresado no es valido')
        

for i in range(n):
    matriz.append([])
    matriz_triangular.append([])
    for j in range(n):
        #ingresar datos a la matriz
        numeros = int (input('ingrese un valor a la matriz'))
        matriz[i].append(numeros)
        #matriz triangular
        temporal = matriz[i][j]
        matriz_triangular[i].append(temporal)


l=0
for j in range(1,n):
    l += 1
    for i in range(l):
        temporal = matriz_triangular[j][i] = 0
        matriz_triangular.append(temporal)
        

#mostrar la matriz por filas y columnas

def mostrar_matriz(matriz):
    for i in range(n):
        for j in range(n):
            print(matriz[i][j], end=' ')
            if j == n-1:
                print("\n")

print('matriz')
mostrar_matriz(matriz)
print('matriz triangular inferior ')
mostrar_matriz(matriz_triangular)



           

           






