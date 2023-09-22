def media_matriz(matriz):
    '''Função que dada uma matriz de inteiros não vazia, retorna a média de
todos os números da matriz (com exatamente duas casas decimais de precisão).'''
    #list -> float
    soma = 0
    tamanho = 0
    media = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tamanho += 1
            soma += matriz[i][j]
            media = soma / tamanho
    return round(media, 2)