def colchao(medidas,H,L):
    if int(medidas[0:1])<H or int(medidas[0:1])<L:
        return True
    if int(medidas[2:5])<H or int(medidas[2:5])<L:
        return True
    if int(medidas[6:9])<H or int(medidas[6:9])<L:
        return True
    else:
        return False