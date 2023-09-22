def colchao(medidas,H,L):
    b = True
    x = medidas[0]
    y = medidas[1]
    z = medidas[2]
    if x < H and y < L:
        return b
    elif x < H and z < L:
        return b
    elif y < H and z < L:
        return b
    elif z < H and y < L:
        return b
    elif y < H and x < L:
        return b
    elif z < H and x < L:
        return b
    else:
        b = False
        return b