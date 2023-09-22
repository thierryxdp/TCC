def colchao(medidas,H,L):
    col=medidas[1]
    por=H
    por2=L
    col2=medidas[2]
    if por>col:
        return True
    elif por==col:
        return True
    if por2>col2:
        return True
    else:
        return False