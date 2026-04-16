#Imprimir números enteros del 1 al 100
for i in range(101):
    print (i)

#Imprimir numeros mulp de 2 entre 2 y 500
for i in range(2,501,2):
    print(i)

#contando vanilla ice
for i in range(1,101):
    if i % 10 ==0:
        print('baby')
    elif i % 5 == 0 :
        print ('ice ice')
    else:
        print(i)

#Número gigante a la vista
suma = 0
for i in range(0,500001, 2):
    suma += 1
print(sum)

#Regresame al 3
for i in range(2024, 0 , -3):
    print(i)


#Contador Dinamico
numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal +1):
    if i % multiplo == 0:
        print(i)


