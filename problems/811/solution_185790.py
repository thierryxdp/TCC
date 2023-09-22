def colchao(medidas,H,L):
    """Retorna True ou False dependendo se o colchão passa ou não pela porta. list,int/float,int/float -> bool """
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A < H:
        if B < L:
            return True
        if C < L:
            return True
    if B < H:
        if A < L:
            return True
        if C < L:
            return True
    if C < H:
        if B < L:
            return True
        if A < L:
            return True
    else:
        return False