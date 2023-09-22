def colchao(medidas,H,L):
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if (L>=b) and (H>=c):
        return True
    else:
        return False