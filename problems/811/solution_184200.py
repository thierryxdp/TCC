def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    caso1 = C<L and A<H
    caso2 = B<H and C<L
    caso3 = B<H and A<L
    caso4 = B<L and C<H
    caso5 = C<H and A<L
    caso6 = B<L and A<H
    if caso1 == True and caso2 == True and caso3 == True and caso4 == True and caso5 == True and caso6 == True:
        return True
    else:
        return False