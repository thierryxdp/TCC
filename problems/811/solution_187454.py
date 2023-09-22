def colchao(medidas,H,L):
    a=medidas[0]
    b=medidas[1]
    c=medidas[2]
    if a<=L and b<=H or a<=H and b<=L:
        return True
    else:
        return False