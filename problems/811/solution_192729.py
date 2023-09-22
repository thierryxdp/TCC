def colchao(medidas,H,L):
    h=medidas[0]
    l=medidas[1]
    c=medidas[2]
    return h<=L and l<=H or h<=L and c<=H or c<=L and h<=H or l<=L and c<=H