def filtra_pares(lista):
    """A função filtra uma tupla de quatro elementos inteiros, retornando 
	apenas os números pares dentro da tupla; tuple -> tuple"""
    lista_pares=[termo for termo in lista if termo %2 ==0]
    lista_filtrada=tuple(lista_pares)
    return lista_filtrada