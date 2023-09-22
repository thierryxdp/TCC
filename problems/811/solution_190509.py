def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if A<H or B<H or C<H:
        if A<L or B<L or C<L:
            return True
        else:
            return False