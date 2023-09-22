def faltante (lista):
    '''função em que dada uma lista com N - 1 números iteiros não repetidos de
    1 a N retorne o número inteiro que pertence ao intervalo [1,N] mas que não
    pertence a lista de entrada L;
    list -> int'''
    lista.sort()
    i=1
    x=0
    while i<=(len(lista)+1):
        if not i in lista:
            x=x+i
        i=i+1
    return x