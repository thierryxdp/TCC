def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if (medidas[0]*medidas[1]*medidas[2])<(H*L):
        return True
    else:
        return False