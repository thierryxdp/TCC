def fatorial(numero):
    '''função que calcula e retorna o fatorial de um número dado; int -> int'''
    
    numeros = range(1, numero+1)
    i = numero-1
    while i < len(numeros):
        i = i-1
        fat = numeros[i]*numeros[i+1]
    return fat