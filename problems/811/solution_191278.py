def colchao (medidas, H, L):
    [x,y,z] = medidas
    result = bool
    if medidas[2] <= H and medidas[1] <= L:
        result = True
    else:
        result = False
    return result