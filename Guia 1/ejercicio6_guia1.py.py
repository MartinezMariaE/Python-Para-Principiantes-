"""
Ejercicio 6 - Guia 1
Escribir un programa que pregunte un nombre de usuario,
y que después muestre por pantalla si su cantidad de letras es par o impar.
"""
nom = input("Ingrese su nombre: ")

contador=0
#el for recorrera las letras de la variable nom
#cada vez que recorra una letra suma un numero
for i in nom:
    contador+=1
    
print("La palabra ",nom," tiene",contador," letras")
if contador %2 == 0:
    print(contador," es par")
else:
    print(contador," es impar")
