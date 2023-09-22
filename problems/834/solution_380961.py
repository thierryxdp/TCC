def media_matriz(matriz):
    '''Essa função calcula a média aritmética de todos
    os elementos que está dentro da matriz;list->float'''
    n = 0
    for linha in matriz:
        for coluna in linha:
            n+=coluna
    elem = len(matriz[0])*len(matriz)
    return n/elem