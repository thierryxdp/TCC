def maiores(lista, n):
    """ Faz uma lista com todos os números da lista original maiores que n.
    	list, int -> list
        
        Parameters:
        lista: Lista original.
        n: Número n.
        
        Returns:
        Lista com todos os números da lista original maiores que n.
    """
    list.sort(lista)
    while len(lista) > 0 and lista[0] < n:
        del lista[0]
    return lista