class Mascota:
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = 100
        self.salud = 100

    def dormir(self):
        self.energia += 25

    def comer(self):
        self.energia += 5
        self.salud += 10

    def jugar(self):
        self.salud += 5

    def ruido(self):
        print("Escuchas algo, tu mascota dice")
        pass

