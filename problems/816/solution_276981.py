def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    if lista>[n]:
    	return lista
    elif x>0:
        return lista2