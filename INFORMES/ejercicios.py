"""Recomendaciones:
 - Recuerde almacenar las respuestas tal como se pide en cada ejercicio
 - Se resuelve de manera individual, la copia será anulada.
 - Muestre sus procedimientos de manera clara"""

nombre_completo = "Juan Sebastian Rodriguez Rodriguez"    #Por favor ingrese su nombre en las comillas


#------------------------ EJERCICIO 1 --------------------------------
"""
Cree los siguientes rangos (tipo range()): 
   rango1 => 334, 331, 328, 325, ... 4, 1
   rango2 => -5,-3,-1, 1, 3, 5, ... 999
   rango3 => -50, -55, -60, -65, -70, ... -195, -200
Después de obtener los rangos, almacenelos de la siguiente manera:
listaDeRangos = [rango1, rango2, rango3]

"""
#Definimos los 3 rangos y asignamos los valores e la siguinte manera
rango1 = range(334, 0, -3)
rango2 = range(-5, 1000, 2)
rango3 = range(-50, -205, -5)

#teniendo en cuenta que la primera entrada define que donde empieza el rango, 
listaDeRangos = [rango1, rango2, rango3]
#------------------------ EJERCICIO 2 --------------------------------
"""
Dados los siguientes puntos geométricos:
"P1" ==> (2, 2, 3)              "P6"  ==> (1, 0.5, 1)
"P2" ==> (2, 3, 4)              "P7"  ==> (3, 2, 0.5)
"P3" ==> (1, 1, 3)              "P8"  ==> (3, 1, 2)
"P4" ==> (0.5, 0.5, 2)          "P9"  ==> (0, 0, 0)
"P5" ==> (1, 2, 1)              "P10" ==> (2, 0, 0.5) 
Determine el par de puntos que se encuentran más cercanos.
Almacene la respuesta en un string llamado parCercano. Ejemplo:
parCercano = "P2-P3" 
"""
# Definir los puntos
P1 = (2, 2, 3)
P2 = (2, 3, 4)
P3 = (1, 1, 3)
P3 = (1, 1, 3)
P4 = (0.5, 0.5, 2)
P5 = (1, 2, 1)
P6 = (1, 0.5, 1)
P7 = (3, 2, 0.5)
P8 = (3, 1, 2)
P9 = (0, 0, 0)
P10 = (2, 0, 0.5)

