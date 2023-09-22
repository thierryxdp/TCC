def eh_quadrada(matriz):
    """Funcao que identifica se uma matriz de entrada e
    quadrada, retornando True, ou nao, retornando False;
    list[list] -> bool"""
    numero_de_linhas=len(matriz)
    numero_de_colunas=len(matriz[0])
    if numero_de_linhas==numero_de_colunas or matriz==[]:
        return True
    else:
        False