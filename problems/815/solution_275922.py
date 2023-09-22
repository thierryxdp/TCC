def insere(lista_numero, n):
    '''funcao que adiciona um dado valor 'n' a uma dada lista.
    list-->list'''
	x = lista_numero
	x.insert(-1, n)
	x.sort()
	return x