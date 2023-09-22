def eh_quadrada(matriz):
    """ Identifica se a matriz é quadrada 
    list(list) -> bool """
    nLinhas = len(matriz)
    for linha in matriz:
        if len(linha) != nLinhas:
            return False
    return True