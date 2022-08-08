matriz1 = []
matriz2 = []
multiplicacion = []
suma = 0
n = int (input('ingrese el valor  de N')) #filas
m = int (input('ingrese el  valor de M')) #columnas

def matriz(matriz):
    for i in range(n):
        matriz.append([])
        for t in range(m):
            m1 = int (input('ingrese un valor a la matriz '))
            matriz[i].append(m1)

print('ingresar datos a la matiz uno')
matriz(matriz1)
print('ingresar los datos a la matriz dos')
matriz(matriz2)

for i in range(n):
    multiplicacion.append([])
    for j in range(m):
        suma = 0
        for l in range():
            multiplicacionr = matriz1[i][l] * matriz2[l][j]
            print(multiplicacionr)
            suma = suma + multiplicacionr
        multiplicacion[i].append(suma)

        
print('matriz uno')            
matriz(matriz1)  
print('matriz dos')     
matriz(matriz2) 
            
print('resultado de la multiplicacion de la matriz uno x la matriz dos')

matriz(multiplicacion)
