def colchao(medidas, H, L):
    [A, B, C] = medidas
    A<B<C
    if B and C < H and L:
        return True
    elif B and C > H and L:
        return False