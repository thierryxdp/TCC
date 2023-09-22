def acima_da_media(lista):
    """essa função calcula a média de uma lista e retorna ps números da lista maiores que a média;
    list->list"""
    n=sum(lista)/len(lista)
    if n not in lista:
    	list.append(lista,n)
    	lista=sorted(lista)
    	x=list.index(lista,n)
    	y=x+1
    	return lista[y:]
    else:
        lista=sorted(lista)
        x=list.index(lista,n)
        y=x+1
        return lista[y:]