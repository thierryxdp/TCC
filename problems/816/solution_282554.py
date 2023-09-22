def maiores(lista,n):
    """
    	Retorna uma lista com os numeros que são maiores que n, em ordem crescente.
        list, int -> list
    """
    lista.append(n)
    lista.sort()
    lista=lista[lista.index(n)+1:]
	return lista