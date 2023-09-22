def colchao(medidas,H,L):
    areacolchao = medidas[0]*medidas[1]
    areaporta = H*L
    if medidas[1] <= H:
        return True
    else:
        return False