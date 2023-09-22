def eh_quadrada(matriz):
    """
    Função recebe uma matriz e identifica se ela é uma matriz quadrada.
    matriz -> booleano
    """
    linhas=len(matriz)
    if linhas==0:
        return True
    colunas=len(matriz[0])
    return linhas==colunas