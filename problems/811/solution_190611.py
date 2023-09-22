def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    elif A > H and B < L:
        return True
    else:
        return True