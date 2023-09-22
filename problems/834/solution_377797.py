def media_matriz(matriz):
    '''função que dada uma matriz de inteiros não vazia
    calcula e retorna a media de todos os numeros da matriz
    parametros:
    list -> float'''
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return soma / tamanho