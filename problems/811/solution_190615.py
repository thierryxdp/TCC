def colchao(medidas, H, L):
    [A, B, C] = medidas
    A<B<C
    if A > H and B > L:
        return False
    else:
        return True