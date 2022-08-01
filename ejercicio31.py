vector1 = []
vector2 = []
resultante = []
valores = int (input('cuantos valores tiene los vectores'))

#agregar datos al vector1
for i in range (valores):
    vector1.append([])
    n = int (input('ingrese un valor a vector uno'))
    vector1[i] = n

#agregar datos al vector1
for h in range (valores):
    vector2.append([])
    a = int (input('ingrese un valor a vector dos'))
    vector2[h] = a
suma = 0
t= 0
# suma del vector1 y vector2 igual resultante
for k in range(valores):
    resultante.append([])
    suma = vector1[k]+vector2[k]
    resultante[k]=suma
        
print('vector uno ',vector1)
print('vector dos ',vector2)
print('suma del vector uno y dos ',resultante)