def eh_quadrda(matriz):
    tam=len(matriz)
    if tam==0:
        return True
    tam1=len(matriz[0])
    if tam1==tam:
        return True
    else:
        return False