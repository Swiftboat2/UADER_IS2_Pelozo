#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

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

print("Este programa calculará los factoriales en un rango especificado.")

desde = int(input("Introduce el número inicial del rango: "))
hasta = int(input("Introduce el número final del rango: "))

if desde > hasta:
    print("El número inicial del rango debe ser menor o igual al número final")
    exit(1)

print("Factoriales en el rango desde", desde, "hasta", hasta, ":")

for num in range(desde, hasta+1):
    print("Factorial", num, "! es", factorial(num))
