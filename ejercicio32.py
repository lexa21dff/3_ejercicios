numeros = [1,2,3,4,5,6,7,8,9]
t = 0
b = 0
x = input('ingrese un valor ')
numeros.append(x)
for i in range(10):
    print(numeros)
    numeros=[]
    t +=1
    for j in range(1,10):
        if j > t:
        #izquierda
            numeros.append(j)
    # movimiento de x
    numeros.append(x)
    for l in range(1,t+1):
        #izquierda
        numeros.append(l)

        
