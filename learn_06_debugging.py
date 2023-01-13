"""
Programa para encontrar los divisores de un numero

Este programa esta mal escrito, intencionalmente para 
el Ejercicio de Debugging

"""

def divisors(num):
    divisors_list=[]
    for i in range(1,num+1):
        if num % i == 1:
            divisors_list.append(i)
    return divisors_list

def run():

    num=int(input("Ingresa un numero: "))
    print(divisors(num))
    print('El programa termino bye!')



if __name__ == '__main__':
    run()

# Solucion con List comprenhesion
# numero=int(input('ingresa un numero'))
# divisores = [i for i in range(1,numero+1) if numero%i ==0]
# print(divisores)

