"""
Cuadrado de un binomio Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) esigual al cuadrado del primer término, más el doble producto del primero por el segundo más el cuadrado del segundo.
"""
a= int(input("Ingrese el primer valor= "))
b= int(input("Ingrese el segundo valor= "))

print("(a+b)2 = a2 + 2xaxb+b2")
resultado= (a**2)+(2*a*b)+(b**2)
print("El resultado del cuadrado, de los numeros ingresados es= ",resultado)