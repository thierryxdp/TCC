def colchao(medidas, H, L):
    [A, B, C] = medidas
    A<B<C
    if B > H and C > L:
        return False
    else:
        return True