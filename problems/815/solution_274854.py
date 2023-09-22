def insere(lista_numero,n):
    """ função que dado uma lista com números
    inteiros se adiciona um novo número n , que
    será posto dentro da lista de forma ordenada.
    assinatura: list --> list
    testes:
    insere( [1,2,3] , 0) == [0,1,2,3]
    insere( [1,2,3] , 4) == [1,2,3,4]
    insere( [2,4,6] , 8) == [2,4,6,8]
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero