# Desarrollar una funcion que reciba una palabra y devuelva True en caso de ser un palindromo y False en caso de no serlo.

# Importar colorama  para dar formato  al texto (instalacion opcional)
# Para instalar colorama, ejecuta:  pip install colorama

import colorama, os
colorama.init()
rojo = "\x1b[1;31;49m"
verde = "\x1b[1;32;49m"
blanco = "\x1b[1;37;49m"

#Funcion
def polindromo(palabra):
    #Filtramos mayusculas
    palabra = palabra.lower()
    #Filtramos espacios
    palabra = palabra.replace(' ', '')
    #Filtramos caracteres especiales
    palabra = ''.join(caracter for caracter in palabra if caracter.isalpha())
    #Invertimos la palabra para comparar
    invertida = palabra[::-1]

    if palabra == invertida:
        return True
    else:
        return False
    
def menu():
    limpiar()
    print(f'{blanco}¡Bienvenido al verificador de polindromos!')
    palabra = input('\nIngresa la palabra para verificar: ')
    if polindromo(palabra):
        print(f'\n{verde}¡{palabra} es un polindromo! :D{blanco}')
    else:
        print(f'\n{rojo}¡{palabra} no es un polindromo! :({blanco}')

def limpiar():
    '''
    Funcion para limpiar pantalla, detecta si el sistema es nativo y usa "cls", de lo contrario usa "clear"
    '''
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

menu()