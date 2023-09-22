def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if (H>medidas[2]):
        return True
    if (H>medidas[1]):
        return True
    else: 
        return False