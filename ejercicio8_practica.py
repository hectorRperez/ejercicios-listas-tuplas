""" Ejercicio 8

Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo. """

def is_polindromo(palabra):
    
    reverse_word = palabra
    palabra = list(palabra)
    reverse_word = list(reverse_word)

    reverse_word.reverse()
    
    if palabra == reverse_word:
        print('Es un polindromo')
    else:
        print('No es polindromo')

if __name__ == '__main__':
    palabra = input('Ingrese una palabra: ')
    is_polindromo(palabra)