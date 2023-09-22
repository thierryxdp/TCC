def colchao (medidas, H, L):
    [x,y,z] = medidas
    result = bool
    if medidas[1] <H and medidas[2] < L:
        result = True
    else:
        result = False
    return result