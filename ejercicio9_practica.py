""" Ejercicio 9

Escribir un programa que pida al usuario una palabra 
y muestre por pantalla el número de veces que contiene cada vocal. """

def mostrar_vocales(palabra):
    
    lista_vocales = ['a','e','i','o','u']

    for i in lista_vocales:
        contador = 0

        for j in palabra:

            if j == i:
                contador+=1
        
        print('La vocal se encuntra {} {} veces'.format(i, contador))


if __name__ == '__main__':
    
    palabra = input('Ingrese una palabra: ')
    mostrar_vocales(palabra)