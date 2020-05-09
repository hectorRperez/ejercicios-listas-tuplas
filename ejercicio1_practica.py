""" Ejercicio 1

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla. """


def mostrar_materias(lista_materias):
    
    for i in lista_materias:
        print(i)
    

if __name__ == '__main__':
    lista_materias = ['Matematicas','Física','Química', 'Historia', 'Lengua']
    mostrar_materias(lista_materias)