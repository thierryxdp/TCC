def colchao(medidas,H,L):
    x = medidas[0]
    y = medidas[1]
    z = medidas[2]
    if H > L:
        if x <= L and H >= y and H >= z:
            return True
    if L > H:
        if x <= H and L >= y and L >= z:
            return True
        return False
    else:
        return False