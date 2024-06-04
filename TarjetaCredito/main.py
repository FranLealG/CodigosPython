from TarjetaCredito import TarjetaCredito

mach = TarjetaCredito(0, 10000, 0.03)
tenpo = TarjetaCredito(0, 10500, 0.05)
bco_chile = TarjetaCredito(0, 7000, 0.02)

print("########## 1 ##########")
mach.compra(4300).compra(2200).pago(3500).cobrar_interes().mostrar_info_tarjeta()
print("########## 2 ##########")
tenpo.compra(3200).compra(4000).compra(800).pago(2000).pago(3200).cobrar_interes().mostrar_info_tarjeta()
print("########## 3 ##########")
bco_chile.compra(2000).compra(500).compra(1500).compra(3000).compra(1000).mostrar_info_tarjeta()
print("########## BONUS ##########")
TarjetaCredito.info_instancias()