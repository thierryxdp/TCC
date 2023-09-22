colchao(medidas,H,L):
    medidas=[A,B,C]
    if L>A>H:
        return True
    if L>B>H:
        return True
    if L>C>H:
        return True
    if C>L or C>H:
        return True
    if B>L or B>H:
        return True
    if A>L or A>H:
        return True
    else:
        return False