def colchao(med,H,L):
    """verifica se o colchao passa pela porta,
    se passar retorna True, caso contrário retorna False;
    list(float,float,float),float,float->bool"""
    if med[0]>H and med[1]>L or med[0]>L and med[1]>H:
        return False
    if med[0]>H and med[2]>L or med[0]>L and med[2]>H:
        return False
    if med[1]>H and med[2]>L or med[1]>L and med[2]>H:
        return False
    else:
        return True