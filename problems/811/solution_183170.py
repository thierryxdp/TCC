def colchao(medidas,H,L):
    """ função que determina se é possível ou não o colchao passar pela porta"""
    if (medidas[0] and medidas [1]) or (medidas[0] and medidas [2]) or (medidas[2] and medidas [1]) > H:
        return False
    else:
        return True