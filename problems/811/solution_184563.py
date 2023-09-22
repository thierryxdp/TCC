def colchao(medidas,H,L):
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]

    return A<=L and(B<=H or C<=H) or B<=L and(A<=H or C<=H) or C<=L and(B<=H or A<=H)