def filtraMultiplos(listadenumeros,n):
    '''função que filtra os multiplos de um numero n. Int -> int'''
    lista=[]
    i=0
    while i<len(listadenumeros):
        if listadenumeros[i]%n==0:
            lista=lista+[listadenumeros[i]]
            i=i+1
        else:
            i=i+1
    return lista