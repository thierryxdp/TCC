def maiores(lista,n):
    '''coment'''
    lista[:]=lista
    resolucao=list.sort(lista)
    
    lista2= lista[:]+[n]
    funcao=list.sort(lista2,reverse=True)
    x=list.index(lista2,n)
    if lista>[n]:
    	return lista
    elif x>n:
        return lista2[x::-1]