# Calcular las distancias entre todos los pares de puntos
d1 = ((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2 + (P1[2]-P2[2])**2)**0.5
d2 = ((P1[0]-P3[0])**2 + (P1[1]-P3[1])**2 + (P1[2]-P3[2])**2)**0.5
d3 = ((P1[0]-P4[0])**2 + (P1[1]-P4[1])**2 + (P1[2]-P4[2])**2)**0.5
d4 = ((P1[0]-P5[0])**2 + (P1[1]-P5[1])**2 + (P1[2]-P5[2])**2)**0.5
d5 = ((P1[0]-P6[0])**2 + (P1[1]-P6[1])**2 + (P1[2]-P6[2])**2)**0.5
d6 = ((P1[0]-P7[0])**2 + (P1[1]-P7[1])**2 + (P1[2]-P7[2])**2)**0.5
d7 = ((P1[0]-P8[0])**2 + (P1[1]-P8[1])**2 + (P1[2]-P8[2])**2)**0.5
d8 = ((P1[0]-P9[0])**2 + (P1[1]-P9[1])**2 + (P1[2]-P9[2])**2)**0.5
d9 = ((P1[0]-P10[0])**2 + (P1[1]-P10[1])**2 + (P1[2]-P10[2])**2)**0.5


d10 = ((P2[0]-P3[0])**2 + (P2[1]-P3[1])**2 + (P2[2]-P3[2])**2)**0.5
d11 = ((P2[0]-P4[0])**2 + (P2[1]-P4[1])**2 + (P2[2]-P4[2])**2)**0.5
d12 = ((P2[0]-P5[0])**2 + (P2[1]-P5[1])**2 + (P2[2]-P5[2])**2)**0.5
d13 = ((P2[0]-P6[0])**2 + (P2[1]-P6[1])**2 + (P2[2]-P6[2])**2)**0.5
d14 = ((P2[0]-P7[0])**2 + (P2[1]-P7[1])**2 + (P2[2]-P7[2])**2)**0.5
d15 = ((P2[0]-P8[0])**2 + (P2[1]-P8[1])**2 + (P2[2]-P8[2])**2)**0.5
d16 = ((P2[0]-P9[0])**2 + (P2[1]-P9[1])**2 + (P2[2]-P9[2])**2)**0.5
d17 = ((P2[0]-P10[0])**2 + (P2[1]-P10[1])**2 + (P2[2]-P10[2])**2)**0.5


d18 = ((P3[0]-P4[0])**2 + (P3[1]-P4[1])**2 + (P3[2]-P4[2])**2)**0.5
d19 = ((P3[0]-P5[0])**2 + (P3[1]-P5[1])**2 + (P3[2]-P5[2])**2)**0.5
d20 = ((P3[0]-P6[0])**2 + (P3[1]-P6[1])**2 + (P3[2]-P6[2])**2)**0.5
d21 = ((P3[0]-P7[0])**2 + (P3[1]-P7[1])**2 + (P3[2]-P7[2])**2)**0.5
d22 = ((P3[0]-P8[0])**2 + (P3[1]-P8[1])**2 + (P3[2]-P8[2])**2)**0.5
d23 = ((P3[0]-P9[0])**2 + (P3[1]-P9[1])**2 + (P3[2]-P9[2])**2)**0.5
d24 = ((P3[0]-P10[0])**2 + (P3[1]-P10[1])**2 + (P3[2]-P10[2])**2)**0.5


d25 = ((P4[0]-P5[0])**2 + (P4[1]-P5[1])**2 + (P4[2]-P5[2])**2)**0.5
d26 = ((P4[0]-P6[0])**2 + (P4[1]-P6[1])**2 + (P4[2]-P6[2])**2)**0.5
d27 = ((P4[0]-P7[0])**2 + (P4[1]-P7[1])**2 + (P4[2]-P7[2])**2)**0.5
d28 = ((P4[0]-P8[0])**2 + (P4[1]-P8[1])**2 + (P4[2]-P8[2])**2)**0.5
d29 = ((P4[0]-P9[0])**2 + (P4[1]-P9[1])**2 + (P4[2]-P9[2])**2)**0.5
d30 = ((P4[0]-P10[0])**2 + (P4[1]-P10[1])**2 + (P4[2]-P10[2])**2)**0.5


d31 = ((P5[0]-P6[0])**2 + (P5[1]-P6[1])**2 + (P5[2]-P6[2])**2)**0.5
d32 = ((P5[0]-P7[0])**2 + (P5[1]-P7[1])**2 + (P5[2]-P7[2])**2)**0.5
d33 = ((P5[0]-P8[0])**2 + (P5[1]-P8[1])**2 + (P5[2]-P8[2])**2)**0.5
d34 = ((P5[0]-P9[0])**2 + (P5[1]-P9[1])**2 + (P5[2]-P9[2])**2)**0.5
d35 = ((P5[0]-P10[0])**2 + (P5[1]-P10[1])**2 + (P5[2]-P10[2])**2)**0.5


d36 = ((P6[0]-P7[0])**2 + (P6[1]-P7[1])**2 + (P6[2]-P7[2])**2)**0.5
d37 = ((P6[0]-P8[0])**2 + (P6[1]-P8[1])**2 + (P6[2]-P8[2])**2)**0.5
d38 = ((P6[0]-P9[0])**2 + (P6[1]-P9[1])**2 + (P6[2]-P9[2])**2)**0.5
d39 = ((P6[0]-P10[0])**2 + (P6[1]-P10[1])**2 + (P6[2]-P10[2])**2)**0.5


d40 = ((P7[0]-P8[0])**2 + (P8[1]-P8[1])**2 + (P8[2]-P8[2])**2)**0.5
d41 = ((P7[0]-P9[0])**2 + (P8[1]-P9[1])**2 + (P8[2]-P9[2])**2)**0.5
d42 = ((P7[0]-P10[0])**2 + (P8[1]-P10[1])**2 + (P8[2]-P10[2])**2)**0.5


d43 = ((P8[0]-P9[0])**2 + (P8[1]-P9[1])**2 + (P8[2]-P9[2])**2)**0.5
d44 = ((P8[0]-P10[0])**2 + (P8[1]-P10[1])**2 + (P8[2]-P10[2])**2)**0.5


d45 = ((P9[0]-P10[0])**2 + (P9[1]-P10[1])**2 + (P9[2]-P10[2])**2)**0.5


# Encontrar la distancia mínima
dist_min = min(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25, d26, d27, d28, d29, d30, d31, d32, d33, d34, d35, d36, d37, d38, d39, d40, d41, d42, d43, d44, d45 )

# Encontrar los puntos más cercanos
if dist_min == d1:
    parCercano = "P1-P2"
elif dist_min == d2:
    parCercano = "P1-P3"
elif dist_min == d3:
        parCercano = "P1-P4"
elif dist_min == d4:
            parCercano = "P1-P5"
elif dist_min == d5:
                parCercano = "P1-P6"
elif dist_min == d6:
                    parCercano = "P1-P7"
elif dist_min == d7:
                        parCercano = "P1-P8"
elif dist_min == d8:
                            parCercano = "P1-P9"
elif dist_min == d9:
                                parCercano = "P1-P10"
elif dist_min == d10:
                                    parCercano = "P2-P3"
elif dist_min == d11:
                                        parCercano = "P2-P4"
elif dist_min == d12:
                                    parCercano = "P2-P5"
elif dist_min == d13:
                                parCercano = "P2-P6"
elif dist_min == d14:
                            parCercano = "P2-P7"
elif dist_min == d15:
                        parCercano = "P2-P8"
elif dist_min == d16:
                    parCercano = "P2-P9"
elif dist_min == d17:
                parCercano = "P2-P10"
elif dist_min == d18:
            parCercano = "P3-P4"
elif dist_min == d19:
        parCercano = "P3-P5"
elif dist_min == d20:
    parCercano = "P3-P6"
elif dist_min == d21:
 parCercano = "P3-P7"
elif dist_min == d22:
 parCercano = "P3-P8"
elif dist_min == d23:
    parCercano = "P3-P9"
elif dist_min == d24:
        parCercano = "P3-P10"
elif dist_min == d25:
            parCercano = "P4-P5"
elif dist_min == d26:
                parCercano = "P4-P6"
elif dist_min == d27:
                    parCercano = "P4-P7"
elif dist_min == d28:
                        parCercano = "P4-P8"
elif dist_min == d29:
                            parCercano = "P4-P9"
elif dist_min == d30:
                                parCercano = "P4-P10"
elif dist_min == d31:
                                    parCercano = "P5-P6"
elif dist_min == d32:
                                        parCercano = "P5-P7"
elif dist_min == d33:
                                            parCercano = "P5-P8"
elif dist_min == d34:
                                                parCercano = "P5-P9"
elif dist_min == d35:
                                            parCercano = "P5-P10"
elif dist_min == d36:
                                        parCercano = "P6-P7"
elif dist_min == d37:
                                    parCercano = "P6-P8"
elif dist_min == d38:
                                parCercano = "P6-P9"
elif dist_min == d39:
                            parCercano = "P6-P10"
elif dist_min == d40:
                        parCercano = "P7-P8"
elif dist_min == d41:
                    parCercano = "P7-P9"
elif dist_min == d42:
                parCercano = "P7-P10"
elif dist_min == d43:
            parCercano = "P8-P9"
elif dist_min == d44:
        parCercano = "P8-P10"
else:
    parCercano = "P9-P10"

print(parCercano)

#------------------------ EJERCICIO 3 --------------------------------
"""
La calificación de informatica se encuentra en el intervalo [0,5] y se calcula tomando 5 notas, 
con porcentajes de 10%, 20%, 15%, 20% y 35%. La materia se aprueba por encima de 3.0
Los siguientes estudiantes tienen las primeras 4 calificaciones definidas.
cod      Nombre          Nota1   Nota2  Nota3  Nota4  Nota 5
01    Miguel Pineda        1.0    1.1    2.3    1.1     ?
02    Maria Gonzalez       3.1    3.1    1.2    3.0     ?
03    Jose Nuñez           5.0    4.0    2.5    5.0     ?
04    Angelica Lozano      3.1    1.0    2.6    1.0     ?
05    Camilo Suarez        3.2    4.0    1.1    3.0     ?
06    Mariana Rosero       5.0    5.0    5.0    3.9     ?
07    Esteban Quesada      3.4    4.0    2.6    3.2     ?
08    Julia Quintero       2.0    2.2    2.1    4.2     ?
09    Mauricio Lizcano     3.7    4.1    4.7    4.0     ?
10    Angie Gomez          4.1    4.7    4.4    5.0     ?
11    Camilo Restrepo      5.0    5.0    1.0    3.2     ?
12    Mauricio Velazquez   5.0    4.2    2.1    5.0     ?
13    Esteban Rodriguez    3.2    4.1    2.2    3.3     ?
   Determine cuantos estudiantes pierden aúnque obtengan la mejor nota5
   Determine cuantos estudiantes ganan aunque obtengan la peor nota5
   Determine cuantos estudiantes tienen posibilidades de pasar
   Almacene sus resultados en una lista llamada estudiantes, tal como se muestra:
   estudiantes = [Cantidad_que_pierden, Cantidad_que_ganan, Cantidadsib_con_poilidades]
"""
#inicializamos nuestra lista donde seran almacenadas todas las variables

#------------------------ EJERCICIO 4 --------------------------------
""" Seis compañeros, contratan un taxi con el objeto de movilizarse juntos a la universidad. 
El contrato es de lunes a viernes, y deben pagar al taxista $15000 por cada trayecto. 
Se prestarán dos servicios al día, uno de ida y el otro de regreso.
Sin embargo, los seis no se movilizan juntos todos los dias. Por tanto, han planteado que la tarifa
debe dividirse entre el numero de compañeros que se movilicen en cada trayecto.En caso, de que ninguno
utilice el servicio. Deben pagar al taxista una tarifa de $10000, repartidos equitativamente entre todos.
A continueación veamos el uso del servicio por parte de los compañeros en la última semana de clases:
                            IDA                             |                       REGRESO
            LUNES   MARTES  MIERCOLES   JUEVES  VIERNES     |    LUNES   MARTES  MIERCOLES   JUEVES  VIERNES
JUAN          Si        Si        Si      Si      No        |      Si        Si        Si      No       No
CAMILA        Si        No        Si      No      Si        |      Si        No        No      No       No
JOSE          Si        No        Si      Si      No        |      Si        No        Si      Si       No
MARIA         Si        Si        Si      No      No        |      No        No        Si      No       No
ESTEBAN       Si        No        No      Si      Si        |      No        No        No      Si       No
ANGIE         Si        No        Si      No      No        |      Si        No        Si      No       No
¿Cuanto debe pagar cada estudiante? 
Almacene el resultado dentro de un diccionario llamado "diccionarioPagos"
las claves deben ser los nombres de los estudiantes (en strings)
y los valores deben ser el dinero total que pagó cada uno al terminar la semana (en flotantes)
"""

matriz_uso = [
    [1, 1, 1, 1, 1, 1],  # Lunes
    [1, 0, 0, 1, 0, 0],  # Martes
    [1, 1, 1, 1, 0, 1],  # Miercoles
    [1, 0, 1, 0, 1, 0],  # Jueves
    [0, 1, 0, 0, 1, 0],  # Viernes
    [1, 1, 1, 0, 0, 1],  # Lunes Retorno
    [1, 0, 0, 0, 0, 1],  # Martes Retorno
    [1, 0, 1, 1, 0, 0],  # Miercoles Retorno
    [0, 1, 1, 0, 1, 1],  # Jueves Retorno
    [0, 0, 0, 0, 0, 0]   # Viernes Retorno
]


TRAYECTO = 15000
TRAYECTO_SIN_USAR = 10000

diccionarioPagos = {
    "Juan": 0,
    "Camila": 0,
    "Jose": 0,
    "Maria": 0,
    "Esteban": 0,
    "Angie": 0,
}

for i in range(len(matriz_uso)):
    suma_estudiante = 0
    pago_trayecto = 0
    for j in range(len(matriz_uso[i])):
        suma_estudiante += 1 if matriz_uso[i][j] == 1 else 0

    if suma_estudiante == 6:
        pago_trayecto = TRAYECTO / 6
        for estudiante in diccionarioPagos:
            diccionarioPagos[estudiante] += pago_trayecto
    elif suma_estudiante == 0:
        pago_trayecto = TRAYECTO_SIN_USAR / 6
        for estudiante in diccionarioPagos:
            diccionarioPagos[estudiante] += pago_trayecto
    else:
        pago_trayecto = TRAYECTO / suma_estudiante

        if matriz_uso[i][0] == 1:
            diccionarioPagos["Juan"] += pago_trayecto
        if matriz_uso[i][1] == 1:
            diccionarioPagos["Camila"] += pago_trayecto
        if matriz_uso[i][2] == 1:
            diccionarioPagos["Jose"] += pago_trayecto
        if matriz_uso[i][3] == 1:
            diccionarioPagos["Maria"] += pago_trayecto
        if matriz_uso[i][4] == 1:
            diccionarioPagos["Esteban"] += pago_trayecto
        if matriz_uso[i][5] == 1:
            diccionarioPagos["Angie"] += pago_trayecto


print(diccionarioPagos)

#------------------------ EJERCICIO 5 --------------------------------

""" El salario mensual de un empleado se calcula solo teniendo en cuenta el numero de seguros vendidos,
    (el precio de cada seguro es de $120000)
    Para los primeros 20 seguros vendidos, la comisión es del 20%.
    Para los siguientes 100 seguros las comisión es del 30%.
    Para los siguientes seguros vendidos. La comisión es de 10%.
   El salario de 4 empleados es el siguiente:
    Empleado   Empleado1   Empleado2    Empleado3   Empleado4
    Salario   $ 7860000    $ 5520000   $ 3720000    $ 2280000
   Determine el numero de seguros vendidos por cada empleado.
   Almacene su respuesta en una lista llamada cantidadSegurosVendidos como muestra el ejemplo:
   cantidadSegurosVendidos = [10, 50, 80, 32]
"""

#para comenzar podemos asignar el salario de cada uno de los empleados
empleado1=int(7860000)
empleado2=int(5520000)
empleado3=int(3720000)
empleado4=int(2280000)


cantidadSegurosVendidos=[0,0,0,0]
#lo primero que podemos hacer es identificar cuanto puede ganar vendiendo 20 seguros, luego los 120 y cuanto puede ganar con cada seguro despues de superar ese limite

comision1=int((120000*0.2)*20)
segindi1=int(120000*0.2)
comision2=int((120000*0.3)*100)
segindi2=int(120000*0.3)
comision3=int((120000*0.1))
seguros1=int(0)
seguros2=int(0)
seguros3=int(0)
seguros4=int(0)
#ahora procedemos a calcular cuantos seguros vendio cada uno utilizando IF y lo hacemos para cada uno de ellos.

if empleado1<=comision1:
    seguros1=empleado1/segindi1
    cantidadSegurosVendidos[0]=seguros1
elif empleado1<=comision2:
    seguros1=(((empleado1-comision1)/segindi2)+20)
    cantidadSegurosVendidos[0]=seguros1 
else :
    seguros1=((empleado1-(comision1+comision2))/comision3)+120
    cantidadSegurosVendidos[0]=seguros1
#/////////////////////////////////////////////////////////////////////////////
if empleado2<=comision1:
    seguros2=empleado2/segindi1
    cantidadSegurosVendidos[1]=seguros2
elif empleado2<=comision2:
    seguros2=(((empleado2-comision1)/segindi2)+20)
    cantidadSegurosVendidos[1]=seguros2 
else :
    seguros2=((empleado2-(comision1+comision2))/comision3)+120
    cantidadSegurosVendidos[1]=seguros2
#////////////////////////////////////////////////////////////////////////////////
if empleado3<=comision1:
    seguros3=empleado3/segindi1
    cantidadSegurosVendidos[2]=seguros3
elif empleado3<=comision2:
    seguros3=(((empleado3-comision1)/segindi2)+20)
    cantidadSegurosVendidos[2]=seguros3 
else :
    seguros3=((empleado3-(comision1+comision2))/comision3)+120
    cantidadSegurosVendidos[2]=seguros3
#///////////////////////////////////////////////////////////////////////////////
if empleado4<=comision1:
    seguros4=empleado4/segindi1
    cantidadSegurosVendidos[3]=seguros4
elif empleado4<=comision2:
    seguros4=(((empleado4-comision1)/segindi2)+20)
    cantidadSegurosVendidos[3]=seguros4 
else :
    seguros4=((empleado4-(comision1+comision2))/comision3)+120
    cantidadSegurosVendidos[3]=seguros4
    

print(cantidadSegurosVendidos)