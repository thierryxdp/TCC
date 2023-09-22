def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A and C > H and L:
        return False
    elif A and C < H and L:
        return True