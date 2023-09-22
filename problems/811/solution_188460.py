def medidas(A,B,C):
    return [A,B,C]
def colchao(medidas,H,L):
    ''''''
    if L>247:
        return True
    if medidas[1]>H:
        return False
    else:
        return True