def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<H:
        if B<L or C<L:
            return True
        else:
            return False
    elif B<H:
        if A<L or C<L:
            return True
        else:
            return False