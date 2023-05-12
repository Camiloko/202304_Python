"""
Ejercicio 03

Basico : Imprime todos los numeros enteros del 0 al 150
"""

for i in range(151):
    print(i)


#Multiplos de 5

for i in range( 5,1001):
    if i % 5 == 0:
        print(i)

#Coding Dojo Conteo

for i in range(1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


#Suma Impares

impares=[]
for i in range(1,500000):
    if i % 2 != 0:
        impares.append(i)

resultado=sum(impares)
print(resultado)

#Cuenta regresiva

for i in range(2018,0,-4):
    print(i)


#Flexible

def flex(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if i % mult ==0:
            print(i)

flex(2,9,3)