def filtraMultiplos(lista,n):
    '''filtraMultiplos recebe uma lista de números e um número n, e devolve uma lista contendo todos os elemento da lista inicial que são divisiveis por n.
    list,float-->list.'''
    i=0
    divisiveis=[]
    while i<len(lista):
        if (lista[i]%n)==0:
            divisiveis=divisiveis+[lista[i]]
        i=i+1
    return divisiveis