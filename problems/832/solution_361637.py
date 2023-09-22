def eh_quadrada(matriz):
    nlinhas=len(matriz)
    mcolunas=len(matriz[0])
    for i in range(nlinhas):
        for j in range(mcolunas):
            if nlinhas==mcolunas:
                return True
            elif matriz==[]:
                return True
            else:
                return False