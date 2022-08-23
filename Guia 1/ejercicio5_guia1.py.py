"""
Ejercicio 5 - Guia 1
Conversión de medidas Desarrolle un programa para convertir una
medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros
metros.
Sabiendo que:
1 pie = 12 pulgadas
1 yarda = 3 pies
1 pulgada = 2.54 centímetros
1 metro =1000
"""

p= int(input("Ingrese el valor en pies, a convertir: "))

y= p/3
pul= (p*12)*(2.54/1)
m= p/3.281

print ("EQUIVALENCIAS")
print("Yardas = ",y)
print("Pulgadas = ",p*12,"pulgadas ---->",round(pul,2), "centimetros")
print("Metros = ", round(m,2) , " metros")
