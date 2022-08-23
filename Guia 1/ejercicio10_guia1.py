"""
Ejercicio 10 - Guia 1
Crear un conversor de dólares a pesos y pesos a dólares,
donde se ingrese por teclado el valor del peso actual.
"""

print(
    """
CONVERSOR

1 - Convertir dolares a pesos
2 - Convertir pesos a dolares
"""
    )
dolar= 136
num= int(input("Ingrese el valor en dolares a convertir: "))
valor= int(input("Ingrese el valor del peso: "))

print(num,"Equivale a $",num*valor)

print(num,"Equivale a US$", round((num/valor),2))
