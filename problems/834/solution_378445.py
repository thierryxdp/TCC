def media_matriz(matriz):
    '''retorna a média de todos os números da matriz;
    list->float(duas casas decimais de precisão)'''
    soma=0
    for linha in matriz:
        soma+=sum(linha)
    return round((soma)/(len(matriz)*len(matriz[0])),2)