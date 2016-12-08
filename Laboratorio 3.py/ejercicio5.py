print "ingresa tu nombre, la primera letra mayuscula:"
a=[raw_input()]
b=a[0][0]
c0="la primera letra %s de tu nombre es vocal"%b
def evalua(b):
        if b== "A":
                print c0
        elif b== "E":
                print c0
        elif b== "I":
                print c0
        elif b== "O":
                print c0
        elif b== "U":
                print c0
                return b
        else:
                print "la primera letra %s de tu nombre es consonante"%b
b=evalua(b)
