# Crea la función multiplica_por_dos(num)
def multiplica_por_dos(num):
    arr=[]
    for i in range (num+1):
        arr.append(i*2)
    return arr
#print(multiplica_por_dos(4))

# Crea la función suma_y_resta(lista)
def suma_y_resta(lista):
    if len(lista) == 2:
        sum = 0
        res = lista[0]
        for i in range(len(lista)):
            sum += lista[i]
            if i == 0:
                continue
            else:
                res -= lista[i]
    print(sum)
    return res

#print(suma_y_resta([3,2]))

def suma_y_resta2(lista):
    print(lista[0]+lista[1])
    return(lista[0]-lista[1])
#print(suma_y_resta2([5,4]))

# Crea la función sumatoria_menos_longitud(lista)
def sumatoria_menos_longitud(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma-len(lista)

#print(sumatoria_menos_longitud([4,3,2,1,10]))

# Crea la función valores_multiplicados_segundo(lista)
def valores_multiplicados_segundo(lista):
    arr = []
    if len(lista) < 2:
        print(len(lista))
        return arr
    else:
        print("largo: ",len(lista))
        for i in range(len(lista)):
            i = (lista[i])*(lista[1])
            arr.append(i)
        return arr

#print(valores_multiplicados_segundo([3,2,1,5]))

# Crea la función valor_multiplicado_longitud(valor, longitud)
def valor_multiplicado_longitud(valor, longitud):
    arr = []
    for i in range(longitud):
        arr.append(valor*longitud)
    return arr

print(valor_multiplicado_longitud(3,7))