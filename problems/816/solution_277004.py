def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    
    if lista>[n]:
        return lista
    else:
        return lista2