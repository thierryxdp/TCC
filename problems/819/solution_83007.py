def filtraMultiplos(lista,n):
    '''função que recebe como entradas uma lista de números e
    um determinado número n, calculando e retornando outra
    lista contendo os elementos divisíveis por n da lista
    original'''
    proximo=0
    n=()
    while n <= len(lista):
        if lista[proximo]%n == 0:
        	proximo = proximo + 1
    return n