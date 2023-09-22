def media_matriz (matriz_int):
    '''Função que retorna a média de todos os números da matriz não vazia fornecida
     list(list) -> float '''
    total=0
    soma=0
    media=0
    if matriz_int != []:
        for ind_linha in range(0, len(matriz_int)):
            for ind_coluna in range(0, len(matriz_int[ind_linha])):
                media = ((soma + matriz_int[ind_linha][ind_coluna]) /(total +1))
    return round(media, 2)