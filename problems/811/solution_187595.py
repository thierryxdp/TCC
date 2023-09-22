def colchao(medidas,H,L):
    if medidas[1] and medidas[2]>H:
        return False
    else:
        if medidas[1] and medidas[2]>L:
            return False
        else:
            return True