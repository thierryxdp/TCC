def colchao(medidas, H, L):
    [A, B, C] = medidas
    if B and C < H and L:
        return False
    else:
        return True