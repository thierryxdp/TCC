def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    medidas(A,B,C)=[A,B,C]
    if A<H and B<=H:
        return True
    if A<H and C<=H:
        return True
    if B<=H and C<=H:
        return True
    if A<=L and B<=L:
        return True
    if A<=L and C<=L:
        return True
    if B<=L and C<=L:
        return True
    else:
        return False