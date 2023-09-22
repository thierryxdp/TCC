def eh_quadrada(matriz):
    nlinhas=len(matriz)
    ncolunas=len(matriz[0])
    if nlinhas==ncolunas:
        return True
    if nlinhas=0:
        return True
    elif nlinhas!=ncolunas:
        return False