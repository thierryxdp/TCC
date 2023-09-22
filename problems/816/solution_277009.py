def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    x=list.sort(lista)
    
    lista2= lista[:]+[n]
    y=list.sort(lista2)
    ident= list.index(y,n)
    if lista>[n]:
        return lista
    else:
        return lista2