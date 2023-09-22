def filtraMultiplos(listanumeros,n):
    '''Filtra os múltiplos de um número n presentes em uma lista e os retorna em uma nova lista
    entrada: lista, int
    saída: lista
    '''
    listamultiplos=[]
    i=0
    while i>=-1:
        if listanumeros[i]%n==0:
        listamultiplos=listamultiplos+[listanumeros[i]]
        i=i+1
    return listamultiplos