"""
Suma - División - Potencia Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo.
"""
a=0
b=0
c=0
suma=0

a=int(input("Ingresar el primer valor: "))
b=int(input("Ingresar el segundo valor: "))
c=int(input("Ingresar el tercero: "))

suma=a+b+c
if suma > 10:
    div=suma/2
    print("Si sumamos el resultado (",suma,") y dividos por dos, nos da: ",round(div,0))
else:
    print("Elevamos el resultado (",suma,") al cubo, el resultado de esto es: ",suma**3)
