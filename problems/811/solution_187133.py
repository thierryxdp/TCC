def colchao(medidas,H,L):
    medidas = A,B,C
    if min(medidas)>min(H,L):
        return False
    elif medidas.sort()[1]>max(H,L):
        return False
    else:
        return True