def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    caso1 = C<=L and A<=H
    caso2 = B<=H and C<=L
    caso3 = B<=H and A<=L
    caso4 = B<=L and C<=H
    caso5 = C<=H and A<=L
    caso6 = B<=L and A<=H
    if caso1 == True or caso2 == True or caso3 == True or caso4 == True or caso5 == True or caso6 == True:
        return True
    else:
        return False