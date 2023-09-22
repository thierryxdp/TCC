def colchao(medidas,H,L):
    A,B,C = medidas
    if min(medidas)>min(H,L):
        return False
    elif medidas.sort(medidas)[1]>max(H,L):
        return False
    else:
        return True