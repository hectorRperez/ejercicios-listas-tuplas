""" Ejercicio 3

Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, 
y después las muestre 
por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
es cada una des las asignaturas de la lista y <nota> 
cada una de las correspondientes notas introducidas por el usuario. """


def mostrar_notas(lista_materias):
    
    lista_notas = []

    for materia in lista_materias:
        nota = float(input('Ingrese la nota obtenida en la materia {}: '.format(materia)))
        lista_notas.append(nota)
    
    for i in range(len(lista_materias)):
        print('En la materia {} obtuve {} '.format(lista_materias[i], lista_notas[i]))

if __name__ == '__main__':
    lista_materias = ['Matematicas','Física','Quimica','Historia', 'Lengua']
    mostrar_notas(lista_materias)