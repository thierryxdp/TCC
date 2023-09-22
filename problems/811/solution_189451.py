def colchao(medidas,H,L):
    medida = medidas[0],medidas[1],medidas[2]
    if medidas[0]<=H and medidas[1]<=L:
        return True
    elif medidas[1]<=H and medidas[2]<=L:
        return True
    elif medidas[0]<=H or medidas[2]<=L:
        return True
    else:
        return False