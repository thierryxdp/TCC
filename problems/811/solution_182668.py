def colchao(medidas,H,L):
    """Pede uma lista com as medidas inteiras de um colchão
    e dois inteiros para a medida da porta, retornando True or False
    para saber se o colchão comprado passa pela porta.
    list[int,int,int], int, int->bool"""
    A,B,C = medidas
    if (A<=H and B<=L) or (B<=H and C<=L) or (A<=H and C<=L):
        return True
    elif (A<=L and B<=H) or (B<=L and C<=H) or (A<=L and C<=H):
        return True
    else:
        return False