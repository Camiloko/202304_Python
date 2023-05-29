class Usuario:
    def __init__(self, nombre, apellido, balance_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.balance_cuenta = balance_cuenta
    def hacer_deposito(self, cantidad):
        self.balance_cuenta += cantidad
        print(f"Se realizo un deposito de {cantidad}.")
        return self

    def hacer_retiro(self, cantidad):
        if self.balance_cuenta >= cantidad:
            self.balance_cuenta -= cantidad
            print(f"Se realizo un retiro de {cantidad}.")
            return self
        else:
            print("Saldo insuficiente. No se pudo realizar el retiro.")
            return self

    def mostrar_balance_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Saldo: {self.balance_cuenta} unidades.")

    def transfer_dinero(self, usuario2, cantidad):
        if self.balance_cuenta >= cantidad:
            self.balance_cuenta -= cantidad
            usuario2.balance_cuenta += cantidad
            print(f"Se transfirieron {cantidad} de {self.nombre} {self.apellido} a {usuario2.nombre} {usuario2.apellido}.")
            return self
        else:
            print("Saldo insuficiente. No se pudo realizar la transferencia.")


user1=Usuario("Claudio", "Contreras", 300)
user2=Usuario("Lisa", "Simpson", 150)
user3=Usuario("Luis", "Perez", 500)

user1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(150).hacer_retiro(300).mostrar_balance_usuario()


user2.hacer_deposito(200).hacer_deposito(120).hacer_retiro(90).hacer_retiro(110).mostrar_balance_usuario()

user3.hacer_deposito(140).hacer_retiro(30).hacer_retiro(90).hacer_retiro(110).mostrar_balance_usuario()


user1.transfer_dinero(user3,100).mostrar_balance_usuario

user3.mostrar_balance_usuario()