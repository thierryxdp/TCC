def media_matriz(matriz):

    '''Função que dada uma matriz de inteiros n˜ao vazia, retorna a média
de todos os números da matriz (com exatamente duas casas decimais de precis˜ao)
list -> float'''
    
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