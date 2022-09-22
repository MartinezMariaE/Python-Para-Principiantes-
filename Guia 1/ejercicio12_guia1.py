"""
Ejercicio 12. 
Crear un conversor de pies y pulgadas a centímetros.
"""
pies=0
pulgadas=0

pies= float(input("Ingrese el valor en pies a convertir= "))
pulgadas= float(input("Ingrese el valor en pulgadas a convertir= "))

pies_cent= (pies*30.48)/1
print(pies, "equivale a ",pies_cent," cm")

pulg_cent= (pulgadas*2.54)/1
print(pulgadas, "equivale a ",pulg_cent," cm")

