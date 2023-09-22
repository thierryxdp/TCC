def colchao(medidas,H,L):
    ''''''
 medidas == [A,B,C]
    if H>C and A<H:
        return True
    if H>B and C<L:
        return True
    else:
        return False