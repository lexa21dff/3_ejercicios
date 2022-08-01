nombreV = []
apellidoV = []
resultate = []
nombre = input('ingrese su nombre')
apellido = input('ingrese su apellido')

for n in nombre: 
    # agregar datos al vector nombreV 
    nombreV.append(n)
    # agregar datos al vector ressultante
    resultate.append(n)
  
for a in apellido: 
    # agregar datos al vector apellido
    apellidoV.append(a)
    # agregar datos al vector resultalte
    resultate.extend(a)



print ('vector nombre ', nombreV) 
print('vector apellido ',apellidoV)
print('vector resultalte nombre y apellido ',resultate)
