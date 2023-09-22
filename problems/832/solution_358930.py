def eh_quadrada(matriz):
    """funcao que identifica se uma funcao é quadrada, tem o mesmo numero de linhas e
    colunas. list->bool"""
    nlin= 0
    ncol= len(matriz)
    for j in range(len(matriz)):
        if len(matriz)==len(matriz[j]):
            nlin +=1
    if ncol==0:
        return True
    if nlin== ncol:
        return True
    if nlin !=ncol:
        return False