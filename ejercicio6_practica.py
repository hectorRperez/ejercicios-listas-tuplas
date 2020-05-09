""" Ejercicio 6

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura 
y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario 
tiene que repetir. """

def materias_aprobadas(lista_materias):
    
    lista_aprobadas = []

    for i in lista_materias:
        nota = float(input('¿Cual fue nota obtenida en la materia {} '.format(i)))
        if nota >= 5:
            lista_aprobadas.append(i)

    for i in lista_aprobadas:
        lista_materias.remove(i)

    print('Materias no aprobadas: ',lista_materias)

if __name__ == '__main__':
    lista_materias = ['Matematicas','Fisica','Quimica','Historia','Lengua']
    materias_aprobadas(lista_materias)