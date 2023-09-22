def colchao(medidas,H,L):
    """função que determina se o colchão passa por uma porta de dimensões H x L ou não"""
    """list, int, int -> bool"""
    if medidas[1][2] <= H:
        return True
    if medidas[1][2] <= L:
        return True
    else:
        return False