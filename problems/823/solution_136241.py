def faltante (lista):
    '''Dada uma lista com N - 1 inteiros numerados de 1 a N,
    retorne com o número inteiro faltante;
    list -> int'''
    num = 1
    while num in lista:
        num = num + 1
        return num