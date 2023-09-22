def faltante (lista):
    '''dada uma lista com N-1 inteiros numerados de 1 a N, retorna qual numero inteiro desse intervalo esta faltando
        : list -> int 
    '''
    i = 1
    while i in lista:
        i = i+1
    return i