def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    A<B<C
    if H>L:
        if B<=H or C<=H:
            return True
        else:
            return False
    if L>H:
        if B<=L or C<=L:
            return True
        else:
            return False
    if H==L:
        if B<=H or C<=H:
            return True
        else:
            return False