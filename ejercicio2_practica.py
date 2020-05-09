""" Ejercicio 2

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
donde <asignatura> es cada una de las asignaturas de la lista. """


def mostrar_materias(lista_materias):
    
    for i in lista_materias:
        print('Yo estudio {} '.format(i))


if __name__ == '__main__':

    lista_materias = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
    mostrar_materias(lista_materias)