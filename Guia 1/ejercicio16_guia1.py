"""
Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno
que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.
"""
print("""-------- MENU PRINCIPAL -------- 
¡¡¡Lea atentamente!!!

Deberá ingresar la opcion correspondiente a su turno de trabajo cuando se le solicite
RECUERDE QUE:
OPCION 1: TURNO DIURNO
OPCION 2: TURNO NOCTURNO

solo debe ingresar el numero correspondiente a su turno """)

cod=int(input("¿En que turno trabaja? (1 diruno o 2 nocturno) ="))
if cod == 1:
    hs_diurno=int(input("¿Cuantas horas trabajó? = "))
    cobro_diurno=hs_diurno*35.50
    print("El empleado del turno diruno debe cobrar un total de= $",cobro_diurno)
else:
    hs_nocturno=int(input("¿Cuantas horas trabajó? = "))
    cobro_nocturno=hs_nocturno*40,60
    print("El empleado del turno nocturno debe cobrar = $",cobro_nocturno)




