def insere(lista,n):
    '''
    retorna a lista dada com n, mantendo a lista ordenada
    list, int -> list
    '''
    lista=lista.append(n)
    lista=lista.sort()
    return lista