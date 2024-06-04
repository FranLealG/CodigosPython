from Persona import Persona

elena = Persona("Elena", "De Troya", "elena@codingdojo.com", 18) #creando instancia de persona
juana = Persona("Juana", "De Arco", "juana@codingdojo.com", 22)

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

pedro = Persona("Pedro", "Perez", "pedro@codingdojo.com", 32)

print(len(Persona.lista_persona))

Persona.imprimir_todos()

pedro.licencia_conducir()