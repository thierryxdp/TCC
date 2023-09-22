def media_matriz(matriz):
    '''Retorna a média de todos os numeros da matriz
    	list(list) -> float'''
    soma = 0
    for linha in matriz:
        for aij in linha:
            soma = soma + aij
    numeros = len(matriz)*len(matriz[0])
    return round(soma/numeros, 2)