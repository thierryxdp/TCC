def colchao(medidas,H,L):
    """
    Informa se o colchão comprado passa pela porta
    list,int,int -> bool
    """
    if medidas[1]>H and medidas[1]>L:
        return False
    else:
        return True