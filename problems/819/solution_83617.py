def filtraMultiplos(lista, n):
    '''analisa uma lista e retorna outra lista contendo todos os elementos que forem divisíveis por n
    list, int -> list'''
    lista_filtrada = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(lista_filtrada, lista[i])
		i = i + 1
	return lista_filtrada