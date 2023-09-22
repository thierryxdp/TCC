def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if (H>medidas[2])and(medidas[0]<H):
        return True
    if (H>medidas[1])and(medidas[2]<L):
        return True
    else: 
        return False