print("Hola mundo")

#variables
booleano = True #True o False
num = 10 #num entero
fl = 10.99 #num float
parse_float = float(num)
print(parse_float)
parse_entero = int(fl)
print(parse_entero)
print(round(fl))

import random
num_random = random.randint(1,5)
print(num_random)

#Cadenas
abc = "ABCDEFG"
otro_txt = "otro texto"
print("Este es el abecedario: ", abc) #1
print("Este es el abecedario: "+abc) #2
print(otro_txt+" "+abc) #1
print(otro_txt,abc) #2
print("este es un número",num)
print("este es un número:"+str(num))

nombre = "Juana"
apodo = "Juanita"
print(f"Hola, te presento a {nombre}, le puedes llamar '{apodo}'")
print("Hola, te presento a "+nombre+", le puedes llamar '"+apodo+"'")

#Métodos de manipulacion de cadenas
frase = "Hola mundo! soy Juana de Arco y hoy es 27 de mayo"
print(frase.title()) #primera letra de cada palabra en mayus
print(frase.upper()) #todo en mayus
print(frase.lower()) #todo en minus
print(frase.count('oy')) #regresa cuantos 'oy' hay en la frase
print(frase.find('Juana')) #indice en donde se encuentra la palabra. Case-sensitive
print(frase.find('juana')) #entrega -1 porque no existe en la frase
print(frase[-1]) #regresa la última letra

#Estructuras de datos
#tuplas: parecido a un arreglo. No puedo cambiar valores. Pueden tener distintos tipos de datos
tupla = ("Elena", "Juana", "Pedro", "Pablo")
print(tupla[0])
tupla2 = ("texto", 7, False, 6.6)
#listas/array/arreglo
lista_name = ["Hugo", "Paco", "Luis"]
print(lista_name[2])
lista_name[2] = "Donald"
print(lista_name)
lista_name.pop()
print(lista_name)
lista_name.pop(0)
print(lista_name)
lista_name.append("Mickey")
print(lista_name)
lista_name.insert(1, "Goofy")
print(lista_name)

lista_mix = ["texto", 11, True, 1.1, ["elemento1", "elemento2"]]
matriz =[
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9]
]

print(matriz[1][2])
print(lista_mix[4][1])

#Diccionario
estudiante = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "edad": 18,
    "soltera": True,
    "hobbies": ["leer", "comer", "salir al parque"]
}
print(estudiante["nombre"])
estudiante["edad"] = 19
print(estudiante)
estudiante.pop("soltera")

lista_alumnos = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#como eliminar el elemento MERN de Pedro
print(lista_alumnos[2]["cursos"][2])
lista_alumnos[2]["cursos"].pop(2)
print(lista_alumnos[2])

'''
COMENTARIOS MAS
EXTEN
SOS
'''
from pprint import pprint
pprint(lista_alumnos)