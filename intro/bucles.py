#==== CONDICIONALES ====
x = 20
if x > 10:
    print("El numero ingresado es mayor a 10")
    print("El numero es:", x)
    print(f"El numero es: {x}. Es decir, el numero es: {x} ") #Format: interpolar variables
    #Otra
    #Otra
else:
    print("El numero es menor o igual a 10")
edad_infante = 4
if edad_infante < 2:
    print("Es un bebe")
elif edad_infante < 5: #elif = else if
    print("Es un toddler")
else:
    print("Es un niño")
y = 5
if y > 3:
    print("Numero mayor a 3")
else:
    print("Numero menor o igual a 3")
    print("tu numero es menor a 3")
temperatura = 20
estaLloviendo = False
if temperatura > 18 and not estaLloviendo: #and == && not = !
    print("Salgamos a pasear al parque")
edad = input("Ingresa tu edad:") #str
edad = int(edad)
permisoPadres = True
if edad > 18 or permisoPadres: #si una u otra se cumple
    print("Puedes obtener tu licencia de manejo")
    #Otra linea
    #Otra linea
    #Otra linea
    #Otra linea

#==== BUCLE/CICLOS ====
for x in range(5): #Rango 0-4. 5 YA NO ENTRA. x < 5
    print(x)

print("-------")

for y in range(5, 13): #(Comienzo, Fin) -> y=5; y<13
    print(y)

print("-------")

for z in range(2, 12, 2): #(Comienzo, Fin, Paso) -> z=2; z < 12; z+=2
    print(z)

print("-------")

for m in range(30, 15, -2):
    print(m)

#RECORRER UN ARREGLO
lista_nombres = ["Elena", "Juana", "Pablo", "Pedro"]
for nombre in lista_nombres:
    print(nombre)

for indice in range(len(lista_nombres)): #i=0; i < 4. i = indice
    print(f"Indice: {indice}; Valor: {lista_nombres[indice]}")

estudiante = { #Equivalente a objetos en javascript
    "nombre": "Elena", #clave: valor
    "apellido": "De Troya",
    "edad": 19
}
'''
dato = "nombre"
print Clave:nombre. Valor: Elena
---
dato = "apellido"
print Clave: apellido. Valor: De Troya
---
dato = "edad"
print Clave: edad. Valor: 19
'''
for dato in estudiante: #recorre claves
    print(f"Clave: {dato}. Valor:{estudiante[dato]}")

lista_estudiantes = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345}
]

for estudiante in lista_estudiantes:
    print(estudiante)
    for dato in estudiante:
        print(f"Clave: {dato}. Valor:{estudiante[dato]}")

texto = "Buen día"
for letra in texto:
    print(letra)

inicio = 0
final = 5
while inicio < final:
    print(f"inicio: {inicio}. Final: {final}")
    inicio += 1
    final -= 2

i = 4
while i < 7:
    print("Entra a while.", i)
    i += 1
else:
    print("Dejó de cumplirse condicional.", i)


#Dado al for del 1 a 15, imprime todos los numeros EXCEPTO aquellos multiplos de 5
print("________________________________________________")
for i in range(1, 15):
    if i%5 == 0:
        continue
    print(i)

#Dada una cadena, imprime cada unos de los caracteres y que se detenga POR COMPLETO si encuentra un . (punto)
print("________________________________________________")
cadena = "Hola, soy Fran. Cómo estás?"
for letra in cadena:
    if letra == ".":
        break
    print(letra)
    