def maiores(Lista, Numero):
    """ 
    Código que retorna todos os numeros da lista dada maiores
    que n.
    :Lista -->List:    
    :Numero-->Int:
    :Return-->List:
    """
    maior_que = 20
    filtrado = [ x for x in Lista if x > maior_que ]
    return filtrado