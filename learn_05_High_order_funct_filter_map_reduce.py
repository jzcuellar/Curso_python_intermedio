"""EJEMPLO FUNCION FILTER"""

""" 
Dada una lista de numeros filtra para quedarte solo con 
los números impares
"""

# my_list = [i for i in range(10)]

# # Usando def
# def get_odds(arr):
#     odds = []
#     for n in arr:
#         if n % 2 == 1:
#             odds.append(n)
#     return odds
# print(get_odds(my_list))

# # Usando List Comprehension
# odds = [n for n in my_list if n % 2 == 1]
# print(odds)

# # Usando Filter
# odds_filter = list(filter(lambda n: n % 2 == 1, my_list))
# print(odds_filter)


"""
EJEMPLO FUNCION MAP

Obtener todos los numeros de una lista multiplicados al cuadrado
"""

def cuadrado(numero):
    return numero**2

numeros = [2, 5, 10, 23, 50, 33]
print(list(map(cuadrado, numeros)))

# Se puede Simplificar utilizando Lambda 

print(list(map(lambda x: x**2, numeros)))

"""
EJEMPLO FUNCION REDUCE

Sumar todos los valores de una lista
"""

from functools import reduce

# Utilizando ciclo For
valores = [2, 4, 6, 5, 4]
suma = 0
for i in valores:
    suma += i
print(suma)

# Utilizando funcion reduce() y lambda
suma = reduce(lambda x, y: x + y, valores)
print(suma)

# En este caso X sera el valor acumulado y 
# Y sera el valor de cada elemento del iterable valores

"""
Multiplicar todos los valores de una lista
"""

list_val=[2,2,2,2,2]

multiplicacion = reduce(lambda x,y: x*y, list_val)
print(multiplicacion)