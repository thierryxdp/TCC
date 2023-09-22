def conta_numero(numero, matriz):
    '''Função retorna, dada um numero inteiro e uma matriz de tamanho qualquer,
    quantas vezes esse determinado numero aparece na matriz'''
    nulo = 0
    result = 0
    tamanho = len(matriz)
    while nulo < tamanho:
        result+= lista[x].count(matriz)
        x+= 1
    return result