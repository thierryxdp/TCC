def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    x=list.index(lista2,n)
    resolucao=list.sort(lista2)
    if lista>[n]:
    	return lista
    elif x>0:
        return lista2[0:x]