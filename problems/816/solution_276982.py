def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    if lista>[n]:
    	return lista
    else
        return lista2