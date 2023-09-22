def eh_quadrada(matriz):
    """Função que identifica se uma matriz é quadrada
    lista -> true or false"""
    if len(matriz) == 1 and len(matriz[0]) == 0:
        return True
    return all(len(matriz) == len(linha) for linha in matriz)