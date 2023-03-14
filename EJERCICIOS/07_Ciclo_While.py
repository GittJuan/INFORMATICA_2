#====================== EJERCICIOS CICLO WHILE ====================
#==> EJERCICIO 1 
"""Desarrolle un ciclo while infinito, con un mensaje que informe, cada vez que el ciclo es repetido."""
condicion=True 
repe=int(0)

while condicion:
    print("el ciclo se ha repetido", (repe), "Veces")
    repe=repe+1
    if repe==100:
        break
#==> EJERCICIO 2 
"""Realice un ciclo while con un numero secreto. Cada vez que se ejecuta un ciclo, el programa pide
adivinar el numero, en caso de no ser acertado se debe mostrar un mensaje diciendo: "Estás atrapado". 
Y en caso contrario terminar el ciclo y avisar que el numero es correcto."""
numsecreto=int(7)
intentos=int(0)

while True:
    # Pedimos al usuario que adivine el número
    adivinanza = int(input("Adivina el número secreto (entre 1 y 10): "))
    intentos += 1
    if adivinanza == numsecreto:
        # Si es correcta, mostramos un mensaje de felicitación y salimos del ciclo
        print(f"¡Felicitaciones! Adivinaste el número en {intentos} intentos.")
        break
    else:
        # Si no es correcta, mostramos un mensaje de error y continuamos el ciclo
        print("Estás atrapado. Intenta nuevamente.")
#==> EJERCICIO 3 
"""Realice un programa, que determine el número mayor para una cantidad indeterminada de numeros. (Utilice el ciclo while)"""

#==> EJERCICIO 4 
"""Realice un programa que lea una secuencia de números, y cuente cuántos números son pares y cuántos son impares. 
El programa termina cuando se ingresa el número cero."""
# Inicializamos las variables para guardar la cantidad de números pares e impares
pares = 0
impares = 0

# Creamos un ciclo while que se ejecuta hasta que se ingresa el número cero
while True:
    # Pedimos al usuario que ingrese un número o el número cero
    entrada = int(input("Ingresa un número o escribe 0 para terminar: "))
    
    # Verificamos si la entrada es el número cero
    if entrada == 0:
        # Si es el número cero, salimos del ciclo
        break
    
    # Verificamos si el número es par o impar
    if entrada % 2 == 0:
        # Si es par, incrementamos el contador de números pares
        pares += 1
    else:
        # Si es impar, incrementamos el contador de números impares
        impares += 1
        
# Mostramos la cantidad de números pares e impares guardar en gitr
print(f"Se ingresaron {pares} números pares y {impares} números impares.")

#==> Ejercicio 5 
"""Utilizando el ciclo while, imprima las siguientes secuencias de numeros:
=> 2,4,5,8,10,11,14,16,17,20 ...598, 599
=> 2,4,8,16,32,64,128, .. 1048576
=> 1,1,2,3,5,8, ... 2178309"""