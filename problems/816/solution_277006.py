def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    list.sort(lista)
    
    lista2= lista[:]+[n]
    list.sort(lista2)
    
    if lista>[n]:
        return lista
    else:
        return lista2