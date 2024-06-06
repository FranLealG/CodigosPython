from TarjetaCredito import TarjetaCredito

class Usuario:

    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

        self.tarjetas = []

    def hacer_compra(self, monto, id):
        self.tarjetas[id -1].compra(monto)
        print(f"Hizo una compra de: ${monto} con la tarjeta {id}. Debe {self.tarjetas[id-1].saldo_pagar}")
        #self.tarjeta.compra(monto)
        return self
    
    def pagar_tarjeta(self, monto, id):
        self.tarjetas[id -1].pago(monto)
        print(f"Pagó ${monto} de la tarjeta {id}. Ahora su deuda es de ${self.tarjetas[id-1].saldo_pagar}")
        #self.tarjeta.pago(monto)
        return self
    
    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}")
        self.tarjeta.mostrar_info_tarjeta()

    #BONUS
    def agregar_tarjeta(self, saldo, limite, interes):
        tarjeta = TarjetaCredito(saldo, limite, interes)
        self.tarjetas.append(tarjeta)
        print(f"El ID de la tarjeta agregada es: ", len(self.tarjetas))