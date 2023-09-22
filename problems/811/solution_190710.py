def colchao(medidas, H, L):
    medida1 = medidas[0]*medidas[1]
    medida2 = medidas[0]*medidas[2]
    areaP = H*L
    if medidas[2] <= H and medidas[2] <= L:
        return True
    elif medida1 <= areaP:
        return True
    elif medida2 <= areaP:
        return True
    else:
        return False