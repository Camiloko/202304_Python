#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())  #tetornara el numero 5


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#representara un error pues no esta definida la primera funcion del print

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) #retornara 5 y luego 10

#al parecer retorno 5 y el 10 no, porque se detuvo en el retorno 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())  #retonara 5 e imprimira el numero 10

#nuevamente se detuvo en el return 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)    #imprimira el numero 5


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))  #imrpimira la suma de todos los numeros , que seria 8


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5)) #pondra los numeros uno al lado del otro, dando 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #retornara 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))  #retornara 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))  #retornara 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#retornara 7 + 14, es decir 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))    #retonara 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

"""
Imprime 2 veces 500, luego una vez 300 y otra vez 500
"""

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#imprimira 1 vez 500, y denuevo 500 luego 300 y otra vez 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#imprimira 500 2 veces, luego 300 2 veces

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#imprimira 1,3 y 2 en ese orden

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#imprimira 1,3 luego retonara 5, despues imprimira 3 y 5, y luego retonara 10