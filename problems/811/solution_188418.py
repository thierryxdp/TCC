medidas == [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if H>C and A<H:
        return True
    if H>B and C<L:
        return True
    else:
        return False