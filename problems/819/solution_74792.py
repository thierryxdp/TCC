def filtraMultiplos(listaNs,N):
    """ recebe uma lista não vazia de numeros e um numero n e retorna todos os numeros
    da lista divisiveis por n;
    lista,int->list"""
    numeros = []
    prox = 0
    while prox <len(listaNs):
        if listaNs[prox]%N == 0:
            numeros = numeros + (listaNs[prox],)
        prox = prox + 1
    return numeros