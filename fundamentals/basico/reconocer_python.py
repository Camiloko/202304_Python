num1 = 42
num2 = 2.3
boolean = True

"""
Declaracion de variables, num1 es entero, num2 es decimal (o float),
boolean con un valor Verdadero
"""
string = 'Hello World' # Cadena de texto
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana')   # conjunto o tupla

print(type(fruit)) #
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

"""
Desde arriba es imprimir la clase de objeto que es fruit
despues imprimir Sausage (o el indice 1 de pizza_toppings)
Despues se añade mushrooms a pizza_toppings usando .append
Despues se imprime John (que seria el nombre de la persona)
luego se cambia el nombre de John a George en el diccionario
Y se añade la clave "eye_color" , con el valor Blue en ella,
y por ultimo, se imprime banana, que seria el indice 2 de fruit
"""

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""
Funcion que analiza num1, y deberia imprimir "It's lower"
"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

"""
Funcion que analiza string, y deberia imprimir "Just right!"
"""

for x in range(5):  #Ciclo for que imprime numeros del 0 al 4 (empieza por 0 y termina antes del 5)
    print(x)
for x in range(2,5): #ciclo for que imprime del 2 al 4
    print(x)
for x in range(2,10,3): #Ciclo for que imprime del 2 hasta el 9, dando saltos de 3 en 3
    print(x)
x = 0   #Declaracion de variable numerica
while(x < 5): #Ciclo while, que imprime numeros del 0 al 4 (se detiene antes del 5)
    print(x)
    x += 1

pizza_toppings.pop() #funcion que elimina el ultimo elemento de pizza_toppings
pizza_toppings.pop(1) #funcion que elimina el elemento de indice 1 de pizza_toppings


print(person) #imprime las claves y valores de Person
person.pop('eye_color') #elimina la clave y valor de eye_color
print(person) #imprime las claves y valores de person, despues de borrar eye_color

for topping in pizza_toppings:      #ciclo for que recorre todos los elementos de pizza_toppings
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():    #definicion de funcion que imprime hello 10 veces
    for num in range(10):
        print('Hello')

print_hello_ten_times() #llamado de la funcion definida anteriormente

def print_hello_x_times(x): #definicion de funcion que imprime Hello un x numero de veces
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #llamado de la funcion que imprimira Hello 4 veces

def print_hello_x_or_ten_times(x = 10): #deficion de funcion que imprime hello 10 veces por default, y x si se define un x
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()    #llamado de la funcion que imprimira 10 veces Hello
print_hello_x_or_ten_times(4)   #llamado de la funcion que imprimira 4 veces Hello


"""
Bonus section
"""

# print(num3)
# num3 = 72

"""
lo de arriba tendria que ser primero declarar el num3 y despues
pedir que lo imprima
"""
# fruit[0] = 'cranberry'    no es posible debido a que fruit es una tupla
# print(person['favorite_team']) no puede por que no existe una clave que sea favorite_team
# print(pizza_toppings[7])      no existe el indice 7 dentro de pizza_toppings, solo llegaria hasta el 4
#   print(boolean)      no se puede imprimir boolean debido a que es un valor de verdadero o falso

# fruit.append('raspberry') no es posible debido a que es una tupla, nos daria atribute error
# fruit.pop(1)  no es posible debido a que es una tupla