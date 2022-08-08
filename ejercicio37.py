matriz1 = [[1,2,3,4,5],[6,7,8,9,10,],[11,12,13,14,15]]
matriz_transpuesta = []
for j in range(5):
    matriz_transpuesta.append([])
    for i in range(3):
        temporal = matriz1[i][j] 
        matriz_transpuesta[j].append(temporal)

def mostrar_matriz(matriz,n,m):
    for i in range(n):
        for j in range(m):
            print(matriz[i][j], end=' ')
            if j == m-1:
                print("\n")

print(matriz_transpuesta)
print('matriz')
mostrar_matriz(matriz1,3,5)


print('matriz transpuesta')
mostrar_matriz(matriz_transpuesta,5,3)