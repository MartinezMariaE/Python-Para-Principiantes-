"""
Ejercicio 7 - Guia 1
Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.
"""

#Pide ingresar la cantidad de numeros de la sucesion
n=int(input("Ingrese la cantidad de numeros a secuenciar: "))

#declaro variables n1 y n2, ya que son pundamentales para la sucesion
n1=0
n2=1
#inicio la suma en 0 y el contador en 1
sum=0
contador=1
print("SECUENCIA DE FIBONACCI ")

#un condicional, termina el programa cuando el contador sea menor o igual a n
while(contador<=n):    
  print(sum)
  contador+=1
  n1=n2
  n2=sum
  sum=n1+n2
