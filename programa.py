# X mayor que y o viseversa

print("-------------------------------------")
print("------------Mayor o Menor------------")
print("-------------------------------------")

#input

n= int(input("Digite el valor de n: "))
r = n
#Procesing

if n>0 : 
    rta = " es positivo"

else:
    rta = " no es positivo"


if   9999>n>1000 :
    rt= " es de 4 digitos"

else:
    rt= " no es de 4 digitos"
print("El valor " + str(rta))
print("El valor " + str(rt))