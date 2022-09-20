#Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
#   Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
#a)Determinar y mostrar el nombre del ganador de la carrera.
#b)Ingresar por teclado el tiempo record registrado para dicha carrera.
#   Determinar si el tiempo del ganador es menor al tiempo record,mostrar un mensaje.
#c)Calcular y mostrar el tiempo promedio entre todos los ciclistas.

cont=0
acum=0
competidores = int(input("cuantos competidores hay: "))

for i in range(competidores):
    print("ciclista",i+1)
    nombre= input("ingrese el nombre: ")
    tiempo= int(input("ingrese el tiempo"))
    
