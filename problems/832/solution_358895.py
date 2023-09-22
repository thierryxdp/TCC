def eh_quadrada(matriz):
    """essa função irá identificar se uma matriz é quadrada ; lista ->bool """
    colunas = len(matriz)
    for linhas in matriz :
        if len(linhas) != colunas :
            return False
    
    return True