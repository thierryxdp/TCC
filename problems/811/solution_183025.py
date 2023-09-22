def colchao(medidas,H,L):
    c = medidas[0]
    l = medidas[1]
    h = medidas[2]
    if (h > H and l > L):
        return False
    elif (h <= h or l <= L):
        return True