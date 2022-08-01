numeros = [1,2,3,4,5,6,7,8,9,0]
t = 0


while True:
    print(numeros)
    x = int (input('ingrese un valor'))
    # el valor ingresado debe ser mayor o igual que cero  y menor o menor o igual que 9 
    # de lo contrario el ciclo se repite asta que ingrese un numero valido
    if x >= 0  and x <= 9 :
        for  i in range(x+1): 
            # agrega los valores  al final del vector asta que sea igual a X
            numeros.append(i)
             # elimina los valores del inicio del vector asta que sea mayor que x 
            numeros.remove(i)
        
        break
    else:
        print('el valor ingresado no es correcto')
    

print(numeros)
