# Imprimir en la terminal

# Dos enteros en una misma linea
# Dos flotantes en una misma linea
# Dos booleanos en una misma linea
# Dos listas en una misma linea
# Un diccionario

print(1, 2)
print(1.5, 1.4)
print(True, False)
print([1,2,3], [4,5,6])
print({"hola":"hello"})

#Imprimir qué tipo de dato son
#los siguientes datos

# 100000001
# 0.00000000000001
# [0,0,0,0]
# {1,2,3}

print(type(100000001))
print(type(0.00000000000001))
print(type([0,0,0,0]))
print(type({1,2,3}))

# Crear variables y asignarles los siguientes tipos de datos:

# Enteros: 1,2,3 999
# Luego reste sucesivamente del ultimo al primero y almacenelo
# en una variable llamada resultado1 

a = 1
b = 2
c = 3
d = 999

resultado1 = d-c-b-a
print("resultado1 ==> ", resultado1)

# Flotantes: 15.2, 29.5, 18.28
# Luego divida sucesivamente del primero al ultimo
# y almacenelo en una variable llamada resultado2

v1 = 15.2
v2 = 29.5
v3 = 18.28

resultado2 = v1/v2/v3
print("resultado2 ==> ", resultado2)

# Strings: "123", "Cristian" 
# Luego sume ambas variables y determine si la 
# operacion es posible, si asi es almacenelo en una variable
# de su eleccion

string1 = "123"
string2 = "Cristian"
sumaStrings = string1 + string2
print("sumaStrings ==>", sumaStrings)


######## EJERCICIOS CONVERSIONES ######

# Busque una manera de convertir:
# un entero a un flotante
# un flotante a un entero
# un string a un entero 
# un numero a un string

entero = 10
flotante = 15.59
string1 = "hola info"
string2 = "1234"
cualquiera = 1234567890

conv1 = float(entero)
conv2 = int(flotante)
conv3 = int(string1)
conv4 = int(string2)
conv5 = str(cualquiera)

print("entero a flotante ==> ", conv1)
print("flotante a entero ==> ", conv2)
print("string1 a entero  ==> ", conv3)
print("string2 a entero  ==> ", conv4)
print("numero a string   ==> ", conv5, type(conv5))