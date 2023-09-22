def insere(lista_numero,n):

    """ Tendo uma lista de números inteiros ordenados, com esta função,
        inseriremos o numero contido em n na posição n na lista, de forma
        que a lista continue ordenada.

        list,int -> list
    """

    return lista_numero[0:n-1]+ list(n) + lista_numero[n-1:]