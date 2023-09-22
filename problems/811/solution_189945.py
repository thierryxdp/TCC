def colchao(medidas,H,L):
    if medidas[1] and medidas[2] > H and L:
        return False
    elif H and L > medidas[1] and medidas[2]:
        return True