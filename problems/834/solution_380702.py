def media_matriz (matriz_int):
    '''Função que retorna a média de todos os números da matriz não vazia fornecida
     list(list) -> float '''
    soma=0
    total=0
    media=0
    for linha in range(len(matriz_int)):
        for coluna in range(len(matriz_int[linha])):
                soma +=matriz_int[linha][coluna]
                total+=len(matriz_int)
                media = soma / total
                return round(media, 2)