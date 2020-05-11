""" Ejercicio 13

Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y 
muestre por pantalla su media y desviación típica. """

def estadistica(sample):
    sample = sample.split(',')
    
    sample = [int(i)for i in sample]
    
    sample = tuple(sample)
    
    sum = 0
    sumsq = 0

    for i in sample:
        sum += i
        sumsq += i**2

    print(sum)
    print(sumsq)

    mean = sum / len(sample)
    stdev = ((sumsq/len(sample)-mean**2)**(1/2))

    print('La media es {} '.format(mean))
    print('La desviación típica es {} '.format(stdev))

if __name__ == '__main__':
    
    sample = input('Ingrese una serie de números separados por comas: ')
    estadistica(sample)