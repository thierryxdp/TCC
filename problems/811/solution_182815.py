def colchao(medidas,H,L):
    """Retorna se o colchão passará ou não com base nas medidas dadas; lista, int, int-> bool."""
    if medidas[1]<=H and medidas[2]<=L:
        return True
    elif medidas[1]<=H and medidas[3]<=L:
        return True
    elif medidas[2]<=H and medidas[3]<=L:
        return True
    elif medidas[1]<=H and medidas[3]<=L:
        return True
    elif medidas[2]<=H and medidas[1]<=L:
        return True
    elif medidas[3]<=H and medidas[1]<=L:
        return True
    elif medidas[3]<=H and medidas[2]<=L:
        return True
    else:
        return False