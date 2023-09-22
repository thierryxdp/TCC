def filtraMultiplos(lista,n):
    '''Esta função filtra os múltiplos de um número n de uma lista dada.
    list,int->list'''
    i=0
    nova_lista=list()
    while i<len(lista):
        mtp=lista[i]%n
        if mtp==0:
            nova_lista.append(lista[i])
        i=i+1
    return nova_lista