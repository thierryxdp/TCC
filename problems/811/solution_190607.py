def colchao(medidas, H, L):
    [A, B, C] = medidas
    if C and A > H and L:
        return False
    else:
        return True