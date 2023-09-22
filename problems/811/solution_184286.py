def colchao(medidas,H,L):
    a = medidas[0]
    b = medidas[1]
    c = medidas[2]
    if (H>b) and (H>c) and (L>b) and (L>c):
        return True
    else:
        return False