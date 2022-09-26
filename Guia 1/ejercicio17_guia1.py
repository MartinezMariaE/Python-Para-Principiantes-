"""
 Galería de Arte Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”.
"""
print("""                   ¡¡¡ATENCIÓN!!!
    Verificaremos si las obras son o no del siglo XX
    Para eso le solicitamos que ingrese el nombre de la obra, y su correspondiente año.
    esta prueba se realizará con 3 obras
      """)
contador=0
while (contador<=2):
    año= int(input("Ingrese el año de la obra ="))
    if (año>=1901) and (año<=2000):
        print("El cuadro pertenece al siglo xx")
    else: 
        print("El cuadro no pertenece al sigo xx")
    if año <= 2012:
        print("El cuadro tiene más de 10 años de antiguedad, considerando el año actual (2022)")
    else: 
        print("RENOVAR STOCK")
    if año > 2022:
        print("ERROR, INGRESAR UN AÑO CORRECTO")
    contador=contador+1    