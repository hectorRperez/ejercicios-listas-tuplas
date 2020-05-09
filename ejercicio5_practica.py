""" Ejercicio 5

Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas. 
"""

def mostrar_numeros(lista_numeros):
    
    lista_numeros = sorted(lista_numeros, reverse=True)
    for i in lista_numeros:
        print(i, end = ',')

if __name__ == '__main__':
    
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    mostrar_numeros(lista_numeros)