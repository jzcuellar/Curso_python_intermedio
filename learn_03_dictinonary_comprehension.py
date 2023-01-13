import math

def run():
    # Crear un diccionario con Key Numeros de 1-100 Valor (cUBO)
    # No incluir los numeros divisibles entre tres  

    # # SOLUCION CON FOR
    # my_dict={}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         my_dict[i]=i**3

    # # SOLUCION CON DICTYONARY COMPRENHESION

    # my_dict={i: i**3 for i in range(1,101) if i % 3 != 0}

    #Reto key(100 Numeros naturales):value(raiz cuadrada)

    my_dict_root={i: round(math.sqrt(i),2) for i in range(1,101)}
    print(my_dict_root)

if __name__ == '__main__':
    run()