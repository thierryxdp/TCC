def acima_da_media (lista):
    """ """
    soma = sum(lista)
    qtd = len(lista)
    media = soma//qtd
    list.sort(lista)
    if media not in lista:
        list.append (lista,media)
    	else:
            lista = lista
	lista = lista [media+1:]
    return lista