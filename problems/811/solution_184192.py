def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    return print(bool(C<L or B<H and C<L or B<H or B>L and C<H or C<H or B<L))