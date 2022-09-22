"""Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.
"""
contador=0
sueldo= float()
acumulador=0.0
porcentaje=0.0

print("Ahorro desde Enero a Diciembre")
sueldo= int(input("Ingrese su sueldo "))
while(contador<= 11):
    porcentaje=(sueldo*0.10)
    acumulador=acumulador+porcentaje
    contador=contador+1
    print("Mes ", contador," tiene un ahorro de ",acumulador )
print("A la derecha puede visualizar los ahorros de ese mes, mas el mes anterior ya sumados.")
print("Finalmente, su ahorro del año fue de: ",acumulador)