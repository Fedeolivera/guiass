n=int(input("ingrese un numero: "))
primero=0
segundo=1
sum=0
cont=1
print("secuencia de fibonacci: ")
while(cont<=n):    
  print(sum)
  cont+=1
  primero=segundo
  segundo=sum
  sum=primero+segundo	
