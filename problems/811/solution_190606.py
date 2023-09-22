def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A and C > H and L:
        return False
    else:
        return True