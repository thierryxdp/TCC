def colchao(medidas,H,L):
    if medidas[1] > H and medidas[2] < L:
        return True
    if medidas[1] < H:
        return True
    if medidas[1] == H:
        return True
    if medidas[1] > H:
        return False