def divisors(num):
    divisors_list=[]
    for i in range(1,num+1):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list

def run():

    num=input("Ingresa un numero: ")
    try:
        assert num.isnumeric() and int(num)>0, "Debes ingresar un numero positivo" #1 #2
        print(divisors(int(num)))
        print('El programa termino bye!')
    except AssertionError as ve:
        print(ve)

if __name__ == '__main__':
    run()

#1 isnumeric devuelve True si el string es numero, else devuelve false
# 
#2 assert Evalúa una condicional, si esta se cumple continuamos con
#  el flujo normal del python, si no se cumple eleva un error del 
#  tipo AssertionError y nos muestra un mensaje.
#  assert Es similar a raise pero Assert evalua la condicion en una 
#  sola linea de codigo de forma mas limpia

# Puedo Convinar assert, con la estructura try, exception