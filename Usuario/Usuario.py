class Usuario:
    def __init__(self, nombre, apellido, email):

       self.nombre = nombre
       self.apellido = apellido
       self.email = email
       self.limite_credito = 30000
       self.saldo_pagar = 0
  
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
       self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

    def pagar_tarjeta(self, monto):
       self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
       print(f"Usario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):
       self.saldo_pagar -= monto
       otro_usuario.saldo_pagar += monto