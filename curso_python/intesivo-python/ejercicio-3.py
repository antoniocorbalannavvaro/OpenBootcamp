'''
Ejercicio 3

Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

Objetivo:

Uso de bucles anidados

El uso de colecciones
'''

def is_prime(num):
    
    for n in range(2, num):
        
        if num % n == 0:        
            return False

    return True

def get_prime_list(start, stop):
    
    prime_list = []
    
    for i in range(start, stop):

        if is_prime(i) == True:
            prime_list.append(i)
        
    return prime_list
        
lista = get_prime_list(11,101)
print(lista)
