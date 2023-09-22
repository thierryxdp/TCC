def colchao(medidas,H,L):
    x=medidas[0]
    y=medidas[1]
    z=medidas[2]
    if H>=x and L>=y:
        return True
    if H>=y and L>=x:
        return True
    else:
        return False