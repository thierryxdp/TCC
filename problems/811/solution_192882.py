def colchao(medidas,H,L):
    Y=medidas[0]
    X=medidas[1]
    Z=medidas[2]
    if H>=Y and L>=X:
        return True
    if H>=X and L>=Y:
        return True
    else:
        return False
''' funcao para saber se o colchao passa ou não passa pela porta'''