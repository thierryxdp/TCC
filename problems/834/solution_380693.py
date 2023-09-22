def media_matriz (matriz_int):
    '''Função que retorna a média de todos os números da matriz não vazia fornecida
     list(list) -> float '''
    total=0
    soma=0
    for linha in range(len(matriz_int)):
        for coluna in range(len(matriz_int[linha])):
                total += 1
                soma += matriz_int[linha][coluna]
                media = soma / total
                return round(media, 2)