def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A<L and B<H:
        return True
    if C<L and B<H:
        return True
    if B<L and A<H:
        return True
    if C<L and A<H:
        return True
    if B<L and C<H:
        return True
    if A<L and C<H:
        return True
    else:
        return False