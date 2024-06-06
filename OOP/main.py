from Persona import Persona
#from Animal import Animal
from gato import Gato
from perro import Perro

##########################################
# aurora = Animal("Aurora", "miau")
# jacinta = Animal("Jacinta", "miau")
# moncho = Animal("Moncho", "guau")

# aurora.hacer_sonido()
##########################################

elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 18, "milli", "AWAWAW") #creando instancia de persona
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 22, "lautaro", "GRRRR")

print(elena.nombre)
print(juana.nombre)
print(juana.edad)
elena.imprimir()

elena.saludar()
juana.saludar()

juana.codificar(15)
juana.codificar(100)
print(juana.linas_codigo)

#cambiando para toda la escuela programación
Persona.escuela = "Escuela de programación"
print(elena.escuela)
print(juana.escuela)

pedro = Persona("Pedro", "Perez", "pedro@codingdojo.com", 32, "Candela", "zzz")

print(len(Persona.lista_persona))

Persona.imprimir_todos()

pedro.licencia_conducir()

#####################################
pedro.mascota.hacer_sonido()

#####################################
miu = Gato("Michi", "meow", "corto")
pluto = Perro("Pluto", "Woof", "golden")

miu.rascar_sofa()
miu.hacer_sonido()
pluto.hacer_sonido()
pluto.perseguir_auto()
miu.ir_baño()
pluto.ir_baño()