def colchao(medidas,H,L):
    if medidas[0]>(H and L) or medidas[1]>(H and L):
        return False
    elif medidas[0]>H and medidas[1]>H:
        return False
    elif medidas[0]>L and medidas[1]>L:
        return False   
    else:
        return True