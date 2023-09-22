def maiores(lista,n):
    """
    	Retorna uma lista com os numeros que são maiores que n, em ordem crescente.
        list, int -> list
    """
    lista.append(n)
    lista.sort()
    lista_aux[0:lista.index(n)+1]
    lista.pop(lista_aux)
	return lista