def colchao(medidas,H,L):
    x=medidas[1]
    y=medidas[2]
    if (x>H and y>H)or (x>L and y>L):
        return False
    else:
        return True