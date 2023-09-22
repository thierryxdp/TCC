def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    x= list.index(lista,n)
    if lista>[n]:
    	return lista
    else:
        return x