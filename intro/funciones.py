#Función: un bloque de codigo dedicado a una tarea  específica que puede invocarse / llamarse las veces que sea necesario.

def saludo():
    print("Hola mundo!")

def saludoNombre(nombre):
    print(f'Hola {nombre}!')

def saludoLista(lista):
    for nombre in lista:
        print(f"Hola {nombre}!")

saludo()
saludoNombre("Fran")
saludoLista(["Juana","Elena","Maria","Pedro"])
###########################################################
def sumatoria(num1,num2):
    print("La suma es:", num1+num2)

def sumatoriaReturn(num1,num2):
    return num1+num2

sumatoria(5,6)
resultado = sumatoriaReturn(5,6) + sumatoriaReturn(7,7)
print(resultado)
###########################################################
def hello(nombre="Elena", apellido="De Troya"):
    print(f"Hola {nombre} {apellido}")

hello()
hello("Juana")
hello(apellido="De Arco")
hello(apellido="De Arco", nombre="Juana")
hello("Juana","De arco")
###########################################################
def multiplicacion(num1=1,num2=1):
 return num1*num2

print(multiplicacion())
print(multiplicacion(4))
print(multiplicacion(4,5))

###########################################################   RETOS   ###########################################################
print("################################################################")
#Función que reciba un arreglo y que regrese la suma de los valores del arreglo
#Ej: [1, 2, 3, 4] return 10
def sum(arr):
    suma = 0
    for num in arr:
        suma += num
    return suma

lista = [1,2,3,4]
print(sum(lista))

#Función que reciba un arreglo y que regrese el número mayor del arreglo
#Ej: [2, 4, 10] return 10
def mayor(arr):
    max = arr[0]
    for num in arr:
        if max < num:
            max = num
    return max

lista2 = [-3,-4,-2,-6,-1]
print(mayor(lista2))


#Función que reciba un arreglo y reciba un número y regrese True si el número se encuentra dentro del arreglo o False si NO se encuentra en el arreglo
#Ej: [2, 4, 6], 1 return False
#Ej: [2, 4, 6], 2 return True
def existe(arr, num):
    for i in range (len(arr)):
        if arr[i] == num:
            return True
    return False
        
lista3=[5,3,2,1,6]
print(existe(lista3,8))

#Función que reciba un arreglo y reemplace cualquier número negativo por 0. Regresa el arreglo SIN números negativos. Ej. Recibes: [1,5,10,-2], Regresas [1,5,10,0]
def positivo(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    return arr

lista4=[1,5,10,-2]
print(positivo(lista4))