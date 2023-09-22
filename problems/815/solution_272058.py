def insere(lista_numero,n):
    '''Recebe uma lista ordenada de forma  crescente e um numero inteiro e coloca esse numero inteiro dentro da lista de forma ordenada e crescente
    list,int->list'''
	lista2 = lista_numero[:]
	list.append(lista2,n)
	list.sort(lista2)
	return lista2