def acima_da_media(lista):
    """funcao que retorna os numeros de uma lista dada maior que de uma determinada media;lista->lista"""
    list.sort(lista)
    index=len(lista)
    if index%2==0:
        media=index/2
    	return lista[media:]
    else:
        media=index//2
        return lista[(media+1):]