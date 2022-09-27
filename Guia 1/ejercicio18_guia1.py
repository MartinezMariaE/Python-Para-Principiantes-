"""Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el 
rango del 1 al 100, que representaría la tarjeta de bingo de una persona. Una vez 
generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, 
a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó ninguno de los números, 
indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar 
“El jugador marcó algún número de la tarjeta”."""
import random
num1=0
num2=0
num3=0
azar=0

print("A continuación deberá ingresar 3 numeros y veremos si coincide con los sorteados")
num1=int(input("1= "))
num2=int(input("2= "))
num3=int(input("3= "))

for i in range(15):
    azar=random.randint(0, 100)
    print(azar)

if (azar != num1) and (azar != num2) and (azar != num3):
    print("Mala suerte... no acerto ningun numero")
else:
    print("""Acertó al menos uno. 
          A continuación vea usted qué numero acertó""")

