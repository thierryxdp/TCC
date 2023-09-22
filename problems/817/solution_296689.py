def acima_da_media (lista):
    """ """
    soma = sum(lista)
    qtd = len(lista)
    media = soma//qtd
    list.sort(lista)
    if media in lista:
        lista = lista[media+1:]
		else:
        	list.append (lista,media)
            lista = lista [media+1:]
	return lista