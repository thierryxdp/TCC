def colchao(medidas,H,L):
    """ função que determina se é possível ou não o colchao passar pela porta"""
    if medidas[0] > H and medidas [1]> H:
        return False
    elif medidas[0]>H and medidas [2]> H: 
        return False
    elif medidas[2] > H and medidas [1] > H:
        return False
    else:
        return True