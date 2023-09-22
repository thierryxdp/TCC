def colchao(medidas,H,L):
    """ função que determina se é possível ou não o colchao passar pela porta"""
    if medidas[0] and medidas [1] > H or L:
    return "False"
elif medidas[1] and medidas [2] > H or L:
    return "False"
elif medidas[0] and medidas [2] > H or L:
    return "False"
else:
    return "True"