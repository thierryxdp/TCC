def  intercala ( lista1 , lista2 ):
    """
    Dada duas listas, essa função gera uma nova lista contendo todos os valores das duas
    listas de forma intercalada.
    :param lista1: lista -> lista
    :param lista2: lista -> lista
    :retorno: lista -> lista
    """
    lista3  =  lista1  +  lista2
    lista3 [:: 2 ] =  lista1
    lista3 [ 1 :: 2 ] =  lista2
    return  lista3