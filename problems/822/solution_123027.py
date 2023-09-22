def repetidos(lista):
    """ Conta quantas vezes um elemento da lista é igual ao elemento anterior.
    	list -> int
        
        Parameter:
        lista: Lista
        
        Returns:
        Quantas vezes um elemento da lista é igual ao elemento anterior.
    """
    i = 0
    cont = []
    while i < len(lista) - 1:
        if lista[i] == lista[i + 1]:
            cont.append(1)
        i = i + 1
    return len(cont)