def colchao(medidas, H, L):
    [A, B, C] = medidas
    A<B<C
    if A and B > H and L:
        return False
    elif B > H and C < L:
        return True
    else:
        return True