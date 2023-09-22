def fatorial(num):
    '''Uma função que recebe um número e retorna seu fatorial
    sem o uso do módulo math int->int'''
    resultado = 1
    for i in range(1, num+1):
        resultado *= i
    return resultado