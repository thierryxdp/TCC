def filtra_pares(tupla):
    """ Retorna uma nova tupla contendo apenas os elementos pares da tupla original.
    	tuple -> tuple
        
        Parameter:
        tupla: Tupla a ser filtrada.
        
        Returns:
        Nova tupla contendo apenas os elementos pares da tupla original.
    """
    a, b, c, d = tupla
    lista1 = list(tupla)
    lista2 = []
    for tupla in lista1:
        if tupla % 2 == 0:
            lista2.append(tupla)
    return tuple(lista2)