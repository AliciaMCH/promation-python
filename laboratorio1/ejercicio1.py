#Alicia Machuca Chamorro
#Introduccion a la programacion en python
#22/11/2016

def calcular (n):
	suma=0
	for i in range(1,n+1):
        suma=suma+i
	return suma
n=input()
print calcular (n)