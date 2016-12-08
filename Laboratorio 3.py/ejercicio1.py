#Latitud,longitud

import matplotlib.pyplot as n
import math
x=input("introduzca longitud(t1):")
y=input("introduzca latitud(g1):")
w=input("introduzca longitud(t2):")
z=input("introduzca latitud(g2):")
a=(x,y)
b=(w,z)

def dist(a,b):
    x,y=a
    x=x*math.pi/180
    y=y*math.pi/180
    w,z=b
    w=w*math.pi/180
    z=z*math.pi/180
    distancia=6371.1*math.acos(math.sin(x)*math.sin(w)+math.cos(x)*math.cos(w)*math.cos(y-z))
    return distancia
print"la distancia en km. es:", dist(a,b)
