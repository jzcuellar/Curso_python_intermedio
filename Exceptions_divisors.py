def divisors(num):
    divisors_list=[]
    # Excepcion para evitar que usuario ingrese Negativos
    try:
        if num<0:
            raise ValueError("No estan permitidos numeros negativos") 
        
        for i in range(1,num+1):
            if num % i == 0:
                divisors_list.append(i)
    
        return divisors_list
    except ValueError as ve:
        return ve

def run():

    # Excepcion para que evitar que el usuario ingrese valor diferente a numero (letra o palabra)
    try:
        num=int(input("Ingresa un numero: "))
        print(divisors(num))
        print('El programa termino bye!')
    except ValueError:
        print('Debes ingresar un número')



if __name__ == '__main__':
    run()