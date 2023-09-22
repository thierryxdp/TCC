def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    elif A and B < H and L:
        return True