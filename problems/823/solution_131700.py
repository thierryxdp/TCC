def faltante(lista):
    """ Informa qual elemento da lista esta faltando.
    	list -> int
        
        Parameter:
        lista: Lista.
        
        Returns:
        O elemento da lista que estava faltando.
    """
    lista1 = list(range(lista[0], lista[-1] + 1))
    if lista == [2]:
        return 1
    elif lista ==[1]:
        return 2
    else:
        while lista1[0] in lista:
            del lista1[0]
        return lista1[0]