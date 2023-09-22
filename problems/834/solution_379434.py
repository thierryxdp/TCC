def media_matriz(matriz):
    '''Recebe uma matriz e retorna a média dos números dessa matriz com duas casas decimais de precisão; list->float'''
    soma=0
    for linha in matriz:
        for coluna in linha:
            soma=soma+coluna
    resultado=soma/(len(matriz)*len(matriz[0]))
    return round(resultado,2)