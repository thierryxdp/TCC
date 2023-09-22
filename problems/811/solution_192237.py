def colchao(medidas,H,L):
    if (medidas[0] <= L):
        return True
    elif (medidas[1] <= L):
        return True
    if (medidas[0] <= H):
        return True
    elif (medidas[1] <= H):
        return True
    else:
        return False