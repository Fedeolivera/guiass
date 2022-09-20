#conversion de pesos a dolares y dolares a a pesos
dls= int(input("ingrese el valor actual del dolar: "))
print("A)pesos a dolares")
print("B)dolares a pesos")
preg= input("que quiere convertir?: ")
if preg == "a":
    pesos= int (input("cantidad de pesos: "))
    reslt=pesos/dls
    print("son",reslt,"dolares")
elif preg == "b":
    dl= int (input("cantidad de dolares: "))
    reslt2=dls*dl
    print("son",reslt2,"pesos")


