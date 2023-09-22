def colchao_pela_porta(colchao,H,L):
    A= colchao[0]
    B= colchao[1]
    C= colchao[2]
    if (A<H or A==H) and (B<L or B==L):
        return True
    elif (A<L or A==L) and (B<H or B==H):
        return True
    elif (B<L or B==L) and (C<H or C==H):
        return True
    elif (C<L or C==L) and (B<H or B==H):
        return True
    elif (A<H or A==H) and (C<L or C==L):
        return True
    elif (A<L or A==L) and (C<H or C==H):
        return True
    else:
        return False