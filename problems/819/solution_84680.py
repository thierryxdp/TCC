def filtraMultiplos(lista, n):
    ''' Retorna outra lista contendo todos os elemento da lista dada como parametro
        e forem divididos por 'n'.'''
    L = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            L.append(lista[i])
        i=i+1
    return L