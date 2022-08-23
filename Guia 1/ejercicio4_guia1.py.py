"""
Ejercicio 4 - Guia 1
Últimos dígitos
¿Cómo usaría el operador resto ( %)para obtener el valor del último
dígito de un número entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue
un número entero por teclado, y muestre el último dígito
del mismo (por un lado) y los dos últimos dígitos (por otro lado)
"""

num=int(input("Ingrese el el valor que desea: "))
ult_dig= num%10
print("El ultimo digito del numero ingresado es: ", ult_dig)

dos_digitos= num%100
print("Los ultimos dos digito del numero ingresado son: ",dos_digitos)
