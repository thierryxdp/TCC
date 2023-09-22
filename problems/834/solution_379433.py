def media_matriz(matriz):
    '''Recebe uma matriz e retorna a média dos números dessa matriz com duas casas decimais de precisão; list->float'''
    soma=0
    for linha in matriz:
        for coluna in linha:
            soma=soma+coluna
    return soma/(len(matriz)*len(matriz[0]))