def maiores(lista):
    '''funcao que dada uma lista de numeros inteiros e um numero inteiro n retorna outra lista
    int->list'''
    media=sum(lista)/len(lista)
    if media not in lista:
    	list.append(lista,media)
    	list.sort(lista)
    	i=list.index(lista,media)
    	return lista[i+1:]
    else:
        list.sort(lista)
    	i=list.index(lista,media)
    	return lista[i+1:]