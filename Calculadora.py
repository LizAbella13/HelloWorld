print "Operacion deseada (suma, resta, multiplicacion, division, residuo)"
operacion= (raw_input("operacion"))
print operacion
print "Ingrese el primer numero"
n1= int(raw_input("n1"))
print "Ingrese el segundo numero"
n2=int(raw_input ("n2"))
if operacion=="suma":
    suma=n1+n2
    print "Suma=",suma
    if suma%2==0:
        print "Numero par"
    else:
            print "Numero impar"
if operacion=="resta":
    resta=n1-n2
    print "Resta=",resta
    if resta%2==0:
        print "Numero par"
    else:
            print "Numero impar"
if operacion=="multiplicacion":
    multiplicacion=n1*n2
    print "Multiplicacion=",multiplicacion
    if multiplicacion%2==0:
        print "Numero par"
    else:
            print "Numero impar"
if operacion=="division":
    if n2!=0:
        division=n1/n2
        print "Division=",division
    if division%2==0:
            print "Numero par"
    else:
            print "Numero impar"
if operacion=="residuo":
    if n2!=0:
        residuo=n1%n2
        print "Residuo=",residuo
