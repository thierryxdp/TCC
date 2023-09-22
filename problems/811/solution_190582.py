def colchao(medidas,H,L):
    x = medidas[0]
    y = medidas[1]
    z = medidas[2]
    if H > L:
        if x <= L and (H >= y or H >= z):
            return True
    elif L > H:
        if x <= H and (L >= y or L >= z):
            return True
    else:
        return False