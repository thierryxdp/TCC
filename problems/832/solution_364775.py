def eh_quadrada(matriz):
    ''' função booleana para identificar se uma matriz é quadrada'''
    if len(matriz)==0:
        return True
    linhas= len(matriz)
    coluna= len(matriz[0])
    return coluna==linhas