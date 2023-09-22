def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    funcao= lista[:]+[n]
    if lista>[n]:
    	return lista
    else:
        return funcao>n