from mascotas import Mascota


class Perro(Mascota):
    def ruido(self):
        super().ruido()
        print("¡Guau!")


class Gato(Mascota):
    def ruido(self):
        super().ruido()
        print("¡Miau!")


class Pajaro(Mascota):
    def ruido(self):
        super().ruido()
        print("¡Pío pío!")


class Ninja:
    def __init__(self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        self.mascota.comer()
        return self

    def bañar(self):
        self.mascota.ruido()
        return self
    
    def mostrar_info(self):
        print(f"Ninja: {self.nombre} {self.apellido}")
        print(f"Mascota: {self.mascota.name} ({self.mascota.tipo}) {self.mascota.energia}")

perro = Perro("Pluto", "perro", 15)


ninja1 = Ninja("Naruto","Uzumaki",15,"Ramen",perro)

ninja1.alimentar().caminar().bañar()
ninja1.mostrar_info()