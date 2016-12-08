print "ingresa el primer numero"
a=int(raw_input())
print "ingresa el segundo numero"
b=int(raw_input())
print "ingresa el tercer numero"
c=int(raw_input())
print "los numeros ordenados de menor a mayaor son:"
if a>=b>=c:
      print c,b,a
elif a>=c>=b:
      print b,c,a
elif b>=a>=c:
      print c,a,b
elif b>=c>=a:
      print a,c,b
elif c>=a>=b:
      print b,a,c
elif c>=b>=a:
      print a,b,c
