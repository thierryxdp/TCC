def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A < H:
        if B or C < L:
            return True:
    if B < H:
        if A or C < L:
            return True:
    if C < H:
        if B or A < L:
            return True:
    else:
        return False