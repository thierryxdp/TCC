def colchao(medida, H, L):
    [A, B, C] = medida
    if A and B and C>H and L:
        return False
    else:
        return True