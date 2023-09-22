def eh_quadrada(x):
    """essa função verifica se uma matriz é quadrada comparando as linhas e colunas
    lista-->bolean"""
    for i in range(len(x)):
        for j in range(len(x[0])):
            if x[i][j]!=x[j][i]:
                return False
    return True