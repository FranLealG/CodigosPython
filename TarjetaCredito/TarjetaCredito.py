class TarjetaCredito:

    lista_tarjetas = []

    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.lista_tarjetas.append(self)

    
    def compra(self, monto):
        if self.saldo_pagar+monto <= self.limite_credito:
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito.")
        return self


    def pago(self, monto):
        self.saldo_pagar -= monto
        return self
        

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    #BONUS
    def imprimir(self):
        print(f"El saldo a pagar es de: ${self.saldo_pagar}\nEl límite es de: ${self.limite_credito}\nLos intereses son de: {self.intereses}")

    @classmethod
    def info_instancias(cls):
        cont = 1
        for dato in cls.lista_tarjetas:
            print(f"####### Tarjeta {cont} #######")
            cont+=1
            dato.imprimir()
    