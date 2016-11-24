Alicia Machuca Chamorro
#Introduccion a la programacion en python
#22/11/2016

num=int(input("ingrese los sesegundos/n"))

dias=int(num/86400.0))
hrs=int((num-(dia*86400))/3600.0)
min=int((num-((hrs*3600.0)+(dia*86400)))/60)
ss=num-((dia*86400)+(hrs*3600)+(min*60))
print(str(dia)+"d "+str(hrs)+"h "+str(min)+"min "+str(ss)+"s")

