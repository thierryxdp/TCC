def maiores(lista,n):
	if not(n in lista):
        list.append(lista,n)
    list.sort(lista)
	return lista[list.index(lista,n)+1:]

def acima_da_media(lista_notas):
    """
    	Retorna uma lista com as notas acima da média
    	list -> list
    """
    return maiores(lista_notas,7.0)