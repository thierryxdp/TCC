def colchao(medidas,H,L):
    """entrada[25,120,220],200,100  saida: True"""

    if medidas[0]<=H and medidas[1]<=L:
        return True
    if medidas[0]<=H and medidas[2]<=L:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True

    else:
        return False