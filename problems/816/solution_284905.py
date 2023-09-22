def maiores(Lista, Numero):
    """ 
    Código que retorna todos os numeros da lista dada maiores
    que n.
    :Lista -->List:    
    :Numero-->Int:
    :Return-->List:
    """
    Lista.append(Numero)
    B = filter(lambda i: i > 2, N)   
    return B