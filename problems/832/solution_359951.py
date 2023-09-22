def eh_quadrada(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if range(matriz[i]) == range(matriz[j]):
                return False
            else:
                return True