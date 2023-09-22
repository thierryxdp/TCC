def colchao(medidas,H,L):
    if medidas[1] > H:
        return False
    elif medidas[1]<=H and medidas[2]<=L:
        return True
    else:
        return True