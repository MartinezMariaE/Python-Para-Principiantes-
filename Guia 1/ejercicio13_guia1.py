"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar.Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces utlizar: .@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
soledad.steffolani@umet.edu.ar
"""
nom=input("Ingrese su nombre: ")
ape=input("Ingrese su apellido: ")
dom=input("Ingrese el dominio: ")

nom=(nom.lower())
ape=(ape.lower())
dom=(dom.lower())

if nom[0] == ape[0]:
    print(nom[0]+ape+"@"+dom)
    
else:
    print(nom+"."+ape+"@"+dom)    
    
