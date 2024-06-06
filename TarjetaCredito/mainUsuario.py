from Usuario import Usuario


user1 = Usuario("Matias", "Lopez", "mlopez@gmail.com")
user2 = Usuario("Roberto", "Muñoz", "robertoskap@gmail.com")
#user1.hacer_compra(200).hacer_compra(1800).pagar_tarjeta(1100).mostrar_saldo_usuario()

user1.agregar_tarjeta(0, 5000, 0.01)
user1.agregar_tarjeta(0, 2000, 0.02)

user2.agregar_tarjeta(0, 3000, 0.01)
user2.agregar_tarjeta(0, 4000, 0.012)
user2.agregar_tarjeta(0, 6000, 0.032)

user1.hacer_compra(200, 1).hacer_compra(300, 1).hacer_compra(1000, 2).pagar_tarjeta(300, 1).pagar_tarjeta(230, 2)