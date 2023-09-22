def colchao(medida, H, L):
    [A, B, C] = medida
    if A and B or C>H and L:
        return False
    else:
        return True