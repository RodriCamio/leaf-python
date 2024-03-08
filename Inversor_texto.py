#Desarrollar una funcion que reciba un texto e invierta el orden de las palabras siendo la ultima palabra la primera y la primera la ultima, debe devolver el texto invertido

# Importar colorama  para dar formato  al texto (instalacion opcional)
# Para instalar colorama, ejecuta:  pip install colorama

import colorama, os
colorama.init()
rojo = "\x1b[1;31;49m"
verde = "\x1b[1;32;49m"
blanco = "\x1b[1;37;49m"

#Funcion
def inversion_texto(texto):
    #Convertimos el texto en una lista
    texto = texto.split()
    #Invertimos el orden de las palabras
    texto = texto[::-1]
    #Unir las palabras con un espacio en el medio
    texto = ' '.join(texto)
    return texto
    
def menu():
    limpiar()
    print(f'{blanco}¡Bienvenido al inversor de orden de textos!')
    texto = input('\nIngresa el texto que desea invertir el orden: ')
    texto = inversion_texto(texto)
    print(f'\nTexto invertido:\n{verde}{texto}{blanco}')


def limpiar():
    '''
    Funcion para limpiar pantalla, detecta si el sistema es nativo y usa "cls", de lo contrario usa "clear"
    '''
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")

menu()