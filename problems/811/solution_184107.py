def colchao(medidas,H,L):
    medidas = [A,B,C]
    if A<L and B<H:
        return True
    if B<L and A<H:
        return True
    if B<L and C<H:
        return True
    else:
        return False