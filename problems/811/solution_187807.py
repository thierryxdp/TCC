def colchao(medidas,H,L):
    if medidas[1] > H:
        return False
    elif medidas[1]<L and medidas[2]<=H:
        return True
    else:
        return True