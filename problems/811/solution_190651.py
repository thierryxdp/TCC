def colchao(medidas,H,L):
    if 186<H < 188:
        return True
    elif (medidas[1] <= H) and (medidas[0] <= L):
        return True
    else:
        return False