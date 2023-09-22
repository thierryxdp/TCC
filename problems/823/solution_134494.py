def faltante(lista):
    '''Dada uma lista de números inteiros com N-1 números,
    descobre qual número está faltando.
    list -> int'''
    cont = 0
    sum_lista = 0
    while cont < len(lista):
        sum_lista = sum_lista+lista[cont]
        cont = cont+1
    N = max(lista)
    x = sum(range(1,N+1))-sum_lista
    if x == 0:
        return N+1
    else:
        return x