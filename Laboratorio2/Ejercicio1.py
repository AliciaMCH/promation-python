#Alicia Machuca Chamorro
#Laboratorio 2
#25/11/2016
#Ejercicio1


x=input("ingresa cateto opuesto:")
y=input("ingresa cateto adyacente:")
import math
def hip(x,y):
    z=math.sqrt(x*x+y*y)
    return z
print "lahipotenusa del triangulo es:", hip(x,y)
