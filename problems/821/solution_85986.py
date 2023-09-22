def fatorial(numero):
    '''função que calcula e retorna o fatorial de um número dado; int -> int'''
    
    numeros = range(1, numero+1)
    i = 0
    while i < len(numeros):
        próximo = numeros[i+1]
        fat = numeros[i]*próximo
        i = i+1
    return fat