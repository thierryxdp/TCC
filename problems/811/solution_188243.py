def colchao(medidas,H,L):
   
    if medidas[1]> H and L:
        return False
    elif medidas[2]>H and L:
        return False
    else:
        if medidas[1] or medidas[2] <= L:
            return True