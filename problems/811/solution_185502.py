def colchao(medidas,H,L):
    if H >= medidas[1]:
        return True
    if H >= medidas[2]:
        return True
    if L >= medidas[1]:
        return True
    if L >= medidas[2]:
        return True
    else:
        return False