from Usuario import Usuario

Juan = Usuario("Juan", "Perez", "jp@gmail.com")
Maria = Usuario("Maria", "Gonzalez", "mg@gmail.com")
Juana = Usuario("Juana", "De Arco", "jda@gmail.com")

print("############ 1 ############")
Juan.hacer_compra(1000)
Juan.hacer_compra(3500)
Juan.pagar_tarjeta(4500)
Juan.mostrar_saldo_usuario()

print("############ 2 ############")
Maria.hacer_compra(5000)
Maria.pagar_tarjeta(1500)
Maria.pagar_tarjeta(3500)
Maria.mostrar_saldo_usuario()

print("############ 3 ############")
Juana.hacer_compra(7300)
Juana.hacer_compra(6000)
Juana.hacer_compra(10000)
Juana.pagar_tarjeta(5400)
Juana.pagar_tarjeta(1900)
Juana.pagar_tarjeta(9600)
Juana.pagar_tarjeta(6400)
Juana.mostrar_saldo_usuario()

print("############ Bonus ############")
Juan.transferir_deuda(Maria, 5000)
Juan.mostrar_saldo_usuario()
Maria.mostrar_saldo_usuario()