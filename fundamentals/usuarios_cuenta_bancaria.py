class CuentaBancaria:
    
    todas_las_cuentas = []

    def __init__(self, tasa_interes, monto=0):
        self.tasa_interes = tasa_interes
        self.balance = monto
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, cantidad):
        self.balance += cantidad
        print(f"Se realizo un deposito de ${cantidad}")
        return self

    def retiro(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f"Se realizo un retiro de ${cantidad}")
            return self
        else:
            self.balance -= 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
            return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")

    def generar_interes(self):
        if self.balance > 0:
            intereses = self.balance * (self.tasa_interes/100)
            self.balance += intereses
            print(f"Se genero un interes de ${intereses}")
            return self

    @classmethod
    def imprimir_info_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f"Tasa de interés: {cuenta.tasa_interes}")
            print(f"Balance: ${cuenta.balance}")
            print()


class Usuario:
    def __init__(self, nombre, apellido,cuenta_bancaria=None):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta_bancaria=CuentaBancaria(tasa_interes=0.02, monto=0)
        
    def hacer_deposito(self, cantidad):
        if self.cuenta_bancaria is not None:
            self.cuenta_bancaria.deposito(cantidad)
            return self
        else:
            print("El usuario no tiene una cuenta bancaria asociada.")

    def hacer_retiro(self, cantidad):
        if self.cuenta_bancaria is not None:
            self.cuenta_bancaria.retiro(cantidad)
            return self
        else:
            print("El usuario no tiene una cuenta bancaria asociada.")

    def mostrar_balance_usuario(self):
        if self.cuenta_bancaria is not None:
            print(f"Usuario: {self.nombre} {self.apellido}")
            self.cuenta_bancaria.mostrar_info_cuenta()
            return self
        else:
            print("El usuario no tiene una cuenta bancaria asociada.")

    def transfer_dinero(self, other_user, cantidad):
        if self.cuenta_bancaria is not None and other_user.cuenta_bancaria is not None:
            self.cuenta_bancaria.retiro(cantidad)
            other_user.cuenta_bancaria.deposito(cantidad)
            return self
        else:
            print("Al menos uno de los usuarios no tiene una cuenta bancaria asociada.")

cuenta1=CuentaBancaria(5,1000)
cuenta2=CuentaBancaria(10,2400)
cuenta3=CuentaBancaria(15,800)

user1=Usuario("Claudio", "Contreras", cuenta1)
user2=Usuario("Lisa", "Simpson", cuenta2)
user3=Usuario("Luis", "Perez", cuenta3)

user1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(150).hacer_retiro(300).mostrar_balance_usuario()


user2.hacer_deposito(200).hacer_deposito(120).hacer_retiro(90).hacer_retiro(110).mostrar_balance_usuario()

user3.hacer_deposito(140).hacer_retiro(30).hacer_retiro(90).hacer_retiro(110).mostrar_balance_usuario()


user1.transfer_dinero(user3,100).mostrar_balance_usuario

user3.mostrar_balance_usuario()