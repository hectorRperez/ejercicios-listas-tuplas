""" Ejercicio 4

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. """

def numeros_loterias(lista_numeros):
    
    lista_numeros = sorted(lista_numeros)

    print('Los numeros ganadores de la loteria')
    for i in lista_numeros:
        print(i)

if __name__ == '__main__':
    lista_numeros = []

    for i in range(6):
        lista_numeros.append(int(input('Ingrese el {}° numero ganador: '.format(i+1))))
    
    numeros_loterias(lista_numeros)