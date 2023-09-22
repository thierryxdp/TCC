def colchao(medidas,H,L):
    """."""
    x = lista[0]
    y = lista[1]
    if (y<=H and x<=L) or (y<=L and x<=H):
        return True
    else:
        return False