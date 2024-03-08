# Desarrollar una funcion que reciba un texto e identifique  que todos los parentesis esten balancieados (chequear que siempre que se abra un parentesis este se cierre), devolver True caso que sea asi, False caso contrario

# Importar colorama  para dar formato  al texto (instalacion opcional)
# Para instalar colorama, ejecuta:  pip install colorama

import colorama, os
colorama.init()
rojo = "\x1b[1;31;49m"
verde = "\x1b[1;32;49m"
blanco = "\x1b[1;37;49m"

#Funcion
def parentesis(texto):
    #Detectamos parentesis
    detector = []
    #Definimos los caracteres de parentesis
    parentesis = {'(':')', '[':']', '{':'}'}
    #Iteramos cada caracter del texto
    for caracter in texto:
    #Si el detector, encuentra un parentesis de apertura lo agrega.
        if caracter in parentesis.keys():
            detector.append(caracter)
    #Si el detector, encuentra un parentesis de cierre verifica si teniamos almacenado un caracter de apertura que coincida
        elif caracter in parentesis.values():
            if not detector or parentesis[detector.pop()] != caracter:
                return False
    return not detector

    
def menu():
    limpiar()
    print(f'{blanco}¡Bienvenido al verificador de polindromos!')
    texto = input('\nIngresa el texto para verificar: ')
    if parentesis(texto):
        print(f'\n{verde}Texto:\n{texto} \n\n¡Todos los parentesis estan en orden! :D{blanco}')
    else:
        print(f'\n{rojo}Texto:\n{texto} \n\n¡Hay parentesis que no estan en orden! :({blanco}')

def limpiar():
    '''
    Funcion para limpiar pantalla, detecta si el sistema es nativo y usa "cls", de lo contrario usa "clear"
    '''
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

menu()