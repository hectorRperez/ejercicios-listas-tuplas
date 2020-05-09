""" Ejercicio 11

Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) 
en dos listas y muestre por pantalla su producto escalar. """

def producto_escalar(a,b):
    
    product = 0
    for i in range(len(a)):
        product+= a[i]*b[i]
    
    print('El producto final de {} {} = {}'.format(a,b,product))

if __name__ == '__main__':
    vector_a = (1,2,3)
    vector_b = (-1,0,2)
    producto_escalar(vector_a, vector_b)