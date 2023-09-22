def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    x=list.index(lista2,n)
    y= lista2[0:x]
    if lista>[n]:
    	return lista
    elif x>n:
        return y