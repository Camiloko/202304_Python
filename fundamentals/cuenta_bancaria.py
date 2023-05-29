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

cuenta1 = CuentaBancaria(10, 1600)
cuenta2 = CuentaBancaria(15, 2000)
cuenta1.deposito(100).deposito(200).deposito(100).retiro(500).generar_interes().mostrar_info_cuenta()
cuenta2.deposito(500).deposito(500).retiro(1000).retiro(100).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_info_cuentas()