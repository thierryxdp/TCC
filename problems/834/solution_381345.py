def media_matriz(matriz):
    '''Recebe uma matriz e retorna a média de todos os números inteiros 
    contidos nesta, com a precisão de duas casas. (list -> list)'''
    soma = 0
    quantidade = 0
    for linha in matriz:
        for aij in linha:
            soma = soma + aij
            quantidade = quantidade + 1
    return round((soma/quantidade),2)