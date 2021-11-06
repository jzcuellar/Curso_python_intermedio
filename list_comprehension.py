def divisible_4_6_9():
    # Crear una lista con multiplos comunes de 4,6,9 hasta 100.000
    # MCM de 4,6,9 = 36 (Hacer Lista de Multiplos de 36)
    
    #Comprenhesion List

    mc = [i for i in range(1,100000) if i % 36 == 0] # Con minimo comun Multiplo
    mc_4_6_9 = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ] # Con minimo comun Multiplo

    print(mc == mc_4_6_9)


def run():
    # SOLUCION DEL PROBLEMA CON FOR 
    
    # squares = []
    # for i in range(1,11):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # SOLUCION CON LIST COMPREHENCION
    
    squares = [i**2 for i in range(1,11) if i % 3 != 0]

    print(squares)

if __name__ == '__main__':
    run()

