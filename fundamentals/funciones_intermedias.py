x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

##Actualizar valores

x[1][0]=15

print(x)

estudiantes[0]['last_name']='Bryant'

print(estudiantes)

directorio_deportes['fútbol'][0]='Andres'

print(directorio_deportes)

z[0]['y']= 30

print(z)

#Iterar a traves de una lista de diccionarios

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

####
def iterateDictionary(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave}: {valor}", end=", ")
        print()
###

iterateDictionary(estudiantes) 

# Obtener valores de una lista de diccionarios

def iterateDictionary2(lista, llave):
    for diccionario in lista:
        valor = diccionario.get(llave, None)
        if valor is not None:
            print(valor)

iterateDictionary2(estudiantes,'first_name')
iterateDictionary2(estudiantes,'last_name')

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave}")
        for elemento in lista:
            print(elemento)
        print()

printInfo(dojo)

