# 1. TAREA: imprime "Hola, mundo"
print( "Hola, mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Camilo"
print( "Hola",name)	# con una coma
print( "Hola "+ name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable

#El error ocurre debido a el 42 esta como int, pero si lo escribimos como texto, se soluciona
name = "42"
print( "Hola", name)	# con una coma
print( "Hola" + name)	# con una +	-- este debería arrojar un error!

# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"

print( "Mis comidas favoritas son {} y {}" .format(fave_food1,fave_food2) ) # con .format()
print(f"Mis comidas favorias son {fave_food1} y {fave_food2}") # con una cadena f

