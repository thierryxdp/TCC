def colchao(medidas,H,L):
    """."""
    x = medidas[0]
    y = medidas[1]
    if (y<=H and x<=L) or (y<=L and x<=H):
        return True
    else:
        return False