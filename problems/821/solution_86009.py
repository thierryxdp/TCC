def fatorial(numero):
    '''função que calcula e retorna o fatorial de um número dado; int -> int'''
    
    numeros = range(1, numero+1)
    i = 0
    fat = 1
    while i < len(numeros):
        fat = fat*numeros[i]
        i = i+1
    return fat