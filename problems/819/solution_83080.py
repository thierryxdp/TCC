def filtraMultiplos(lista,n):
    '''Retorna uma lista contendo apenas os múltiplos de n;
    [int]->[int]'''
    i=0
    while i<len(lista):
        if lista[i]/n==0:
            lista.append(lista)
        i+=1
    return lista