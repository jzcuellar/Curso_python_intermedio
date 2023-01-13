def palindrome(string):
    # Esta estructura try, except controla que el usuario no ingrese cadena vacia
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías") #1
        return string == string[::-1]
    except ValueError as ve: #2
        print(ve)
        return False

def run():
    
    # Esta Estructura try, except permite controlar el error en caso de que el 
    # usuario ingrese un numero
    try:
        palabra=input('Ingresa una palabra: ')
        print(palindrome(palabra))
    except TypeError:
        print("Solo se pueden ingresar strings")

if __name__ == '__main__':
    run()

#1 raise la utilizamos para lanzar un error (con una excepcion personalizada) 
#  en caso de que se cumpla una condicion

#2 except ValueError as ve: con esta expresion indicamos que si nos salta el 
#  error indicado con el raise ejecute el codigo de las lineas subsecuentes