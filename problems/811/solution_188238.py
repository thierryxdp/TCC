def colchao(medidas,H,L):
   
    if medidas[1] or medidas[2] > H:
        return False
    elif medidas[1] or medidas[2] <= H:
        return True
    else:
        if medidas[1] or medidas[2] <= L:
            return True