def colchao(medida,H,L):
    """ se "a" e "b" forem maior que a larg e altura,
    a funcao retornará false.
    se nao, a funcao retornará true.
    : int -> bool
    """
    [A,B,C] = medida
    if A and B > H and L:
        return False
    else:
        return True