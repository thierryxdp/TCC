def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    if lista>[n]:
    	return lista
    else:
        return lista[:]+[n]