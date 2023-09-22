def maiores(lista, n):
    '''retorna uma lista com os valores da lista de entrada maiores que n, em ordem crescente
    list -> list'''
	if n in lista:
        indice = list.index(lista,n) + 1
    	return lista[indice:]
    else:
        list.insert(lista,1,n)
    	list.sort(lista)
    	indice = list.index(lista,n) + 1
    	return lista[indice:]