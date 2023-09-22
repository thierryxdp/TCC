def eh_quadrada(matriz):
    if matriz==[]:
        return True
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        for j in range(mcolunas):
            if nlinhas==mcolunas:
                return True
            else:
                return False