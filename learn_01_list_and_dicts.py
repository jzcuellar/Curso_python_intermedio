def run():
    my_list = [1,'Hello',True,4.5]
    my_dict = {"firsname": "Jefferzon", "lastname": "Cuellar"}

    #  Este es una Lista con diccionarios en su interior
    
    super_list = [
        {"firsname": "Jefferzon", "lastname": "Cuellar"},
        {"firsname": "Miguel", "lastname": "Torres"},
        {"firsname": "Pepe", "lastname": "Rodelo"},
        {"firsname": "Kathe", "lastname": "Ayala"},
        {"firsname": "Jenny", "lastname": "Castrillon"},
    ] 

    #  Este es un diccionario de listas
    
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    } 

    # for key, value in super_dict.items():
    #     print(f'{key} {value}')

    # Este es un ciclo for con dos variables de control (key, value)
    # .items Return the dictionary's key-value pairs

    for i in super_list:
        for key, values in i.items():
            print(f'{key} : {values}',end=" -");
        print('')

    # Este es el ciclo for para imprimir los valores dentro de la lista con diccionarios en su interior

if __name__ == '__main__':
    run()