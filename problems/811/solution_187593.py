def colchao(medidas,H,L):
    if medidas[1] and medidas[2]>H:
        return false
    if medidas[1] and medidas[2]>L:
        return false
    else:
        return true