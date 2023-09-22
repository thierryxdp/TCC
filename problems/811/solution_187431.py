def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    if (B<=L and C<=H)or(C<=L and B<=H)or(B<=L and A<=H)or(A<=L and C<=H)or(C<=L and A<=H)or(A<=H and B<=H):
        return True
    else:
        return False