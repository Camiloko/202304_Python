#cuenta regresiva

def countdown(x):
    for i in range(x, -1, -1):
        print(i)

countdown(5)


#Imprimir y devolver

def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]

prueba=[1,2]

imprimir_y_devolver(prueba)

#Primero mas longitud

def primero_mas_longitud (lista):
    suma=lista[0]+ len(lista)
    print(suma)

prueba=[1,2,3,4,5]
primero_mas_longitud(prueba)

#Valores mayores que el segundo

def filtrar_mayores(lista):
    if len(lista) < 2:
        return False
    valor2 = lista[1]
    mayores_que_el_2 = [valor for valor in lista if valor > valor2]
    cantidad_valores = len(mayores_que_el_2)

    print(cantidad_valores)

    return mayores_que_el_2

prueba=[5,2,3,2,1,4]

filtrar_mayores(prueba)

#Esta longitud, ese valor

def longitud_valor (longitud,valor):
    nueva_lista = longitud * [valor]
    return nueva_lista

prueba1=longitud_valor(4,7)
prueba2=longitud_valor(6,2)

print(prueba1)
print(prueba2)
