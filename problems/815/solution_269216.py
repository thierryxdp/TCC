def insere(lista_numero,n):

    """ Tendo uma lista de números inteiros ordenados, com esta função,
        inseriremos o numero contido em n na posição n na lista, de forma
        que a lista continue ordenada.

        list,int -> list
    """
    
	lista_aumentada = lista_numero[0:n-1]+ [n] + lista_numero[n-1:]
    
    return list.sort(lista_aumentada)