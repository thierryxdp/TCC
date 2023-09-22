def colchao(medidas,H,L):
    c = medidas[0]
    l = medidas[1]
    h = medidas[2]
    if l > L and h > H:
        return False
    elif l <= L or h <= H:
        return True
    elif l < L or h > H:
        return True
    elif l > L or h < H:
        return True