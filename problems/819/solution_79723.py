def filtraMultiplos(lista,n):
    '''
    '''
    listaN=[]
    indice=0

    while indice<len(lista):
        if lista[indice]%n==0:
            list.append(listaN,lista[indice])
        else: 
            listaN=listaN+[]
        indice=indice+1
    return listaN