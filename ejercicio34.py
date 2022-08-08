matriz1 = [[1,2,3],[6,7,8],[4,5,3]]
matriz2 = [[4,5,5]
           ,[9,0,3],
           [2,3,4]]
multiplicacion = []
suma = 0

for i in range(3):
    multiplicacion.append([])
    for j in range(3):
        suma = 0
        for l in range(3):
            multiplicacionr = matriz1[i][l] * matriz2[l][j]
            print(multiplicacionr)
            suma = suma + multiplicacionr
        multiplicacion[i].append(suma)
        print('suma ',suma)
            
              
                 

def mostrarmatriz(matriz):
    for n in range(3):
        for z in range(3):
            print(matriz[n][z], end=' ')
            if z == 3-1:
                print('\n')   
   
        
        
print('matriz uno')            
mostrarmatriz(matriz1)  
print('matriz dos')     
mostrarmatriz(matriz2) 
            
print('resultado de la multiplicacion de la matriz uno x la matriz dos')

mostrarmatriz(multiplicacion)
