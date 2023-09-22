def colchao(medidas,H,L):
    if medidas [0]<=L and medidas[1]<=H:
        return True
    if medidas[1]<=L and medidas[0]<=H:
        return True
    else:
        return False