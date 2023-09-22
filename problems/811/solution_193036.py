def colchao(medidas,H,L):
    y=medidas[1]
    i=medidas[2]
    if H<=y:
        if L<=i:
            return True
    else:
        return False