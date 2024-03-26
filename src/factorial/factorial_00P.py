#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* Calcula el factorial de un número mediante programación orientada a     *
#* objetos.                                                                 *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative Commons                                                        *
#*-------------------------------------------------------------------------*

import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) == 0:
   print("Debe informar un número!")
   sys.exit()
num=int(sys.argv[1])
print("Factorial ",num,"! es ", factorial(num)) 
import sys

class Factorial:
    def calculate_factorial(self, num):
        if num < 0:
            raise ValueError("Factorial of a negative number does not exist")
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num 
                num -= 1
            return fact 

    def run(self, min_num, max_num):

        results = {}
        for num in range(min_num, max_num + 1):
            results[num] = self.calculate_factorial(num)
        return results

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Debe informar un rango de números!")
        sys.exit()

    min_num = int(sys.argv[1])
    max_num = int(sys.argv[2])

    factorial_calculator = Factorial()
    results = factorial_calculator.run(min_num, max_num)

    for num, result in results.items():
        print(f"Factorial de {num} es {result}")