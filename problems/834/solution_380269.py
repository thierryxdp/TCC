def media_matriz(matriz):
    """
    função que recebe uma matriz de inteiros não vazia e retorna a média de
    todos os números da matriz(com exatamente duas casas de precisão)
   list---->float
    """
    
    soma = 0
    tamanho = 0
    media = 0
    if matriz != []:
        for linha in range(0, len(matriz)):
            for coluna in range(0, len(matriz[linha])):
                tamanho += 1
                soma += matriz[linha][coluna]
                media = soma / tamanho

    return round(media, 2)