from classes.ninja import Ninja
from classes.pirate import Pirate



michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")


while michelangelo.health>0 and jack_sparrow.health>0:
    choice = input("Elige una función (Estado / Atacar / Descansar) o 'Salir' para salir: ")

    if choice == "Estado":
        michelangelo.Estado()
        jack_sparrow.Estado()
    elif choice == "Atacar":
        michelangelo.Atacar(jack_sparrow)
        print(f"{michelangelo.name} atacó a {jack_sparrow.name}!")
    elif choice == "Descansar":
        michelangelo.Descansar()
        print(f"{michelangelo.name} se ha recuperado!")
    elif choice == "Salir":
        break
    else:
        print("Opción inválida. Inténtalo nuevamente.")