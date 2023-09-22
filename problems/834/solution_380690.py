def media_matriz (matriz_int):
    '''Função que retorna a média de todos os números da matriz não vazia fornecida
     list(list) -> float '''
    toal=0
    soma=0
    for linha in range(0, len(matriz_int)):
        for coluna in range(0, len(matriz_int[linha])):
                total += len(matriz_int)
                soma += matriz_int[linha][coluna]
                media = soma / tamanho
                return round(media, 2)