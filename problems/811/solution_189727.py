def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if B>H and C>L:
        return False
    if B<H and C<L:
        return True
    if B>H and C<L:
        return True
    if B<H and C>L:
        return True
    if B==H and C>L:
        return True