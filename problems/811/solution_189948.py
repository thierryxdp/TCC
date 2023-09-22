def colchao(medidas,H,L):
    if medidas[1] > H:
        return False
    elif H > medidas[1]:
        return True
    elif medidas[1] == H:
        return True
    elif medidas[2] < L:
        return True