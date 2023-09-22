def colchao(medidas,H,L):
   
    if medidas[1]> H:
        return False
    elif medidas[2]>H:
        return False
    else:
        if medidas[1] or medidas[2] <= L or H:
            return True