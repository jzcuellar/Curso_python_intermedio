import sys
import os
import random


def open_file_palabras():

    try:
        with open("./proyecto_01_juego_ahorcado/palabras.txt", "r", encoding="utf-8") as f:
            lst_palabras = []
            for line in f: 
                lst_palabras.append(line.strip())
            return lst_palabras
    
    except FileNotFoundError:
        print("No se ha encontrado el archivo de palabras, verifica la ruta")
        sys.exit()
    
    except:
        print("Ha ocurrido un error al abrir el archivo, verifica que el archivo esta en formato utf-8 ")
        sys.exit()


def palabra_random():
    lst_palabras = open_file_palabras()
    palabra = random.choice(lst_palabras)
    return replace_tilde(palabra)


def replace_tilde(string):
    vowels = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    for accent_vowel, non_accent_vowel in vowels.items():
        string = string.replace(accent_vowel, non_accent_vowel)
    return string

def clean_screen():
    os.system('cls')

def print_ongoing_game(lst_palabra,letters_user):
    clean_screen()
    adivinado = [i if i in letters_user else '-' for i in lst_palabra]
    print('Adivina la palabra')
    print(''.join(adivinado))
    letter = input('Ingresa una letra: ')
    if letter in lst_palabra:
        letters_user.append(letter)


def run():

    palabra = palabra_random()
    lst_palabra = [x for x in palabra]
    letters_user = []

    while set(lst_palabra) != set(letters_user):
        print_ongoing_game(lst_palabra,letters_user)
    clean_screen()
    print(f'Ganaste la palabra era {palabra}')

if __name__ == '__main__':
    run()