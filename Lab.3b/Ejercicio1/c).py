#Alicia Machuca Chamorro
#Laboratorio 3b
#Ejercicio 1c

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(-1,5,120)
f=t*math.e**(-2*t)
plt.plot(t,f,linewidth=5,color='g')
plt.legend()
plt.title('$F(t)=te^(-2t)$')
plt.xlabel('Horas')
plt.ylabel('Kilometros')
plt.grid(True)
plt.show()
