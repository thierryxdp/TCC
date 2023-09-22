def eh_quadrada(matriz):
    linhas = len(matriz)
    if(linhas == 0):
        return False
    for linha in matriz:
        if len(linha) != linhas:
            return False
    return True