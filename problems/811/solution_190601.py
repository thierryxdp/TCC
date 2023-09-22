def colchao(medidas, H, L):
    [A, B, C] = medidas
    if C and B > H and L:
        return False
    elif C and B < H and L:
        return True