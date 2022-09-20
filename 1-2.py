#contador de letras
nombre = input("¿Cómo te llamas? ")
cont = len(nombre)
resto = cont % 2
if resto == 0:
    print("Es par")
else:
    print("Es impar")

