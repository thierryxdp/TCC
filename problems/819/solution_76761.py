def filtraMultiplos(lista, n):
    """ Filtra os elementos da lista retornando apenas os divisíveis por n.
    	list, int -> list
        
        Parameters:
        lista: Lista a ser filtrada.
        n: Número n.
        
        Returns:
        Lista contendo os números da lista original divisíveis por n.
    """
    lista1 = []
    i = 0
    while i < len(lista):
        if lista[i] % n == 0:
            lista1.append(lista[i])
        i = i + 1
    return lista1