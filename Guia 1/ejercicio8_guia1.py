"""
Ejercicio 8 - Guia 1
Multiplicacion. Ingresar un numero cualquiera por teclado y que
muestre su respectiva tabla del 1 al 10.
"""

n= int(input("Ingrese un numero: "))
for i in range (1,11):
    mult= n*i
    print(i," x ",n," = ",mult)
    
