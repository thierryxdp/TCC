def colchao(medidas,H,L):
    if (H >= mediadas[2] and L >= medidas[0]) or (H >= medidas[0] and H >= medidas[2]):
        return True
    elif (H >= mediadas[0] and L >= medidas[1]) or (H >= medidas[1] and H >= medidas[0]):
        return True
    else:
        if H >= mediadas[2] and L >= medidas[1]:
            return True
        else:
            return False