def colchao(medidas, H, L):
    [A, B, C] = medidas
    if C and A > H and L:
        return False
    elif C and A < H and L:
        return True