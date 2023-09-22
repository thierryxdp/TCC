def filtraMultiplos(lista,n):
    ''' list,int --> list '''
    i = 0
    filtrados = []
    while i<len(lista):
        if lista(i)%n==0:
            filtrados = filtrados + [lista(i)]
    return filtrados