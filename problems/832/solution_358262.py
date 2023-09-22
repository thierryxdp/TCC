def eh_quadrada(m):
    """função que analisa a matriz de entrada (m) e verifica se ela é
    quadrada, ou seja, se o número de linhas é igual ao número de
    colunas da matriz de entrada;
    matriz-> bool"""
    linhas = len(m)
    colunas = len(m[0])
    if m==[]:
        return True
    elif linhas==colunas:
        return True
    else:
        return False