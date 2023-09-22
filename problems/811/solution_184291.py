def colchao(medidas,H,L):
    b = medidas[1]
    c = medidas[2]
    if (L>=b):
        return True
    elif (L>=c):
        return True
    elif (H>=b):
        return True
    elif (H>=c):
        return True
    else:
        return False