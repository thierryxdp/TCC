def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    lista2=list.sort(lista,reverse=True)
    if lista>[n]:
    	return lista
    else:
        return lista2