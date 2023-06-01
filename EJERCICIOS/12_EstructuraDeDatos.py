import pandas as pd

data = [31,28,31,30,31,30,31,31,30,31,30,31]

index= ["Ene","Feb","Mar","Abr","May","Jun","Jul","Agos","Sep","Oct","Nov","Dec"]

seriesDiasPorMes= pd.Series(data=data, index=index)


Data2= [1,2,6,8,7,73]
index2= ["H","He","C","O","N","Ta"]

seriesatomicos=pd.Series(data=Data2, index=index2)

"""
Buscar Funciones que me permitan calcular sobre ambas series 
La suma de cada serie 
El promedio de cada serie 
La desviacion de estandar de cada serie 
Extraer aquellos meses con menos de 30 dias 
Extraer aquellos elementos con numero atomico mayor a 6 
"""

##La suma de cada serie ##

print("Suma dias por mes ==>", seriesDiasPorMes.sum())
print("Suma de numeros atomicos ==>", seriesatomicos.sum())

##El promedio de cada serie 

print("Suma dias por mes ==>", seriesDiasPorMes.mean())
print("Suma de numeros atomicos ==>", seriesatomicos.mean())

##La desviacion de estandar de cada serie 

print("Suma dias por mes ==>", seriesDiasPorMes.std())
print("Suma de numeros atomicos ==>", seriesatomicos.std())


## Extraer los dias de mayo 

print("Dias de mayo  ==>", seriesDiasPorMes["May"], seriesDiasPorMes[4])



##Extraer aquellos meses con menos de 30 dias 

print()