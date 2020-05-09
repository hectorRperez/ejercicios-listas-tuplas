""" Ejercicio 10

Escribir un programa que almacene en una lista los siguientes 
precios, 50, 75, 46, 22, 80, 65, 8, 
y muestre por pantalla el menor y el mayor de los precios. """


def mostrar_precio(lista_precio):
    numero_max = max(lista_precio)
    numero_min = min(lista_precio)

    print('Numero mayor: {}'.format(numero_max))
    print('Numero menor: {}'.format(numero_min))

if __name__ == '__main__':
    lista_precio = [50,75,46,22,80,65,8]
    mostrar_precio(lista_precio)