"""
Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.
"""
promedio=0
minimo=1000
acum=0
#Primero establecemos el tiempo record
tiempo_record=float(input("Ingrese el tiempo record actual de la carrera: "))

#El usuario ingresa por teclado la cantidad de competidores

n_competidores=int(input("¿Cuantos competidores tuvo la carrera?= "))

for i in range(n_competidores):
    print("----     Competidor Nro"+str(i+1)+"   ---- ")
    nom=input("Nombre= ")
    tiempo=int(input("Tiempo final (ingrese el valor en minutos)= "))
    
    acum=acum+tiempo
    
    if tiempo < minimo:
        minimo=tiempo
        ganador=nom
promedio=acum/n_competidores

if minimo < tiempo_record:
    print(ganador," rompió un nuevo record")
else:
    print("El record, se sigue manteniendo en: ", tiempo_record)
    
print("El ganador de la competición es: ",ganador)
print("El promedio de tiempo, contando todos los competidores, fue de: ", promedio)

