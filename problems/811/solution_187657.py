def colchao(medidas,H,L):
    x=medidas[1]
    y=medidas[2]
    if x>H and y<=H:
        return True
    if x>L and y<=L:
        return True
    else:
        return False