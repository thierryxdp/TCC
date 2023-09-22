def colchao(medidas,H,L):
    x=medidas
    if x[1]<=H or x[1]<=L:
        return True
    if x[2]<=H or x[2]<=L:
        return True
    else:
        return False