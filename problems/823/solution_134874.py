def faltante (lista):
    '''dada uma lista com N-1 inteiros numerados de 1 a N, retorna qual numero inteiro desse intervalo esta faltando
        : list -> int 
    '''
    N = len(lista)+1
    i = 1
    while i<=N:
        if i in lista:
            i = i+1
        return i