def media_matriz(matriz):
    '''
    Recebe uma matriz de inteiros
    Retorna a média de todos os números da matriz
    '''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)

    return round(soma/tamanho,2)