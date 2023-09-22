def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if H>medidas[2]:
        return True
    if H>medidas[1]:
        return True
    if medidas[0]<H:
        return True
    if medidas[2]<L:
        return True
    else: 
        return False