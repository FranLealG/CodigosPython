########################################### EJERCICIO 1 ###########################################
matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6
print("1 ",matriz)

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("2", cantantes[0])

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print("3", ciudades["México"])
      
# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431
print("4", coordenadas)

########################################### EJERCICIO 2 ###########################################
def iterarDiccionario(lista):
    for i in lista:
        print("nombre -",i["nombre"]+", país -",i["pais"])

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
iterarDiccionario(cantantes)

########################################### EJERCICIO 3 ###########################################
def iterarDiccionario2(llave, lista):
    for i in lista:
        print(i[llave])

#usé el mismo diccionario de cantantes
iterarDiccionario2("pais",cantantes)

########################################### EJERCICIO 4 ###########################################
def imprimirInformacion(diccionario):
    for dato in diccionario:
        print(len(diccionario[dato]),dato.upper())
        for i in diccionario[dato]:
            print(i)

chile = {
   "ciudades": ["Arica", "Concepción", "Talca", "Santiago", "Punta Arenas"],
   "comidas": ["porotos con riendas", "charquicán", "sopaipillas", "empanadas"]
}

imprimirInformacion(chile)