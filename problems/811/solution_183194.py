def colchao(medidas,H,L):
    """ função que determina se é possível ou não o colchao passar pela porta"""
    if medidas[0] > H or medidas [1]> L:
        return False
    elif medidas[0]>H or medidas [2]> L: 
        return False
    elif medidas[2] > H or medidas [1] > L:
        return False
    else:
        return True