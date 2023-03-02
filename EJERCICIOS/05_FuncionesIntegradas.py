
#'''
#Ejecutar cada una de las funciones
#integradas mostradas en el el archivo 
#05_FuncionesIntegradas.txt

#Nota: Busque la manera para poder ejecutarlas······

#Entrada y salida
print("==========funcion entrada y salida==========")

x = input("Por favor ingrese un numero: ") #Recibe strings
x_num = int(x)
print("El numero ingresado fue: ", x_num, type(x_num))

#Ayuda

print("==========funcion ayuda==================")
datos = [1,2,3,4]
print("typo de dato =>", type(datos))  # Retorna el tipo de dato que se usa
print(dir(datos))

#help(datos)
datos.append(10000)
print(datos)

print("=====================Conversiones===============")

conv1=int(19.9) #devuelve  el 19
conv2=float("25") #devuelve el 25.0
conv3=bool(1) #devuelve true
conv4=list("hola") #
conv6=dict() #delvelve un tupla: &tres


rango=list(range(10,101,3))
rango1=list(range(-100,11,1))
rango2=list(range(-10,1,1))

print("el con paso de 3 en 3 es:  ", (rango))
print("el rango con paso de 1 en 1 desde -100 es:  ", (rango1))
print("el rango con paso de 1 en 1 desde -10 es:  ", (rango2))
