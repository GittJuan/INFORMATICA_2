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