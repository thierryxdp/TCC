def colchao(medidas,H,L):
    y=medidas[1]
    i=medidas[2]
    if y>=H:
        if i>=L:
            return True
    else:
        return False