def colchao(a,b):
    a = [A,B,C]
    b = [H,L]
    if A<L and B<H:
        return True
    if B<L and A<H:
        return True
    if B<L and C<H:
        return True
    else:
        return False