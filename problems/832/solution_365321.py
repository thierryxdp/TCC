def eh_quadrada(matriz):
# list > bool
    linhas = len(matriz)
    for linha in matriz:
        if len(linha) != linhas:
           return False
    return True