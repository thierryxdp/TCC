def filtraMultiplos(listaNs,N):
    '''Recebe uma lista não vazia de números e um número n. Retorna todos os números da lista divisíveis por n;
    list,int -> list'''
    numeros = []
    prox = 0
    while prox< len(listaNs):
        if listaNs[prox]%N == 0:
        	numeros = numeros + [listaNs[prox],]
        prox = prox + 1
    return numeros