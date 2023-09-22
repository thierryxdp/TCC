def eh_quadrada(matriz):
    if len(matriz)==0:
        return True
    linhas= len(matriz)
    coluna= len(matriz[0])
    return coluna==linhas