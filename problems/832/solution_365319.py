def eh_quadrada(matriz):
# list, int > list
    linhas = len(matriz)
    for linha in matriz:
        if len(linha) != linhas:
           return False
     return True