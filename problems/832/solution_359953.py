def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    if len(matriz) == 0:
        return True
    for i in range(linhas):
        for j in range(colunas):
            if len(matriz[i]) == len(matriz[j]):
                return False
            else:
                return True