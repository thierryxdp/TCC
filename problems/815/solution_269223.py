def insere(lista_numero,n):

    """ Tendo uma lista de números inteiros ordenados, com esta função,
        inseriremos o numero contido em n na posição n na lista, de forma
        que a lista continue ordenada.

        list,int -> list
    """
    
    lista_numero_aumentada = lista_numero + [n]
    lista_ordenada = list.sort(lista_numero_aumentada)
    
    return lista_ordenada