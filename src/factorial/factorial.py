#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 1:
   desde = int(input("Ingrese el número inicial del rango: "))
   hasta = int(input("Ingrese el número final del rango: "))
elif len(sys.argv) == 3:
    desde = int(sys.argv[1])
    hasta = int(sys.argv[2])
else:
    print("Uso: python factorial.py [desde] [hasta]")
    sys.exit(1)

if desde < 0 or hasta < 0:
    print("Los números del rango deben ser mayores o iguales a cero")
    sys.exit(1)

if desde > hasta:
    print("El número inicial del rango debe ser menor o igual al número final")
    sys.exit(1)

print("Factoriales en el rango desde", desde, "hasta", hasta, ":")

for num in range(desde, hasta+1):
    print("Factorial", num, "! es", factorial(num))
